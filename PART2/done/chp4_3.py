
# 아쉬운 부분
# 1. 방문한 좌표를 저장한 nested array를 만들어서 처리하는 대신에 set을 사용한 점
# 2. 방향별 이동 값을 하나의 array에 담아놓고 처리하는 게 더 효율적이었을텐데, if문을 사용함으로써 코드가 불필요하게 길어지고 실수할 가능성도 커졌다.
# 3. 네 방향 모두 갈 수 없음을 처리하는 방식이 아쉬움

# 틀린 부분
# 1. 최종적으로 문제에서 요구한 건 count를 구하는 거였는데, 이 부분을 구하지 않았음
# 2. 사방이 막혔을 때, 후진하는 요건 구현하는 거 빠졌음

def solution():
    N, M = list(map(int, input().split()))

    current_x, current_y, current_direction = list(map(int, input().split()))

    # input the game map
    game_map_list = list()
    for _ in range(N):
        game_map_list.append(list(map(int, input().split())))

    visited_pt_set = set()

    while True:

        # check valid neighborhoods
        valid_neighborhoods_set = set()
        for i in range(4):
            if i == 0:
                neighbor_x = current_x
                neighbor_y = current_y-1
            elif i == 1:
                neighbor_x = current_x+1
                neighbor_y = current_y
            elif i == 2:
                neighbor_x = current_x
                neighbor_y = current_y+1
            elif i == 3:
                neighbor_x = current_x-1
                neighbor_y = current_y
            
            if neighbor_x < M and neighbor_x >= 0 and neighbor_y < N and neighbor_y >= 0:
                if game_map_list[neighbor_y][neighbor_x] == 0:
                    valid_neighborhoods_set.add((neighbor_x, neighbor_y))

        if len(valid_neighborhoods_set) == 0:
            break

        # change direction
        current_direction = current_direction+1 if current_direction < 3 else 0

        if current_direction == 0:
            new_x = current_x
            new_y = current_y-1
        elif i == 1:
            new_x = current_x+1
            new_y = current_y
        elif i == 2:
            new_x = current_x
            new_y = current_y+1
        elif i == 3:
            new_x = current_x-1
            new_y = current_y
        
        if new_x < M and new_x >= 0 and new_y < N and new_y >= 0:
                if (new_x, new_y) not in visited_pt_set and game_map_list[neighbor_y][neighbor_x] == 0:
                    visited_pt_set.add((new_x, new_y))
                    current_x = new_x
                    current_y = new_y
