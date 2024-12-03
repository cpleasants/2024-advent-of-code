# utility
def drop_index(li:list, i:int):
    return li[:i] + li[i+1:]

class Day2:
    def __init__(self, fname):
        with open(fname) as f:
            self.data = [[int(item) for item in line.split(' ')] for line in f]
    
    def is_safe(self, li:list):
        increasing_counter = 0
        decreasing_counter = 0
        for i in range(1, len(li)):
            if 0 < li[i] - li[i-1] <= 3 and decreasing_counter == 0:
                increasing_counter += 1
                continue
            elif -3 <= li[i] - li[i-1] < 0 and increasing_counter == 0:
                decreasing_counter += 1
                continue
            else:
                return False
        return True
    
    def count_safe(self):
        counter = 0
        for sub_li in self.data:
            if self.is_safe(sub_li):
                counter += 1
        return counter
    
    def is_really_safe(self, li:list):
        increasing_counter = 0
        decreasing_counter = 0
        for i in range(1, len(li)):
            if 0 < li[i] - li[i-1] <= 3 and decreasing_counter == 0:
                increasing_counter += 1
                continue
            elif -3 <= li[i] - li[i-1] < 0 and increasing_counter == 0:
                decreasing_counter += 1
                continue
            else:
                # Check if removing this item would make the unsafe report safe
                if self.is_safe(drop_index(li, i)):
                    return True
                # Cases where the first needs to be removed to make the report
                # safe are not covered in the logic above, so test that as well
                elif self.is_safe(drop_index(li, 0)):
                    return True
                else:
                    return False
        return True
    
    def count_really_safe(self):
        counter = 0
        for sub_li in self.data:
            if self.is_really_safe(sub_li):
                counter += 1
        return counter