class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # curr algorithm, walk through the thing, treating as a stack (or keeping an external
        # variable of the top of the stack) where we store the top 2 elements, multiply / add them
        # together by the next item, and then append that value to the stack as the next 
        # value to do operations on. The last item in the stack is the answer
        # do it my way, where we just operate left to right on tokens, and then
        # store 2 variables, a left and a right, then go until the end. This way we don't need to
        # create any extra memeory for the stack
        # we move on from this, since there are cases where we can get 3+ numbers in a row
        
        # instead we can treat this like a stack problem
        # in this case, we iterate through the tokens and add it to our stack
        # if it is a number, add it.
        # if it is a operand, pop the last 2 numbers, add them, and then push that result onto the stack
        # this allows us to continue working as each operand only deals with the "last 2" numbers
        stack = []

        for token in tokens:
            if token in "+-*/":
                # pop the last 2 elements, and then manipulate them, then add result back to stack
                r = stack.pop()
                l = stack.pop()
                match token:
                    case "+":
                        stack.append(l + r)
                    case "-":
                        stack.append(l - r)
                    case "*":
                        stack.append(l * r)
                    case "/":
                        stack.append(int(l / r))
            else:
                stack.append(int(token))
        return stack[0]
        
        # stack = [5]
        # r = 2, l = 1
        
        