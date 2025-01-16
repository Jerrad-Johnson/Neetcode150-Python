def topKFrequent(nums, k):
    count = {};
    answerSet = [[] for i in range(len(nums) + 1)]
    kAnswers = [];

    for n in nums:
        count[n] = 1 + count.get(n, 0);

    for item, freq in count.items():
        answerSet[freq].append(item);

    for i in range(len(answerSet) -1, 0, -1):
        for n in answerSet[i]:
            kAnswers.append(n);
            if len(kAnswers) == k:
                return kAnswers;


nums = [4,1,-1,2,-1,2,3];
print(topKFrequent(nums, 2));