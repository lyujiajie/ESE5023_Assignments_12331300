
#Problem 3
def Pascal_triangle(k):
    triangle = []
    for i in range(k):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle

def print_pascals_triangle(triangle):
    for row in triangle: 
        print(" ".join(map(str, row)).center(len(triangle[-1]) * 3))

k= 5  # 指定要生成的行数
pascals_triangle = Pascal_triangle(k)
print_pascals_triangle(pascals_triangle)
