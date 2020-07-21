import random
import sqlite3
import hashlib
import jwt


class AuthDB:
    db_name = 'my.db'

    @classmethod
    def get_user(cls, name):
        conn = sqlite3.connect(cls.db_name)
        curr = conn.cursor()
        curr.execute('SELECT * FROM users WHERE name = ? LIMIT 1', (name, ))
        t = curr.fetchone()
        conn.close()
        return t


class MyJWTTemplate:
    secr = "sfdksdklfsdlqreioqpwepqwekpoqmwmasmflksd"
    def __init__(self, token):
        self.valid = False
        try:
            q = jwt.decode(token, MyJWTTemplate.secr, algorithms=['HS256'])
        except Exception:
            return
        hs = q.get("nmhs", None)
        nm = q.get("name", None)
        sc = q.get("sec", None)
        if hs is None or nm is None or sc is None:
            return
        if hashlib.sha256(nm.encode()).hexdigest() != hs:
            return
        self.valid = True
        self.name = nm
        self.sec = sc

    @classmethod
    def get_token(cls, name, scc):
        dc = {
            "name": name,
            "nmhs": hashlib.sha256(name.encode()).hexdigest(),
            "sec": scc,
            "random": str(random.random())
        }
        return jwt.encode(dc, MyJWTTemplate.secr, algorithm='HS256')


class Auth:
    @classmethod
    def authorise(cls, user, password):
        us_n = str(user)
        us = AuthDB.get_user(us_n)
        if us is None:
            return False
        if str(password) != us[1]:
            return False
        return MyJWTTemplate.get_token(us[0], us[2]).decode()

    @classmethod
    def get_user_info(cls, token):
        jtt = MyJWTTemplate(token)
        if not jtt.valid:
            return False
        us = AuthDB.get_user(jtt.name)
        if us is None:
            return False
        if us[2] != jtt.sec:
            return False
        return jtt.name
