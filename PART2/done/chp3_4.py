
# 별로 효율적이지 못한 코드

def solution():
    # N, K = list(map(int, input().split()))
    N, K = map(int, input().split())

    answer = 0
    while N > 1:
        if N % K == 0:
            N /= K
        else:
            N -= 1
        
        answer += 1
    
    return answer
