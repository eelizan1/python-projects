import pandas as pd
import csv
from datetime import datetime
from data_entry import get_amount, get_category, get_date, get_description

# CSV: Manages reading from and writing to the local finance data CSV file.
# Handles file initialization and appending new transaction entries.
class CSV:
    # will live in the class itself not on instances 
    CSV_FILE = "finaince_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    FORMAT = "%d-%m-%Y"

    # annotation for method to be called on the class itslef on on an instance
    @classmethod # note that we dont need to pass in a cls instance when calling CSV.initialize_csv() since the class is auto passed in
    def initialize_csv(cls): # "cls" - class 
        try: 
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError: 
            # specify the columns in csv file using data frame
            df = pd.DataFrame(columns=cls.COLUMNS) 
            # converted to CSV file and save locally
            df.to_csv(cls.CSV_FILE, index=False)

    
    @classmethod 
    def add_entry(cls, date, amount, category, description): 
        # create new entry with a dictionary
        new_entry = {
            "date" : date, 
            "amount" : amount, 
            "category" : category, 
            "description" : description
        }

        # Opens the CSV file 
        with open(cls.CSV_FILE, "a", newline="") as csvfile: 
            # take a dictionary and write it to the CSV file 
            writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        
        print("Entry added successfully")
    
    @classmethod
    def get_transaction(cls, start_date, end_date): 
        df = pd.read_csv(cls.CSV_FILE)
        df["date"] = pd.to_datetime(df["date"], format=cls.FORMAT)
        start_date = datetime.strptime(start_date, cls.FORMAT)
        end_date = datetime.strptime(end_date, cls.FORMAT)

        # check if current row that we're looking at is in the date range 
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        # locating (loc) all the rows where the mask applies 
        filtered_df = df.loc[mask]

        if filtered_df.empty: 
            print('No transactions found in date range')
        else: 
            print(f"Transaction from {start_date.strftime(CSV.FORMAT)} to {end_date.strftime(cls.FORMAT)}")
            print(filtered_df.to_string(index=False, formatters={"date" : lambda x : x.strftime(cls.FORMAT)}))
        
        total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
        total_expense = filtered_df[filtered_df["category"] == "Expense"]["amount"].sum()

        print("\nSummary:")
        print(f"Total Income: ${total_income:.2f}") # round to two dec places 
        print(f"Total Expense: ${total_expense:.2f}") # round to two dec places 
        print(f"Net savings: ${(total_income - total_expense):.2f}")

        return df

# outside CSV class so can call like "add()"
def add(): 
    CSV.initialize_csv()
    date = get_date("Enter the date of the transaction (dd-mm-yyy) or hit enter for today's date:", allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description() 

    CSV.add_entry(date, amount, category, description)


CSV.get_transaction("01-01-2023", "30-07-2024")
#add() 