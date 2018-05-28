#!/bin/python3

def rotLeft(a, d):
    return a[d:] + a[:d] # List slicing

def main():
    l = input().split() 
    n = int(l[0]) # Extracting the first element
    d = int(l[1]) # Extracting the second element
    # Creating the list of input values
    a = list(map(int, input().rstrip().split()))
    output = rotLeft(a, d) # Calling the rotLeft function
    
    print(' '.join(map(str, output)))
    
if __name__ == '__main__':
    main()
