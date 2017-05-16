from MyGraph import Graph

d = {}
g = Graph()
wfile = open('words.txt','r')
# create buckets of words that differ by one letter
for line in wfile:
    print(line)
    word = line[:-1]
    print word
    for i in range(len(word)):
        bucket = word[:i] + '_' + word[i+1:]
        if bucket in d:
            d[bucket].append(word)
        else:
            d[bucket] = [word]
print d

# add vertices and edges for words in the same bucket
for bucket in d.keys():
    for word1 in d[bucket]:
        for word2 in d[bucket]:
            if word1 != word2:
                g.add_edge(word1,word2)
print(g.__str__())
print(g.bfs('pope','park'))