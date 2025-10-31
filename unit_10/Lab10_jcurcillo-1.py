"""
Lab10_jcurcillo-1.py
Author: Jack Curcillo
Purpose: Create a program to count the frequency of words within a file. 
Date: 10/30/2025
"""
from pathlib import Path


def printWds(data):
    #print each key-value pair
    for i in sorted(data.keys()):
        print(f'{i} : {data[i]}')



def wordFreq(file):
    #empty data type
    freq = {}
    #punctuation
    punctChars = ['.', ',', '?', '!', ';', ':', '"', "'", '-', '(', ')', '[', ']', '{', '}', '*']

    
    #read first line
    line = file.readline()

    #remove punctuation
    while line:
        for c in punctChars:
            line = line.replace(c,'')

        #list for each line
        words = line.split()

        for word in words:
            #temporary word lowercased
            temp = word.lower()
            #count
            freq[temp] = freq.get(temp, 0) + 1

        #next line
        line = file.readline()
    
    return freq


def main():
    try:
        base_path = Path('unit_10')
        shorthand_file = input('Enter file name here (Tarzan.txt): ')
        file_name = base_path / shorthand_file
        with open(file_name, 'r') as file:
            data = wordFreq(file)
            printWds(data)
    except FileNotFoundError:
        print('Error. Requested file does not exist. Please try again.')


if __name__ == "__main__":
    main()