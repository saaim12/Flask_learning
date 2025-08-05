from Models.User import User
from app import db


#updating
user = User.query.get("veronica.lodge@email.com")
print(user)

user.email = "veronica@email.com"
try:
    db.session.commit()
except Excetion as e:
    db.session.rollback()

print("All Users : ", User.query.all())

#deleting
user = User.query.get("veronica.lodge@email.com")
print(user)

db.session.delete(user)

try:
    db.session.commit()
except Excetion as e:
    db.session.rollback()

print("All Users : ", User.query.all())