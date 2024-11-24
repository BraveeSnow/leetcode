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
22ms
Beats26.58%

Memory
19.18MB
Beats8.39%
"""


class Solution:
    VOWELS = ["a", "e", "i", "o", "u"]

    def reverseVowels(self, s: str) -> str:
        s = list(s)
        indices = [i for i in range(len(s)) if s[i].lower() in Solution.VOWELS]

        if len(indices) % 2 == 1:
            indices.pop(len(indices) // 2)

        if len(indices) == 0:
            return "".join(s)

        for i, j in zip(
            indices[: len(indices) // 2],
            indices[len(indices) - 1 : len(indices) // 2 - 1 : -1],
        ):
            print(i, j)
            s[i], s[j] = s[j], s[i]

        return "".join(s)


sol = Solution()
print(sol.reverseVowels("IceCreAm"))
print(sol.reverseVowels("leetcode"))
