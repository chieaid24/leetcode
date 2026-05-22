class MinStack:
    # initial idea is use a list and a min heap (but then how do we remove an element that is not the min)
    # instead of doing this, for each push, we store another "stack" list that tracks the min value at this point so we
    # can return at any time. Then at any pop() we pop from both stacks, to get the min value at the next point
    # this allows us to track the min value at ANY point by breaking down into subproblems, and realizing that we can track
    # the ongoing min -> and treat it as a parallel stack
    def __init__(self):
        self.stack = []
        self.min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min:
            self.min.append(val)
        else:
            self.min.append(min(val, self.min[-1]))

    def pop(self) -> None:
        self.stack.pop()
        self.min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]
