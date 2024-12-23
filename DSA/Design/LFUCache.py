from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_map = {}  # Key -> (value, frequency)
        self.freq_map = defaultdict(OrderedDict)  # frequency -> OrderedDict of keys
        self.min_freq = 0

    def get(self, key: int) -> int:
        if key not in self.key_map:
            return -1

        value, freq = self.key_map[key]
        self._update_(key, value, freq)
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.key_map:
            _, freq = self.key_map[key]
            self._update_(key, value, freq)
        else:
            if len(self.key_map) >= self.capacity:
                self._evict_()

            self.key_map[key] = (value, 1)
            self.freq_map[1][key] = None
            self.min_freq = 1

    def _update_(self, key: int, value: int, freq: int):
        del self.freq_map[freq][key]

        new_freq = freq + 1
        self.key_map[key] = (value, new_freq)
        self.freq_map[new_freq][key] = None

        if not self.freq_map[freq]:
            del self.freq_map[freq]
            if freq == self.min_freq:
                self.min_freq += 1

    def _evict_(self):
        key, _ = self.freq_map[self.min_freq].popitem(last=False)
        del self.key_map[key]
