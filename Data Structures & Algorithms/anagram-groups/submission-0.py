class Solution:
    def groupAnagrams(self, strs: List[str]):
        d = {}
        
        for word in strs:
            k = ''.join(sorted(word))
            if k not in d:
                d[k] = []
            d[k].append(word)
        return (list(d.values()))
        