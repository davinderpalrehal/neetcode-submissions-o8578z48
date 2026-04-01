class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        j = 0
        n = ''

        for c in abbr:
            if c.isnumeric():
                if n == '' and c == '0':
                    return False
                n += c
            else:
                if n != '':
                    j += int(n)
                    n = ''
                if j >= len(word) or word[j] != c:
                    return False
                j += 1
        
        if n != '':
            j += int(n)
            
        return j == len(word)