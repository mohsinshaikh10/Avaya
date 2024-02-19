import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from chatBot.accountcredentials import senderAddress ,  passw
import csv
import os.path

def addEmail(to_addr):
    with open('./assets/knownemails.csv', 'a', newline="") as csvfile:
        csvwriter = csv.writer(csvfile)
        name = input("name: ")
        csvwriter.writerow([name, to_addr])

def sendEmail(to_addr):
    from_addr = senderAddress
    # to_addr = "shubhammahindrakar82@gmail.com"
    # to_addr = ['jgduyfh@gmail.com', 'hisbdcuegf.@gmail.com']
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    # msg['To'] = " ,".join(to_addr)
    mysub = input("Tell the subject for mail :")
    msg['subject'] = mysub
    mytext = input("What do you want me to write: ")
    body = mytext
    msg.attach(MIMEText(body, 'plain'))
    email = senderAddress
    password = passw
    try:
        print("Connecting to server and sending mail")
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(email, password)
        text = msg.as_string()
        mail.sendmail(from_addr, to_addr, text)
        mail.quit()
    except:
        print("Message not send")
    else:
        with open('./assets/knownemails.csv', 'r') as read_obj:
            csv_dict_reader = csv.DictReader(read_obj)
            for row in csv_dict_reader:
                if row['Email'] == to_addr:
                    print(row['Name'])
        print(f"E-mail sent successfully!")

def mymailerfunc():
    print(f"To whom do you want to send the e-mail?")
    to_addr = input()
    status = 0
    if os.path.isfile('./assets/knownemails.csv'):
        with open('./assets/knownemails.csv', 'r') as read_obj:
            csv_dict_reader = csv.DictReader(read_obj)
            for row in csv_dict_reader:
                print(row['Email'],row['Name'])
                if row['Email'] == to_addr:
                    print("Email found!")
                    status =1
                    print(status)
                    break
                else:
                    print("Email not found!")
                    print("2")
                        # file.close

    else:
        with open('./assets/knownemails.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Email"])
            print("New File created!\nEntering first row of file")
            namefield = input("Enter Name: ")
            emailfield = to_addr
            writer.writerow([namefield, emailfield])

    if status == 0:
        addEmail(to_addr)
        sendEmail(to_addr)
    else:
        sendEmail(to_addr)

# mymailerfunc()
# if status == 1:


"""
from_addr = senderAddress
# to_addr = "shubhammahindrakar82@gmail.com"
# to_addr = ['jgduyfh@gmail.com', 'hisbdcuegf.@gmail.com']
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
# msg['To'] = " ,".join(to_addr)
msg['subject'] = 'Check mail'
body = 'hello world'
msg.attach(MIMEText(body, 'plain'))
email = senderAddress
password = password
try:
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(email, password)
    text = msg.as_string()
    mail.sendmail(from_addr, to_addr, text)
    mail.quit()
except:
    print("Message not send")
else:
    with open('knownemails.csv', 'r') as read_obj:
        csv_dict_reader = csv.DictReader(read_obj)
        for row in csv_dict_reader:
            if row['Email'] == to_addr:
                print(row['Name'])
    print(f"E-mail sent successfully!")
    
"""