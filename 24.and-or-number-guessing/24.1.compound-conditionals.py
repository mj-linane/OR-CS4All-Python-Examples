# Compound Conditions
access_security_lvl = 3

username = ""
while not username:
    username = input("Username: ")

password = ""
while not password:
    password = input("Password: ")

# AND Operator
if username == "S.Johansson" and password == "BlackWidow" and access_security_lvl == 2:
    print("Hello Black Widow!")

elif username == "T.Stark" and password == "IronMan":
    print("Whats up, Ironman?")

elif username == "S.Rogers" and password == "CaptainAmerica":
    print("Hello Capt")

elif username == "B.Banner" and password == "Hulk":
    print("Hulk Smash")

# OR Operator
elif username == "guest" or password == "guest":
    print("Guest access granted")

else:
    print("Login Failed. Incorrect username and/or password")
