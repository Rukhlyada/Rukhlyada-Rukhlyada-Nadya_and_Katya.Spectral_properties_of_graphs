import os
import numpy as np

def get_eigen_values(matrix):
    return np.linalg.eig(matrix)[0]

def get_eigen_vector(matrix):
    return np.linalg.eig(matrix)[1]
    
def get_triangles_number(matrix):
    return np.trace(np.linalg.matrix_power(matrix, 3))/6
    
def get_independencies_ub(matrix):
    k = np.count_nonzero(matrix[0])
    return len(matrix)/(1 - k/min(get_eigen_values(matrix)))
    
def get_triangles(matrix):
    n = len(matrix)
    for a in range(0, n):
        for b in range(a + 1, n):
            if not matrix[a][b]:
                continue
            for c in range(b + 1, n):
                if matrix[b][c] and matrix[a][c]:
                    print(a + 1, b + 1, c + 1)
                    
def remove_node(matrix, node):
    n = len(matrix)
    x = -1*numpy.ones(n)
    matrix[:, node-1] = x
    matrix[node-1, :] = x
    return matrix

def get_neighbors_nodes(matrix, node):
    n = len(matrix)
    return [i+1 for i in range(n) if matrix[node-1][i] == 1]

def get_nodes_number(matrix):
    return len(nodes)

def get_nodes(matrix):
    nodes = []
    for i in range(len(matrix)):
        if len(matrix[i][matrix[i] > 0]) > 0:
            nodes.append(i+1)
    return nodes

def get_independence_set(matrix):
    I = set([])
    while get_nodes_number(matrix) > 0: # цикл сложности O(n)
        n = get_nodes(matrix)[0] # первая попавшаяся вершина
        I.add(n) # добавляем одну вершину из ребра
        for s in get_neighbors_nodes(matrix, n): # удаляем всех соседей
            remove_node(s)
        remove_node(n) # и исходную вершину
    return I
    
print('Введите размерность матрицы')
n = int(input())
print('Введите матрицу')
matrix = np.array([input().strip().split(',') for _ in range(n)]).astype(int)
print(matrix)

while True:
    print('Введите число')
    print('1. Собственные числа')
    print('2. Собственные вектора')
    print('3. Число треугольников')
    print('4. Оценка числа независимостей из неравенства Хоффмана-Дельсарта')
    print('5. Треугольники')
    print('6. Независимое множество')

    alg_code = int(input())
    algs = {
        1: get_eigen_values,
        2: get_eigen_vector,
        3: get_triangles_number,
        4: get_independencies_ub,
        5: get_triangles,
        6: get_independence_set,
    }
    print(algs[alg_code](matrix))