---
title: Use List as Stack (LIFO)
description: Zero-dependency Python snippets for using a list as a stack (Last-In, First-Out) with the standard library.
keywords: LIFO, clear, data-structures, error-handling, list, peek, pop, push, safe, size, stack
---

# Use List as Stack (LIFO)

Zero-dependency Python snippets for using a list as a stack (Last-In, First-Out) with the standard library.

4 snippets available in this sub-category.

---

## Simple

###  Push and pop with list

`stack` `list` `push` `pop` `LIFO` `data-structures`

Use list append() and pop() for stack operations

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

!!! note "Notes"
    - append() adds to the end (top of stack)
    - pop() removes from the end (top of stack)

<hr class="snippet-divider">

### Peek at top of stack

`stack` `peek` `list` `data-structures`

Access the top element without removing it

```python
stack = [1, 2, 3]
top = stack[-1]
print(top)  # 3
```

!!! note "Notes"
    - Use stack[-1] to peek at the top
    - Raises IndexError if stack is empty

<hr class="snippet-divider">

## Complex

###  Stack with error handling

`stack` `error-handling` `safe` `data-structures`

Safe pop with empty stack check

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

!!! note "Notes"
    - Always check if stack is not empty before popping

<hr class="snippet-divider">

### Stack size and clear

`stack` `size` `clear` `list` `data-structures`

Get stack size and clear stack

```python
stack = [1, 2, 3]
print(len(stack))  # 3
stack.clear()
print(stack)  # []
```

!!! note "Notes"
    - len(stack) for size, clear() to empty

<hr class="snippet-divider">

## 🔗 Cross Reference

- **Reference**: See [📂 Use deque as Queue](queue_deque.md)

## 🏷️ Tags

`stack`, `list`, `push`, `pop`, `peek`, `size`, `clear`, `LIFO`, `data-structures`

## 📝 Notes
- Python lists are efficient for stack operations
- For thread-safe or multi-producer/consumer stacks, use queue.LifoQueue
