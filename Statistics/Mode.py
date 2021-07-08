import statistics
def mode(x):
    '''
    count = {}
    mode = []
    highest = 0
    
    for num in x:
        count[num] += 1
        if num in count.keys():
            count[num] += 1
            if count.get(num) > highest:
                highest_repeat = count.get(num)
        else:
            count[num] = 1

        if highest > 1:
            for num in count.keys():
                if count.get(num) == highest:
                    mode.append(num)
        else:
            return None

        result = mode
        return result
        '''
    return statistics.mode(x)