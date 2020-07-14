from .web_api import WebApp
from prog.database import DataBaseConnector, DataBaseConfig


database_config = DataBaseConfig()
db = DataBaseConnector()
database_config.database_address = 'influx'
db.set_configuration(database_config)
db.connect()
WebApp(db).start()
