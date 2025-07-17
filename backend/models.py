from config import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(12), unique=True, nullable=False)
    item_prod = db.Column(db.String(30), unique=False, nullable=False)
    item_description = db.Column(db.String(60), unique=False, nullable=False)
    status = db.Column(db.String(1), unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "project": self.project,
            "itemProd": self.item_prod,
            "itemDescription": self.item_description,
            "status": self.status,
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64), unique=False, nullable=False)
    first_name = db.Column(db.String(64), unique=False, nullable=False)
    exact_number = db.Column(db.Integer, unique=True, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "lastName": self.last_name,
            "firstName": self.first_name,
            "exactNumber": self.exact_number,
        }


class HourEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done_at = db.Column(db.Date, unique=False, nullable=False)
    project = db.Column(db.String(12), unique=False, nullable=False)
    quantity = db.Column(db.Numeric, unique=False, nullable=False)
    user = db.Column(db.Integer, unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    edited_at = db.Column(db.DateTime, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "doneAt": self.done_at,
            "project": self.project,
            "quantity": self.quantity,
            "user": self.user,
            "createdAt": self.created_at,
            "editedAt": self.edited_at,
        }
