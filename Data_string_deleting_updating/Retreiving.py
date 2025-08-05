# 📁 Import Model from Models Directory
from Models.User import User

# 🔎 1. Get All Users
users = User.query.all()
print("All Users:", users)

# 🔍 2. Get First User
first_user = User.query.first()
print("First User:", first_user)

# 🔑 3. Get User by Primary Key (Assuming email is the primary key)
user = User.query.get("veronica.lodge@email.com")
print("User by Primary Key:")
print(user)
print("Email:", user.email)
print("Password:", user.password)

# 🧪 4. Filter by Password (Returns BaseQuery object)
query = User.query.filter_by(password="football4life")
print("Base Query Object:", query)

print("*" * 20)

# ✅ 5. Get First Result from Filter
user = User.query.filter_by(password="football4life").first()
print("Filtered User:")
print(user)
print("Email:", user.email)
print("Password:", user.password)

# 🧾 6. Equivalent SQL Query
# SELECT user.email AS user_email, user.password AS user_password
# FROM user
# WHERE user.password = ?
# a full query would be like
Student.query.filter_by(batch = "2015").filter(Student.name.endswith("ah")).all()