import csv
import os
from prettytable import PrettyTable
from pushbullet import Pushbullet


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def send_sms(phone_number, message):
    pb = Pushbullet('o.dQ75BMOxjgber6nLxVC7RwxyRTHMBTbs')

    device = pb.devices[1]
    push = pb.push_sms(device, phone_number, message)
    if push.active:
        print('SMS sent successfully.')
    else:
        print('Failed to send SMS.')


def index_table(csvreader):
    first_row = next(csvreader)
    table = PrettyTable()
    table.field_names = ["Index", "Field Name"]
    for index, value in enumerate(first_row):
        table.add_row([index, value], divider=True)
    print(table)
    print("")


def print_table(csv_reader, first_name_i, phone_number_i, date_i):
    table = PrettyTable()

    header = next(csv_reader)
    table.field_names = [header[first_name_i], header[phone_number_i], header[date_i]]

    for row in csv_reader:
        first_name = row[first_name_i]
        phone_number = row[phone_number_i]
        filter = row[date_i]
        if first_name != "":
            table.add_row([first_name, phone_number, filter])
    print(table)
    print("")

def print_filtered_table(csv_reader, send_list, first_name_i, phone_number_i, date_i):
    table = PrettyTable()

    header = next(csv_reader)
    table.field_names = [header[first_name_i], header[phone_number_i], header[date_i]]

    for row in send_list:
        table.add_row(row) 
    
    print(table)
    print("")


def attendance_text_sender():
    table = PrettyTable()
    with open("csv/attendance.csv", 'r') as csvfile:
        csv_reader = csv.reader(csvfile)

        index_table(csv_reader)
        csvfile.seek(0)

        first_name_index = int(input("Enter index of first name coloum: "))
        phone_number_index = int(input("Enter index of the Phone Number coloum: "))
        date_index = int(input("Enter index of the date to filter by: "))

        # clear_terminal()
        print_table(csv_reader, first_name_index, phone_number_index, date_index)
        csvfile.seek(0)

        filter_value = input('Enter value to filter by. eg. "Check": ')
        # clear_terminal()

        send_list = []
        for row in csv_reader:
            if row[date_index] == filter_value:
                send_list.append([row[first_name_index], row[phone_number_index], row[date_index]])
        csvfile.seek(0)
        
        print_filtered_table(csv_reader, send_list, first_name_index, phone_number_index, date_index)


        

        




if __name__ == "__main__":
    attendance_text_sender()




