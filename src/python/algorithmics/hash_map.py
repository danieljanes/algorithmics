from typing import Any
from typing import List
from typing import Optional
from typing import Tuple


class EmptyValue(object):
    def __repr__(self) -> str:
        return "[EMPTY]"


class TombstoneValue(object):
    def __repr__(self) -> str:
        return "[TOMBSTONE]"


EMPTY = EmptyValue()
TOMBSTONE = TombstoneValue()


class Entry(object):
    def __init__(self, hash_value: int = 0, key: Any = EMPTY, value: Any = EMPTY) -> None:
        self.hash_value = hash_value
        self.key = key
        self.value = value
    
    def __repr__(self) -> str:
        return "{0} : {1}".format(self.key, self.value)


class HashMap(object):

    PERTURB_SHIFT = 5

    def __init__(self, capacity: Optional[int] = None) -> None:
        initial_capacity = max(8, capacity * 2) if capacity else 8
        self.entries = [Entry()] * initial_capacity
        self.fill = 0
        self.used = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_value = hash(key)
        index = hash_value % len(self.entries)
        perturb = self.signed_to_unsigned(hash_value)
        target_index = None
        while self.entries[index].key is not EMPTY:
            if self.entries[index].hash_value == hash_value and \
               self.entries[index].key == key:
                target_index = index
                break
            if target_index is None and \
               self.entries[index].key is TOMBSTONE:
                target_index = index
            index = (index * 5 + perturb + 1) % len(self.entries)
            perturb >>= self.PERTURB_SHIFT
        if target_index is None:
            target_index = index
        if self.entries[target_index].key is EMPTY:
            self.used += 1
            self.fill += 1
        elif self.entries[target_index].key is TOMBSTONE:
            self.used += 1
        self.entries[target_index] = Entry(hash_value, key, value)
        # resize `entries` if necessary
        if self.fill * 3 >= len(self.entries) * 2:
            self._resize()

    def __getitem__(self, key: Any) -> Any:
        index = self._find_key(key)
        return self.entries[index].value

    def __delitem__(self, key: Any) -> None:
        index = self._find_key(key)
        self.used -= 1
        self.entries[index].key = TOMBSTONE
        self.entries[index].value = TOMBSTONE

    def __repr__(self) -> str:
        rep = "HashMap {\n"
        if self.used > 0:
            for entry in self.entries:
                if entry.key is EMPTY or entry.key is TOMBSTONE:
                    continue
                rep += "  {0},\n".format(entry)
        else:
            rep += "  < empty >\n"
        rep += "}"
        return rep
    
    def insert_tuples(self, tuples: List[Tuple[Any, Any]]) -> None:
        for k, v in tuples:
            self[k] = v

    def _resize(self) -> None:
        previous_entries = self.entries
        # provide at least twice the required capacity
        min_capacity = self.used * (4 if self.used <= 50_000 else 2)
        next_capacity = self._next_capacity(min_capacity)
        self.entries = [Entry()] * next_capacity
        self.fill = self.used
        for entry in previous_entries:
            if entry.key is not EMPTY and entry.key is not TOMBSTONE:
                index = entry.hash_value % len(self.entries)
                perturb = self.signed_to_unsigned(entry.hash_value)
                while self.entries[index].key is not EMPTY:
                    index = (index * 5 + perturb + 1) % len(self.entries)
                    perturb >>= self.PERTURB_SHIFT
                self.entries[index] = Entry(entry.hash_value, entry.key, entry.value)

    def _next_capacity(self, required_capacity: int) -> int:
        # find next power of two
        return 1 << (required_capacity - 1).bit_length()

    def _find_key(self, key: Any) -> int:
        hash_value: int = hash(key)
        index: int = hash_value % len(self.entries)
        perturb = self.signed_to_unsigned(hash_value)
        while self.entries[index].key is not EMPTY:
            if self.entries[index].hash_value == hash_value and \
               self.entries[index].key == key:
                return index
            index = (index * 5 + perturb + 1) % len(self.entries)
            perturb >>= self.PERTURB_SHIFT
        raise KeyError()

    @staticmethod
    def signed_to_unsigned(hash_value: int) -> int:
        return 2**64 + hash_value if hash_value < 0 else hash_value


class SimpleHashMap(object):
    def __init__(self, capacity: Optional[int] = None) -> None:
        initial_capacity = max(8, capacity * 2) if capacity else 8
        self.entries = [Entry()] * initial_capacity
        self.fill = 0
        self.used = 0

    def __setitem__(self, key: Any, value: Any) -> None:
        hash_value = hash(key)
        index = hash_value % len(self.entries)
        target_index = None
        while self.entries[index].key is not EMPTY:
            if self.entries[index].hash_value == hash_value and \
               self.entries[index].key == key:
                target_index = index
                break
            if target_index is None and \
               self.entries[index].key is TOMBSTONE:
                target_index = index
            index = (index + 1) % len(self.entries)
        if target_index is None:
            target_index = index
        if self.entries[target_index].key is EMPTY:
            self.used += 1
            self.fill += 1
        elif self.entries[target_index].key is TOMBSTONE:
            self.used += 1
        self.entries[target_index] = Entry(hash_value, key, value)
        # resize `entries` if necessary
        if self.fill * 3 >= len(self.entries) * 2:
            self._resize()

    def __getitem__(self, key: Any) -> Any:
        index = self._find_key(key)
        return self.entries[index].value

    def __delitem__(self, key: Any) -> None:
        index = self._find_key(key)
        self.used -= 1
        self.entries[index].key = TOMBSTONE
        self.entries[index].value = TOMBSTONE

    def __repr__(self) -> str:
        rep = "SimpleHashMap {\n"
        if self.used > 0:
            for entry in self.entries:
                if entry.key is EMPTY or entry.key is TOMBSTONE:
                    continue
                rep += "  {0},\n".format(entry)
        else:
            rep += "  < empty >\n"
        rep += "}"
        return rep
    
    def insert_tuples(self, tuples: List[Tuple[Any, Any]]) -> None:
        for k, v in tuples:
            self[k] = v

    def _resize(self) -> None:
        previous_entries = self.entries
        # provide at least twice the required capacity
        next_capacity = self._next_capacity(self.used * 2)
        self.entries = [Entry()] * next_capacity
        self.fill = self.used
        for entry in previous_entries:
            if entry.key is not EMPTY and entry.key is not TOMBSTONE:
                index = entry.hash_value % len(self.entries)
                while self.entries[index].key is not EMPTY:
                    index = (index + 1) % len(self.entries)
                self.entries[index] = Entry(entry.hash_value, entry.key, entry.value)

    def _next_capacity(self, required_capacity: int) -> int:
        # find next power of two
        return 1 << (required_capacity - 1).bit_length()

    def _find_key(self, key: Any) -> int:
        hash_value: int = hash(key)
        index: int = hash_value % len(self.entries)
        while self.entries[index].key is not EMPTY:
            if self.entries[index].hash_value == hash_value and \
               self.entries[index].key == key:
                return index
            index = (index + 1) % len(self.entries)
        raise KeyError()
