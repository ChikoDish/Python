users = []
print("************************Please sing up************************")
reg_user = input("Enter user name: ")
reg_pass = input("Enter password: ")
user_dist = {"username": reg_user, "password": reg_pass}
users.append(user_dist)
print("Successfully signed up!")
print("************************Please login************************")
log_user = input("Enter user name: ")
log_pass = input("Enter password: ")

for user in users:
    if user.get("username") == log_user and user.get("password") == log_pass:
        print("You have successfully logged in")
    else:
        print("No user found")
        
