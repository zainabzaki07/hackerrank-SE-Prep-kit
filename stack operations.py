def processCouponStackOperations(operations):
    # Write your code here
    stack=[]
    n=len(operations)
    totalpush=0
    result=[]
    for operation in operations:
        if operation[:4] == "push" and totalpush<=n:
            x=int(operation[5:])
            stack.append(x)
            totalpush+=1
        elif len(stack)!=0:
            if operation=="getMin" :
                x=min(stack)
                result.append(x)
            elif operation=="pop":
                stack.pop()
            elif operation=="top":
                x=stack[-1]
                result.append(x)
    return result
operations = ['push 2', 'push 0', 'push 3', 'push 0', 'getMin', 'pop', 'getMin', 'pop', 'top', 'getMin']
x= processCouponStackOperations(operations)
print(x)
operations = ['push 2', 'push 0', 'pop', 'pop', 'top']
x= processCouponStackOperations(operations)
print(x)
operations=["push 5","getMin"]
x= processCouponStackOperations(operations)
print(x)
