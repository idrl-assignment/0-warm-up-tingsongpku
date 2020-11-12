# TODO: import ...
import numpy as np
import matplotlib.image as plt2
def generate_random_matrix(m, n):
    matrix = np.random.randint(0, 2, size=(m,n))#numpy.random.randint(low, high=None, size=None, dtype='l')
    return matrix
def save_matrix(matrix, file_name):
    plt2.imsave(file_name, matrix)
if __name__ == "__main__":
    matrix = generate_random_matrix(10, 10)
    save_matrix(matrix, "example.jpg")