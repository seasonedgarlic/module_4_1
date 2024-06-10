from fake_math import divide as finDiv
from true_math import divide as infDiv

result1 = finDiv(69, 3)
result2 = finDiv(3, 0)
result3 = infDiv(49, 7)
result4 = infDiv(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)