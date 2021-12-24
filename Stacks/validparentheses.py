# given a set of parentheses in the form of a string, return if they are of valid combination or not.
# Example: ()[] - valid ; [{]} - invalid
def isValid(s):
    stack = []
    openlist = ['(', '[', '{']
    closelist = [')', ']', '}']
    for i in s:
        if i in openlist:
            stack.append(i)
        elif len(stack) != 0 and openlist[closelist.index(i)] == stack[len(stack) - 1]:
            stack.pop()
        else:
            return False
    if len(stack) == 0:
        return True
    else:
        return False

