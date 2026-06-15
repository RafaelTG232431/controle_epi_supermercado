import os

TIPO_BANCO = "sqlite"

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

SQLITE_URL = "sqlite:///" + os.path.join(BASE_DIR, "controle_epi.db")

MYSQL_URL = "mysql+pymysql://root:123456@localhost/controle_epi"

POSTGRESQL_URL = "postgresql://postgres:123456@localhost:5432/controle_epi"


def obter_banco():
    if TIPO_BANCO == "mysql":
        return MYSQL_URL

    if TIPO_BANCO == "postgresql":
        return POSTGRESQL_URL

    return SQLITE_URL
