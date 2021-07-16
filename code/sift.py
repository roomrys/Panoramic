import os
import cv2
import numpy as np
from import_files import func as importFiles


def create_coors(n):
    xline = np.arange(-n, n+1)
    xx, yy = np.meshgrid(xline, xline)
    xy = np.vstack((np.reshape(xx, (1, -1), 'C'), np.reshape(yy, (1, -1), 'C')))
    return xy


def mv_norm01(x):
    num_dim, num_coor = np.shape(x)
    # print(f'num_dim = {num_dim} \nnum_coor = {num_coor}')
    Cov = np.eye(num_dim)
    mean = np.zeros_like(x)

    dev = x - mean
    a = oneD_to_3D(np.transpose(dev))
    c = oneD_to_3D(dev)
    b = twoD_to_3D(np.linalg.pinv(Cov), num_coor)
    print(f'a = {np.shape(a)}')
    print(f'b = {np.shape(b)}')
    print(f'c = {np.shape(c)}')

    mdist_sqrd = oneD_to_3D(np.transpose(dev)) @ twoD_to_3D(np.linalg.pinv(Cov), num_coor) @ oneD_to_3D(dev)
    print(np.shape(mdist_sqrd))

    num = np.exp(- (1 / 2) * mdist_sqrd)
    den = np.sqrt((2 * np.pi) ** num_dim * np.linalg.det(Cov))

    pdf = num / den
    return pdf


if __name__ == '__main__':
    images = importFiles()

    coors = create_coors(5)
    print(np.shape(coors))

    # gauss = mv_norm01(coors)