class Solution(object):
    def uniqueMorseRepresentations(self, words):
        morse = [
            ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."

        ]

        transformations = set()

        for word in words:
            code = ""
            for letter in word:

                index = ord(letter) - ord('a')
                code += morse[index]

            transformations.add(code)

        return len(transformations)



        