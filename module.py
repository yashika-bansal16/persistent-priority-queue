import heapq
import json
import os


class PersistentPriorityQueue:
    def __init__(self, storage_file="queue.json"):
        self.storage_file = storage_file

        self.items = {}
        self.min_heap = []
        self.max_heap = []
        self.next_id = 1

        self._load()

    def insert(self, value, priority):
        item_id = self.next_id
        self.next_id += 1

        self.items[item_id] = {
            "value": value,
            "priority": priority
        }

        heapq.heappush(self.min_heap, (priority, item_id))
        heapq.heappush(self.max_heap, (-priority, item_id))

        self._save()

        return item_id

    def peek(self):
        while self.min_heap:
            priority, item_id = self.min_heap[0]

            if item_id not in self.items:
                heapq.heappop(self.min_heap)
                continue

            if self.items[item_id]["priority"] != priority:
                heapq.heappop(self.min_heap)
                continue

            return {
                "id": item_id,
                "value": self.items[item_id]["value"],
                "priority": priority
            }

        return None

    def extract_min(self):
        while self.min_heap:
            priority, item_id = heapq.heappop(self.min_heap)

            if item_id not in self.items:
                continue

            item = self.items[item_id]

            if item["priority"] != priority:
                continue

            item = self.items.pop(item_id)

            self._save()

            return {
                "id": item_id,
                "value": item["value"],
                "priority": priority
            }

        return None

    def extract_max(self):
        while self.max_heap:
            negative_priority, item_id = heapq.heappop(self.max_heap)

            if item_id not in self.items:
                continue

            priority = -negative_priority
            item = self.items[item_id]

            if item["priority"] != priority:
                continue

            item = self.items.pop(item_id)

            self._save()

            return {
                "id": item_id,
                "value": item["value"],
                "priority": priority
            }

        return None

    def update(self, item_id, new_priority):
        if item_id not in self.items:
            return None

        self.items[item_id]["priority"] = new_priority

        heapq.heappush(self.min_heap, (new_priority, item_id))
        heapq.heappush(self.max_heap, (-new_priority, item_id))

        self._save()

        return {
            "id": item_id,
            "value": self.items[item_id]["value"],
            "priority": new_priority
        }

    def delete(self, item_id):
        if item_id not in self.items:
            return None

        item = self.items.pop(item_id)

        self._save()

        return {
            "id": item_id,
            "value": item["value"],
            "priority": item["priority"]
        }

    def is_empty(self):
        return len(self.items) == 0

    def _save(self):
        data = {
            "next_id": self.next_id,
            "items": self.items
        }

        with open(self.storage_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def _load(self):
        if not os.path.exists(self.storage_file):
            return

        with open(self.storage_file, "r", encoding="utf-8") as file:
            data = json.load(file)

        self.next_id = data.get("next_id", 1)

        self.items = {
            int(item_id): item
            for item_id, item in data.get("items", {}).items()
        }

        self.min_heap = []
        self.max_heap = []

        for item_id, item in self.items.items():
            priority = item["priority"]

            heapq.heappush(
                self.min_heap,
                (priority, item_id)
            )

            heapq.heappush(
                self.max_heap,
                (-priority, item_id)
            )