words = input().split()
result = []
for word in words:
    if word[-1] == 's':
        result.append(word)
print("_".join(result))
