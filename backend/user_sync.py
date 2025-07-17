from sql_server_conn import get_sql_server_conn
from config import app, db
from models import User


def start_user_sync():

    with app.app_context():

        cursor = get_sql_server_conn().cursor()

        cursor.execute("SELECT * from CSPRY_PHS_users")
        rows = cursor.fetchall()

        for row in rows:
            new_record = User(
                last_name=row.lastName,
                first_name=row.firstName,
                exact_number=row.exactNumber,
            )
            db.session.add(new_record)

        db.session.commit()

        cursor.close()
        get_sql_server_conn().close()


if __name__ == "__main__":
    start_user_sync()
