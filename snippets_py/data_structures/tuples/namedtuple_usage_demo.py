# 🧩 Create and use a namedtuple
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p)  # Point(x=10, y=20)
print(p.x)  # 10
print(p.y)  # 20


# 🧩 Access by index and unpacking
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p[0])  # 10
x, y = p
print(x, y)  # 10 20


# 🧩 Namedtuple with defaults (Python 3.7+)
from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "city"], defaults=["Unknown"])
p1 = Person("Alice", 30)
p2 = Person("Bob", 25, "NYC")
print(p1)  # Person(name='Alice', age=30, city='Unknown')
print(p2)  # Person(name='Bob', age=25, city='NYC')


# 🧩 Namedtuple as dictionary (._asdict())
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
d = p._asdict()
print(d)  # {'x': 10, 'y': 20}


# 🧩 Replace fields with ._replace()
from collections import namedtuple


Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
p2 = p._replace(x=99)
print(p2)  # Point(x=99, y=20)


# 🧩 Nested namedtuples and practical usage
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
Rectangle = namedtuple("Rectangle", ["top_left", "bottom_right"])
rect = Rectangle(Point(0, 0), Point(10, 10))
print(rect.top_left.x, rect.bottom_right.y)  # 0 10
