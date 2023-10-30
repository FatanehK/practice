''' You decide to test if your oddly-mathematical heating company is fulfilling its
 All-Time Max, Min, Mean and Mode Temperature Guarantee™.
 * Write a class TempTracker with these methods:
 * 
 * insert()—records a new temperature
 * get_max()—returns the highest temp we've seen so far
 * get_min()—returns the lowest temp we've seen so far
 * get_mean()—returns the mean of all temps we've seen so far
 * get_mode()—returns the mode of all temps we've seen so far
 * Optimize for space and time. Favor speeding up the getter functions (get_max(), get_min(), get_mean(), and get_mode()) 
 * over speeding up the insert() function.
 * 
 * get_mean() should return a float, but the rest of the getter functions can return integers. 
 * Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll 
 * all be in the range 0..110.
 * 
 * If there is more than one mode, return any of the modes.'''
class Temp:
    def __init__(self):
        self.min = float('inf')
        self.max = float('-inf')
        self.sum = 0
        self.mean = 0
        self.mode =0
        self.tempreature_record = []

    def insert(self,temp):
        self.tempreature_record.append(temp)
        self.sum += temp
        if temp < self.min :
            self.min = temp
        if temp> self.max:
            self.max = temp
    

    def get_min(self):
        return self.min 
    
    def get_max(self):
        return self.max

    def get_mean(self):
        if self.sum == 0 or len(self.tempreature_record) == 0:
            return None
        else:
            return self.sum /len(self.tempreature_record)

    def get_mode(self):
        self.map ={}
        for num in self.tempreature_record:
            self.map[num]= self.map.get(num,0)+1
        # self.mode = sorted(self.map, key=lambda x: x[1], reverse=True)
        self.mode = max(self.map, key=self.map.get)
        return self.mode



tracker= Temp()
tracker.insert(12)
tracker.insert(15)
tracker.insert(20)
tracker.insert(40)
tracker.insert(11)
tracker.insert(20)
tracker.insert(20)
tracker.insert(20)
print(tracker.get_max())
print(tracker.get_mean())
print(tracker.get_min())
print(tracker.get_mode())
