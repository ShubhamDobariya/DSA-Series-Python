# LeeCode: 49 Group Anagram

from collections import defaultdict


def groupAnagrams(strs):
    if len(strs) == 0:
        return []

    anagram_map = defaultdict(list)

    for s in strs:
        word = sorted(s)
        key = " ".join(word)
        anagram_map[key].append(s)

    return list(anagram_map.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = groupAnagrams(strs)
    print(result)
