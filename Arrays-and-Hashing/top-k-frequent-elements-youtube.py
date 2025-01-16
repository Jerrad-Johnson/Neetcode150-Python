def topKFrequent(nums, k):
    lengthOfArray = len(nums);
    answerSet = [];
    currPos = {};
    temp = None;

    for _ in range(lengthOfArray):
        answerSet.append([]);

    for num in nums:
        if num not in currPos:
            currPos[num] = 1;
        else:
            currPos[num] += 1;

    for num in currPos:
        answerSet[currPos[num]].append(num);

    while answerSet and not answerSet[-1]:
        answerSet.pop();

    flattened = [item for sublist in answerSet for item in sublist];
    return(flattened[-k:]);

nums = [4,1,-1,2,-1,2,3];
print(topKFrequent(nums, 2));