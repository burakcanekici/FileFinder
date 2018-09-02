import os,sys

def traverseAllAndFindFile(root, desire):
    desireList = [];
    for directoryName, subDirList, subDirectoryList in os.walk(root):
        for file in subDirectoryList:
            if(file == desire):
                path = directoryName + '/' + file
                print(path)
                desireList.append(path)

operation = sys.argv[1]
if(operation == 'F'):
    root = sys.argv[2]
    desireFileName = sys.argv[3]
    traverseAllAndFindFile(root, desireFileName)