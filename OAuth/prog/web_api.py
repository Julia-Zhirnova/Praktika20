from multiprocessing import Process

from flask import Flask, request, jsonify
from prog.publisher import PublisherClass, Var
from prog.mosquitto_listener import listener_func
from .oauth import Auth


class ReturnSchema:
    @classmethod
    def ret(cls, log):
        return jsonify(status=log)

    @classmethod
    def ret_list(cls, lst):
        return jsonify(count=len(lst), val=lst)


class WebApp:
    def __init__(self, db):
        self._pub = PublisherClass(db)
        self._web = Flask(__name__)
        self._msq = {}

        @self._web.route("/start")
        def start():
            r_c = self._pub.start_work()
            if r_c:
                return ReturnSchema.ret("Started")
            return ReturnSchema.ret("Started before")

        @self._web.route("/stop")
        def stop():
            r_c = self._pub.stop_work()
            if r_c:
                return ReturnSchema.ret("Stopped")
            return ReturnSchema.ret("Still stopped")

        @self._web.route("/list")
        def lst():
            return ReturnSchema.ret_list(self._pub.get_var_list())

        @self._web.route("/add")
        def add():
            nm = request.args.get("name", None)
            b_v = request.args.get("bv", None)
            f_r = request.args.get("f_r", 1.0)
            if nm is None or b_v is None:
                return ReturnSchema.ret("ErrorVals")
            try:
                e = float(b_v)
            except Exception:
                return ReturnSchema.ret("BeginValueNotFloat")
            self._pub.add_field(nm, Var(b_v, f_r))
            return ReturnSchema.ret("Added")

        @self._web.route("/del")
        def delv():
            nm = request.args.get("name", None)
            if nm is None:
                return ReturnSchema.ret("Error in name")
            e = self._pub.del_field(nm)
            if e:
                return ReturnSchema.ret("Deleted")
            return ReturnSchema.ret("No var with name")

        @self._web.route('/user', methods=["POST"])
        def user():
            nm = request.form.get("usern", None)
            ps = request.form.get("passw", None)
            if nm is None or ps is None:
                return ReturnSchema.ret('ERROR params')
            return ReturnSchema.ret(Auth.authorise(nm, ps))

        @self._web.route('/mosq')
        def msq():
            token = request.headers.get("Authorization", "a b").split(" ")[-1]
            if not Auth.get_user_info(token):
                return ReturnSchema.ret("not AUTH")
            nm = request.args.get("name", None)
            topic = request.args.get("top", None)
            if nm is None or topic is None:
                return ReturnSchema.ret("Error in Values")
            if nm in self._msq:
                return ReturnSchema.ret("Already exists")
            self._msq[nm] = Process(target=listener_func, args=(self._pub, nm, topic))
            self._msq[nm].start()
            return ReturnSchema.ret("Done")

    def start(self):
        self._web.run(host="0.0.0.0", port=8011, debug=False)
        print('STOPPING')
        for a in self._msq:
            a.terminate()
            a.join()

