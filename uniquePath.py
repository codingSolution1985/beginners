# -*- coding: utf-8 -*-
"""
Created on Sat May 16 15:10:44 2020

@author: interview_CodingSolution
"""

import numpy as np

#input values
m = 2
n = 2

def NumberOfWays(m,n):
    numberWays = np.zeros((m+1, n+1))
    numberWays[0][0] = 1
    for i in range(m+1):
        for j in range(n+1):
            if (i-1 >= 0 and j-1 >=0):
                numberWays[i][j] = numberWays[i-1][j]+numberWays[i][j-1]
            if (i-1 < 0 and j-1 >=0):
                numberWays[i][j] = numberWays[i][j-1]
            if (i-1 >= 0 and j-1 <0):
                numberWays[i][j] = numberWays[i-1][j]
    print("The number of unique paths "+str(int(numberWays[m][n])))
    
    
if __name__ == "__main__": 
    print("Test Case 1: m = 2, n = 2:")
    NumberOfWays(2,2)
    print("Test Case 2: m = 4, n = 2:")
    NumberOfWays(4,2)
    print("Test Case 3: m = 10, n = 10:")
    NumberOfWays(10,10)
    
    
                
                
        










































