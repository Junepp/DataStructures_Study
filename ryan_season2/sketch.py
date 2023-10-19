"""


n	m	tests	result
3	5	[[2, 3, 2, 1], [1, 0, 4, 0], [0, 4, 1, 0]]	4
99999	99999	[[0, 0, 199997, 1]]	9999999999
99999	99999	[[50000, 50000, 3, 0]]	9999999975
300	100	[[123, 28, 124, 1], [183, 22, 34, 0], [188, 81, 116, 1], [167, 53, 33, 0], [125, 55, 20, 0]]	6535
"""

# CHECK 경진대회


def getHitmap(n, m, x, y, d, flag):
    hitmap = [[False for _ in range(n)] for _ in range(m)]
    weight = [[0 for _ in range(n + 1)] for _ in range(m)]

    for y_axis_com in range(d + 1):
        y_down = y - y_axis_com
        y_up = y + y_axis_com

        y_down = max(y_down, 0)
        y_up = min(y_up, m - 1)

        x_down = x - (d - y_axis_com)
        x_up = x + (d - y_axis_com) + 1

        x_down = max(x_down, 0)
        x_up = min(x_up, n)

        weight[y_down][x_down] = 1
        weight[y_down][x_up] = -1
        weight[y_up][x_down] = 1
        weight[y_up][x_up] = -1

    for each in weight:
        print(each)

    for j in range(m):
        for i in range(n):
            for k in range(i, n):
                hitmap[j][k] += weight[j][i]

    for each in hitmap:
        print(each)


getHitmap(3, 5, 2, 3, 2, 1)

