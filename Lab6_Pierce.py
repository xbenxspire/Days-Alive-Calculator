'''
Created on Sep 27, 2023
@author: Benjamin Pierce
This program has the user input their name, age, DOB and will calculate how many days ago they were born.
'''
import datetime    #imports datetime module

def main():

    #Acquire user information
    full_name = input("Enter your full name <first last>: ")
    age = int(input("Enter your age: "))
    date_of_birth = input("Enter your date of birth <month day year>: ")

    #Convert date_of_birth to datetime object
    dob = datetime.datetime.strptime(date_of_birth, "%m %d %Y")

    #Calculate number of days old
    today = datetime.datetime.now()
    days_old = (today - dob).days

    # Create output message
    message = (f"Hello {full_name}!\nYou are {age} years old and that means you were born {days_old} days ago on {date_of_birth}.")

    # Write the message to date_report.txt
    with open("date_report.txt", "w") as file:
        file.write(message)

if __name__ == "__main__":
    main()