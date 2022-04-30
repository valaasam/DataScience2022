#!/usr/bin/env python
# coding: utf-8

# In[ ]:


## Final Project Script
#### Valentina Alaasam
#### April 2022
#### Data Science for Biology II 

#!/usr/bin/env python3

import os
import os.path
import glob
import numpy as np
import pandas as pd
from datetime import datetime
from pathlib import Path

#create path for outfile
outdir_path = input("type path for OUTPUT directory, no quotes (hint: /Users/val/Desktop/hop_data/hopdata_cleaned): ")
os.makedirs(outdir_path, exist_ok=True)
os.chdir(outdir_path)
print("Directory for output is set up!")

                     
# Set up for big loop                     
path = input("type path for INPUT directory, no quotes (hint: /Users/val/Desktop/hop_data/july_samples): ")
folder = os.fsencode(path)
all_files = glob.glob(os.path.join(path, "*.txt"))

counter = 0
print("files completed:0 ")
     
# Big loop, here we go!

for file in all_files:
    # Read in file
    df=pd.read_csv(file, header=None, sep='\t')
             
    # Remove last column, which is all NAs
    df = df.dropna(axis=1, how='all')   
             
    #  Assign every 24 rows to an integer 
    Hours_list = list(range(24))
    df.insert(loc=0,
          column='hour',
          value=Hours_list*24)
             
    # Add bird ID to each 24 rows
    BirdIDs = list(range(1,25,1))
    Birds_list = np.repeat(BirdIDs,24)
    # Add bird ID to each row 
    df.insert(loc=1,
          column='cage',
          value=Birds_list)
    # Change wide dataset to long format         
    df_long = pd.melt(df, id_vars=['cage','hour'], var_name='minute', value_name='hops')
    
    # Add binomial for activity 
    df_long['active'] = np.where((df_long.hops > 0), 1, 0)
             
    # Add phase (night/day) 
    df_long['phase'] = np.where((df_long.hour > 11), "night", "day")
    
    # Convert date to nice format      
    date = os.path.basename(file)
    newdate = date.strip(".txt")
    newdate = newdate.replace(",","")
    newdate = newdate.replace(" ", "_")
    newdate = datetime.strptime(newdate, '%B_%d_%Y')
             
    # Add date as column
    df_long['date'] = newdate      
             
    #separate the date into 3 separate columns 
    df_long['year']= df_long['date'].dt.year
    df_long['month']= df_long['date'].dt.month
    df_long['day']= df_long['date'].dt.day
    
    #write out csv file
    newfilename=str(newdate.date())
    newfilename=str(newdate.date())+'.csv'
    df_long.to_csv(newfilename)
        
    # Track progress
    counter = counter +1
    print(counter)
             
# In the end, combine all new csv files into one mega-file
os.chdir(outdir_path)
all_new_files = [i for i in glob.glob(f"*{'.csv'}")]
combined_csv = pd.concat([pd.read_csv(f) for f in all_new_files ])
combined_csv.to_csv( "combined_cleaned.csv", index=False, encoding='utf-8-sig')

