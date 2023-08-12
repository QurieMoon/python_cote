
def dfs(graph, first_iter, second_iter, visited, N, M):

    # Update the status of the starting node as visited
    # row_num = start_node // M
    # col_num = start_node % M

    visited[first_iter][second_iter]= True

    mv_directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for mv_direction in mv_directions:
        new_row_num = first_iter + mv_direction[0]
        new_col_num = second_iter + mv_direction[1]

        if new_row_num >= N or new_row_num < 0 or new_col_num >= M or new_col_num < 0:
            continue

        if graph[new_row_num][new_col_num]:
            continue

        if not visited[new_row_num][new_col_num]:
            dfs(graph, new_row_num, new_col_num, visited, N, M)

def solution():
    N, M = map(int, input("Input N M: ").split())

    graph = []
    for i in range(N):
        graph.append(list(map(int, list(input("Input the row " + str(i) + " : ")))))
    
    # print("**graph**")
    # print(graph)
    # print("****************")

    # 주의! 아래처럼 visited 초기화하면 각 row 에 대한 array가 사실상 같은 object다!
    # visited = [[False] * M] * N

    visited = [[False] * M for _ in range(N)]
    # print("**visited**")
    # print(visited)
    # print("****************")

    answer = 0
    for first_iter in range(N):
        for second_iter in range(M):
            if not graph[first_iter][second_iter] and not visited[first_iter][second_iter]:
                # print("first_iter: ", first_iter)
                # print("second_iter: ", second_iter)
                dfs(graph, first_iter, second_iter, visited, N, M)
                answer += 1
    
    return answer

final_answer = solution()
print("Answer: ", final_answer)