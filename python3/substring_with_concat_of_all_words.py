# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        if not words or len(words) == 0:
            return res
        word_count, word_len = len(words), len(words[0])
        freq_map = {}
        for word in words:
            if word not in freq_map:
                freq_map[word] = 0
            freq_map[word] += 1
        window = word_count*word_len
        for i in range(len(s)-window+1):
            start = i
            j = 0
            temp = {}
            while j < word_count:
                w = s[start:start+word_len]
                count = temp[w]+1 if w in temp else 1
                if w not in freq_map or count > freq_map[w]:
                    break
                temp[w] = count
                j += 1
                start += word_len
            if j == word_count:
                res.append(i)
        return res