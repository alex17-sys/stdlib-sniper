# 🧩 Push and pop with list
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

item = stack.pop()  # Pop
print(item)  # 3
print(stack)  # [1, 2]


# 🧩 Peek at top of stack
stack = [1, 2, 3]
top = stack[-1]
print(top)  # 3


# 🧩 Stack with error handling
def safe_pop(stack):
    if stack:
        return stack.pop()
    else:
        print("Stack is empty!")
        return None


stack = []
safe_pop(stack)  # Prints warning, returns None


# 🧩 Stack size and clear
stack = [1, 2, 3]
print(len(stack))  # 3
stack.clear()
print(stack)  # []
