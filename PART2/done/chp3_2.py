
# 오답: 아이디어가 틀렸음 -> 두번째로 작은 수는 1번만 더해졌어야했음

def solution(N, M, K, arr):
    
    sorted_arr = sorted(arr)

    first_max_val = sorted_arr[-1]
    second_max_val = sorted_arr[-2]

    answer = 0

    current_max_val_order = 1
    k_ctn = 0
    for _ in range(M):
        if k_ctn >= K:
            current_max_val_order = 2 if current_max_val_order == 1 else 1
            k_ctn = 0
        
        if current_max_val_order == 1:
            answer += first_max_val
        else:
            answer += second_max_val
        
        k_ctn += 1

    return answer