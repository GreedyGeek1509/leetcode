class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        from_n_1 = self.countAndSay(n-1)
        res = ''
        digit = from_n_1[0]
        count = 1
        for i in range(1, len(from_n_1)):
            if from_n_1[i] == digit:
                count += 1
            else:
                res += str(count)
                res += digit
                count = 1
                digit = from_n_1[i]
        res += str(count)
        res += digit
        return res