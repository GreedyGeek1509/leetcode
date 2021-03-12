class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return s
        word, res = '', ''
        length = len(s)
        i = 0
        while i < length:
            if s[i] ==' ':
                if word:
                    res = word + ' ' + res if res else word
                    word = ''
            else:
                word += s[i]
            i += 1
        if word:
            res = word + ' ' + res if res else word
        return res