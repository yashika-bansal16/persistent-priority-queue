Persistent Priority Queue

A Python implementation of a persistent priority queue using heaps and JSON file storage.

The queue supports both minimum and maximum priority operations, and the data remains available even after restarting the program.

Features

- Insert an item with a priority
- Peek at the minimum-priority item
- Extract minimum-priority item
- Extract maximum-priority item
- Update an item's priority
- Delete an item
- Check if the queue is empty
- Persistent storage using JSON
- Automatically restores data when the program starts

How It Works

The implementation uses:

1. Dictionary

The "items" dictionary stores the actual queue items using a unique ID.

ID → Value + Priority

2. Min Heap

A min heap is used to quickly find the item with the lowest priority.

3. Max Heap

A second heap is used for maximum-priority operations.

Python's "heapq" module only provides a min heap, so negative priorities are stored to simulate a max heap.

4. JSON Storage

The current queue state is stored in "queue.json".

When the program starts, the saved items are loaded and the heaps are rebuilt.

Example

from module import PersistentPriorityQueue

pq = PersistentPriorityQueue()

item_id = pq.insert("Study DSA", 5)

print(pq.peek())

pq.update(item_id, 1)

print(pq.extract_min())

Operations

Operation| Description
"insert(value, priority)"| Adds a new item
"peek()"| Returns the lowest-priority item
"extract_min()"| Removes the lowest-priority item
"extract_max()"| Removes the highest-priority item
"update(id, priority)"| Changes an item's priority
"delete(id)"| Removes an item
"is_empty()"| Checks whether the queue is empty

Persistence

Queue data is stored in:

queue.json

For example:

{
    "next_id": 4,
    "items": {
        "1": {
            "value": "Study DSA",
            "priority": 5
        }
    }
}

The file is updated whenever the queue is modified.

If the program is closed and started again, the previous queue data is loaded automatically.

Handling Updates and Deletes

The heaps may contain old entries after an item is updated or deleted.

Instead of searching through the heap and removing those entries immediately, the implementation checks whether a heap entry is still valid when it is accessed.

Invalid entries are skipped.

This approach is commonly known as lazy deletion.

Time Complexity

Operation| Complexity
Insert| O(log n)
Peek| O(1)
Extract Min| O(log n) amortized
Extract Max| O(log n) amortized
Update| O(log n)
Delete| O(1)
Is Empty| O(1)

The JSON file is rewritten when the queue is modified, so persistence adds file I/O overhead.

Testing

Automated tests are included in "test_module.py".

Run:

python -m unittest test_module.py

The tests cover:

- Insert and peek
- Extract minimum
- Extract maximum
- Update
- Delete
- Empty queue check
- Data persistence

Project Structure

persistent-priority-queue/
│
├── module.py
├── test_module.py
├── queue.json
├── README.md
└── .gitignore

Requirements

- Python 3
- No external Python packages required

Author

Yashika Bansal