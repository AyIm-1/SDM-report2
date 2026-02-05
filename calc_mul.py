#!/usr/bin/python3

import re
                
def calc(A,B):
        if isinstance(A, int) and isinstance(B, int):
                a=A
                b=B
                if 1<=a<=999 and 1<=b<=999:
                        ans=a*b
                        return ans
                
        return -1
        
                
def main ():
	matchstring = ''
	while matchstring != 'end':
                A = input ('input A: ')
                B = input ('input B: ')
                print ('input A * input B = ', calc(A,B))

if __name__ == '__main__':
	main()
