class Solution:
    def simplifyPath(self, path: str) -> str:
        s_path = ['']*len(path)
        s_cursor, p_cursor = 0, 0
        first = True
        while s_cursor < len(path):
            if path[s_cursor] == '/':
                while s_cursor < len(path) and path[s_cursor] == '/':
                    s_cursor = s_cursor+1
                if first:
                    first = False
                else:
                    p_cursor = p_cursor+1
            elif path[s_cursor] == '.':
                if s_cursor < len(path)-1 and path[s_cursor+1] == '.':
                    p_cursor = p_cursor - 2 if p_cursor > 1 else p_cursor
                    s_path[p_cursor] = ''
                    s_cursor = s_cursor+2
                else:
                    p_cursor = p_cursor - 1 if p_cursor > 0 else p_cursor
                    s_cursor = s_cursor+1
            else:
                s_path[p_cursor] = s_path[p_cursor] + path[s_cursor]
                s_cursor = s_cursor+1
        ans = ''
        for i in range(p_cursor+1):
            if s_path[i] != '':
                ans = ans+'/'
                ans = ans+s_path[i]
        return ans if len(ans) > 0 else '/'
