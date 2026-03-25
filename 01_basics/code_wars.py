# arr = [4, 6, 2, 1, 9, 63, -134, 566]
# arr.sort()
# print(arr[0])
# print(arr[len(arr)-1])

# arr = [1, 2, 3]
# res = map(lambda n: n*2, arr)
# print(list(res))

def first_non_consecutive(arr):
    for i in range(len(arr)):
        if (arr[i]+1 != arr[i+1]):
            return arr[i+1]
    return None


def count_sheeps(sheep):
    count = 0
    for s in sheep:
        if s:
            count += 1
    return count

# arr = [1, 2, 3, 4, 6, 7, 8]
# print(first_non_consecutive(arr))


sheep = [True,  True,  True,  False,
         True,  True,  True,  True,
         True,  False, True,  False,
         True,  False, False, True,
         True,  True,  True,  True,
         False, False, True,  True]

# print(count_sheeps(sheep))


def correct(s):
    result = ''
    for char in s:
        if char == '5':
            result += 'S'
        elif char == '0':
            result += 'O'
        elif char == '1':
            result += 'I'
        else:
            result += char
    return result


text = 'L0NDON'
print(correct(text))
