
# coding: utf-8

# In[62]:

def rev_word1(s):
    return " ".join(reversed(s.split()))

#Or

def rev_word2(s):
    return " ".join(s.split()[::-1])

def rev_word3(s):
    """
    Manually doing the splits on the spaces.
    """
    
    words = []
    length = len(s)
    spaces = [' ']
    
    # Index Tracker
    i = 0
    
    # While index is less than length of string
    while i < length:
        
        # If element isn't a space
        if s[i] not in spaces:
            
            # The word starts at this index
            word_start = i
            
            while i < length and s[i] not in spaces:
                
                # Get index where word ends
                i += 1
            # Append that word to the list
            words.append(s[word_start:i])
        # Add to index
        i += 1
        
    # Join the reversed words
    return " ".join(reversed(words))


# In[ ]:




# In[63]:

rev_word1('Hi John,   are you ready to go?')


# In[64]:

rev_word2('Hi John,   are you ready to go?')


# In[65]:

rev_word3('Hi John,   are you ready to go?')


# In[ ]:




# In[ ]:



