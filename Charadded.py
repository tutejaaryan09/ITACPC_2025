

from collections import Counter
def charadded(st):
    count_ = Counter(st)
    for char, count in count_.items():
        if count % 2 != 0:
            return char
n=int(input())
st=input()
print(charadded(st))
