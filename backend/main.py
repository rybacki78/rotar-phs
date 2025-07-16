from config import app, db
from routes import hour_entry_bp


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.register_blueprint(hour_entry_bp)
    app.run(debug=True)
