'''
problem url :-https://www.codingninjas.com/codestudio/problems/873366?topList=striver-sde-sheet-problems&utm_source=striver&utm_medium=website&leftPanelTab=0
'''

def missingAndRepeating(arr, n):
    # Write your code here
    l = [0]*(n+1)
    for i in range(n):
        l[arr[i]]+=1
    for i in range(1,n+1):
        if l[i]==0:
            a = i
        if l[i]>1:
            b = i
    return a,b
