import random
from datetime import timedelta, date, datetime
import pandas as pd
import time
import os
import glob

def delete_files_folder(folder):
    "Delete files in folder"
    
    files = glob.glob("{0}/*".format(folder))
    for f in files:
        os.remove(f)
        
        
def get_word():
    "Returns a random word from a list"
    
    list_words = ["Spark", "Hadoop", "Python", "Scala", "Java", "Mesos"]
    
    return random.choice(list_words)


def generate_df(date_time, num_obs, time_delta):
    "Generate a Pandas DataFrame with two columns: 'word' and 'timestamp'"
    
    dict_data = {"word":[], "timestamp":[]}
    
    for _ in range(num_obs):
        
        date_time += time_delta
        dict_data["word"].append(get_word())
        dict_data["timestamp"].append(date_time.strftime("%Y-%m-%d %H:%M:%S"))
        
    return pd.DataFrame(dict_data, columns=["word", "timestamp"]), date_time


def generate_data(folder):
    "Generates csv files in the speficied folder"
    
    delete_files_folder(folder)
    
    time_delta = timedelta(seconds=10)
    ini_date = datetime(year=2000, month=1, day=1, hour=0, minute=0, second=0)
    num_data = 10
    
    for idx in range(100):
        print("Generating File: Iteration: {0}".format(idx))
        csv_name = os.path.join(folder, "file_{0}.csv".format(idx))
        df, ini_date = generate_df(ini_date, 10, time_delta)
        df.to_csv(csv_name, index=False, sep=",")
        time.sleep(10)
        
if __name__=="__main__":
    generate_data("../data/streaming")