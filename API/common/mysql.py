# from environs import Env
import MySQLdb
from common.logger import Logger

# env = Env()

conf = {}


class MySQLDatabase:
    def __init__(self):
        SQL_HOST = conf['db_host']
        SQL_USER = conf['db_user']
        SQL_PASSWORD = conf['db_password']
        SQL_DATABASE = conf['db_name']

        self.connection = MySQLdb.connect(host=SQL_HOST,
                                          user=SQL_USER,
                                          passwd=SQL_PASSWORD,
                                          db=SQL_DATABASE,
                                          use_unicode=True,
                                          charset='utf8')
        self.cursor = self.connection.cursor()
        self.logger = Logger().logger
        self.logger.info("Database ready to query")


