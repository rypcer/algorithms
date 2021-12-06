"""
 This algorithm extracts the elements which are in Range of a start and end Index
 Range Indices can be wrapped around the array like a circular array
 This could be used in the Kfold algorithm 
 -----------------------------------------
 Example: a = [1,2,3,4,5] 
 Print Index Range 2 - 0 
 Output: 3,4,5,1 
 -----------------------------------------
 Manually you would print it like this:
 a[2]= 3, a[3]= 4, a[4]= 5, a[0]= 1 
"""
# Gets the number/length of elements inbetween that range
def getRangeCount(startIndex,endIndex,arrayLen):
    return (endIndex-startIndex+arrayLen) % arrayLen +1

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

#-------------------- Main ------------------- 
        
a =  [1,2,3,4,5];

startIndex = 1;
endIndex = 3;

# Print Array Ranges
for i in getRangedValues(startIndex,endIndex,a):
    print(i,end=' ');
print("\n");
# Print Inverse of Array Range
for i in getRangedValues(startIndex,endIndex,a,1):
    print(i,end=' ');

# Output:
# In Range: 2 3 4
# Out Range: 5 1
