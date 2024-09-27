def generate_combinations(arr,k):
    result =[]

    def backtrack(start,path,result):
        if len(path)== k:
            result.append(path[:])
            return 
        for i in range(start,len(arr)):
            path.append(arr[i])
            backtrack(i+1,path, result)
            path.pop()
    backtrack(0,[], result)
    return result 
print(generate_combinations([1,2,3,4],2))


