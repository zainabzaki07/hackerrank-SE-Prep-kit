def findSmallestMissingPositive(orderNumbers):
    n=len(orderNumbers)
    pointer=0
    while pointer<n:
        pointerValue= orderNumbers[pointer]
        if pointerValue>0 and pointerValue<=n:
            if pointerValue-1!=pointer: 
                swapindex=pointerValue-1
                tempValue=orderNumbers[swapindex]
                if tempValue==pointerValue:
                    pointer+=1 # if 2 same occure move to next
                    continue
                orderNumbers[pointer]=tempValue
                orderNumbers[swapindex]=pointerValue
            else:# correct value ,move to next
                pointer+=1
        else:#if out of range value comes move to next
            pointer+=1
    index=0
    #checking which one is on wrong position
    while index<n:
        if orderNumbers[index]!=index+1:
            return index+1
        index+=1
    #if nothing is wrong
    if index==n:
        return n+1
