from datetime import datetime

class Timer():
    # A simple timer class
    def __init__(self):
        pass

    def start(self):
        # Starts the timer
        self.start = datetime.now()
        return self.start

    def stop(self, message="Total: "):
        # Stops the timer.  Returns the time elapsed
        self.stop = datetime.now()
        return message + str(self.stop - self.start)

    def now(self, message="Now: "):
        # Returns the current time with a message
        return message + str(datetime.now())

    def elapsed(self, message="Elapsed: "):
        # Time elapsed since start was called
        return message + str(datetime.now() - self.start)

    def split(self, message="Split started at: "):
        # Start a split timer
        self.split_start = datetime.now()
        return message + str(self.split_start)

    def unsplit(self, message="Unsplit: "):
        # Stops a split. Returns the time elapsed since split was called
        return message + str(datetime.now() - self.split_start)