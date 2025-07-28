class Solution:
    def join_with_padding(self, words: List[str], padding: int) -> str:
        n = len(words) - 1
        if n < 1:
            return words[0] + " "*padding

        extras = padding%n
        ans = words[0]
        pads = " "*(padding//n)
        for word in words[1:]:
            if extras:
                ans += " "
                extras -= 1
            ans += pads + word
        
        return ans

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        current_words = []
        current_len = 0
        ans = []
        
        for word in words:
            word_len = len(word)
            if current_len + word_len + len(current_words) <= maxWidth:
                current_words.append(word)
                current_len += word_len
            else:
                ans.append(self.join_with_padding(current_words, maxWidth - current_len))
                current_words = [word]
                current_len = word_len

        ans.append(" ".join(current_words) + " "*(maxWidth - (current_len + len(current_words) - 1)))
        return ans
