
# coding: utf-8

# In[5]:

# Dynamic programming implementation of LCS problem
 
# Returns length of LCS for X[0..m-1], Y[0..n-1] 
def lcs(X, Y, m, n):
    L = [[0 for x in xrange(n+1)] for x in xrange(m+1)]
    print L
    # Following steps build L[m+1][n+1] in bottom up fashion. Note
    # that L[i][j] contains length of LCS of X[0..i-1] and Y[0..j-1] 
    for i in xrange(1,m+1):
        for j in xrange(1,n+1):
           # if i == 0 or j == 0:
            #    L[i][j] = 0
           # el
            print "i={}, j={}".format(i,j)
            if X[i-1] == Y[j-1]:
                print "Equal L[i][j] = L[i-1][j-1] + 1 - {}+1".format(L[i-1][j-1])
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
                print "Not equal , max(L[i-1][j], L[i][j-1]) - max({},{})".format(L[i-1][j], L[i][j-1])
 
    # Following code is used to print LCS
    index = L[m][n]
 
    # Create a character array to store the lcs string
    lcs = [""] * (index)
 
    # Start from the right-most-bottom-most corner and
    # one by one store characters in lcs[]
    i = m
    j = n
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
 
    print "LCS of " + X + " and " + Y + " is " + "".join(lcs) 
 

X = "ABCBDAB"
Y = "BDCABA"
m = len(X)
n = len(Y)
lcs(X, Y, m, n)


# In[ ]:




# In[ ]:



