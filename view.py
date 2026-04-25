import csv
from datetime import datetime

def today():
    target_date=str(datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))[:10]

    with open('data.csv',mode='r', encoding='utf-8-sig') as file:
        fields = ['subject', 'hrs', 'notes', 'dt_timestamp']
        reader=csv.DictReader(file, fieldnames=fields)

        print(f"{'Subject':<15} | {'Hours':<7} | {'Notes':<30} | {'Logging time'}")
        print('\n')

        for row in reader:

            row_date=row['dt_timestamp'][:10]
            if row_date==target_date:
                log_time = row['dt_timestamp'][11:17]
                print(f"{row['subject']:<15} | {row['hrs']} hrs | {row['notes']:<30} | {log_time}")


def totals():

    with open('data.csv',mode='r', encoding='utf-8-sig') as file:
        fields = ['subject', 'hrs', 'notes', 'dt_timestamp']
        reader=csv.DictReader(file, fieldnames=fields)

        print(f"{'S.No':<4} | {'Date':<10} | {'Subject':<15} | {'Hours':<7} | {'Notes':<30} | {'Logging time'}")
        print(f"{'':<4} | {'':<10} | {'':<15} | {'':<7} | {'':<30} | {''}")
        

        count=1

        for row in reader:
            
            row_date=row['dt_timestamp'][:10] 
            log_time = row['dt_timestamp'][11:17]

            print(f"{count:<4} | {row_date} | {row['subject']:<15} | {row['hrs']} hrs | {row['notes']:<30} | {log_time}")
            count=count+1

