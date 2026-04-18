class Reverse:
    def reverse_words(self, s):
        words = s.split()
        words.reverse()
        return " ".join(words)

r = Reverse()

s = input("Enter a sentence: ")
print("Reversed:", r.reverse_words(s))
