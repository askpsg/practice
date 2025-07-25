class Solution:
    def normalise(self, s):
        s_compact_str = s[0]
        s_compact_freq = [1]
        for _s in s[1:]:
            if _s == s_compact_str[-1]:
                s_compact_freq[-1] += 1
            else:
                s_compact_str += _s
                s_compact_freq.append(1)
        
        return s_compact_str, s_compact_freq

    def expressiveWords(self, s: str, words: List[str]) -> int:
        s_compact_str, s_compact_freq = self.normalise(s)
        s_len = len(s_compact_freq)

        count = 0
        for w in words:
            w_compact_str, w_compact_freq = self.normalise(w)
            if s_compact_str != w_compact_str:
                continue
            
            flag = True
            for i in range(s_len):
                if s_compact_freq[i] != w_compact_freq[i] and (s_compact_freq[i] < 3 or s_compact_freq[i] < w_compact_freq[i]):
                    flag = False
                    break
            
            if flag:
                count += 1
        
        return count
