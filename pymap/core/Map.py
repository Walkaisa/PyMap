from typing import Optional, Iterable, Tuple, Callable, Dict
from random import choice


class Map[K, V]:
    """A simple `key-value` data structure."""
    
    def __init__(self, data: Iterable[Tuple[K, V]] = ()):
        """
        A simple `key-value` data structure.
        
        Parameters:
        - data (Iterable[Tuple[K, V]]): The data to initialize the map with. (default: `()`)
        """
        
        self.__data: Dict[K, V] = {}

        for key, value in data:
            self.set(key, value)

    @property
    def size(self) -> int:
        """Returns the amount of entries in the map."""
        
        return len(self.__data)
    
    @property
    def items(self) -> Dict[K, V]:
        """Returns all key-value pairs of the map."""
        
        return self.__data

    def set(self, key: K, value: V) -> Dict[K, V]:
        """
        Adds or overwrites a key-value pair in the map.
        
        Parameters:
        - key (K): The key to add or overwrite.
        - value (V): The value to add or overwrite.
        
        Returns:
        - Tuple[K, V]: The data of the map.
        """
        
        self.__data[key] = value
        return self.items

    def get(self, key: K) -> Optional[V]:
        """
        Returns the value of a key in the map.
        
        Parameters:
        - key (K): The key to get the value of.
        
        Returns:
        - V | None: The value of the key or `None` if the key does not exist.
        """
        
        return self.__data.get(key)

    def has(self, key: K) -> bool:
        """
        Checks if the map has a key.
        
        Parameters:
        - key (K): The key to check.
        
        Returns:
        - bool: Whether the map has the key or not.
        """
        
        return key in self.__data

    def delete(self, key: K) -> bool:
        """
        Deletes a key-value pair from the map.
        
        Parameters:
        - key (K): The key to delete.
        
        Returns:
        - bool: Whether the entry was deleted or not.
        """
        
        has_item = self.has(key)
        if has_item:
            del self.__data[key]
            
        return has_item

    def clear(self) -> int:
        """
        Deletes all key-value pairs from the map.
        
        Returns:
        - int: The amount of deleted entries.
        """
        
        item_count = self.size
        
        self.__data.clear()
        return item_count

    def keys(self) -> Tuple[K]:
        """
        Returns all keys of the map.
        
        Returns:
        - Tuple[K]: All keys of the map.
        """
        
        return tuple(self.__data.keys())

    def values(self) -> Tuple[V]:
        """
        Returns all values of the map.
        
        Returns:
        - Tuple[V]: All values of the map.
        """
        
        return tuple(self.__data.values())

    def entries(self) -> Tuple[Tuple[K, V]]:
        """
        Returns all key-value pairs of the map.
        
        Returns:
        - Tuple[Tuple[K, V]]: All key-value pairs of the map.
        """
        
        return tuple(self.__data.items())
    
    def first(self) -> Optional[V]:
        """
        Returns the first value of the map.
        
        Returns:
        - V | None: The first value of the map.
        """
        
        return next(iter(self.__data.values()), None)
    
    def last(self) -> Optional[V]:
        """
        Returns the last value of the map.
        
        Returns:
        - V | None: The last value of the map.
        """
        
        return next(reversed(self.__data.values()), None)
    
    def find(self, callback: Callable[[V], bool]) -> Optional[V]:
        """
        Finds a value in the map.
        
        Parameters:
        - callback (Callable[[V], bool]): The callback to use for finding the value.
        
        Returns:
        - V | None: The found value or `None` if no value was found.
        """
        
        for value in self.__data.values():
            if callback(value):
                return value
            
        return None
    
    def filter(self, callback: Callable[[V], bool]) -> Tuple[V]:
        """
        Filters the map.
        
        Parameters:
        - callback (Callable[[V], bool]): The callback to use for filtering the map.
        
        Returns:
        - Tuple[V]: The filtered map.
        """
        
        return tuple(filter(callback, self.__data.values()))
    
    def random(self) -> Optional[V]:
        """
        Returns a random value from the map.
        
        Returns:
        - V | None: A random value from the map.
        """
        
        return choice([*self.__data.values()]) if self.size else None
    
    def __repr__(self) -> str:
        """Returns the representation of the map."""
        
        return f"{self.__class__.__name__}({self.__data if self.__data else None})"
    
    def __str__(self) -> str:
        """Returns the map as a string."""
        
        return f"{self.__class__.__name__}({self.__data if self.__data else None})"
    
    def __iter__(self) -> Iterable[V]:
        """Returns an iterator for the map."""
        
        return iter(self.__data.values())
    
    def __len__(self) -> int:
        """Returns the amount of entries in the map."""
        
        return self.size
    
    def __getitem__(self, key: K) -> Optional[V]:
        """Returns the value of a key in the map."""
        
        return self.get(key)
    
    def __setitem__(self, key: K, value: V) -> Dict[K, V]:
        """Adds or overwrites a key-value pair in the map."""
        
        return self.set(key, value)
    
    def __delitem__(self, key: K) -> bool:
        """Deletes a key-value pair from the map."""
        
        return self.delete(key)
    
    def __contains__(self, key: K) -> bool:
        """Checks if the map has a key."""
        
        return self.has(key)
    
    def __lt__(self, other: "Map[K, V]") -> bool:
        """Checks if the map is less than another map."""
        
        return self.size < other.size
    
    def __le__(self, other: "Map[K, V]") -> bool:
        """Checks if the map is less than or equal to another map."""
        
        return self.size <= other.size
    
    def __gt__(self, other: "Map[K, V]") -> bool:
        """Checks if the map is greater than another map."""
        
        return self.size > other.size
    
    def __ge__(self, other: "Map[K, V]") -> bool:
        """Checks if the map is greater than or equal to another map."""
        
        return self.size >= other.size
    
    def __hash__(self) -> int:
        """Returns the hash of the map."""
        
        return hash(self.__data)
    
    def __eq__(self, other: "Map[K, V]") -> bool:
        """Checks if the map is equal to another map."""
        
        return self.items == other.items
    
    def __ne__(self, other: "Map[K, V]") -> bool:
        """Checks if the map is not equal to another map."""
        
        return self.items != other.items
    
    def __add__(self, other: "Map[K, V]") -> "Map[K, V]":
        """Adds two maps together."""
        
        return Map((*self.entries(), *other.entries()))
    
    def __sub__(self, other: "Map[K, V]") -> "Map[K, V]":
        """Subtracts two maps from each other."""
        
        return Map((entry for entry in self.entries() if entry not in other.entries()))
