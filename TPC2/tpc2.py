import csv
import sys
import pandas as pd
from distfit import distfit
import numpy as np


def readFile():
    ficheiro = open('ex.txt','r')
    reader = csv.reader(ficheiro)
    myList=[]
    i=0

def ex1(line):
    total=0
    total = 0
    for letter in line:
        for y in letter:
            if (y.isdigit() == True): total += int(y)

def ex(numberLines):
    string = ""
    for i in numberLines:
        for line in sys.stdin:
            newline = line.rstrip()
            string = string + newline
            if (newline.lower() == 'off'):
                break
            elif (newline.lower() == '='): 
                digitSum(string)


def main():
    myList =readFile()
    ex(myList)


if __name__ == "__main__":
   main()
