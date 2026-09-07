import os
import unittest

from module import PersistentPriorityQueue


TEST_FILE = "test_queue.json"


class TestPersistentPriorityQueue(unittest.TestCase):

    def setUp(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

        self.pq = PersistentPriorityQueue(TEST_FILE)

    def tearDown(self):
        if os.path.exists(TEST_FILE):
            os.remove(TEST_FILE)

    def test_insert_and_peek(self):
        item_id = self.pq.insert("Fix bug", 1)

        result = self.pq.peek()

        self.assertEqual(result["id"], item_id)
        self.assertEqual(result["value"], "Fix bug")
        self.assertEqual(result["priority"], 1)

    def test_extract_min(self):
        self.pq.insert("Fix bug", 1)
        self.pq.insert("Study DSA", 5)
        self.pq.insert("Watch movie", 10)

        result = self.pq.extract_min()

        self.assertEqual(result["value"], "Fix bug")
        self.assertEqual(result["priority"], 1)

    def test_extract_max(self):
        self.pq.insert("Fix bug", 1)
        self.pq.insert("Study DSA", 5)
        self.pq.insert("Watch movie", 10)

        result = self.pq.extract_max()

        self.assertEqual(result["value"], "Watch movie")
        self.assertEqual(result["priority"], 10)

    def test_update(self):
        item_id = self.pq.insert("Study DSA", 5)

        result = self.pq.update(item_id, 1)

        self.assertEqual(result["priority"], 1)
        self.assertEqual(
            self.pq.items[item_id]["priority"],
            1
        )

    def test_delete(self):
        item_id = self.pq.insert("Fix bug", 1)

        result = self.pq.delete(item_id)

        self.assertEqual(result["id"], item_id)
        self.assertNotIn(item_id, self.pq.items)

    def test_is_empty(self):
        self.assertTrue(self.pq.is_empty())

        self.pq.insert("Fix bug", 1)

        self.assertFalse(self.pq.is_empty())

    def test_persistence(self):
        item_id = self.pq.insert("Study DSA", 5)

        # Create a new queue using the same storage file
        new_queue = PersistentPriorityQueue(TEST_FILE)

        self.assertIn(item_id, new_queue.items)
        self.assertEqual(
            new_queue.items[item_id]["value"],
            "Study DSA"
        )
        self.assertEqual(
            new_queue.items[item_id]["priority"],
            5
        )


if __name__ == "__main__":
    unittest.main()