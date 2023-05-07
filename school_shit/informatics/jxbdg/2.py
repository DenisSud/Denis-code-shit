n = int(input())
arr = [int(s) for s in input().split()]
def find_maximum_subarray(arr):
    max_sum = 0
    start = 0
    end = 0
    current_sum = 0
    current_start = 1
    for i in range(n):
        current_sum += arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
            start = current_start
            end = i
        if current_sum < 0:
            current_sum = 0
            current_start = i + 1
    return start + 1, end + 1, max_sum
    
start, end, max_sum = find_maximum_subarray(arr)
print(start, end, max_sum)

    


