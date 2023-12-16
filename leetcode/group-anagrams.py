class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        values = defaultdict(list)
        for val in strs:
            letters = [0]*26
            for char in val:
                letters[ord(char)-97] += 1
            values[tuple(letters)].append(val)
        ans = []
        for words in values.values():
            ans.append(words)
        return ans