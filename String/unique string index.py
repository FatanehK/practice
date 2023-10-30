def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        map={}

        map = {}
        for i, char in enumerate(s):
            if not char in map:
                map[char] = 1
            else:
                map[char] += 1
        for i, char in enumerate(s):
            if map[char] == 1:
                return i
        return -1
        # for i,char in enumerate(s):
        #     if not char in map:
        #         map[char] = [i,1]
        #     else:
        #         map[char][1]+=1
        # for value in map.values():
        #     if value[1] == 1:
        #         return value[0]
        # return -1


print(firstUniqChar("loveleetcode"))
