def password():
    passkey = input("Enter the password: ")
    
    # Criteria
    if len(passkey) < 10:
        print("Password should be at least 10 characters long.")
        return password()
    
    if sum(1 for c in passkey if c.isupper()) < 2:
        print("Password should contain at least two uppercase letters.")
        return password()

    if sum(1 for c in passkey if c.islower()) < 2:
        print("Password should contain at least two lowercase letters.")
        return password()

    if sum(1 for c in passkey if c.isdigit()) < 2:
        print("Password should contain at least two digits.")
        return password()

    special_characters = "!@#$%^&*()-_=+[{]}|;:',<.>/?"
    if sum(1 for c in passkey if c in special_characters) < 2:
        print("Password should contain at least two special characters.")
        return password()

    for i in range(len(passkey) - 3):
        if passkey[i] == passkey[i+1] == passkey[i+2] == passkey[i+3]:
            print("Password should not contain more than three consecutive same characters.")
            return password()

    for prev_pass in previous:
        if passkey == prev_pass:
            print("Password matches the previously set password.")
            return password()

    for i in range(len(passkey) - 2):
        for j in range(len(username) - 2):
            if passkey[i:i+3] == username[j:j+3]:
                print("Password should not contain sequence of three or more consecutive characters from the username.")
                return password()

    print("Password Verified Successfully!!!")

# Criteria
print("Hi, Welcome to the Password Generator!")
print("Your password should match the following criteria:")
print("(1) It must be at least 10 characters long.")
print("(2) It must contain at least 2 uppercase letters.")
print("(3) It must contain at least 2 lowercase letters.")
print("(4) It must contain at least 2 special characters.")
print("(5) It should not contain any sequence of three or more consecutive letters from the username.")
print("(6) No character should repeat more than three times in a row.")
print("(7) The new password must not be the same as the previous three passwords.")

# Obtaining username
username = input("Enter the Username: ")

# Obtaining previous passwords
previous = []
for _ in range(3):
    previous.append(input(f"Enter the {['first', 'second', 'third'][_]} last password: "))

# Obtaining password
password()
