from naive import naive_string_matching
from automat import fa_string_matching
from automat import transition_table
from KMP import kmp_string_matching
import time

pattern = "art"
textfile = open("1997_714.txt", 'r')
filetext = textfile.read()
textfile.close()
result = open("result.txt", "a")

# print(len(naive_string_matching(filetext,pattern)))
# print(kmp_string_matching(filetext,pattern))
# print(fa_string_matching(filetext, transition_table(pattern)))

result.write("\nTime measurements for pattern art\n")

start = time.time()
naive_string_matching(filetext, pattern)
end = time.time()
result.write("\nNaive: \n")
result.write('{}'.format(end - start))

start = time.time()
fa_string_matching(filetext, transition_table(pattern))
end = time.time()
result.write("\nAutomat: \n")
result.write('{}'.format(end - start))

start = time.time()
kmp_string_matching(filetext, pattern)
end = time.time()
result.write("\nKMP: \n")
result.write('{}'.format(end - start))
