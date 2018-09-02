import os,sys

def traverseAllAndFindFile(root, desire):
    count = 1
    for directoryName, subDirList, subDirectoryList in os.walk(root):
        for file in subDirectoryList:
            if(file == desire):
                path = directoryName + '/' + file
                print('[%d] %s' %(count, path))
                count = count+1

operation = sys.argv[1]
if(operation == 'F'):
    root = sys.argv[2]
    desireFileName = sys.argv[3]
    traverseAllAndFindFile(root, desireFileName)