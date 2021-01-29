from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        length = len(s)
        res = list()

        def back_track(cursor: int, position: int, so_far: str):
            if position == 4:
                if cursor >= length:
                    res.append(so_far)
                return
            if (length-cursor) > (4-position)*3 or (length-cursor) < (4-position):
                return
            tail = '.' if position < 3 else ''
            s1 = so_far + s[cursor] + tail
            back_track(cursor+1, position+1, s1)
            if s[cursor] != '0':
                if cursor+1 < length:
                    s2 = so_far + s[cursor:cursor+2] + tail
                    back_track(cursor+2, position+1, s2)

                if cursor+2 < length and int(s[cursor:cursor+3]) < 256:
                    s3 = so_far + s[cursor:cursor+3] + tail
                    back_track(cursor+3, position+1, s3)

        back_track(0, 0, '')
        return res


if __name__ == '__main__':
    print(Solution().restoreIpAddresses("25525511135"))