import csv
import os.path


def addEmail(to_addr):
    with open('./assets/knownemails.csv', 'a', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        name = input("name: ")
        csvwriter.writerow([name, to_addr])


def sendmail():
    print("mail sent")


def newfun():
    to_addr = input(f"To whom do you want to send the e-mail? : ")
    try:
        with open('./assets/knownemails.csv', 'r') as file:
            dict1 = csv.DictReader(file)
            print(dict1)
            for row in dict1:
                print(row['Email'])
                if row['Email'] == to_addr:
                    print("Email found!")
                    status = 1
                    break
                    # addEmail(to_addr)
                    # return
                else:
                    print("Email not found!")
                    status = 0
                    # sendmail()
                    # return
    except IOError:
        with open('./assets/knownemails.csv', 'a', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(["Name", "Email"])
            name = input("name: ")
            csvwriter.writerow([name, to_addr])
    if status == 0:
        addEmail(to_addr)
        sendmail()
    else:
        sendmail()



newfun()