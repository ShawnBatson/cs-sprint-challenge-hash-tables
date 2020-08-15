def has_negatives(a):
    result = [] # make a result
    box = {} # make the dictionary
    a.sort(reverse=True) # sort the given list, reverse it.

    for iterable, start in enumerate(a):  # enumerate the list to make it easier
        box[start] = iterable
    
    for key, value in box.items():
        if key > 0:
            current = (key - (key*2))
            if box.get(current):
                result.append(key)


    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
