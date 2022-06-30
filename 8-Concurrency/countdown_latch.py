import time
import random
import threading

class xCountDownLatch:
    """
    Initial implementation
    """
    def __init__(self, count, name):
        self.name = name
        self.count = count
        self.lock = threading.Lock()
        self.count_is_zero = threading.Condition(self.lock)

    def count_down(self):
        self.lock.acquire()
        self.count = max(self.count-1, 0)
        if self.count == 0:
            self.count_is_zero.notify_all()
            print ("latch done :: %s" % self)
        self.lock.release()

    def wait(self):
        try:
            self.lock.acquire()
            while self.count > 0:
                print ("latch waiting :: %s " % self)
                self.count_is_zero.wait()
        finally:
            self.lock.release()

    def __str__(self):
        return "[%s:%s]" % (self.name, self.count)

class CountDownLatch:
    def __init__(self, count, name):
        self.name = name
        self.count = count
        self.count_is_zero = threading.Condition()

    def count_down(self):
        with self.count_is_zero:
            self.count = max(self.count-1, 0)
            if self.count == 0:
                self.count_is_zero.notify_all()
                print ("latch done :: %s" % self)

    def wait(self):
        with self.count_is_zero:
            while self.count > 0:
                print ("latch waiting :: %s " % self)
                self.count_is_zero.wait()

    def __str__(self):
        return "[%s:%s]" % (self.name, self.count)

class Race:
    def __init__(self, num_runners=5):
        self.num_runners = num_runners
        self.ready = CountDownLatch(num_runners, "READY")
        self.signal = CountDownLatch(1, "START")
        self.done = CountDownLatch(num_runners, "DONE")

    def start(self):
        # start worker threads
        for i in range(self.num_runners):
            name = "runner:%d" % i
            t = threading.Thread(name=name, target=self.run)
            t.start()

        print ("referee is signaling the start")
        self.signal.count_down()
        print ("referee signalled the start")
        print ("referee is waiting for runners to finish the race")
        self.done.wait()
        print ("race done")

    def run(self):
        thread_name = threading.current_thread().name
        self.ready.count_down()
        print ("%s is waiting to start :: %s" % (thread_name, self.ready))
        self.signal.wait()
        print ("%s is starting" % thread_name)
        for i in range(5):
            print ("%s is working" % thread_name)
            time.sleep(0.1 * random.randint(1,5))
        self.done.count_down()
        print ("%s is done :: %s" % (thread_name, self.done))

def main():
    race = Race(5)
    race.start()

if __name__ == "__main__":
    main()
