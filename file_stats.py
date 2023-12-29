"""
Author: Jorly Metzger
License: GPLv3
Date: 10/30/2023

Description:
    Reads in a file and displays the total number of words, total number of lines, and avg words / line

"""

"""Import modules"""


"""Classes and functions"""


""" === MAIN === """
def main():
    filename = input("Enter filename: ")
    document = open(filename, "r")          # open fil

    numLines = 0                                                # initialize variables
    totalWords = 0

    for line in document:                                       # iterate the document line-by-line
        words = len(line.split())                               # count number of words
        if (words > 0):
            totalWords += words                                 # add to word total
            numLines += 1                                       # increment line counter

    document.close()                                            # close document

    print (f"Total number of words: {totalWords}")
    print (f"Total number of lines: {numLines}")
    print (f"Average number of words per line: {(totalWords / numLines):.1f}")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
