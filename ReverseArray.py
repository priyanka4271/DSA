num=[2,4,1,7,6,3,8,9,5]

def func(num,left,right):
    if left >= right:
        return
    num[left], num[right] = num[right],num[left]
    func(num,left+1,right-1)

def reverse_array(num):
    func(num, 0, len(num)-1)
    return num

print(reverse_array(num))





