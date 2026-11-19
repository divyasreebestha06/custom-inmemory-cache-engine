import threading
from typing import Any, Optional, Dict
from cache.node import CacheNode

class LRUCache:
    def __init__(self, capacity: int = 100):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.lookup: Dict[str, CacheNode] = {}
        self.head = CacheNode("__HEAD__", None)
        self.tail = CacheNode("__TAIL__", None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.lock = threading.Lock()
        self.hits = 0
        self.misses = 0

    def _remove(self, node: CacheNode):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: CacheNode):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: str) -> Optional[Any]:
        with self.lock:
            if key not in self.lookup:
                self.misses += 1
                return None
            node = self.lookup[key]
            if node.is_expired():
                self._remove(node)
                del self.lookup[key]
                self.misses += 1
                return None
            self._remove(node)
            self._add_to_front(node)
            self.hits += 1
            return node.value

    def set(self, key: str, value: Any, ttl: Optional[float] = None):
        with self.lock:
            if key in self.lookup:
                node = self.lookup[key]
                self._remove(node)
                del self.lookup[key]
            elif len(self.lookup) >= self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.lookup[lru.key]

            new_node = CacheNode(key, value, ttl)
            self._add_to_front(new_node)
            self.lookup[key] = new_node

    def stats(self) -> Dict[str, Any]:
        with self.lock:
            total = self.hits + self.misses
            rate = (self.hits / total * 100) if total > 0 else 0.0
            return {
                "size": len(self.lookup),
                "capacity": self.capacity,
                "hits": self.hits,
                "misses": self.misses,
                "hit_rate_pct": round(rate, 2)
            }
