import numpy as np

def pca(data, ncomponents=2):
    
    if data.shape[0] < data.shape[1]:
        data = data.T
        
    data_centered = data- np.mean(data, axis=0)                          # Center the data
    data_cov = np.cov(data_centered.T)                                   # Compute the covariance matrix
    eigenvalues, eigenvectors = np.linalg.eig(data_cov)                  # Compute the eigenvalues and eigenvectors
    idx = eigenvalues.argsort()[::-1]                                    # Arrange eigenvalues and eigenvectors in descending order, aligning the first principal component with the eigenvector of the highest eigenvalue
    eigenvalues = eigenvalues[idx]
    eigenvectors = eigenvectors[:, idx]
    weight= eigenvectors[:,0:ncomponents]                                # Select the best features
    return data_centered.dot(weight)