""" 
Date: 2018/12/16
Author: Edward Chen
Documentation:  Given a set S of n real numbers and another real number x, 
                determine whether or not there exist. 
                two elements in S whose sum is exactly x.
Vserion: v1
"""

import getopt
import sys

def usage():
    
    print('USAGE: python two_element_in_sum.py --sum=20 --alist=8,14,30,6,13')
    print('USAGE: python two_element_in_sum.py --unit')

def main():
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "", ["sum=", "alist=", "unit"])
        if len(opts) < 1:
            usage()
            sys.exit(2)

        for o, a in  opts:
            if o == "--sum":
                aSum = a
            elif o == "--alist":
                aList = a
            elif o == "--unit":
                unitTest()
                sys.exit(2)
            else:
                usage()
                assert False, "Unknown option" + o

        two_element_in_sum(aSum, aList)


    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)


def two_element_in_sum(aSum, aList):

    aList = aList.split (',')
    keep = []
    for i in range(0, len(aList)):

        temp = int(aSum) - int(aList[i]) 
        if (temp > 0 and str(temp) in keep):
            print "Sum = ", aSum
            print "The 2 elements are", (int(aList[i]), temp)
        keep.append(aList[i])

def unitTest():
    print ("Unit Test starting...\n")
    two_element_in_sum(30, "10,20,8,15,2")
    two_element_in_sum(7, "1,2,0,5,9")
    two_element_in_sum(16, "8,8,2,5,10")
    two_element_in_sum(999887, "89821,900000,99887,1,100000")
    two_element_in_sum(-2, "8,6,9,-10,1")
    print ('\n')


if __name__ == "__main__":
    main()
