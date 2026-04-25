import csv
from datetime import datetime

def log():

    # asking for input
    subject=input("Subject name: ")
    duration=float(input("Hours studied: "))
    notes=input("Notes: ")

    cur_date=datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

    # writing into the csv file
    with open("data.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([subject,duration,notes,cur_date])
    
    print("Logged successfully!")
