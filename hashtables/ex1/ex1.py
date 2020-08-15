def get_indices_of_item_weights(weights, length, limit):
    box = {}
    result = None
    # enumerate the list, to make it easier
    for iterable, weight in enumerate(weights):
        box[iterable] = weight  # make the dictionary.
    for key, value in box.items():  # loop over all
        current = value  # set a current
        for index, weight in box.items():  # loop through the box
            if key != index:  # if the key is not the index.
                if length != 1:  # also if the length is not 1
                    if current + weight == limit:  # if the current weight and the next weight equals the limit
                        if key > index:  # check to see if the left or right is bigger and set accordingly
                            result = [key, index]
                        else:
                            result = [index, key]

    return result
