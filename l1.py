pos = -1


def search(maan, n):
    i = 0
    while i < len(maan):
        if maan[i] == n:
            globals()['pos'] = i
            return True
        i = i + 1
    return False


maan = [1, 5, 6, 8, 99, 77, 22, 55, 33, 44, 78]
n = 33
if search(maan, n):
    print("searching element found", pos)
else:
    print("searching element not found")
