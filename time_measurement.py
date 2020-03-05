import time
from naive import naive_string_matching
from automat import fa_string_matching
from automat import transition_table
from KMP import kmp_string_matching

textfile=open("1997_714.txt", 'r')
text=textfile.read()
textfile.close()

pattern="art"

# text="abaabaaaabaabababababaaidhauidhiaadaidwqddohdoqwhabaababahfkshfshksfhksfabababababagdsgdbsbabababgdsgdasdababa"
# pattern = "ababababababa"

start=0
start=time.time()
naive_string_matching(text, pattern)
print(f"Naive:  {time.time()-start}")

start2=0
start2=time.time()
fa_string_matching(text, transition_table(pattern))
print(f"Automat: {time.time()-start2}")

start3=0
start3=time.time()
kmp_string_matching(text, pattern)
print(f"KMP: {time.time()-start3}")
