import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    print("------------------")
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length < 8:
                print("Password length should be at least 8 characters. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    password = generate_password(length)
    print("Generated Password:")
    print(password)

if __name__ == "__main__":
    main()