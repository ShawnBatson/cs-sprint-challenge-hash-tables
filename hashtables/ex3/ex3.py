def intersection(arrays):
    # box = {}
    # result = []
    # for iterable, arrays in enumerate(arrays):
    #     box[iterable] = arrays
    # for key, value in box.items():
    #     pass

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
