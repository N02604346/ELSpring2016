from datetime import date, datetime, timedelta


def chunks(l, n):
    n = max(1, n)
    return [l[i:i + n] for i in range(0, len(l), n)]
#chunks breaks the list l into a list of n sized lists

def average(TempChunks):
    AverageTemps = []
    for x in range(0, len(TempChunks)):
        AverageTemps.extend([(sum(TempChunks[x])) / len(TempChunks[x])])
    return AverageTemps

def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta
        

def test():
    """ render svg graph """
    tempFList = range(1, 1423)
#this is just an array to test with
    dataNum = len(tempFList)
    interval = (dataNum / 20)
#so 20 will be the amount of data points, you can increase or decrease this
    TempChunks = chunks(tempFList, interval)
    AverageTemps = average(TempChunks)

#now we divide each chunk by the size of that particular chunk, obtaining the average, and put it into the AverageTemps list.     
    print '*******************************************'
    print AverageTemps

test()
