def interleave(*args):
    max_len = max(len(arg) for arg in args)
    
    for i in range(max_len):
        for arg in args:
            if i < len(arg):
                yield arg[i]


if __name__ == '__main__':
    result = list(interleave('abc', [1, 2, 3], ('!', '@', '#')))
    print(result)

