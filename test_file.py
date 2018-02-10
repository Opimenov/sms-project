import fileinput
import math
import pandas as pd
from pandas import ExcelWriter

def search_and_enter(phonenum, newKey, newValue):
    x1 = pd.ExcelFile('filename.xlsx')
    df = x1.parse('Sheet1')
    i = 0
    while df["PHONE NUMBER"][i] != phonenum:
        print(df["PHONE NUMBER"][i])
        print("i = " + str(i))
        if math.isnan(float(df["PHONE NUMBER"][i])):
            print('We got here! i =')
            print(i)
            df["PHONE NUMBER"][i] = phonenum
            print("Phonenum =")
            print(phonenum)
            print(df["PHONE NUMBER"][i])
            break
        i = i + 1
    
    df[newKey][i] = newValue
    print(newKey + newValue)
    print(i)
    print(df[newKey][i])
    df.to_csv('filename.csv', sep=',')
        


def main():
    phonenum = "86475834"
    newKey = "MIDDLE NAME"
    newtext = "Jeremy"
    #phonenum, newtext = tuple
    search_and_enter(phonenum, newKey, newtext)

if __name__ == "__main__":
    main()
