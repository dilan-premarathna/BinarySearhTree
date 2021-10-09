import importlib
from datetime import datetime

# import BinarySearchTree from BST.py file
bst = importlib.import_module("BST").BinarySearchTree()


def bst_insert():
    fileList = ["insert_set1_data_1.txt", "insert_set1_data_2.txt", "insert_set1_data_3.txt", "insert_set2_data_1.txt",
                "insert_set2_data_2.txt", "insert_set2_data_3.txt"]
    fileOutput = []
    for fileName in fileList:
        f = open(fileName, "r")
        start = datetime.now()

        for x in f:
            bst.insert(int(x.strip()))
        end = datetime.now()
        duration = end - start

        fileOutput.append(duration.microseconds)

    return fileOutput


def bst_search():
    # We must insert data before doing any operation
    bst_insert()  # Please ignore the time measurement of this data insertion
    fileList = ["search_set1_data_1.txt", "search_set1_data_2.txt", "search_set1_data_3.txt", "search_set2_data_1.txt",
                "search_set2_data_2.txt", "search_set2_data_3.txt"]
    fileOutput = []
    for fileName in fileList:
        f = open(fileName, "r")

        start = datetime.now()

        for x in f:
            bst.search(int(x.strip()))

        end = datetime.now()
        duration = end - start
        fileOutput.append(duration.microseconds)
    return fileOutput


def bst_delete():
    # We must insert data before doing any operation
    bst_insert()
    fileList = ["delete_set1_data_1.txt", "delete_set1_data_2.txt", "delete_set1_data_3.txt", "delete_set2_data_1.txt",
                "delete_set2_data_2.txt", "delete_set2_data_3.txt"]
    fileOutput = []
    for fileName in fileList:
        f = open(fileName, "r")

        start = datetime.now()

        for x in f:
            bst.delete(int(x.strip()))

        end = datetime.now()
        duration = end - start
        fileOutput.append(duration.microseconds)
    return fileOutput


if __name__ == '__main__':
    print(bst_insert())
