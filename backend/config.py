from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent.parent / ".env")

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

app.config["SQL_SERVER_DRIVER"] = os.getenv(
    "SQL_SERVER_DRIVER", "ODBC Driver 18 for SQL Server"
)
app.config["SQL_SERVER"] = os.getenv("SQL_SERVER")
app.config["SQL_DATABASE"] = os.getenv("SQL_DATABASE")
app.config["SQL_USERNAME"] = os.getenv("SQL_USERNAME")
app.config["SQL_PASSWORD"] = os.getenv("SQL_PASSWORD")

required_sql_server_vars = [
    "SQL_SERVER",
    "SQL_DATABASE",
    "SQL_USERNAME",
    "SQL_PASSWORD",
]
for var in required_sql_server_vars:
    if not app.config.get(var):
        raise ValueError(f"Missing environment variable: {var}")

db = SQLAlchemy(app)
