def groupAnagrams(strs):
    map = {};

    for entry in strs:
        sortedEntry = ''.join(sorted(entry));
        if sortedEntry not in map:
            map[sortedEntry] = [];
            map[sortedEntry].append(entry);
        else:
            map[sortedEntry].append(entry);

    answers = [];
    for entry in map:
        answers.append(map[entry]);
    return answers;

strs = ["act", "pots", "tops", "cat", "stop", "hat"];
expected = [["hat"], ["act", "cat"], ["stop", "pots", "tops"]];
groupAnagrams(strs);