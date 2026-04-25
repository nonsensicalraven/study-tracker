import csv
from datetime import datetime

def today():
    target_date="25/04/2026"

    with open('data.csv',mode='r', encoding='utf-8-sig') as file:
        fields = ['subject', 'hrs', 'notes', 'dt_timestamp']
        reader=csv.DictReader(file, fieldnames=fields)

        print(f"{'Subject':<15} | {'Hours':<7} | {'Notes':<30} | {'Logging time'}")
        print('\n')

        for row in reader:

            row_date=row['dt_timestamp'][:10]
            if row_date==target_date:
                print(f"{row['subject']:<15} | {row['hrs']} hrs | {row['notes']:<30} | {row['dt_timestamp'][12:]}")

