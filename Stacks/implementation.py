def create_stack():
    stack = []
    return stack

def stack_push(stack,k):
    stack.append(k)
    return stack

def stack_pop(stack):
    if isEmpty(stack):
        return False
    else:
        return stack.pop()

def isEmpty(stack):
    return len(stack) == 0

def Peek(stack):
    return stack[len(stack-1)]

