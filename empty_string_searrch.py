"""Given a sorted array of strings that is interspersed with empty strings, 
write a method to find the location of a given string."""

def search(arry,target):
    low =0
    high = len(arry)-1
    while low<= high:
        # ensure we don't include any empty string 
        while low <= high and arry[high] == "":
            high -=1
        while low <= high and arry[low] == "":
            low +=1
        mid = low +(high-low)//2
        while arry[mid] == "":
            mid +=1

        if arry[mid] == target:
            return mid 
        elif arry[mid] < target:
            low = mid+1
        else:
            high = mid -1
    return -1


arry = ["apple", "", "banana", "", "cherry", "date", "grape"]
target = "cherry"
print(search(arry,target))