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


# text = 'L0NDON'
# print(correct(text))

def solution(text, ending):
    substr = ''
    for i in range(len(text)-len(ending), len(text)):
        substr += text[i]
    for i in range(len(substr)):
        if (substr[i] != ending[i]):
            return False
    return True
    # a lot easier: return text.endswith(ending)


# text = 'abc'
# ending = 'bc'
# print(solution(text, ending))

def digitize(n):
    stack = []
    while (n != 0):
        r = n % 10
        stack.append(r)
        n = n // 10
    return stack


# n = 13245
# print(digitize(n))

def find_short(s):
    list = s.split()
    shortest = len(list[0])
    for s in list:
        if (len(s) < shortest):
            shortest = len(s)
    return shortest


# s = "hello my friend"
# print(find_short(s))

def powers_of_two(n):
    result = []
    for i in range(n+1):
        result.append(2**i)
    return result


# print(powers_of_two(3))

def str_count(string, letter):
    count = 0
    for char in string:
        if (char == letter):
            count += 1
    return count


# print(str_count('', 'l'))


def count_sheep(n):
    return ''.join(f"{x} sheep..." for x in range(1, n+1))


print(count_sheep(3))
