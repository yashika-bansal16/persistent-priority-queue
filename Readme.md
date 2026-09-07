Persistent Priority Queue

A Python implementation of a persistent priority queue.

The queue supports both minimum and maximum priority operations and stores its data in a JSON file so that the data is available even after restarting the program.

Features

- Insert an item with a priority
- Peek at the minimum-priority item
- Extract minimum-priority item
- Extract maximum-priority item
- Update an item's priority
- Delete an item
- Check if the queue is empty
- Save and load queue data using JSON

How It Works

I used three main data structures:

- "items" - stores the actual items using their unique IDs.
- "min_heap" - helps find the item with the lowest priority.
- "max_heap" - helps find the item with the highest priority.

Python's "heapq" module is used for the heaps. For the max-heap, negative priority values are stored because "heapq" provides a min-heap.

For persistence, the queue is saved in "queue.json". When the program starts, the saved data is loaded and the heaps are rebuilt.

For update and delete operations, old heap entries can remain in the heap. These entries are checked and ignored when they are no longer valid.

Main Operations

Insert

item_id = pq.insert("Study DSA", 5)

Peek

Returns the item with the lowest priority without removing it.

pq.peek()

Extract Min

Removes and returns the item with the lowest priority.

pq.extract_min()

Extract Max

Removes and returns the item with the highest priority.

pq.extract_max()

Update

Changes the priority of an existing item.

pq.update(item_id, 1)

Delete

Deletes an item using its ID.

pq.delete(item_id)

Is Empty

Checks whether the queue contains any items.

pq.is_empty()

Persistence

The queue data is stored in:

queue.json

The file is updated whenever the queue is modified.

When a new "PersistentPriorityQueue" object is created, it loads the saved data from the file.

Testing

Automated tests are included in "test_module.py".

Run the tests with:

python -m unittest test_module.py

The tests cover insertion, peek, extraction, update, delete, empty-checking, and persistence.

Time Complexity

Operation| Complexity
Insert| O(log n)
Peek| O(1)
Extract Min| O(log n) amortized
Extract Max| O(log n) amortized
Update| O(log n)
Delete| O(1)
Is Empty| O(1)

The JSON file adds some file-writing overhead whenever the queue is modified.

Project Structure

persistent-priority-queue/
│
├── module.py
├── test_module.py
├── queue.json
└── README.md

Requirements

- Python 3
- No external Python packages are required.