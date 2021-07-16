import matplotlib.pyplot as plt
import os, sys, cv2
from os import listdir
from os.path import isfile, join


class ImagePiece:
    def __init__(self, name):
        self.name = name
        self.img = cv2.imread(name)
        self.points = []

    def get_coord(self):
        fig = plt.figure()
        ax = fig.add_subplot(111)
        plt.imshow(self.img)
        cid = fig.canvas.mpl_connect('button_press_event', self._onclick)
        plt.show(block=True)
        return self.points

    def _onclick(self, click):
        self.points.append((round(click.xdata),round(click.ydata)))
        plt.scatter(click.xdata, click.ydata, c='r', s=40)
        plt.draw()
        return self.points


if __name__ == "__main__":
    # specify path and file types
    file_types = ["JPG"]
    cwd = os.getcwd()
#     print(f'Current Working Directory = {cwd}')

    # get all the images of specific format in cwd
    all_files = [f for f in listdir(cwd) if isfile(join(cwd, f))]
    images = []
    for ft in file_types:
        images.extend([f for f in all_files if f.endswith('.' + ft)])
    del all_files
    print(f'files = {images}')

    # plot images
    # images[0] = ImagePiece(images[0])
    # images[0].get_coord()

    for i in range(0, len(images)):
        images[i] = ImagePiece(images[i])
        images[i].get_coord()

#     for i in range(0, len(images)):
#         im = plt.imread(images[i])
#         implot = plt.imshow(im)

#         # put a blue dot at (10, 20)
#         plt.scatter([500], [200])

#         # put a red dot, size 40, at 2 locations:
#         plt.scatter(x=[30, 40], y=[500, 3000], c='r', s=40)
    print(images[0].points)
#         plt.show()