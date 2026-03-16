class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s = s.split()
        lst = []
        while True:
            for i in range(len(s)):
                if k==len(lst):
                    return " ".join(lst)
                else:
                    lst.append(s[i])
