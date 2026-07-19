class StockSpanner:
    '''U: return the span(consecutive days less than or equal to today's price)
    for today's price
        I: price
        [[], [100], [80], [60], [70], [60], [75], [85]]

        stack = [100] return 1
        stack = [100, 80] return 1
        stack = [100, 80, 60] return 1
        stack = [100, 80, 60, 70]  return 2
        stack = [100, 80, 60, 70, 60] return 1
        stack = [100, 80, 60, 70, 60, 75] return 4
                      l                
    '''

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        self.stack.append(price)    # stack = [100, 80]
        l = len(self.stack) - 1     # l = 0
        span = 0                    # span = 1

        while l >= 0 and self.stack[l] <= price:
            span += 1
            l -= 1
        
        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)