import time
import random
import threading
from threading import Lock, Condition

class Queue:
    def __init__(self, max_size=10):
        self.arr = [None] * max_size
        self.item_count = 0
        self.max_size = max_size
        self.get_idx = 0
        self.put_idx = 0
        self.lock = Lock()
        self.not_full = Condition(self.lock)
        self.not_empty = Condition(self.lock)

    def put(self, item):
        try:
            self.lock.acquire()
            while self.item_count == self.max_size:
                self.not_full.wait()

            self.arr[self.put_idx] = item
            self.put_idx += 1
            if self.put_idx == self.max_size:
                self.put_idx = 0
            self.item_count += 1
            self.not_empty.notify()
            print ("[%s] produced item: %s :: %s" % (threading.current_thread().name, item, self))
            print ("-----------------------------------------------------------------")
        finally:
            self.lock.release()

    def get(self):
        try:
            self.lock.acquire()
            while self.item_count == 0:
                self.not_empty.wait()

            item = self.arr[self.get_idx]
            self.get_idx += 1
            if self.get_idx == self.max_size:
                self.get_idx = 0
            self.item_count -= 1
            self.not_full.notify()
            print ("[%s] consumed item: %s :: %s" % (threading.current_thread().name, item, self))
            print ("-----------------------------------------------------------------")
            return item
        finally:
            self.lock.release()

    def __str__(self):
        return "[Count:%s :: GetPtr:%s :: PutPtr:%s :: %s]" % (self.item_count, self.get_idx, self.put_idx, self.arr)

class ProducerConsumer:
    def __init__(self, queue, num_producers, num_consumers):
        self.queue = queue
        self.producer_threads = []
        self.consumer_threads = []
        for i in range(num_producers):
            _name = "producer:%d" % i
            thread = threading.Thread(name=_name, target=self.produce, args=(i,))
            self.producer_threads.append(thread)

        for i in range(num_consumers):
            _name = "consumer:%d" % i
            thread = threading.Thread(name=_name, target=self.consume, args=(i,))
            self.consumer_threads.append(thread)

    def produce(self, item_id):
        while True:
            item = "[Item:%d]" % item_id
            self.queue.put(item)
            time.sleep(random.randint(1,5))

    def consume(self, *args):
        while True:
            item = self.queue.get()
            time.sleep(random.randint(1,5))

    def start(self):
        for t in self.producer_threads + self.consumer_threads:
            print ("starting: %s" % t.name)
            t.start()

        for t in self.consumer_threads + self.producer_threads:
            t.join()

def main():
    queue = Queue(5)
    pc = ProducerConsumer(queue, 4, 1)
    pc.start()

if __name__ == "__main__":
    main()
