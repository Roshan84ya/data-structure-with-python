#their solution
def detectCapitalUse(self, word):
    
    return word.isupper() or word.islower() or word.istitle()

#mysolution
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #if word is smaller or equal to 1 the it is always true
        if len(word)<=1:
            return True
        #condtition for checking all the string is capital word.isupper()
        if "A"<=word[0]<="Z" and "A"<=word[-1]<="Z":
            for i in word:
                if "A"<=i<="Z":
                    continue
                else:
                    return False
            return True
        #condition for only the first character is capital word.islower()
        elif "A"<=word[0]<="Z" and "a"<=word[-1]<="z":
            for i in word[1:]:
                if "a"<=i<="z":
                    continue
                else:
                    return False
            return True
        #condition for all the character is small word.istitle()
        elif "a"<=word[0]<="z" and "a"<=word[-1]<="z":
            
            for i in word:
                if "a"<=i<="z":
                    continue
                else:
                    return False
            return True
