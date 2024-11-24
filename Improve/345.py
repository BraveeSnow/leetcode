"""
345. Reverse Vowels of a String
Easy
Topics
Companies

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "IceCreAm"

Output: "AceCreIm"

Explanation:

The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

Example 2:

Input: s = "leetcode"

Output: "leotcede"

 

Constraints:

    1 <= s.length <= 3 * 105
    s consist of printable ASCII characters.

Runtime
15ms
Beats48.98%

Memory
17.65MB
Beats41.86%
"""


class Solution:
    VOWELS = ["a", "e", "i", "o", "u"]

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1

        while left <= right:
            while s[left].lower() not in Solution.VOWELS and left <= right:
                left += 1

            while s[right].lower() not in Solution.VOWELS and left <= right:
                right -= 1

            if left <= right:
                s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)


sol = Solution()
print(sol.reverseVowels("IceCreAm"))
print(sol.reverseVowels("leetcode"))
