class TimeMap:

    def __init__(self):
        # Initialize the dictionary
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Add value and timestamp to the key
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Return empty string if key is not found
        if not key in self.hash_map:
            return ""
        
        values = self.hash_map[key]
        left, right = 0, len(values) - 1

        # Binary search for the closest timestamp <= given timestamp
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                left = mid + 1
            else:
                right = mid - 1

        # Return the value with the closest timestamp <= given timestamp
        return values[right][0] if right >= 0 else ""



t = TimeMap()
t.set("foo", "bar", 1)
print(t.get("foo", 1))