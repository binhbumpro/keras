import threading
import time


class ThreadingBatches(object):
    """ Threading example class
    The run() method will be started and it will run in the background
    Will run next( GENERATOR ) in this thresh and using CPU while GPU training
    until the application exits.
    """
    batch_thread = None

    def __init__(self, generator=None):
        """ Constructor
        :type interval: int
        :param interval: Check interval, in seconds
        """
        self.generator = generator
        self.stack = []
        self.queue_size = 50
        self.thread = threading.Thread(target=self.run, args=())
        self.thread.daemon = True  # Daemonize thread

        # self.thread.start()  # Start the execution

    def run(self):
        """ Method that runs forever """
        print('Create generator Thresh')
        while True:
            # Do something
            if (len(self.stack) < self.queue_size):

                # print('add batch {}'.format(len(self.stack)))
                try:
                    batch = next(self.generator)
                    self.stack.append(batch)
                except ValueError:
                    None

    def thresh_next(self):
        while len(self.stack) == 0:
            """return next while none stack"""
            time.sleep(0.001)
        return self.stack.pop(0)

    def restart(self, generator):
        self.generator = generator
        self.stack = []