from queue import LifoQueue

stack = LifoQueue(maxsize = 3)
print(stack.qsize())
stack.put('hello')
stack.put('world')
stack.put('!')
print('\nElement poped from stack')
print(stack.get())
print(stack.get())

print(stack.get())

print('\nEmpty:', stack.empty())
