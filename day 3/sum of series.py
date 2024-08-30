total_sum = 0

while True:

    num = int(input("Enter a positive integer (or 0 to quit): "))


    if num == 0:
        break
    if num > 100:
        print("Skipping number greater than 100...")
        continue
    total_sum += num
print("The sum of the numbers is:", total_sum)