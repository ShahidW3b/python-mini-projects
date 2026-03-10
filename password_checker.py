password = input("Enter your password ")

length = len(password)
has_digit = False
has_upper = False

for char in password:
    if char.isdigit():
        has_digit = True

    if char.isupper():
        has_upper = True

if length >= 8 and has_digit and has_upper and ("@" in password or "!" in password or "?" in password):
    print("Password is Strong")

elif length >= 8 and has_digit and has_upper:
    print("Password is Medium")

elif length < 8:
    print("Password is Weak")

else:
    print("Wrong Entry")
