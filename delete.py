import csv
import pandas as pd



def delete_row():
    
    df = pd.read_csv('data.csv', header=None)
    
    row_to_delete = int(input("Row to delete?: "))
    target_index = row_to_delete - 1
    
   
    if 0 <= target_index < len(df):
        
        df = df.drop(df.index[target_index])
        
        
        df.to_csv('data.csv', index=False, header=False)
        print('Row deleted successfully!')
    else:
        print("Invalid row number.")


def del_all():
    filename='data.csv'
    
    with open(filename,"w") as f:
        pass

