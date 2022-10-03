def sort(s):
    for i in range(len(s) - 1, 0, -1):
        for j in range(i):
            if s[j]>s[j+1]:
                temp = s[j]
                s[j] = s[j + 1]
                s[j + 1] = temp


s = [2, 8, 4, 1, 5, 9, 6, 78]
sort(s)
print(s)
