class Queue:
    def pop(self):
        pass

    def push(self, n):
        pass

    def size(self):
        pass


class Stack:
    def __init__(self):
        self._stack = []

    def pop(self):
        return self._stack.pop()

    def push(self, x):
        self._stack.append(x)

    def size(self):
        return len(self._stack)


# implement Queue
class StacksQueue(Queue):
    def __init__(self):
        self._q_part1 = Stack()
        self._q_part2 = Stack()

    def pop(self):
        if self._q_part2.size() == 0:
            if self._q_part1.size() > 0:
                for i in range(self._q_part1.size()):
                    self._q_part2.push(self._q_part1.pop())
                n = self._q_part2.pop()
                print("popped", n)
                return n
            else:
                print("stack is empty, nothing to pop")
        else:
            n = self._q_part2.pop()
            print("popped", n)
            return n

    def push(self, x):
        self._q_part1.push(x)
        print("pushed", x)

    def size(self):
        return self._q_part1.size() + self._q_part2.size()


class MaxElementQueue(Queue):
    def __init__(self):
        self._q_part1 = Stack()
        self._q_part2 = Stack()
        self.max = 0

    def pop(self):
        arr = []
        self.max = - (2 ** 128)
        if self._q_part2.size() == 0:
            if self._q_part1.size() > 0:
                for i in range(1, self._q_part1.size()):
                    value = self._q_part1.pop()
                    self._q_part2.push(value)
                    if value > self.max:
                        self.max = value
                n = self._q_part1.pop()
                print("popped", n)
                return n
            else:
                print("stack is empty, nothing to pop")
        else:
            n = self._q_part2.pop()
            print("popped", n)
            for i in range(self._q_part2.size()):
                value = self._q_part2.pop()
                if value > self.max:
                    self.max = value
                arr.append(value)
            arr.reverse()
            for i in range(len(arr)):
                self._q_part2.push(arr[i])
            return n

    def push(self, n):
        if self.size() == 0:
            self.max = n
        else:
            if n >= self.max:
                self.max = n
        self._q_part1.push(n)
        print("pushed", n)

    def size(self):
        return self._q_part1.size() + self._q_part2.size()

    def max_elem(self):
        if self.size() == 0:
            print("stack is empty")
        else:
            print(self.max)
            return self.max

