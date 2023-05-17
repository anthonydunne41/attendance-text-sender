from pushbullet import Pushbullet



def send_sms():

    pb = Pushbullet('o.dQ75BMOxjgber6nLxVC7RwxyRTHMBTbs')

    device = pb.devices[1]







# def attendance_text_sender():
#     with open("csv/testdata.csv", 'r') as csvfile:
#         csv_reader = csv.reader(csvfile)

#         next(csv_reader)

#         for row in csv_reader:
#             first_name = row[3]
#             ph_number = row[8]
#             state = row[15]

#             print(f"{first_name} {state}")
#             if row[15] == "Check":
#                 # print(first_name + " " + ph_number)
#                 print("txt sent")
#             if row[3] == '':
#                 break




if __name__ == "__main__":
    send_sms()




    #push = pb.push_sms(device, "0401249642", "Python text message!")
    # if push.active:
    #     print('SMS sent successfully.')
    # else:
    #     print('Failed to send SMS.')