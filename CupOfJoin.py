def CupOfJoin(*args:list , sep: str = '-'):
    JoinList = []
    for arg in args:
        for i in range(len(arg)):
            JoinList.append(arg[i])
        JoinList.append(sep)
    return JoinList[:-1]
if __name__ == '__main__':
    l1 = [1, 2]
    l2 = [3, 4]
    l3 = [5, 6]
    print(CupOfJoin(l1, l2, l3))
