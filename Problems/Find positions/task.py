numbers = input().split()
chosen_one = input()
result = []
counter = 0
for x in numbers:
    if x == chosen_one:
        result.append(str(counter))
    counter += 1
if len(result) == 0:
    print("not found")
else:
    print(" ".join(result))
