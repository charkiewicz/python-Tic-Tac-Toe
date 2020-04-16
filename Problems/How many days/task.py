seconds = [86400, 3600, 1028397, 8372891, 219983, 865779330, 3276993204380912]
# create a list of days here
days = [int((x / 3600) // 24) for x in seconds]
print(days)
