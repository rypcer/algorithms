def getRange(startIndex,endIndex,arrayLen):
    
    if startIndex > endIndex:
        return arrayLen-startIndex+1+endIndex
    else:
        return endIndex-startIndex+1;


def printRange(rangeLen,startIndex,arrayLen,array):
    i = 0;
    while(i<rangeLen):
        print(array[startIndex%arrayLen])
        startIndex +=1;
        i+=1;


a =  [1,2,3,4,5]
aLen = len(a);

startIndex = 1;
endIndex = 3;

inverseStartIndex = endIndex+1%aLen;
inverseEndIndex = startIndex-1%aLen;

# Get Range Count
rangeLen = getRange(startIndex,endIndex,aLen);
inverseRangeLen = getRange(inverseStartIndex,inverseEndIndex,aLen)

# Print Array Ranges
printRange(rangeLen,startIndex,aLen,a);
print();
printRange(inverseRangeLen,inverseStartIndex,aLen,a);



