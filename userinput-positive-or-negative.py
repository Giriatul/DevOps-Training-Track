user_number = input("Enter your number ")

print("\n")
try:
    val = int(user_number)
    if val > 0:
        print("User number is positive ")
    else:
        print("User number is negative ")
except ValueError:
    print("No.. input string is not a number. It's a string")
    
    
