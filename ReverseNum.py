num = 2345678
total = 0
while num> 0:
         ld = num % 10
         total = (total*10)+ld
         num = num // 10
print(total)