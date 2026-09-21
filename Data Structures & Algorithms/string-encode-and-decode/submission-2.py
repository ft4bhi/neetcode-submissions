class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res+=str(len(s))+"*"+s
        return res
    def decode(self,s):
        res = []
        i = 0
        while i<len(s):
            j=i
            while s[j] != "*":
                j+=1
            leng = int(s[i:j])
            j+=1
            word =s[j:j+leng]

            res.append(word)
            i = j+leng
        return res 