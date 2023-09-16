def quick_sort(array):
    if len(array) == 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

def solution():
    N = int(input())
    num_array = []
    for _ in range(N):
        num_array.append(int(input()))
    # Sol. 1
    # return sorted(num_array)[::-1] # return sorted(num_array, reverse=True)
    # Sol. 2 - quick sort
    result = quick_sort(num_array)
    return result[::-1]