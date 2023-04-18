from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    serialnum = db.Column.db(db.String(80), unique=True, nullable=False)

    def __repr__(self):
        return '<Paperclip %r>' % self.serialnum
