def sort(maan):
    for i in range(len(maan) - 1, 0, -1):
        for j in range(i):
            if maan[j] > maan[j + 1]:
                temp = maan[j]
                maan[j] = maan[j + 1]
                maan[j + 1] = temp


maan = [65, 89, 5, 78, 2, 15, 26]
sort(maan)
print(maan)
