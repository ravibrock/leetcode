class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.pairs = collections.OrderedDict()

    def get(self, key: int) -> int:
        try: self.pairs.move_to_end(key, last=True)
        except: return -1
        else: return self.pairs[key]
        
    def put(self, key: int, value: int) -> None:
        self.pairs[key] = value
        self.pairs.move_to_end(key, last=True)
        if len(self.pairs) > self.capacity: self.pairs.popitem(last=False)
