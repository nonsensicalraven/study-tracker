import csv
def log():

    # asking for input
    subject=input("Subject name: ")
    duration=int(input("Hours studied: "))
    notes=input("Notes: ")

    # writing into the csv file
    with open("data.csv","a",newline="") as file:
        writer = csv.writer(file)
        writer.writerow([subject,duration,notes])
