class Solution:
    def freq(self,arr):
        word = defaultdict(int)
        for char in arr:
            word[char] += 1
        final = min(word,key = lambda x: x[0])
        return word[final]
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        mWords = [self.freq(word) for word in words]
        mQueries = [self.freq(query) for query in queries]
        mWords.sort()
        ans = []
        for query in mQueries:
            low = 0
            high = len(mWords)-1
            while low <= high:
                mid = low + (high - low) // 2
                if mWords[mid] <= query:
                    low = mid + 1
                elif mWords[mid] > query:
                    high = mid - 1
            ans.append(len(mWords[low:]))
        return ans