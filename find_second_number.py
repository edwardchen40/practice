""" 
Date: 2018/12/17
Author: Edward Chen
Documentation:  Given that the input is an array of numbers, 
                please write a function to output the second largest number. 
                For example, input is [3,1,2], output should be 2.

Vserion: v1
"""

import getopt
import sys

NUM_LARGEST = 2

def usage():
    
    print('USAGE: python find_second_largest_number.py --alist=8,14,30,6,13')
    print('USAGE: python find_second_largest_number.py --unit')

def main():
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["alist=", "unit"])
        if len(opts) < 1:
            usage()
            sys.exit(2)

        for o, a in  opts:
            if o == "--alist":
                aList = a
            elif o == "--unit":
                unitTest()
                sys.exit(2)
            else:
                usage()
                assert False, "Unknown option" + o

        find_second_largest_number(aList)


    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)


def find_second_largest_number(aList):

    aList = aList.split (',')

    #, reverse=True
    result = sorted([int (i) for i in aList])  
    print "Sort result = ", result
    print "2nd largest number = ", result[len(result) - NUM_LARGEST], "\n"

def unitTest():
    print ("Unit Test starting...\n")
    find_second_largest_number("10,20,8,15,2")
    find_second_largest_number("-8,-6,-2,-5,-10")
    find_second_largest_number("8,-6,9,-10,1")
    find_second_largest_number("89821,900000,99887,110000,100000")
    print ('\n')


if __name__ == "__main__":
    main()
