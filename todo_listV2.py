# samod subhasha
# 16/14/2025

# somple to do app with OOP

data = {}
is_working = True
userdata ={"samod":"samod1"}
authentication = False
attempts = 0

print("Welcome to to do list in python using OOP!")
print("---------------------------------")

while authentication is not True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if attempts < 3:
        for values, keys in userdata.items():
            if values == username:
                print("User name access granted")
                if keys == password:
                    print("Password access granted ! ")
                    print(f"Welcome {username}")
                    authentication = True
                else:
                    print("wrong password!")
                    attempts += 1
                    print(f"You have {3-attempts} attempts left")
                    
            else:
                print("Wrong username ! try again!")
                attempts += 1
                print(f"You have {3-attempts} attempts left")


