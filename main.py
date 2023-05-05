import csv
import subprocess

def attendance_text_sender():
    recipient = "+6149121374"
    message = "Message Text"

    # Build the AppleScript command as a string
    applescript = f'tell application "Messages" to send "{message}" to buddy "{recipient}" of service "SMS"'

    # Run the AppleScript command using the osascript module
    subprocess.call(['osascript', '-e', applescript])



#  with open("csv/testdata.csv", 'r') as csvfile:
#     csv_reader = csv.reader(csvfile)

#     next(csv_reader)

#     for row in csv_reader:
#        first_name = row[3]
#        ph_number = row[8]
#        #print(first_name + " " + ph_number)
#        if row[15] == "Check":
#           print(first_name + " " + ph_number)
#           print("txt sent")
#        if row[3] == '':
#           break




if __name__ == "__main__":
    attendance_text_sender()