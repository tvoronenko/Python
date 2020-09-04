
def lcs(X, Y, m, n):
    L = [[0 for x in range(n+1)] for x in range(m+1)]
    # Following steps build L[m+1][n+1] in bottom up fashion. Note
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] 
    for i in range(1,m+1):
        for j in range(1,n+1):
           # if i == 0 or j == 0:
            #    L[i][j] = 0
           # el
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
 
    # Following code is used to print LCS
    index = L[m][n]
    
    # Create a character array to store the lcs string
    lcs = [""] * (index)
 
    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
    print(lcs)
    if len(lcs)!=len(Y):
        print("Not match")
    else:
        while i > 0 and j > 0:
        
            # If current character in X[] and Y are same, then
            # current character is part of LCS
            if X[i-1] == Y[j-1]:
                lcs[index-1] = X[i-1]
                i-=1
                j-=1
                index-=1
        
            # If not same, then find the larger of two and
            # go in the direction of larger value
            elif L[i-1][j] > L[i][j-1]:
                i-=1
            else:
                j-=1
        
        print("LCS of " + X + " and " + Y + " is " + "".join(lcs))

s = 'nwthgbbnxgq'
alhpabet='abcdefgehijklmnopqrstuvwxuz'
m = len(s)
n = len(alhpabet)
list_l=[]
l=[s[0]]
for i in range(len(s)-1):
    if s[i]<=s[i+1]:
        l.append(s[i+1])
    else:
        list_l.append(l)
        l=[s[i+1]]
if l!=[]:
    list_l.append(l)
max_l=0
s_1=""
for i in list_l:
    if max_l<len(i):
        max_l=len(i)
        s_1=i
print("Longest substring in alphabetical order is: "+"".join(s_1))