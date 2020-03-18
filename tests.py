import time
from naive import naive_string_matching
from automat import fa_string_matching
from automat import transition_table
from KMP import kmp_string_matching
from KMP import prefix_function


def make_test(text, pattern, alg):
    if  alg == "Naive":
        start = time.time()
        res = naive_string_matching(text, pattern)
        end = time.time()
        l = len(res)
        print('Number of patterns: ', l)
    elif alg == "KMP":
        patter = prefix_function(pattern)
        start  = time.time()
        kmp_string_matching(text, pattern)
        end = time.time()
    elif  alg == "Automat":
        pattern = transition_table(pattern)
        start = time.time()
        fa_string_matching(text, pattern)
        end = time.time()

    return end - start

textfile=open("1997_714.txt", 'r')
text=textfile.read()
textfile.close()
alg = ["Naive", "KMP", "Automat"]


#ZAD 2
# patterns = ["os", "nr", "przy", "gospodarst", 'o', 'ro']
#
#
# for i in patterns:
#     for j in alg:
#         print(j , make_test(text, i,j))
#     print("\n")

#zad 6 patter = aaaaa....aa, text - wikipediakruszwil
p = 'przyc'*300
t = open("1997_714.txt", "r")
txt = t.read()
t.close()

for i in alg:
    print(make_test(txt, p ,i))

# zad 7

# p2 = "gosps" * 100
# start = time.time()
# transition_table(p2)
# end = time.time()
# print("transition table", end - start)
# start = time.time()
# prefix_function(p2)
# end = time.time()
# print("prefix_function", end - start)
