class Solution:
    def decodeString(self, s: str) -> str:
        digit = {f"{d}": d for d in range(10)}

        st = [[1, ""]]

        current_mul = 0
        for _s in s:
            if _s == '[':
                st.append([current_mul, ""])
                current_mul = 0
            elif _s == ']':
                [top_mul, string] = st.pop(-1)
                st[-1][1] += (top_mul*string)
            elif _s in digit:
                current_mul = current_mul * 10 + digit[_s]
            else:
                st[-1][1] += _s
        return st[0][1]
