
# coding: utf-8

# In[137]:

rec_sum(4)


# In[177]:

print # Create cache for known results
memo = {}
def rec_sum(n):
    
    sum = 0
     # Base Case
    if n == 0:
        return 0
    else:
        if n not in memo:
            memo[n] = n + rec_sum(n - 1)
            
    return memo[n]

memo = {}
def sum_func(n):

        if n < 10:
            return n
        else:
            if n not in memo:
                memo[n] = n%10 + sum_func(n/10)
        
        return memo[n]
    
def word_split(phrase,list_of_words, output = None):
   
    l = len(phrase)
    word = ""
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []
    
    for i in range(l+1):
        word = phrase[0:i]
        if word in list_of_words:
            list_of_words.remove(word)
            output = word_split(phrase[i:l],list_of_words,output)
            output.append(word)
        else:
            i += 1
            
    return output

def word_split2(phrase,list_of_words, output = None):
    '''
    Note: This is a very "python-y" solution.
    ''' 
    
    # Checks to see if any output has been initiated.
    # If you default output=[], it would be overwritten for every recursion!
    if output is None:
        output = []
    
    # For every word in list
    for word in list_of_words:
        
        # If the current phrase begins with the word, we have a split point!
        if phrase.startswith(word):
            
            # Add the word to the output
            output.append(word)
            
            # Recursively call the split function on the remaining portion of the phrase--- phrase[len(word):]
            # Remember to pass along the output and list of words
            return word_split2(phrase[len(word):],list_of_words,output)
    
    # Finally return output if no phrase.startswith(word) returns True
    return output  


# In[178]:

sum_func(4321)


# In[179]:

word_split('themanran',['the','ran','man'])


# In[180]:

get_ipython().magic(u"timeit word_split('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])")


# In[181]:

word_split('themanran',['clown','ran','man'])


# In[182]:

get_ipython().magic(u"timeit word_split2('ilovedogsJohn',['i','am','a','dogs','lover','love','John'])")


# In[ ]:




# In[ ]:



