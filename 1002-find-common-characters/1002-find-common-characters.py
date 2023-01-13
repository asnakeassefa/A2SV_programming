class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        string = defaultdict(int)
        ans = []
        for char in words[0]:
            string[char] += 1
        
        for word in words:
            for key,value in string.items():
                string[key] = min(string[key],word.count(key))
        
        for key,value in string.items():
            for _ in range(value):
                ans.append(key)
        return ans