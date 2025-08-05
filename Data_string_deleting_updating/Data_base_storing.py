#first we make an object of user
from Models.User import User
from app import db
newuser= User(email = "archie.andrews@email.com", password = "football4life")
# then store in database
db.session.add(newuser)
db.session.commit()
#📌 Note: the session variable indicates an ongoing transaction of changes to the database. It keeps a record of insertion, updates, and deletion.
#without committing the changes, the updated state will not persist in the database. It will only remain persistent in the current session. In other words, if we do not commit these changes, but try to retrieve this object in the current session, we will be successful. But, when this session closes, everything we inserted/updated will be lost.