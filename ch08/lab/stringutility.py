class StringUtility:
    def __init__(self, string):
        self.string = string
        print(self.string)
    def __str__(self):
        """
        takes self as the argument, 
        and returns the string unchanged. 
        """
        return self.string
    def vowels (self):
        """
        takes self.string as an argument,
        and returns the amount of vowels in the word
        """
        self.string.lower()
        print(self.string) #why is this saying that the whole string is just interesting?
        self.vowelCounter = 0
        for i in self.string:
            if i == "a" or i == "e" or i == "i" or i == "o" or i =="u":
                self.vowelCounter += 1
        print(self.vowelCounter)
        if self.vowelCounter > 4:
            return ("many")
        else:
            return str(self.vowelCounter)
    def bothEnds(self):
        """
        takes self.string as an argument,
        returns the first two and last two letters unless the word is less than 2 
        """
        self.size = len(self.string)
        if self.size > 2:
           newWord = (self.string[0] + self.string[1] + self.string[-2] + self.string[-1])
           return newWord
        else:
            return ""
    def fixStart(self):
        """
        takes self.string as an agrument, 
        returns self.string edited so that whenever the first letter appears again in the word,
        it appears as an *
        """
        self.fixed = self.string
        if self.size > 1:
            self.fixed = self.string[0] + self.fixed[1:].replace(self.string[0],"*")  
        # self.fixed = self.firstLetter + self.change
        return self.fixed
    def asciiSum(self):
        """
        takes self.string as an argument, 
        returns the ascii sum of each word. 
        """
        self.asciiCounter = 0
        for i in self.string:
            self.asciiCounter += ord(i)
        return self.asciiCounter
    def cipher(self):
        """
        take self.string as an arguement
        returns self.result which is the encyrpted string
          based on the number of letters of the word
        """
        self.result = ""
        for i in self.string:
            if i.isalpha():
                start = ord("A") if i.isupper() else ord("a")
                new_pos = (ord(i) - start + self.size) % 26
                i = chr(start + new_pos)
                self.result += i
            else:
                self.result += i
        return self.result