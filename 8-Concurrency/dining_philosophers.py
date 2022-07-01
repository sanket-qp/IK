import time
import random
from threading import Thread, Condition

class Chopstick(Condition):
    """
    Chopstick is a condition variable which acts as a lock
    """
    def __init__(self, name):
        Condition.__init__(self)
        self.name = name

    def __str__(self):
        return self.name


class Philosopher(Thread):
    def __init__(self, name, left_chopstick, right_chopstick):
        Thread.__init__(self)
        self.name = name
        self.left_chopstick = left_chopstick
        self.right_chopstick = right_chopstick
        self.done = False

    def run(self):
        while not self.done:
            self.think()
            self.eat()
        print ("%s is done eating" % self.name)

    def eat(self):
        """
        We're trying to avoid the deadlock by fixing the order of locks. 
        Every philosopher first tries to pick up the left chopstick first and then the right chopstick.

        This is a one way we can avoid deadlock by enforcing that every thread acquires the lock in a 
        predefined static fashion.
        """
        with self.left_chopstick:
            with self.right_chopstick:
                print ("%s is eating" % self.name)
                self.random_sleep()
                self.right_chopstick.notify_all()
            self.left_chopstick.notify_all()

        # just some random stop condition
        self.done = (random.randint(1,6) == 5)

    def think(self):
        print ("%s is thinking" % self.name)
        self.random_sleep()

    def random_sleep(self):
        time.sleep(0.1 * random.randint(1,5))

    def __str__(self):
        return "%s:[%s, %s]" % (self.name, self.left_chopstick, self.right_chopstick)


class DiningPhilosophersWithMultipleLocks:
    def __init__(self, num_philosophers=5):
        self.num_philosophers = num_philosophers
        self.chopsticks = [Chopstick("Chopstick:%d" % i) for i in range(num_philosophers)]
        self.philosophers = []
        for i in range(self.num_philosophers):
            name = "Philosopher:%d" % i
            left_chopstick = self.chopsticks[i-1]
            right_chopstick = self.chopsticks[i]
            self.philosophers.append(Philosopher(name, left_chopstick, right_chopstick))
            print ("%s" % self.philosophers[i])

    def start(self):
        for p in self.philosophers:
            p.start()


def main():
    dp = DiningPhilosophersWithMultipleLocks(5)
    dp.start()

if __name__ == "__main__":
    main()
