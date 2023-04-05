import sqlalchemy
from sqlalchemy.orm import sessionmaker

DATABASE = "mysql"
USER = ""
PASSWORD = ""
HOST = "host.docker.internal"
PORT = 3306
DB_NAME = "codetest"

DATABASE_URL = '{}://{}:{}@{}:{}/{}?charset=utf8'.format(DATABASE, USER, PASSWORD, HOST, PORT, DB_NAME)

ECHO_LOG = False

engine = sqlalchemy.create_engine(DATABASE_URL, echo=ECHO_LOG, pool_pre_ping=True)

metadata = sqlalchemy.MetaData()

def get_session():
    SessionClass = sessionmaker(engine)
    return SessionClass()



