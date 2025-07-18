from config import app
import pyodbc


def get_sql_server_conn():

    conn_str = (
        f"DRIVER={{{app.config['SQL_SERVER_DRIVER']}}};"
        f"SERVER={app.config['SQL_SERVER']};"
        f"DATABASE={app.config['SQL_DATABASE']};"
        f"UID={app.config['SQL_USERNAME']};"
        f"PWD={app.config['SQL_PASSWORD']};"
        "TrustServerCertificate=yes;"
    )
    return pyodbc.connect(conn_str)
