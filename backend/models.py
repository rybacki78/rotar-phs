from config import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project = db.Column(db.String(12), unique=True, nullable=False)
    item_prod = db.Column(db.String(30), unique=False, nullable=False)
    item_description = db.Column(db.String(60), unique=False, nullable=False)
    quantity = db.Column(db.Integer, unique=False, nullable=False)
    status = db.Column(db.String(1), unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "project": self.project,
            "itemProd": self.item_prod,
            "itemDescription": self.item_description,
            "quantity": self.quantity,
            "status": self.status,
        }


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(64), unique=False, nullable=True)
    first_name = db.Column(db.String(64), unique=False, nullable=True)
    exact_number = db.Column(db.Integer, unique=True, nullable=False)
    in_phs = db.Column(db.Boolean, unique=False, nullable=False)

    def to_json(self):
        return {
            "id": self.id,
            "lastName": self.last_name,
            "firstName": self.first_name,
            "exactNumber": self.exact_number,
            "inPhs": self.in_phs,
        }


class HourEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    done_at = db.Column(db.Date, unique=False, nullable=False)
    project = db.Column(db.String(12), db.ForeignKey('project.project'), unique=False, nullable=False)
    quantity = db.Column(db.Numeric, unique=False, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('user.exact_number'), unique=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    edited_at = db.Column(db.DateTime, nullable=False)

    project_rel = db.relationship('Project', foreign_keys=[project], backref='hour_entries')
    user_rel = db.relationship('User', foreign_keys=[user], backref='hour_entries')

    def to_json(self):
        return {
            "id": self.id,
            "doneAt": self.done_at,
            "project": self.project,
            "quantity": self.quantity,
            "user": self.user,
            "createdAt": self.created_at,
            "editedAt": self.edited_at,
            "projectDetails": self.project_rel.to_json() if self.project_rel else None,
            "userDetails": self.user_rel.to_json() if self.user_rel else None
        }
