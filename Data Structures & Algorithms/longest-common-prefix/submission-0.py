class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        strs.sort()
        first = strs[0]
        last = strs[-1]

        prefix = ""
        for i in range (len(first)):
            if i < len(last) and first[i]==last[i]:
                prefix += first[i]

            else:
                break
        return prefix