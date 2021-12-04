def getRangeCount(startIndex,endIndex,arrayLen):
    
    if startIndex > endIndex:
        return arrayLen-startIndex+1+endIndex;
    else:
        return endIndex-startIndex+1;

# Returns array of in Range values
def getRangedValues(startIndex,endIndex,array,inverse = 0):
    
    arrayLen = len(array);
    
    if inverse:
        istartIndex = endIndex+1%arrayLen;
        endIndex = startIndex-1%arrayLen;
        startIndex = istartIndex;
        rangeLen = getRangeCount(startIndex,endIndex,arrayLen);
    else:
        rangeLen = getRangeCount(startIndex,endIndex,arrayLen);

    rangedValues = [0]*rangeLen;
    # Extract Values    
    i = 0;
    while(i<rangeLen):
        rangedValues[i]=array[startIndex%arrayLen];
        startIndex +=1;
        i+=1;
    return rangedValues;

#--------------------

        
a =  [1,2,3,4,5]


startIndex = 1;
endIndex = 3;


# Print Array Ranges
for i in getRangedValues(startIndex,endIndex,a):
    print(i);



