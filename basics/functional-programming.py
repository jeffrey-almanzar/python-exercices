


def get_even_squared(arr):
    even_nums = filter(lambda num: num % 2 == 0, arr)
    return map(lambda num: num * num, even_nums)

nums = [1, 2, 3, 4, 5 ]

print(list(get_even_squared(nums)))


words = ['hello', 'test', 'how']

def sample_func(arr):
    return map(lambda word: word.upper(), arr)

print(list(sample_func(words)))
