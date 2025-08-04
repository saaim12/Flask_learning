from sqlalchemy import String,Integer

from app import db

class Employee(db.Model):
    id=db.Column(db.Integer,primary_key = True,nullable=False)
    age=db.Column(db.Integer,nullable=False)
    name=db.Column(db.String(100),nullable=False)
    department_id=db.Column(db.Integer,db.ForeignKey('department.id'),nullable=False)
    is_head_of = db.Column(db.String, db.ForeignKey('department.id'), nullable=True)
class Department(db.Model):
    id=db.Column(db.Integer,nullable=False,primary_key=True)
    name=db.Column(db.String(100),nullable=False)
    location = db.Column(db.String(120), nullable=False)
    employees = db.relationship('Employee',backref = 'department')
    head = db.relationship('Employee', backref='head_of_department',uselist=False)


#many to many relationship
project_members = db.Table('project_members',
    db.Column('employee_id', db.Integer, db.ForeignKey('employee.employee_id'), primary_key=True),
    db.Column('project_id', db.Integer, db.ForeignKey('project.project_id'), primary_key=True)
)

class Project(db.Model):
    project_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    members=db.relationship('Employee', secondary=project_members, backref='projects')