import unittest
import time
from cache.lru_cache import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_lru_eviction(self):
        c = LRUCache(capacity=2)
        c.set("k1", "v1")
        c.set("k2", "v2")
        self.assertEqual(c.get("k1"), "v1")
        c.set("k3", "v3") # k2 evicted
        self.assertIsNone(c.get("k2"))
        self.assertEqual(c.get("k3"), "v3")

    def test_ttl_expiration(self):
        c = LRUCache(capacity=5)
        c.set("temp", "value", ttl=0.1)
        self.assertEqual(c.get("temp"), "value")
        time.sleep(0.15)
        self.assertIsNone(c.get("temp"))

if __name__ == "__main__":
    unittest.main()
