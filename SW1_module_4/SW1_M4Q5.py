password = str("rules")
account = str("python")
# Always remember kids, store decrypted passwords on your server!
# I know some of you ain't doing that. Shame on you.
accinput = str("")
passinput = str("")
tries = 0

while tries < 5:
    accinput = str(input("Enter username: "))
    passinput = str(input("Enter password: "))
    tries += 1
    if accinput == account and passinput == password:
        print("Welcome")
        break
    elif tries == 5:
        print("Access denied")
        break
    else:
        print("Incorrect username or password. Please try again.")




