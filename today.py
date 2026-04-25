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

