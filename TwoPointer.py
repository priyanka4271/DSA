def twosum(arr, target):
    arr = sorted(arr)

    i = 0
    j = len(arr) - 1

    while i < j:
        sum = arr[i] + arr[j]

        if sum == target:
            print("Pair found at indexes {} and {}: ({}, {})".format(i, j, arr[i], arr[j]))
            return
        elif sum < target:
            i += 1
        else:
            j -= 1

    print("No pair found")


arr = [1, 56, 48, 57, 70, 80, 99, 100]
target = 128
twosum(arr, target)
