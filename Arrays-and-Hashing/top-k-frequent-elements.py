def topKFrequent(nums, k):
    map = {};
    for entry in nums:
       if entry not in map:
           map[entry] = 1;
       else:
           map[entry] += 1;

    answers = [];

    for entry in map:
        answers.append([entry, map[entry]]);
        if len(answers) == k:
            break;

    for entry in answers:
        del(map[entry[0]]);

    for entry in map:
        currentAnswer = answers[-1];
        currentMap = map[entry]
        if currentAnswer[1] < currentMap:
            answers.append([entry, map[entry]]);
            answers.pop(0);

    formatted = [];


    for entry in answers:
        formatted.append(entry[0]);

    return formatted;

nums = [1, 2, 2, 3, 3, 3];
topKFrequent(nums, 2);