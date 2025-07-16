from config import db


class HourEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done_at = db.Column(db.Date, unique=False, nullable=False)
    project = db.Column(db.String(12), unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    user = db.Column(db.Integer, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "doneAt": self.done_at,
            "project": self.project,
            "quantity": self.quantity,
            "user": self.user,
            "createdAt": self.created_at,
        }
