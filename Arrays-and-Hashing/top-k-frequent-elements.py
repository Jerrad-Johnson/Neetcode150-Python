def topKFrequent(nums, k):
    map = {};
    for entry in nums:
       if entry not in map:
           map[entry] = 1;
       else:
           map[entry] += 1;

    correlatedMap = [];
    for entry in map:
        correlatedMap.append([entry, map[entry]]);

    topK = sorted(correlatedMap, key=lambda x: x[1]);
    answerSet = topK[-k:];
    return([entry[0] for entry in answerSet]);

nums = [4,1,-1,2,-1,2,3];
print(topKFrequent(nums, 2));