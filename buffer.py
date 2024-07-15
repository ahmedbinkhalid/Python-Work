import threading
import random
import time
import sys

# Class to represent the bounded buffer
class BoundedBuffer:
    def __init__(self, size):
        # Initialize the buffer and synchronization primitives
        self.buffer = [None] * size
        self.size = size
        self.in_index = 0
        self.out_index = 0
        self.count = 0
        self.lock = threading.Lock()
        self.not_empty = threading.Condition(self.lock)
        self.not_full = threading.Condition(self.lock)

    # Method for producer to add items to the buffer
    def produce(self, item):
        with self.not_full:
            while self.count == self.size:
                self.not_full.wait()  # Wait until there's space in the buffer
            self.buffer[self.in_index] = item
            self.in_index = (self.in_index + 1) % self.size
            self.count += 1
            self.not_empty.notify()  # Notify consumers that the buffer is not empty

    # Method for consumer to remove items from the buffer
    def consume(self):
        with self.not_empty:
            while self.count == 0:
                self.not_empty.wait()  # Wait until there's something to consume
            item = self.buffer[self.out_index]
            self.out_index = (self.out_index + 1) % self.size
            self.count -= 1
            self.not_full.notify()  # Notify producers that the buffer is not full
            return item

# Producer function that generates items and adds them to the buffer
def producer(buffer, limit):
    for _ in range(limit):
        item = random.randint(1, 100)
        buffer.produce(item)
        print(f"Produced: {item}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate production time

# Consumer function that consumes items from the buffer
def consumer(buffer, limit):
    for _ in range(limit):
        item = buffer.consume()
        print(f"Consumed: {item}")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate consumption time

# Main function that sets up and runs the producer and consumer threads
def main():
    if len(sys.argv) != 3:
        print("Usage: python producer_consumer.py <buffer_size> <counter_limit>")
        sys.exit(1)

    buffer_size = int(sys.argv[1])
    counter_limit = int(sys.argv[2])

    buffer = BoundedBuffer(buffer_size)

    producer_thread = threading.Thread(target=producer, args=(buffer, counter_limit))
    consumer_thread = threading.Thread(target=consumer, args=(buffer, counter_limit))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    print("Both threads have finished. Main program terminates.")

if __name__ == "__main__":
    main()
