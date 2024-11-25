import sys
import os

sys.path.append(os.path.abspath("../others"))
import lambdaTest

list_a = list(("abc", 12, True))

print(list_a[2])

for item in list_a:
    print(item)

print(lambdaTest.mydoubler(5))

