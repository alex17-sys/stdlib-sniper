# 🧩 Check if item is in set
fruits = {"apple", "banana", "cherry"}
print("banana" in fruits)  # True
print("orange" in fruits)  # False


# 🧩 Not in set
numbers = {1, 2, 3}
print(4 not in numbers)  # True


# 🧩 Set membership with custom objects
class User:
    def __init__(self, name):
        self.name = name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, User) and self.name == other.name


users = {User("alice"), User("bob")}
print(User("alice") in users)  # True
print(User("carol") in users)  # False
