def count_and_say(n: int) -> str:
    if n == 1:
        return "1"
    
    previous = count_and_say(n - 1)
    result = ""
    count = 1
    
    for i in range(1, len(previous)):
        if previous[i] == previous[i - 1]:
            count += 1
        else:
            result += str(count) + previous[i - 1]
            count = 1
    
    result += str(count) + previous[-1]
    
    return result
n = 5
print(f"The {n}th term in the Count and Say sequence is: {count_and_say(n)}")
