class Solution(object):
    def getModifiedArray(self, length, updates):
        if length <= 0:
            return None
        
        diff = [0 for _ in range(length)]
        for update in updates:
            diff[update[0]] += update[2]
            if update[1]+1 < length:
                diff[update[1]+1] -= update[2]
        
        output = [0 for _ in range(length)]
        output[0] = diff[0]
        for i in range(1, length):
            output[i] = output[i-1] + diff[i]
    
        return output

