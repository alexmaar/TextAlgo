def kmp_string_matching(text, pattern):
    res=[]
    pi = prefix_function(pattern)
    q = 0
    for i in range(0, len(text)):
        while(q > 0 and pattern[q] != text[i]):
            q = pi[q-1]
        if(pattern[q] == text[i]):
            q = q + 1
        if(q == len(pattern)):
            res.append(i+1-q)
            q = pi[q-1]
    return res

def prefix_function(pattern):
    pi = [0]
    k = 0
    for q in range(1, len(pattern)):
        while(k > 0 and pattern[k] != pattern[q]):
            k = pi[k-1]
        if(pattern[k] == pattern[q]):
            k = k + 1
        pi.append(k)
    return pi

textfile=open("1997_714.txt", 'r')
filetext=textfile.read()
textfile.close()

pattern="art"
print(kmp_string_matching(filetext, pattern))
