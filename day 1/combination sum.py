def combination_sum(candidates, target):
    def backtrack(remaining, combination, start):
        if remaining == 0:
            result.append(list(combination))
            return
        elif remaining < 0:
          
            return
        
        for i in range(start, len(candidates)):
            combination.append(candidates[i])
     
            backtrack(remaining - candidates[i], combination, i)
            combination.pop()
    
    result = []
    candidates.sort()
    backtrack(target, [], 0)
    return result

candidates = [2, 3, 6, 7]
target = 7
print(f"Combinations of {candidates} that sum up to {target}: {combination_sum(candidates, target)}")
