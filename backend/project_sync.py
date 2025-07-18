from sql_server_conn import get_sql_server_conn
from config import app, db
from models import Project


def start_project_sync():

    with app.app_context():

        try:
            db.session.begin()

            cursor = get_sql_server_conn().cursor()

            cursor.execute("SELECT * FROM CSPRY_PHS_projects order by project")
            rows = cursor.fetchall()

            Project.query.delete()

            for row in rows:
                new_record = Project(
                    project=row.project,
                    item_prod=row.itemProd,
                    item_description=row.itemDescription,
                    quantity=row.quantity,
                    status=row.status
                )
                db.session.add(new_record)

            db.session.commit()

            return True, "Project sync done"
        
        except Exception as e:
            db.session.rollback()

            return False, f"Project sync failed, error: {e}"

        finally:
            if "cursor" in locals():
                cursor.close()
            if "conn" in locals():
                get_sql_server_conn().close()


if __name__ == "__main__":
    print(start_project_sync())