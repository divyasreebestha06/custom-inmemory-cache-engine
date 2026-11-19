import time
from typing import Any, Optional

class CacheNode:
    def __init__(self, key: str, value: Any, ttl_seconds: Optional[float] = None):
        self.key = key
        self.value = value
        self.expires_at = (time.time() + ttl_seconds) if ttl_seconds else None
        self.prev: Optional['CacheNode'] = None
        self.next: Optional['CacheNode'] = None

    def is_expired(self) -> bool:
        if self.expires_at is None:
            return False
        return time.time() > self.expires_at
