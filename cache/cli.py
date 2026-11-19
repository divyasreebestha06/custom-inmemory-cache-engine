from cache.lru_cache import LRUCache

def demo():
    cache = LRUCache(capacity=3)
    cache.set("A", "Alpha")
    cache.set("B", "Beta")
    cache.set("C", "Gamma")
    print("Fetched A:", cache.get("A"))
    cache.set("D", "Delta") # Should evict B
    print("Fetched B (evicted):", cache.get("B"))
    print("Cache stats:", cache.stats())

if __name__ == "__main__":
    demo()
