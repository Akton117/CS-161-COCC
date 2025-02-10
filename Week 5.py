import requests
import psutil

def divisible_by_five():
    """Check if a number is divisible by 5."""
    num = int(input("Enter a number: "))
    if num % 5 == 0:
        print(f"{num} is divisible by 5.")
    else:
        print(f"{num} is not divisible by 5.")

def state_capital_if_elif():
    """Uses if-elif to determine the capital of a given state."""
    state = input("Enter a state name: ")
    if state == "Wisconsin":
        print("Madison")
    elif state == "Colorado":
        print("Denver")
    elif state == "Oregon":
        print("Salem")
    elif state == "Washington":
        print("Olympia")
    elif state == "Idaho":
        print("Boise")
    elif state == "California":
        print("Sacramento")
    else:
        print("I do not know that one.")

def state_capital_dict():
    """Uses a dictionary to find the capital of a given state."""
    states = {
        "Wisconsin": "Madison",
        "Colorado": "Denver",
        "Oregon": "Salem",
        "Washington": "Olympia",
        "Idaho": "Boise",
        "California": "Sacramento"
    }
    state = input("Enter a state name: ")
    print(states.get(state, "I do not know that one."))

def state_capital_match():
    """Uses match-case to determine the capital of a given state."""
    state = input("Enter a state name: ")
    match state:
        case "Wisconsin":
            print("Madison")
        case "Colorado":
            print("Denver")
        case "Oregon":
            print("Salem")
        case "Washington":
            print("Olympia")
        case "Idaho":
            print("Boise")
        case "California":
            print("Sacramento")
        case _:
            print("I do not know that one.")

def pool_admission(age):
    """Determines the price based on age."""
    if age < 2:
        return 0
    elif age < 12:
        return 3
    elif age <= 60:
        return 6
    else:
        return 4

def count_substring_in_html():
    """Counts how many times '160' appears in the HTML source"""
    url = "http://coccbobcat.com"
    response = requests.get(url)
    count = response.text.count("160")
    print(f'The substring "160" appears {count} times in the HTML source of {url}.')

def count_running_processes():
    """Counts the number of running processes on the system."""
    process_count = len(psutil.pids())
    print(f"Number of running processes: {process_count}")

# Run functions for testing
divisible_by_five()
state_capital_if_elif()
state_capital_dict()
state_capital_match()

age = int(input("Enter your age for pool admission price: "))
print(f"Your pool admission price is: ${pool_admission(age)}")

count_substring_in_html()
count_running_processes()
