#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    box = {}
    for x in tickets:
        box[x.source] = x.destination
    # make a starting point, it must be "NONE"
    start = box["NONE"]  # set the start
    route = [start] # set the result
    count = 0 # set the count
    current = start # set the current
    
    for _ in box:  # open the box
        for source, destination in box.items():  # for the source and destination
            if count > 0: # if the count is 0 (tier 1)
                if current == source and destination != "NONE":  # if current is the source and destintaion is not None
                    route.append(destination)  # append the destination
                    current = box[source] # change the current to the new source
            count += 1 # add 1 (tier 1) 
    route.append("NONE")

    return route
