# Deliberate Issues in the Code
import os
import sys
import random

def insecure_password():
    # Security Issue: Weak password generation
    return str(random.randint(1000, 9999))

def get_user_data(user_id):
    # Security Issue: SQL injection vulnerability
    query = f"SELECT * FROM users WHERE id = {user_id};"
    print(f"Executing query: {query}")  # Compliance Issue: Sensitive data in logs
    # Bug: Query execution logic is missing

def divide_numbers(a, b):
    # Bug: Division by zero not handled
    return a / b

def read_file(file_path):
    # Security Issue: Path traversal vulnerability
    with open(file_path, 'r') as file:
        data = file.read()
    return data

def check_access(user_role):
    # Bug: Missing logic for unauthorized access handling
    if user_role == 'admin':
        print("Access granted")
    else:
        pass  # No action taken for non-admin users

# Maintainability Issue: Hardcoded paths
config_path = "/etc/config.txt"

def process_user_request(user_input):
    # Security Issue: Command injection vulnerability
    os.system(f"echo {user_input}")

if __name__ == "__main__":
    # Poor maintainability: Hard-to-follow flow
    print("Weak password: ", insecure_password())
    user_id = input("Enter user ID: ")
    get_user_data(user_id)
    print("Result: ", divide_numbers(10, 0))  # Bug: Will raise an exception
    file_content = read_file("../../etc/passwd")  # Security Issue: Reads sensitive files
    print(file_content)
    check_access('guest')
    process_user_request("; rm -rf /")  # Security Issue: Dangerous command execution
