import queue


class RecentCounter:

    def __init__(self):
        self.counter = 0
        self.queue = queue.Queue()


    def ping(self, t: int) -> int:
        self.queue.put(t)
        self.counter += 1

        min_val = t - 3000

        while self.queue.queue[0] < min_val:
            self.queue.get()
            self.counter -= 1

        return self.counter

q = RecentCounter()
print(q.ping(1))
print(q.ping(100))
print(q.ping(3001))
print(q.ping(3002))
