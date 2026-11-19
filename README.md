# ⚡ custom-inmemory-cache-engine

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LRU](https://img.shields.io/badge/Eviction-O(1)_LRU-brightgreen?style=for-the-badge)](cache/)

Thread-Safe In-Memory Key-Value Cache Engine in Python supporting LRU eviction and TTL expiration.

## Key Technical Highlights
- **$O(1)$ Hash Map + Doubly Linked List:** Constant time access and update operations.
- **TTL Support:** Automatic lazy eviction of expired keys.
- **Thread-Safe:** Protected by mutex locks for multi-threaded applications.
- **Cache Telemetry:** Tracks hits, misses, and hit rate percentage.
