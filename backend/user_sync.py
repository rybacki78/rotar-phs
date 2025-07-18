from sql_server_conn import get_sql_server_conn
from config import app, db
from models import User


def start_user_sync():

    with app.app_context():

        try:
            db.session.begin()

            cursor = get_sql_server_conn().cursor()

            cursor.execute("SELECT * from CSPRY_PHS_users order by exactNumber")
            rows = cursor.fetchall()

            User.query.delete()

            for row in rows:
                new_record = User(
                    last_name=row.lastName,
                    first_name=row.firstName,
                    exact_number=row.exactNumber,
                    in_phs=row.in_phs
                )
                db.session.add(new_record)

            db.session.commit()

            return True, "User sync done"

        except Exception as e:
            db.session.rollback()

            return False, f"User sync failed, error: {e}"

        finally:
            if "cursor" in locals():
                cursor.close()
            if "conn" in locals():
                get_sql_server_conn().close()


if __name__ == "__main__":
    start_user_sync()
