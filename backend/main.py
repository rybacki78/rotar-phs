from config import app, db
from routes import hour_entry, project


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.register_blueprint(hour_entry)
    app.register_blueprint(project)
    app.run(debug=True)
