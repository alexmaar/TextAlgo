def naive_string_matching(text, pattern):
    res=[]
    for s in range(0, len(text) - len(pattern) + 1):
        if(pattern == text[s:s+len(pattern)]):
            res.append(s)
    return res

textfile=open("1997_714.txt", 'r')
filetext=textfile.read()
textfile.close()
pattern="art"
print(naive_string_matching(filetext, pattern))
