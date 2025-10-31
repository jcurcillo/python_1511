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
    punctChars = ['“', '’', '‘', '”', '.', ',', '?', '!', ';', ':', '"', "'", '-', '(', ')', '[', ']', '{', '}', '*']

    
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
    while True:
        try:
            base_path = Path(__file__).parent
            shorthand_file = input('Enter file name here (Tarzan.txt): ')
            file_name = base_path / shorthand_file
            with open(file_name, 'r', encoding='utf-8-sig') as file:
                data = wordFreq(file)
                printWds(data)
        except FileNotFoundError:
            print('Error. Requested file does not exist. Please try again.')
        test = input('Press enter to continue. Enter q to quit: ')
        if test == 'q':
            break
    print('Exiting')


if __name__ == "__main__":
    main()