from logging import log
from view import today,totals
from delete import delete_row, del_all


def main():

    print("\nStudy Tracker")
    print("1. Log a session")
    print("2. View today's sessions")
    print("3. View totals")
    print("4. Delete a log")
    print("5. Clear all logs")
    print("6. Quit")

    choice=int(input("Enter your choice: "))

    print('\n')

    match choice:
        case 1:
            log()
        case 2:
            today()
        case 3:
            totals()
        case 4:
            delete_row()
        case 5:
            del_all()
        case 6:
            print("Bye!!!")
            exit(1)
            
if __name__=="__main__":
    while True:
        main()


# how to view totals?
# date    subject     duration        notes     time

# how to delete a log?
# ask for the row to delete(simple)
    











        