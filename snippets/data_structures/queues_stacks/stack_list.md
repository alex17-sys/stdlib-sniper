# Use List as Stack (LIFO)

Zero-dependency Python snippets for using a list as a stack (Last-In, First-Out) with the standard library.

## Simple

### 🧩 Push and pop with list

```python
stack = []
stack.append(1)  # Push
stack.append(2)
stack.append(3)
print(stack)  # [1, 2, 3]

item = stack.pop()  # Pop
print(item)  # 3
print(stack)  # [1, 2]
```

📂 Use list append() and pop() for stack operations

🏷️ Tags: stack, list, push, pop, LIFO, data-structures
📝 Notes:
- append() adds to the end (top of stack)
- pop() removes from the end (top of stack)

### 🧩 Peek at top of stack

```python
stack = [1, 2, 3]
top = stack[-1]
print(top)  # 3
```

📂 Access the top element without removing it

🏷️ Tags: stack, peek, list, data-structures
📝 Notes:
- Use stack[-1] to peek at the top
- Raises IndexError if stack is empty

## Complex

### 🧩 Stack with error handling

```python
def safe_pop(stack):
    if stack:
        return stack.pop()
    else:
        print("Stack is empty!")
        return None


stack = []
safe_pop(stack)  # Prints warning, returns None
```

📂 Safe pop with empty stack check

🏷️ Tags: stack, error-handling, safe, data-structures
📝 Notes:
- Always check if stack is not empty before popping

### 🧩 Stack size and clear

```python
stack = [1, 2, 3]
print(len(stack))  # 3
stack.clear()
print(stack)  # []
```

📂 Get stack size and clear stack

🏷️ Tags: stack, size, clear, list, data-structures
📝 Notes:
- len(stack) for size, clear() to empty

## 🔗 Cross Reference

- **Reference**: See [📂 Use deque as Queue](queue_deque.md)

## 🏷️ Tags

`stack`, `list`, `push`, `pop`, `peek`, `size`, `clear`, `LIFO`, `data-structures`

## 📝 Notes
- Python lists are efficient for stack operations
- For thread-safe or multi-producer/consumer stacks, use queue.LifoQueue
