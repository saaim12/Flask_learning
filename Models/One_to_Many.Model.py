from sqlalchemy import String,Integer

from app import db

class Employee(db.Model):
    id=db.Column(db.Integer,primary_key = True,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    name=db.Column(db.String(100),nullable=False)
    department_id=db.Column(db.Integer,db.ForeignKey('department.id'),nullable=False)

class Department(db.Model):
    id=db.Column(db.Integer,nullable=False,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    location = db.Column(db.String(120), nullable=False)
    employees = db.relationship('Employee',backref = 'department')


class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)

