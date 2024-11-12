import time
import sys

print ('argument list', sys.argv)
password = sys.argv[1]
print ("Hello Nikhil. Authenticating the password...")
print(f"Entered password: {password}")
assert password == 'pass', f"Incorrect password: {password}"
print("Welcome Boss")

