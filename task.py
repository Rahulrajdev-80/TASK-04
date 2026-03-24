#Mini Project 1: Employee Management System Concepts: Dictionary, List, Function
employees = []

def add_employee():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    role = input("Enter role: ")
    salary = float(input("Enter salary: "))
    
    emp = {"name": name, "age": age, "role": role, "salary": salary}
    employees.append(emp)
    print("Employee Added")

def display_employees():
    if not employees:
        print("No employees found")
    else:
        for i, emp in enumerate(employees):
            print(i, emp)

def update_employee():
    display_employees()
    index = int(input("Enter index to update: "))
    
    if 0 <= index < len(employees):
        employees[index]["name"] = input("Enter new name: ")
        employees[index]["age"] = int(input("Enter new age: "))
        employees[index]["role"] = input("Enter new role: ")
        employees[index]["salary"] = float(input("Enter new salary: "))
        print("Employee Updated")
    else:
        print("Invalid index")

def delete_employee():
    display_employees()
    index = int(input("Enter index to delete: "))
    
    if 0 <= index < len(employees):
        employees.pop(index)
        print("Employee Deleted")
    else:
        print("Invalid index")

while True:
    print("\n1.Add 2.Display 3.Update 4.Delete 5.Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        add_employee()
    elif choice == 2:
        display_employees()
    elif choice == 3:
        update_employee()
    elif choice == 4:
        delete_employee()
    elif choice == 5:
        break
    else:
        print("Invalid choice")



# Mini Project 2: Student Report Card Concepts: Dictionary, Functions, Formatting
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

def report_card():
    name = input("Enter student name: ")
    
    m1 = int(input("Enter marks for Subject 1: "))
    m2 = int(input("Enter marks for Subject 2: "))
    m3 = int(input("Enter marks for Subject 3: "))
    
    total = m1 + m2 + m3
    avg = total / 3
    grade = calculate_grade(avg)
    
    print("\n----- Report Card -----")
    print("Name :", name)
    print("Marks :", m1, m2, m3)
    print("Total :", total)
    print("Average :", avg)
    print("Grade :", grade)

report_card()

#Mini Project 3: Shopping Cart System Concepts: List, Dictionary, Loop

cart = []

def add_item():
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))
    
    item = {"name": name, "price": price, "qty": qty}
    cart.append(item)
    print("Item Added")

def display_cart():
    if not cart:
        print("Cart is empty")
    else:
        print("\n--- Cart Items ---")
        for i, item in enumerate(cart):
            print(i, item["name"], "| Price:", item["price"], "| Qty:", item["qty"])

def remove_item():
    display_cart()
    index = int(input("Enter index to remove: "))
    
    if 0 <= index < len(cart):
        cart.pop(index)
        print("Item Removed")
    else:
        print("Invalid index")

def total_bill():
    total = 0
    for item in cart:
        total += item["price"] * item["qty"]
    print("Total Bill:", total)

while True:
    print("\n1.Add 2.Display 3.Remove 4.Total 5.Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        add_item()
    elif choice == 2:
        display_cart()
    elif choice == 3:
        remove_item()
    elif choice == 4:
        total_bill()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

#Mini Project 4: Login & User Validation Concepts: Dictionary, Condition
users = {
    "admin": "1234",
    "ravi": "pass1",
    "meena": "pass2"
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Invalid Username or Password")    

#Mini Project 5: Unique Visitor Counter Concepts: Set
visitors = set()

while True:
    name = input("Enter visitor name (or type 'stop'): ")
    
    if name == "stop":
        break
    
    visitors.add(name)

print("Unique Visitors:", visitors)
print("Total Unique Visitors:", len(visitors)) 

#Mini Project 6: String Formatter Tool Concepts: String Formatting
name = input("Enter name: ")
product = input("Enter product: ")

sentence = f"{name} purchased {product}"
print(sentence)

print(name.ljust(20, "-"))
print(name.rjust(20, "-"))
print(name.center(20, "-"))

#Mini Project 6: String Formatter Tool Concepts: String Formatting
name = input("Enter name: ")
product = input("Enter product: ")

sentence = f"{name} purchased {product}"
print(sentence)

print(name.ljust(20, "-"))
print(name.rjust(20, "-"))
print(name.center(20, "-"))

#Mini Project 7: Bank Account System Concepts: Functions, Dictionary
account = {}

def create_account():
    name = input("Enter name: ")
    balance = float(input("Enter initial balance: "))
    account["name"] = name
    account["balance"] = balance
    print("Account Created")

def deposit():
    amount = float(input("Enter amount to deposit: "))
    account["balance"] += amount
    print("Amount Deposited")

def withdraw():
    amount = float(input("Enter amount to withdraw: "))
    if amount <= account["balance"]:
        account["balance"] -= amount
        print("Amount Withdrawn")
    else:
        print("Insufficient Balance")

def check_balance():
    print("Name:", account.get("name"))
    print("Balance:", account.get("balance"))

while True:
    print("\n1.Create 2.Deposit 3.Withdraw 4.Check 5.Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        create_account()
    elif choice == 2:
        deposit()
    elif choice == 3:
        withdraw()
    elif choice == 4:
        check_balance()
    elif choice == 5:
        break
    else:
        print("Invalid choice")

#Mini Project 8: Voting System Concepts: Dictionary, Loop
votes = {}

def add_vote():
    name = input("Enter candidate name: ")
    if name in votes:
        votes[name] += 1
    else:
        votes[name] = 1
    print("Vote Added")

def display_winner():
    if not votes:
        print("No votes yet")
    else:
        winner = max(votes, key=votes.get)
        print("\nVotes:", votes)
        print("Winner:", winner, "with", votes[winner], "votes")

while True:
    print("\n1.Vote 2.Winner 3.Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        add_vote()
    elif choice == 2:
        display_winner()
    elif choice == 3:
        break
    else:
        print("Invalid choice")    


#Mini Project 9: Course Enrollment System Concepts: List + Dictionary
students = []

def add_student():
    name = input("Enter student name: ")
    courses = input("Enter courses (comma separated): ").split(",")
    
    student = {"name": name, "courses": courses}
    students.append(student)
    print("Student Added")

def update_courses():
    display_students()
    index = int(input("Enter index to update: "))
    
    if 0 <= index < len(students):
        courses = input("Enter new courses (comma separated): ").split(",")
        students[index]["courses"] = courses
        print("Courses Updated")
    else:
        print("Invalid index")

def display_students():
    if not students:
        print("No students found")
    else:
        for i, s in enumerate(students):
            print(i, "Name:", s["name"], "| Courses:", ", ".join(s["courses"]))

while True:
    print("\n1.Add 2.Update 3.Display 4.Exit")
    choice = int(input("Enter choice: "))
    
    if choice == 1:
        add_student()
    elif choice == 2:
        update_courses()
    elif choice == 3:
        display_students()
    elif choice == 4:
        break
    else:
        print("Invalid choice")

#Mini Project 10: Number Utility Tool Concepts: Functions, Formatting
def convert_number(n):
    print("Binary:", bin(n))
    print("Octal:", oct(n))
    print("Hexadecimal:", hex(n))

def format_number(n):
    print("With commas:", f"{n:,}")
    print("Scientific notation:", f"{n:.2e}")

n = int(input("Enter number: "))

convert_number(n)
format_number(n)        
