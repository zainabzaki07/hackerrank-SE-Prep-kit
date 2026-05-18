def countResponseTimeRegressions(responseTimes):
    count=0
    for i in range(1,len(responseTimes)):
        total=0
        for j in range(i):
            total+=responseTimes[j]
      
        avg=total/i
        if responseTimes[i]>avg:
            count+=1
    return count
  
if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
