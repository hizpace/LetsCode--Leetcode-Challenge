class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        lst  = []
        for word in s:
            word = "".join(reversed(word))
            lst.append(word)

        return " ".join(lst)            
            
