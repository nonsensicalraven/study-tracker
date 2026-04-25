from logging import log
from today import today

def main():
    print("Study Tracker")
    print("1. Log a session")
    print("2. View today's sessions")
    print("3. View totals")
    print("4. Quit")

main()

choice=int(input("Enter your choice: "))


match choice:
    case 1:
        log()
    case 2:
        today()
#     case 3:
#         # viewing totals
#     case 4:
#         # exit
    



#1. log date 
    # ->manual
    # ->automatic(done)

# 2. to view today's sessions
    # format:-
        # date:-     time:-
        # subject:-    hrs_studied:-
        # notes:- 







        