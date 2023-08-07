
# TODO: 풀이처럼 탐색 가능한 범위를 리스트로 만들어서 for-loop 돌자.

def solution():

    answer = 0

    char_col, current_num_row = list(input())

    current_char_val = ord(char_col)

    min_char_val = ord('a')
    max_char_val = ord('h')

    min_num_row_val = 1
    max_num_row_val = 8

    # 수평 1 # right
    if current_char_val+2 <= max_char_val:
        if current_num_row-1 >= min_num_row_val:
            # up
            answer += 1
        if current_num_row + 1 <= max_num_row_val:
            # down
            answer += 1
    
    # 수평 2 # left
    if current_char_val-2 <= min_char_val:
        if current_num_row-1 >= min_num_row_val:
            # up
            answer += 1
        if current_num_row + 1 <= max_num_row_val:
            # down
            answer += 1

    # 수직 1 # up
    if current_num_row-2 >= min_num_row_val:
        if current_char_val-1 >= min_char_val:
            # left
            answer += 1
        if current_char_val + 1 <= max_char_val:
            # right
            answer += 1

    # 수직 2 # down
    if current_num_row+2 >= max_num_row_val:
        if current_char_val-1 >= min_char_val:
            # left
            answer += 1
        if current_char_val + 1 <= max_char_val:
            # right
            answer += 1
    
    return answer