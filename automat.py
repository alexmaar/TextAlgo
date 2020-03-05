def fa_string_matching(text, delta):
    res=[]
    q = 0
    for s in range(0, len(text)):
        if(text[s]  in delta[q].keys()):
            q=delta[q][text[s]]
        else :
            q = 0
        if(q == len(delta) - 1):
            res.append(s+1-q)
    return res


def transition_table(pattern):
    alphabet=set(pattern)
    alphabet=list(alphabet)
    result = []
    for q in range(0, len(pattern) + 1):
        result.append({})
        for a in alphabet:
            k = min(len(pattern) + 1, q + 2)
            while True:
                k = k - 1
                p=pattern[:k]
                s=(pattern[:q]+a)
                suf=s[len(s)-k:]
                if suf==p:
                    break
            result[q][a] = k
    return result

textfile=open("1997_714.txt", 'r')
filetext=textfile.read()
textfile.close()

pattern="art"
print(fa_string_matching(filetext, transition_table(pattern)))
