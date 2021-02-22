from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def is_palindrome(string: str) -> bool:
            beg, end = 0, len(string) - 1
            while beg < end:
                if string[beg] != string[end]:
                    return False
                beg += 1
                end -= 1
            return True

        ans = []

        def partition_helper(remnant: str, parts: List[str]):
            if not remnant:
                ans.append(list(parts))
                return
            for i in range(1, len(remnant)+1):
                if is_palindrome(remnant[0:i]):
                    parts.append(remnant[0:i])
                    partition_helper(remnant[i:], parts)
                    parts.pop()

        partition_helper(s, [])
        return ans