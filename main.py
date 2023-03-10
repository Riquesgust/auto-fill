#------ IMPORTS
from concurrent.futures import process
from pathlib import Path
from xml.etree.ElementInclude import include  # provides functions for creating and removing a directory (folder), fetching its contents, changing and identifying the current directory
import pandas as pd  # flexible open source data analysis/manipulation tool
import os, sys
import pathlib
import random
from random import randrange
import decimal
import math
#--------



def main():
    PartNum = str(input("PN:"))
    SerialNum = str(input("SN:"))
    my_dataframe = pd.DataFrame()
    while(True):
        itens = input().split('/')
        for i in range(0, len(itens)):
            itens[i] = itens[i].replace(",", ".")
    #For each entry value it will determine the number of decimals, and create 2 random numbers from it
        for i in range(0, len(itens)):
    #Distinguish between float and int strings
            if(itens[i].find(".")!= -1):
                decimals = int(len(itens[i].split('.')[1]))
                aList = []
                for j in range(3):
                    if j == 0:
                        aList.append(((round(float(itens[i]), decimals))))
                    else:
                        randomFactor = randrange(0,10)
                        randomFactor = (randomFactor/(10**(decimals)))
                        x = random.uniform(-randomFactor, randomFactor)
                        y = float(itens[i])
                        z = ((round((x+y), decimals)))
                        aList.append(z)
            else:
                aList = []
                for j in range(3):
                    if j == 0:
                        aList.append(float(itens[i]))
                    else: 
                        y = int(itens[i])
                        z = (int(round((math.log(y, 10)))))
                        x = random.randrange((-z-1),(z+1))
                        aList.append(int(x+y))
            #Creating a list with the random numbers created
            my_list = [aList[0], aList[1], aList[2]]
            # append my list as a row in the dataframe.
            my_list = pd.Series(my_list)
            # append the list of keywords as a row to my dataframe.
            my_dataframe = my_dataframe.append(my_list, ignore_index=True)
        
        my_list = ["-", "-", "-"]
        my_list = pd.Series(my_list)
        my_dataframe = my_dataframe.append(my_list, ignore_index=True)

        if((input("Continue?:").lower()) != ""):
            break
    # rename dataframe columns using dictionaries.
    my_dataframe = my_dataframe.rename(
        columns={
            0: "1?? medida",
            1: "2?? medida",
            2: "3?? medida"
        }
    )
    #getting the current work directory
    cwd = os.getcwd()
    #joinin paths to create a new folder
    path = os.path.join(cwd, "files")
#If the folder does not exists it will create the folder, and save all the files there
    try:
        os.mkdir(path)
        os.chdir(path)
        # extract my dataframe to an .xlsx file! With the values inserted at the start
        my_dataframe.to_excel(PartNum+" - "+SerialNum+".xlsx", sheet_name="my dataframe")
        print("")
        #Preview of the result
        print(my_dataframe)
#If the folder exists it will suppress the error, change the directory and save the files
    except OSError as error:
        os.chdir(path)
        # extract my dataframe to an .xlsx file! With the values inserted at the start
        my_dataframe.to_excel(PartNum+" - "+SerialNum+".xlsx", sheet_name="my dataframe")
        print("")
        #Preview of the result
        print(my_dataframe)
        

if __name__ == "__main__":
    main()