import os

def print_directory_tree(startpath, level=0):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

if __name__ == "__main__":
    directory = r"C:\Users\zreba\Documents\color_space_project\Mirror Clones\Mirror-Two\Ghost1"  # Change this to your directory path
    print_directory_tree(directory)
