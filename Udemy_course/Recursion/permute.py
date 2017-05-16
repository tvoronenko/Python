
# coding: utf-8

# In[18]:

def permute(s):
    out = []
    
    # Base Case
    if len(s) == 1:
        out = [s]
        
    else:
        # For every letter in string
        for i, let in enumerate(s):
            print "____"
            print "i= "+str(i)
            print "let = "+let
            print "s[:i] = "+s[:i]
            print "s[i+1:] = "+s[i+1:]
            # For every permutation resulting from Step 2 and 3 described above
            for perm in permute(s[:i] + s[i+1:]):
                print "???"
                print "perm = "+perm
                # Add it to output
                out += [let + perm]

    return out



        
print(permute('abc'))


# In[ ]:

