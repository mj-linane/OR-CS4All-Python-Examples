# Python program for implementation of Selection Sort
numList = [64, 25, 12, 22, 11]

# Traverse through all array elements
for currentNum in range(len(numList)):
    # Find the minimum element in remaining
    # unsorted array
    minNum = currentNum
    for nextNum in range(currentNum+1, len(numList)):
        if numList[nextNum] < numList[minNum]:
            minNum = nextNum
    # Swap the found minimum element with
    # the first element
    numList[currentNum], numList[minNum] = numList[minNum], numList[currentNum]

# Test code
print("Sorted array")
for i in range(len(numList)):
    print("%d" % numList[i]),
