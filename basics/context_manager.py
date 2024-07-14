



try:
    with open("test.txt") as f:   
        data = f.read()
        print(data)
except Exception as e:
    print(e)


## Custom Context Manager

# ---------------------- DatabaseConnection
import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
    
    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

with DatabaseConnection('example.db') as conn:
    cursor = conn.cursor()
    # Perform database operations

# ---------------------- Time a block of code
import time

class ExecutionTimer:
    def __enter__(self):
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.end_time = time.time()
        self.duration = self.end_time - self.start_time
        print(f"Execution time: {self.duration:.6f} seconds")

# Usage example
with ExecutionTimer():
    # Place the code block you want to measure here
    sum = 0
    for i in range(1000000):
        sum += i

