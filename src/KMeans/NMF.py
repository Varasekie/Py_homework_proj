import numpy


def matrix_factorisation(R, P, Q, K, steps=5000, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i, :], Q[:, j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        eR = numpy.dot(P, Q)
        e = 0

        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i, :], Q[:, j]), 2)
                    for k in range(K):
                        e = e + (beta / 2) * (pow(P[i][k], 2) + pow(Q[k][j], 2))

        if e < 0.001:
            break

    return P, Q.T


# R = [
#     [5, 3, 2, 1],
#     [4, 9, 6, 7],
#     [10, 1, 7, 5],
#     [1, 6, 2, 4],
#     [8, 1, 5, 4],
# ]

#
R = [[0.38664962, 0.16638268, 0.39102959, 0.05728903, 0.5135022, 0.62416992,
      0.11491555, 0.10134749],
     [0.39318026, 0.09949694, 0.25951626, 0.13258455, 0.8154092, 0.27088582,
      0.11031143, 0.09728698],
     [0.3942161, 0.01267462, 0.55330853, 0.11279071, 0.07415864, 0.07108481,
      0.04575425, 0.44741369]
     ]
R = numpy.array(R)

N = len(R)
M = len(R[0])
K = 2

# 随机生成PQ两个
P = numpy.random.rand(N, K)
Q = numpy.random.rand(M, K)

nP, nQ = matrix_factorisation(R, P, Q, K)
# 矩阵相乘
nR = numpy.dot(nP, nQ.T)
# print("复原之后的矩阵")
print(nR)

