import random
import string
characters = string.ascii_letters + string.digits
def crack_password(password):
    attempts = 0
    length = len(password)
    while True:
        guess = ''.join(random.choices(characters, k=length))
        attempts += 1
        if guess == password:
            return attempts
        
def main():
    while True:
        password = input("Enter a password to crack: ")
        print("Cracking password...")
        attempts = crack_password(password)
        print(f"Password cracked in {attempts} attempts.")

main()


