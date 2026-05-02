import pandas as pd 
import csv 
from datetime import datetime 

class CSV: 
    # will live in the class itself not on instances 
    CSV_FILE = "finaince_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]

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

CSV.initialize_csv()
CSV.add_entry("20-07-2024", 125.65, "Income", "Salary")