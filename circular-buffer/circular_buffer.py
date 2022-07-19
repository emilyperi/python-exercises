class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer:

    def __init__(self, capacity):
        # RPOINTER defines next read location, , WPOINTER the next write, SIZE stores number of items in buffer
        self.buffer = [0] * capacity
        self.capacity = capacity
        self.rpointer = 0
        self.wpointer = 0
        self.size = 0

    def read(self):
        # return BaseException for reads at end of buffer
        if self.size == 0:
            raise BaseException("End of buffer")

        else:
            # read at pointer index
            to_read = self.buffer[self.rpointer]
            self.rpointer = (self.rpointer + 1) % self.capacity
            # free up write if end of buffer
            self.size -= 1 

            return to_read

    def write(self, data):
        # write to buffer if there is still space   
        if self.size < self.capacity:
            self.buffer[self.wpointer] = data
            self.wpointer = (self.wpointer + 1) % self.capacity
            self.size += 1

        else:
            # raise error with the buffer is full
            raise Exception("Buffer is full, to force write use overwrite(data)")

    def overwrite(self, data):
        # when buffer if is full, wpointer is positioned at oldest data, otherwise is next write location
        self.buffer[self.wpointer] = data
        self.wpointer = (self.wpointer + 1) % self.capacity

        # when buffer is not full, we increment the size
        if self.size < self.capacity:
            self.size += 1
         # when buffer is full, rpointer must increment to next oldest data   
        else:
            self.rpointer = (self.rpointer + 1) % self.capacity

    def clear(self):
        self.buffer = [0] * self.capacity
        self.size = self.rpointer = self.wpointer = 0
