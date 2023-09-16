# TODO: 파이썬 내장함수 써서 다시 풀어보기

def quicksort(score_list, sorted_idx_list):
    if len(score_list) <= 1:
        return score_list, sorted_idx_list
    pivot = score_list[0]
    tail = score_list[1:]
    pivot_idx = sorted_idx_list[0]
    left = []
    left_idx = []
    for i in range(len(tail)):
        if score_list[i+1] < pivot:
            left.append(score_list[i+1])
            left_idx.append(sorted_idx_list[i+1])
    right = []
    right_idx = []
    for i in range(len(tail)):
        if score_list[i+1] > pivot:
            right.append(score_list[i+1])
            right_idx.append(sorted_idx_list[i+1])
    left, left_idx = quicksort(left, left_idx)
    right, right_idx = quicksort(right, right_idx)
    return left + [pivot] + right, left_idx + [pivot_idx] + right_idx

def solution():
    N = int(input())
    name_list = []
    score_list = []
    for _ in range(N):
        ith_name, ith_score = input().split()
        name_list.append(ith_name)
        score_list.append(int(ith_score))
    sorted_idx_list = list(range(N))
    _, sorted_idx_list = quicksort(score_list, sorted_idx_list)
    for sorted_idx in sorted_idx_list:
        print(name_list[sorted_idx], end = ' ')
    
