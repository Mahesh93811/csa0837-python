def calculate(s: str) -> int:
    def helper(stack):
        num = 0
        sign = "+"
        
        while stack:
            char = stack.pop(0)
            
            if char.isdigit():
                num = num * 10 + int(char)
            if char == '(':
                num = helper(stack)
            if not char.isdigit() or not stack:
                if sign == '+':
                    result.append(num)
                elif sign == '-':
                    result.append(-num)
                elif sign == '*':
                    result[-1] = result[-1] * num
                elif sign == '/':
                    result[-1] = int(result[-1] / num)
                num = 0
                sign = char
            if char == ')':
                break
        
        return sum(result)
    
    stack = list(s.replace(" ", ""))
    result = []
    return helper(stack)


expression = "3 + 2 * 2 - (2 + 1) * 2"
print(calculate(expression)) 
