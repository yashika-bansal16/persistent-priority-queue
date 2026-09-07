Persistent Priority Queue

A Python implementation of a persistent priority queue using min heap, max heap, and JSON storage.

Features

- Insert item with priority
- Peek minimum priority
- Extract minimum / maximum
- Update priority
- Delete item
- Check if queue is empty
- Persistent storage using JSON

Tech Stack

- Python 3
- "heapq"
- JSON
- "unittest"

Operations

Operation| Complexity
Insert| O(log n)
Peek| O(1)
Extract Min| O(log n)
Extract Max| O(log n)
Update| O(log n)
Delete| O(1)

Persistence

Queue data is stored in "queue.json" and automatically loaded when the program starts.

Testing

Run:

python -m unittest test_module.py

Project Structure

persistent-priority-queue/
├── module.py
├── test_module.py
├── queue.json
├── README.md
└── .gitignore

Requirements

Python 3. No external packages required.

Author

Yashika Bansal
