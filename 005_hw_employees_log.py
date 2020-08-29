# Given 10000 logs...

    # 1. Group logs by employee

    # 2. Number of each category 'enter_for' an employee has entered
        # Example: 'Employee 1002 entered meeting 52 times, call 89 times.'

    # 3. Show rush-hours for entering facilities

import csv
import random
from datetime import datetime

# CONSTANTS
FILENAME = 'tmp/writing_csv.csv'
COLUMN_NAMES = ['employee_id', 'entered_at', 'enter_for']
MAX_NUMBER_LOGS = 101

#FUNCTIONS
# def fake_employee_id():
#     employee_id_list = []
#     for n in MAX_NUMBER_LOGS / 10:
#         employee_id_list.append(random.randint( 1, round(MAX_NUMBER_LOGS / 10)))
#     return random.choice(employee_id_list)

# print(fake_employee_id())
# print(random.randint( 1, round(MAX_NUMBER_LOGS / 10)))
for n in 10:
    print(random.randint( 1, round(MAX_NUMBER_LOGS / 10)))