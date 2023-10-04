# PyMap

[![Status](https://img.shields.io/badge/status-Not_Released-e44d3c.svg)](https://github.com/Walkaisa/PyMap)
[![License](https://img.shields.io/github/license/Walkaisa/PyMap)](https://github.com/Walkaisa/PyMap/blob/master/LICENSE.txt)
[![Release](https://img.shields.io/github/v/release/Walkaisa/PyMap.svg)](https://github.com/Walkaisa/PyMap/releases/latest)
[![Downloads](https://img.shields.io/github/downloads/Walkaisa/PyMap/total.svg)](https://github.com/Walkaisa/PyMap)
[![Discord](https://img.shields.io/discord/996889527698341978?label=discord)](https://walkaisa.dev/discord)

PyMap is a Python module that provides a simple and efficient key-value data structure. With PyMap, you can easily manage, manipulate, and retrieve key-value pairs. This README.md file provides a detailed guide on how to use PyMap, including example usages and responses for all its functions.

## Installation

To install PyMap, you can use `pip`. Make sure you have `Python 3.12` installed.

```bash
pip install pymap
```

## Usage

To get started with PyMap, you'll need to import the Map class and create an instance. You can provide data to initialize the map with, or you can initialize it with no data.

```python
from pymap import Map

class User:
    def __init__(self, id: str, name: str, age: int) -> None:
        self.id: str = id
        self.name: str = name
        self.age: int = age

    def __repr__(self) -> str:
        return f"User(id={self.id}, name={self.name}, age={self.age})"


data = [
    ("c8a43542-e330-416d-8a92-edcbbcaf2c3f", User("c8a43542-e330-416d-8a92-edcbbcaf2c3f", "John", 25)),
    ("a136571b-0afd-483d-b8a5-422515363856", User("a136571b-0afd-483d-b8a5-422515363856", "Alice", 50)),
    ("76746904-0dbe-461a-8b0d-3fd27485b23f", User("76746904-0dbe-461a-8b0d-3fd27485b23f", "Tim", 75))
]

users = Map[str, User](data) # For no data, use `users = Map[str, User]()` instead.
print(users) # Output: Map({'c8a43542-e330-416d-8a92-edcbbcaf2c3f': User(id=c8a43542-e330-416d-8a92-edcbbcaf2c3f, name=John, age=25), ...})
```

## Available Getters

### Map.size

The `Map.size -> int` getter allows you to retrieve the number of key-value pairs in the map.

```python
size = users.size
print(size) # Output: 3
```

### Map.items

The `Map.items -> Dict[str, User]` getter allows you to retrieve all key-value pairs in the map.

```python
items = users.items
print(items) # Output: {'c8a43542-e330-416d-8a92-edcbbcaf2c3f': User(id=c8a43542-e330-416d-8a92-edcbbcaf2c3f, name=John, age=25), ...}
```

## Available Methods

### Map.set()

The `Map.set(key: str, value: User) -> Dict[str, User]` function allows you to set a key-value pair in the map. If the key already exists, the value will be overwritten. If the key does not exist, a new key-value pair will be created.

```python
users = users.set("4809f036-7d99-4437-af16-7395941e1637", User("4809f036-7d99-4437-af16-7395941e1637", "Bob", 100))
print(users) # Output: {'4809f036-7d99-4437-af16-7395941e1637': User(id=4809f036-7d99-4437-af16-7395941e1637, name=Bob, age=100), ...}
```

### Map.get()

The `Map.get(key: str) -> User | None` function allows you to retrieve a value from the map. If the key does not exist, it will return `None`.

```python
user = users.get("4809f036-7d99-4437-af16-7395941e1637")
print(user) # Output: User(id=4809f036-7d99-4437-af16-7395941e1637, name=Bob, age=100)
```

### Map.has()

The `Map.has(key: str) -> bool` function allows you to check if a key exists in the map.

```python
exists = users.has("4809f036-7d99-4437-af16-7395941e1637")
print(exists) # Output: True
```

### Map.delete()

The `Map.delete(key: str) -> bool` function allows you to delete a key-value pair from the map. If the key does not exist, it will return `False` otherwise it will return `True`.

```python
deleted = users.delete("4809f036-7d99-4437-af16-7395941e1637")
print(deleted) # Output: True
```

### Map.keys()

The `Map.keys() -> Tuple[str]` function allows you to retrieve all keys from the map.

```python
keys = users.keys()
print(keys) # Output: ('c8a43542-e330-416d-8a92-edcbbcaf2c3f', ...)
```

### Map.values()

The `Map.values() -> Tuple[User]` function allows you to retrieve all values from the map.

```python
values = users.values()
print(values) # Output: (User(id=c8a43542-e330-416d-8a92-edcbbcaf2c3f, name=John, age=25), ...)
```

### Map.entries()

The `Map.entries() -> Tuple[Tuple[str, User]]` function allows you to retrieve all key-value pairs from the map.

```python
entries = users.entries()
print(entries) # Output: (('c8a43542-e330-416d-8a92-edcbbcaf2c3f', User(id=c8a43542-e330-416d-8a92-edcbbcaf2c3f, name=John, age=25)), ...)
```

### Map.first()

The `Map.first() -> User | None` function allows you to retrieve the first value from the map. If the map is empty, it will return `None`.

```python
user = users.first()
print(user) # Output: User(id=c8a43542-e330-416d-8a92-edcbbcaf2c3f, name=John, age=25)
```

### Map.last()

The `Map.last() -> User | None` function allows you to retrieve the last value from the map. If the map is empty, it will return `None`.

```python
user = users.last()
print(user) # Output: User(id=76746904-0dbe-461a-8b0d-3fd27485b23f, name=Tim, age=75)
```

### Map.find()

The `Map.find(callback: Callable[[User], bool]) -> User | None` function allows you to find a value in the map. If the value is found, it will return the value otherwise it will return `None`.

```python
user = users.find(lambda user: user.name == "Alice")
print(user) # Output: User(id=a136571b-0afd-483d-b8a5-422515363856, name=Alice, age=50)
```

### Map.filter()

The `Map.filter(callback: Callable[[User], bool]) -> Tuple[User]` function allows you to filter values in the map.

```python
users = users.filter(lambda user: user.age > 50)
print(users) # Output: (User(id=76746904-0dbe-461a-8b0d-3fd27485b23f, name=Tim, age=75), ...)
```

### Map.random()

The `Map.random() -> User | None` function allows you to retrieve a random value from the map. If the map is empty, it will return `None`.

```python
user = users.random()
print(user) # Output: User(id=c8a43542-e330-416d-8a92-edcbbcaf2c3f, name=John, age=25)
```

### Map.clear()

The `Map.clear() -> int` function allows you to clear all key-value pairs from the map. It will return the number of key-value pairs that were deleted.

```python
cleared = users.clear()
print(cleared) # Output: 3
```

# License

PyMap is licensed under the [MIT License](LICENSE.txt)
