"""Compare and update the inventory stored in a 2D array against a second 2D array of a fresh delivery. Update the current existing inventory item quantities (in arr1). If an item cannot be found, add the new item and quantity into the inventory array. 
The returned inventory array should be in alphabetical order by item."""

def update_inventory(arr1, arr2):
    map = {}
    for item in arr1:
        count, name = item
        if map[name] not in map:
            map[name] = count
        else:
            map[name] += count
    for item in arr2:
        count, name = item
        if name not in map:
            map[name]= count
        else:
            map[name] += count
    result = []
    for key, value in map.items():

        result.append([value, key])
    result.sort(key = lambda x:x[1])
    return result


print(
    update_inventory(
        [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]],
        [
            [2, "Hair Pin"],
            [3, "Half-Eaten Apple"],
            [67, "Bowling Ball"],
            [7, "Toothpaste"],
        ],
    )
)
