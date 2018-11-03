from random import seed, random


from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import pylab




def generateEdges(n, p):
    """
    n is the size of an n*n matrix
    p is the probability that a position's neighbor (up, down, left, right) is connected
    p needs to be 0 <= p < 1, although if p = 0, then the partitions will = n

    returns a collection of edges which represent what positions are connected
    """
    def inMatrix(position):
        return 0 <= position[0] < len(matrix) and 0 <= position[1] < len(matrix[position[0]])
    
    matrix = [[i + (j * n) for i in range(n)] for j in range(n)]
    edges = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for possibleNeighbor in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if inMatrix(possibleNeighbor):
                    if not random() > p:
                        x, y = possibleNeighbor
                        edges.append([matrix[i][j], matrix[x][y]])
    return edges



#modified from Stefan Pochmann's solution to Leetcode 261. Thank you Stefan for your many elegant solutions :)
def countPartitions(n, edges):
    p = [i for i in range(n)]
    def find(v):
        if p[v] != v:
            p[v] = find(p[v])
        return p[v]
    for v, w in edges:
        p[find(v)] = find(w)
    return len(set(map(find, p)))



#test
if __name__ == '__main__':
    seed()

    #generateEdges(5, .999999999999)
    #print(countPartitions(5*5, generateEdges(5, .3)))

    
    dataPoints = [] #tuple where is (number of spots in matrix, probability that neighbors will be connected, total partitions in matrix)
    for n in range(1, 25, 1):
        #n is length of side of n*n matrix
        print('Calculating at size {0}'.format(n))
        for p in [j/100 for j in range(1, 100, 1)]:
            #p is the probability neighbors are connected
            edgesOfMatrix = generateEdges(n, p)
            numberOfPartitions = countPartitions(n*n, edgesOfMatrix)
            dataPoints.append((n, p, numberOfPartitions))

    #print(dataPoints)
    x, y, z = zip(*dataPoints)
    #print(x)
    ax = plt.axes(projection='3d')
    ax.set_xlabel('Matrix size')
    ax.set_ylabel('Probability of neighboring connections')
    ax.set_zlabel('Number of partitions')
    ax.scatter3D(x, y, z, c=z, cmap='gnuplot')
    pylab.show()
    
