import os,sys

def traverseAllAndFindFile(root, desire, isExt):
    count = 1
    for directoryName, subDirList, subDirectoryList in os.walk(root):
        for file in subDirectoryList:
            item = file
            if(isExt == 1):
                fname, fext = os.path.splitext(file)
                item = fext
            if(item == desire):
                path = directoryName + '/' + file
                print('[%d] %s' %(count, path))
                count = count+1
    print('----- Finished Successfuly! -----')

operation = sys.argv[1]
if(operation == 'F'):
    root = sys.argv[2]
    param = sys.argv[3]
    ext = 0
    if param[:1] == '.':
        ext = 1
    traverseAllAndFindFile(root, param, ext)
