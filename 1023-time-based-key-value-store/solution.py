class TimeMap:
    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.keys.keys(): self.keys[key][timestamp] = value
        else: self.keys[key] = {timestamp: value}

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keys.keys(): return ""
        timestamps = self.keys[key].keys()
        for timestamp_prev in reversed(timestamps):
            if timestamp_prev <= timestamp: return self.keys[key][timestamp_prev]
        return ""
