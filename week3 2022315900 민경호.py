def isHappy(n):
    def cal(number):
        sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            sum += digit ** 2
        return sum
    
    slow = n
    fast = cal(n)
    while fast != 1 and slow != fast:
        slow = cal(slow)
        fast = cal(cal(fast))
    
    return fast == 1
