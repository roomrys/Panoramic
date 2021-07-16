import os


def func(path_to_files='.', file_types=['.JPG']):
    path_to_files = '.'
    files = os.listdir(path_to_files)

    file_types = ['.JPG']
    for ftype in file_types:
        files = [file for file in files if ftype in file]

    return files


if __name__ == '__main__':
    images = func()
    print(images)

