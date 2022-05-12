from enum import EnumMeta
from typing import Generic, List, Optional, TypeVar

T = TypeVar('T')

class Vector(Generic[T]):
  def __init__(self) -> None:
    # Using a tuple because it's closest to a fixed-size array
    self._list: List[Optional[T]] = [None] * 16
    self._size = 0

  def size(self) -> int:
    return self._size

  def capacity(self) -> int:
    return len(self._list)

  def is_empty(self) -> bool:
    return self._size == 0

  def at(self, index: int) -> T:
    if 0 > index >= self._size:
      raise IndexError()

    value = self._list[index]

    assert(value is not None)

    return value

  def push(self, item: T) -> None:
    if self._size == self.capacity():
      self._resize(self.capacity() * 2)

    self._list[self._size] = item
    self._size += 1

  def _resize(self, new_capacity: int) -> None:
    new_list: List[Optional[T]] = [None] * new_capacity

    for index, item in enumerate(self._list):
      new_list[index] = item

    self._list = new_list

  def insert(self, index: int, item: T) -> None:
    if 0 > index >= self._size:
      raise IndexError()

    # !! Potential optimaztion to perform insertion and resize simultaneously
    # 1. Allocate new array
    # 2. Copy elements from old array up to index
    # 3. Set element at index
    # 4. Copy elements up to index with indices incremented by 1
    # 5. Set new array as current
    if self._size == self.capacity():
      self._resize(self.capacity() * 2)

    for i in range(self._size, index, -1):
      self._list[i] = self._list[i - 1]

    self._list[index] = item
    self._size += 1

  def prepend(self, item: T) -> None:
    self.insert(0, item)

  def __repr__(self) -> str:
    return f'Vector { self._list[:self.size()] }'

  def pop(self) -> T:
    index = self._size - 1
    value = self.at(index)

    self._list[index] = None
    self._size -= 1

    if self._size / self.capacity() <= 0.25:
      self._resize(self.capacity() // 2)

    return value

  def delete(self, index: int) -> None:
    if 0 > index >= self._size:
      raise IndexError()

    for i in range(index, self._size - 1):
      self._list[i] = self._list[i + 1]

    self._list[self._size - 1] = None
    self._size -= 1

    if self._size / self.capacity() <= 0.25:
      self._resize(self.capacity() // 2)

  def remove(self, item: T) -> None:
    index = 0

    # Likely a much better way of doing this without performing multiple O(n) calls
    while index < self._size:
      if self._list[index] == item:
        self.delete(index)

      index += 1

  def find(self, item: T) -> int:
    for index, value in zip(range(self._size), self._list):
      if value == item:
        return index

    return -1



if __name__ == '__main__':
  v: Vector[int] = Vector()

  for i in range(10):
    v.push(i)

  print(f'{v=}')

  v.insert(5, 10)
  print(f'{v=}')

  v.prepend(11)
  print(f'{v=}')

  for i in range(12, 16):
    v.push(i)

  print(f'{v=}')

  v.push(16)
  print(f'{v=}')

  print(f'{v.pop()=}')
  print(f'{v=}')

  v.delete(11)
  print(f'{v=}')

  v.insert(7, 1)
  print(f'{v=}')

  v.remove(1)
  print(f'{v=}')

  print(f'{v.find(6)=}')
  print(f'{v.find(16)=}')
