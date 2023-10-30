def inflight(mins, array):

    map={}
    for mvlenght in array:
        diff = mins-mvlenght
        if diff in map:
            return True
        else:
            map[mvlenght]=1
    return False
print(inflight(85,[35,80,50,40]))