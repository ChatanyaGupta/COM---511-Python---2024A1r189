#Write a python program that asks the user to enter the username and password .The user should get only 3 attempts>
# If the correct credentials are entered ,display"Login successfully " and stop the loop.If all attempts are used ,display"Account locked
# Program to check username and password
correct_username = "Chatanya"
correct_password = "1234"
attempts = 0
while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login successfully")
        break
    else:
        print("Incorrect username or password")
        attempts += 1

if attempts == 3:
    print("Account locked")