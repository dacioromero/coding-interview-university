## Singly-linked

SImilar to "links in a chain" head that points to a node which then point to nodes themselves.

Fixes the problem where inserting anywhere at the end of a normal list the operation is always O(n) time

Recursive data structure.

Automatically grows compared to regular lists

LinkedList

- `head` -> `Node`

`Node`

- `item`

- `next` -> `Node`

### API

| Function       | Description       | Order |
| -------------- | ----------------- | ----- |
| PushFront(Key) | add to front      | O(1)  |
| Key TopFront() | return front item | O(1)  |
| PopFront()     | remove front item | O(1)  |
| PushBack(Key)  | add to back       | O(n)  |
| Key TopBack    | return back item  | O(n)  |
| PopBack        | remove back item  | O(1)  |
