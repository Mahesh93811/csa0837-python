def intersection(arr1, arr2):
    result = []
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                found = False
                
                for k in range(len(result)):
                    if result[k] == arr1[i]:
                        found == True
                        break
                if not found:
                    result.append(arr1[i])
    return result


arr1 = [1, 2, 3, 4, 8]
arr2 = [2, 3, 4]

result = intersection(arr1, arr2)
print(result)