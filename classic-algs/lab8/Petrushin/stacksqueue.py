__author__ = 'Dmitry Petrushin'

from sys import stdin as inp
from sys import stdout as out


class Stack:
    def __init__(self):
        self._stack = []
        self._max_stack = []

    def push(self, element):
        self._stack.append(element)
        self._max_stack.append(max(element, self._max_stack[len(self._max_stack) - 1] if self._max_stack else 0))

    def pop(self):
        self._max_stack.pop()
        return self._stack.pop()

    def max(self):
        return self._max_stack[len(self._max_stack) - 1] if self._max_stack else 0

    def empty(self):
        return self._stack

    def __len__(self):
        return len(self._stack)


class Queue:
    def pop(self):
        pass

    def push(self, element):
        pass

    def size(self):
        pass


class StacksQueue(Queue):
    def __init__(self):
        self._inbox = Stack()
        self._outbox = Stack()

    def pop(self):
        if not self._outbox.empty():
            while self._inbox.empty():
                self._outbox.push(self._inbox.pop())
        return self._outbox.pop()

    def push(self, element):
        self._inbox.push(element)

    def size(self):
        return len(self._inbox) + len(self._outbox)


class MaxElementQueue(Queue):
    def __init__(self):
        self._queue = StacksQueue()

    def pop(self):
        self._queue.pop()

    def push(self, element):
        self._queue.push(element)

    def size(self):
        return self._queue.size()

    def max(self):
        return max(self._queue._inbox.max(), self._queue._outbox.max())


def arg_check(arg):
    try:
        int(arg)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    queue = MaxElementQueue()
    requests = [line.split() for line in inp.readlines()]
    for request in requests:
        if not request:
            out.write('empty\n')
        else:
            if request[0] == 'push':
                if len(request) > 1:
                    if arg_check(request[1]):
                        queue.push(int(request[1]))
                        out.write('ok\n')
                    else:
                        out.write('empty\n')
                else:
                    out.write('empty\n')
            elif request[0] == 'pop':
                if queue.size() > 0:
                    queue.pop()
                    out.write('ok\n')
                else:
                    out.write('empty\n')
            elif request[0] == 'max':
                if queue.size() > 0:
                    out.write(str(queue.max()) + '\n')
                else:
                    out.write('empty\n')