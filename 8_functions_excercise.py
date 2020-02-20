# Email Parsing 

def sum(a,b):
    return a+b

print(sum(1,2))

import random
import string
def create_random_emails():
    email_services = ["@gmail.com", "@yahoo.com", "@outlook.com", "@naver.com"]
    randlength = random.randrange(6,13,1)
    res = ""
    letters = string.ascii_lowercase
    res = "".join(random.choice(letters) for i in range(randlength))
    res = res + random.choice(email_services)
    return res


# Problem 1
# create_email_list()
# input : the desired number (int) of randomly generated emails
# output : a list of n randomly generated email strings (list of Strings), where n was the input

def create_email_list(desired_email_ct):
    res = [] # empty list
    for x in range(desired_email_ct):
        res.append(create_random_emails())
    return res

print(create_email_list(20))

#-----------------------------------------------------------------
# Problem 2
# count_email_services()
# input:    a list of email Strings (list of Strings)
# output:   a dictionary that shows the number of occurences of each emails 
# (dictionary w/ email strings as keys, count integer as values)

def count_email_services(email_list):
    result_dictionary = {} # curly brakets for dictionary
    for email in email_list: 
        # we want to find the index of the '@' symbol in each email
        # we'll search "find a char in string python" in Google, and look at
        # Python String's find() function
        email_service = email[email.find('@')+1:]
        if email_service in result_dictionary:
            result_dictionary[email_service] += 1
        else: 
            result_dictionary[email_service] = 1
    return result_dictionary 
    


#random_email_list = create_email_list(20)
#print(count_email_services(random_email_list))

# ---------------------------------------------------------
# Problem 3
# print the result

# print(create_email_list(20))  
# print(count_email_services(create_email_list(20))) # why is it different?
# because a call to create_email_list() creates a random list each time it's called

email_list = create_email_list(30)
print(count_email_services(email_list))

#----------------------------------------------------------------------------

# Problem 4
# Using real-life data, a .csv file
# We want to find out how to use a csv file (default Excel spreadsheet file) in a Python Program
# We'll search "read csv python" in Google, and look/follow https://pythonprogramming.net/reading-csv-files-python-3/
# If you want to learn more about file in/output streams with Python, visit https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
# We'll be using the "csv" module that Python provides; it provides functions that allow us easily read .csv files, without parsing!
# create_email_list_csv()
# input:    csv file's name (String)
# output:   list of emails Strings from the csv file (list of String)

import csv
def create_email_list_csv(input_file):
    res = []
    with open(input_file) as csvfile: 
        readCSV = csv.reader(csvfile, delimiter= ",")
        for row in readCSV:
            res.append(row[10])
        return res

email_list_csv = create_email_list_csv("100-contacts.csv")
print(count_email_services(email_list_csv))

#----------------------------------------------------------------------------

# Problem 5
# Get each email's usage percentage
# percantage = (#of times that email is found in list) / (# of all the emails)
# email_percentages()
# input:    a list of email Strings (list of Strings)
# output:   a dictionary that shows the usage percentage of each emails (dictionary w/ email strings as keys, percentage integer as values)

def email_percentages(email_list):
    email_total_count = len(email_list)
    email_dict = count_email_services(email_list)
    print(email_dict)

email_percentages(email_list)