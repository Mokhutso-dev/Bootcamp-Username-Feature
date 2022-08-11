from xml.dom import UserDataHandler
import datetime

def user_details():
    """
    Prompt user input
    """
    # First name input validation
    first_name = input("Insert your first name\n").lower()

    while first_name == "" or any(char.isdigit() for char in first_name):
        print("Invalid first name")
        first_name = input("Insert your first name\n").lower()

    # Last name input validation
    last_name = input("Insert your last name\n").lower()
    while last_name == "" or any(char.isdigit() for char in last_name):
        print("Invalid last name")
        last_name = input("Insert your last name\n").lower()

    # Cohort year input validation
    cohort = input("Insert your cohort\n")
    current_year = datetime.datetime.now().year

    while cohort == "" or not any(char.isdigit() for char in cohort) or int(cohort) < current_year:
        print("Invalid first name")
        cohort = input("Insert your cohort\n").lower()

    campus = input("Insert the campus you will be attending in\n").lower()

    username = create_user_name(first_name, last_name, cohort, user_campus(campus))
    print(username)


def user_campus(campus):
    """
    Return valid campus abbreviations
    """
    valid_campus = {
        "johannesburg": "JHB",
        "cape town": "CPT",
        "durban": "DBN",
        "phokeng": "PHO",
    }
    while not campus in valid_campus:
        print("Invalid campus")
        campus = input("Insert the campus you will be attending in\n").lower()
    final_campus = valid_campus[campus]
    return final_campus


def create_user_name(first_name, last_name, cohort, final_campus):
    """
    Create and return a valid username
    """
    # first name validation
    while len(str(first_name)) < 3:
        first_name += "o"
    first_name = first_name[-3:].lower()

    # last name validation
    while len(str(last_name)) < 3:
        last_name += "o"
    last_name = last_name[0:3].lower()

    username = first_name + last_name + str(cohort) + final_campus
    return username


if __name__ == '__main__':
    user_details()
