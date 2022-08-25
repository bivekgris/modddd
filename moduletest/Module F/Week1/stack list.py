stack=[]

#use to check if the stack is empty or not
print(not bool(stack))

#push element operation
stack.append('1')
stack.append('2')
stack.append('3')

print('Initial Stack')
print(stack)

print(len(stack))

#get top() operation
print(stack[-1])
