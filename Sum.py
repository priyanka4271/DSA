# sum of n netural number using recursion
def Func(sum,i,n):
    if i >n:
        print(sum)
        return
    Func(sum+i,i+1,n)


Func(0,1,100)
