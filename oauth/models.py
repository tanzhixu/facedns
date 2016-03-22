from app import db
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    __tablename__ = 'user'
    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String(64), unique=True, index=True)
    password_hash   = db.Column(db.String(120))
    dname           = db.relationship('Dname', backref='user', lazy='dynamic')

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)


class Dname(db.Model):
    __tablename__ = 'dname'
    id      = db.Column(db.Integer, primary_key=True)
    dname   = db.Column(db.String(64), unique=True)
    userid  = db.Column(db.Integer, db.ForeignKey('user.id'))
    record  = db.relationship('Record', backref='dname', lazy='dynamic')


class Record(db.Model):
    __tablename__ = 'record'
    id          = db.Column(db.Integer, primary_key=True)
    record      = db.Column(db.String(30), unique=True)
    type        = db.Column(db.String(10), unique=True)
    line_type   = db.Column(db.String(20), default = None)
    value       = db.Column(db.String(100), unique=True)
    weight      = db.Column(db.String(100), default=None)
    mx          = db.Column(db.String(20))
    ttl         = db.Column(db.Integer, unique=True)
    dname_id    = db.Column(db.Integer, db.ForeignKey('dname.id'))
