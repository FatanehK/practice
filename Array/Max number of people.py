"find max number of people in one builiding of multistory_building"


def max_count_people_in_building(building):
    count = 0
    max_count = 0
    for element in building:
        if element == "o":
            count += 1
        elif element == ".":
            continue
        else:
            count = 0
        max_count = max(max_count, count)
    return max_count


def count_all_people(multistory_building):
    max_building = 0
    for building in multistory_building:
        one_building_count = max_count_people_in_building(building)
        max_building = max(one_building_count, max_building)
    return max_building


building = ["o", "o", ".", "o", "W", "o", ".", "W", "o", "o"]

multistory_building = [
    ["o", "o", ".", "W", "o", ".", "W", "o", "o"],
    ["o", "W", ".", "W", "o", "o", ".", "o", "o"],
    ["o", "W", ".", ".", ".", "W", ".", ".", "o"],
    ["o", "o", ".", "W", "o", ".", "W", "o", "."],
]
print(count_all_people(multistory_building))

floorplan = [
    ["o", "o", ".", "W", "o"],
    ["o", "W", ".", "W", "o"],
    ["o", "W", "W", ".", "."],
    ["o", "o", ".", "W", "o"],
]
