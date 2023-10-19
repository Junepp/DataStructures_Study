"""
배달

마을의 개수 N은 1 이상 50 이하의 자연수입니다.
road의 길이(도로 정보의 개수)는 1 이상 2,000 이하입니다.
road의 각 원소는 마을을 연결하고 있는 각 도로의 정보를 나타냅니다.
road는 길이가 3인 배열이며, 순서대로 (a, b, c)를 나타냅니다.
a, b(1 ≤ a, b ≤ N, a != b)는 도로가 연결하는 두 마을의 번호이며, c(1 ≤ c ≤ 10,000, c는 자연수)는 도로를 지나는데 걸리는 시간입니다.
두 마을 a, b를 연결하는 도로는 여러 개가 있을 수 있습니다.
한 도로의 정보가 여러 번 중복해서 주어지지 않습니다.
K는 음식 배달이 가능한 시간을 나타내며, 1 이상 500,000 이하입니다.
임의의 두 마을간에 항상 이동 가능한 경로가 존재합니다.
1번 마을에 있는 음식점이 K 이하의 시간에 배달이 가능한 마을의 개수를 return 하면 됩니다.

입출력 예
N	road	K	result
5	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]	3	4
6	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]	4	4
"""
from collections import defaultdict


def dijkstra(n, start, graph):
    inf = 2000 * 10000

    distances = [inf for _ in range(n)]
    is_visit = [False for _ in range(n)]

    distances[start] = 0
    que = [0]

    while que:
        que.sort(key=lambda x:distances[x])
        now = que.pop(0)

        is_visit[now] = True
        now_dist = distances[now]

        for dest, weight in graph[now].items():
            distances[dest] = min(distances[dest], now_dist + weight)

            if dest not in que and not is_visit[dest]:
                que.append(dest)

    return distances


def solution(N, road, K):
    graph = defaultdict(lambda: defaultdict(lambda:10000))

    for dep, dest, weight in road:
        dep -= 1
        dest -= 1

        graph[dep][dest] = min(graph[dep][dest], weight)
        graph[dest][dep] = min(graph[dest][dep], weight)

    distances = dijkstra(N, 0, graph)
    answer = [True if distances[i] <= K else False for i in range(N)]

    return sum(answer)


print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))
print(solution(6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4))
