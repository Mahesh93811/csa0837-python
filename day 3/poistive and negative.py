positive_count = 0
negative_count = 0


while True:
    
    num = int(input("Enter an integer (or 0 to quit): "))


    if num == 0:
        break

   
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1


print("Number of positive values entered:", positive_count)
print("Number of negative values entered:", negative_count)