
def solution():

    # input
    N, M = [int(x) for x in input().split()]

    # input 참고 내용
    # input_data 부분에서 한줄씩 입력 받는 게 더 깔끔해보인다.
    # data = list(map(int, input().split()))

    input_data = []
    for _ in range(N+1):
        input_data.append([int(x) for x in input().split()])
    
    # input_data = [[3,1,2], [4,1,4], [2,2,2]]
    # input_data = [[7, 3, 1, 8], [3, 3, 3, 4]]

    return max([min(single_case) for single_case in input_data])