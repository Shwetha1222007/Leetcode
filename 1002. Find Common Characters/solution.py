from collections import Counter

class Solution(object):
    def commonChars(self, words):

        common = Counter(words[0])

        for word in words[1:]:
            current = Counter(word)
            common &= current
        return list(common.elements())
        
        