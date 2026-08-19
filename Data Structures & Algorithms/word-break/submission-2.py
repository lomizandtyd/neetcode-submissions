class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s)+1)
        dp[0] = True
        
        for i in range(len(s)):
            if not dp[i]:
                continue
    
            for w in wordDict:
                if (i+len(w)) <= len(s) and w == s[i:i+len(w)]:
                    dp[i+len(w)] = dp[i]

        return dp[len(s)]

