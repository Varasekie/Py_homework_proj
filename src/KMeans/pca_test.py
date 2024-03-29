import numpy as np


def pca(X, k):  # k is the components you want
    # mean of each feature
    n_samples, n_features = X.shape
    mean = np.array([np.mean(X[:, i]) for i in range(n_features)])
    # normalization
    norm_X = X - mean
    # scatter matrix
    scatter_matrix = np.dot(np.transpose(norm_X), norm_X)
    # Calculate the eigenvectors and eigenvalues
    eig_val, eig_vec = np.linalg.eig(scatter_matrix)
    eig_pairs = [(np.abs(eig_val[i]), eig_vec[:, i]) for i in range(n_features)]
    # sort eig_vec based on eig_val from highest to lowest
    eig_pairs.sort(reverse=True)
    # select the top k eig_vec
    feature = np.array([ele[1] for ele in eig_pairs[:k]])
    # get new data
    data = np.dot(norm_X, np.transpose(feature))
    return data


# X = np.array([[-1, 1], [-3, -2], [1, 1], [2, 1], [-2, -1], [3, 2]])
X = np.array(
    [
        [5, 3, 2, 1],
        [4, 9, 6, 7],
        [10, 1, 7, 5],
        [1, 6, 2, 4],
        [8, 1, 5, 4],
    ])
print(pca(X, 1))
