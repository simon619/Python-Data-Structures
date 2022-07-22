class Priority_Queue:

    def __init__(self):
        self.que = []

    def __heapify__(self, que, n, pointer):
        largest = pointer
        left, right = 2 * pointer + 1, 2 * pointer + 2

        if left < n and que[left] > que[largest]:
            largest = left

        if right < n and que[right] > que[largest]:
            largest = right

        if largest != pointer:
            que[largest], que[pointer] = que[pointer], que[largest]
            self.__heapify__(que, n, largest)

    def __insert__(self, number):
        if not self.que:
            self.que.append(number)

        else:
            self.que.append(number)
            for i in range(len(self.que) // 2 - 1, -1, -1):
                self.__heapify__(self.que, len(self.que), i)

    def __delete__(self, number):
        if not self.que:
            print("Not Possible")

        else:
            delete = None
            for i in range(len(self.que)):
                if self.que[i] is number:
                    delete = i
                    break

            self.que[delete], self.que[len(self.que) - 1] = self.que[len(self.que) - 1], self.que[delete]
            del self.que[-1]
            for i in range(len(self.que) // 2 - 1, -1, -1):
                self.__heapify__(self.que, len(self.que), i)

    def __print__(self):
        print(f'Priority Queue: {self.que}')


if __name__ == "__main__":
    print("Insert Data In Priority Queue: ")
    queue = Priority_Queue()
    queue.__insert__(3)
    queue.__insert__(4)
    queue.__insert__(9)
    queue.__insert__(5)
    queue.__insert__(2)
    queue.__print__()
    print("Delete Data In Priority Queue: ")
    queue.__delete__(4)
    queue.__print__()
