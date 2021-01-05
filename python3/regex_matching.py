class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not s or len(s) == 0:
            return p == '.' or p == '.*'
        if not p or len(p) == 0:
            return False

        slen = len(s)
        plen = len(p)

        def recursive_match(sc: int, pc: int) -> bool:
            if sc >= slen:
                return pc >= plen or (pc == plen-2 and p[pc+1] == '*')
            if pc >= plen:
                return False
            first_match = p[pc] in [s[sc], '.']
            if pc+1 < plen and p[pc+1] == '*':
                return (first_match and recursive_match(sc+1, pc)) or recursive_match(sc, pc+2)
            return first_match and recursive_match(sc+1, pc+1)

        return recursive_match(0, 0)