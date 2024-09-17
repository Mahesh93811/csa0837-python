def is_subsequence(list1, list2):
    idx = 0
    for elem in list1:
        while idx < len(list2) and list2[idx] != elem:
            idx += 1
        if idx == len(list2):
            return False
        idx += 1
    return True


list1 = [1, 3, 5]
list2 = [1, 2, 3, 4, 5, 6]

result = is_subsequence(list1, list2)
print(result)  