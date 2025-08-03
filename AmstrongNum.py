# Amstrong number = kisi bhi number m kitne digit h oska oski power se multipy karke
# whi number aa jaye to osko amstrong number bolte h
num = 153
org = num
total = 0
nod = len(str(num))
while num>0:
        ld = num % 10
        total = total +(ld ** nod)
        num = num// 10
if total == org:
            print("number is amstrong")
else:
            print("number is  not amstrong")