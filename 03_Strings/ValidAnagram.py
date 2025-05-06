# Leetcode : 242 Valid Anagram
# Given two string s and t, return if t is anagram of s, and false otherwise.

# Definition of the "Anagram" : If every single character that is currently present in t is also present in s then they are anagram of each other not more not less


# Optimized Approach (TC = O(n) and SC = O(1) constant space(26) )
def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    charCount = [0] * 26

    for i in range(len(s)):
        charCount[ord(s[i]) - ord("a")] += 1
        charCount[ord(t[i]) - ord("a")] -= 1

    for count in charCount:
        if count != 0:
            return False

    return True


if __name__ == "__main__":
    s = "cat"
    t = "tac"

    print(isAnagram(s, t))
