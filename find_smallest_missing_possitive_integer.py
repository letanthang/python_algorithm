# index based placement
def find_missing(integers):  
    # the result is in [1, n+1]
    n = len(integers)
    print(integers)
    for i in range(n):
        while integers[i] > 0 and integers[i] <= n and integers[i] != integers[integers[i]-1]:
            correct_idx = integers[i] - 1
            integers[i], integers[correct_idx] = integers[correct_idx], integers[i]
            print(i, integers)
    
    for i in range(n):
        if integers[i] != i + 1:
            return i + 1
    
    return n + 1

arr = [5, 2, 4, 1]
result = find_missing(arr)
print("result", result)