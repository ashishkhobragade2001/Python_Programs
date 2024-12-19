import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.elapsed_time = 0

    def start(self):
        if self.start_time is None:
            self.start_time = time.time()

    def stop(self):
        if self.start_time is not None:
            self.elapsed_time += time.time() - self.start_time
            self.start_time = None

    def reset(self):
        self.start_time = None
        self.elapsed_time = 0

    def elapsed(self):
        if self.start_time is None:
            return self.elapsed_time
        return self.elapsed_time + (time.time() - self.start_time)

stopwatch = Stopwatch()
stopwatch.start()
time.sleep(2)  # Simulating a process
stopwatch.stop()
print("Elapsed time:", stopwatch.elapsed())
# Output: Approximately 2.0 seconds
