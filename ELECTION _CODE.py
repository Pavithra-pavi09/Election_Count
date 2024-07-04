import mysql.connector
import datetime
import smtplib
import random

x = datetime.datetime.now()
current = x.strftime("%H:%M:%S %p")
f=open("bill.txt","a")
f.write("\n***SUPER MARKET**\n")
f.write(f"\nTime of Purchase is {current}\n")

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="election_db"
)
mycursor=mydb.cursor()

def insert_data():
    candidate_id = int(input("Enter your candidate_id number: "))
    voter_name = input("Enter your name: ")
    voter_mailid = input("Enter your mail id: ")

    # Insert the vote into the votes table
    sql_insert_vote = "INSERT INTO votes (candidate_id, voter_name, voter_mailid) VALUES (%s, %s, %s)"
    val = (candidate_id, voter_name, voter_mailid)
    mycursor.execute(sql_insert_vote, val)
    
    # Update the vote count in the candidates table
    sql_update_vote_count = "UPDATE candidates SET vote_count = vote_count + 1 WHERE candidate_id = %s"
    mycursor.execute(sql_update_vote_count, (candidate_id,))

    mydb.commit()
    print("Data saved successfully and updated the count.")
    email_sending ('Thank you for voting!', 'Your vote has been recorded.')
insert_data()    

def view_data():
    mycursor.execute("SELECT * FROM candidates")
    myresult = mycursor.fetchall()
    for record in myresult:
        print(record)
view_data()

def email_sending():
    try:
        receiver_mails=["durpavadhaarani@gmail.com"]
        for i in receiver_mails:
            otp_number=random.randint(0000,9999)
            print(i,otp_number)
            s=smtplib.SMTP('SMTP.gmail.com',587)
            s.starttls()
            s.login("adipavi2005@gmail.com","aryn vqxl iupq oxet")
            message=f" your otp number is {otp_number}"
            s.sendmail("adipavi2005@gmail.com",i,message)
            s.quit()
            print("mail sent successfully")
    except:
        print("mail not sent")             