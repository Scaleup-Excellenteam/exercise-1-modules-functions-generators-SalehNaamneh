import os;
def thisIsTheWay(path:str ) :
    deepFileList = []
    filesList = os.listdir(path)
    for fileName in filesList :
            if fileName[:4] == "deep" :
                deepFileList.append(fileName)
    return deepFileList

if __name__ == '__main__':
    print(thisIsTheWay("PATH TO deep text"))
    
