from difflib import SequenceMatcher

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

similarity = SequenceMatcher(None, s1, s2).ratio() * 100

print("Similarity Percentage:", similarity, "%")
if similarity>85:
    print("Strings are nearly equal.")
else:
    print("Not equal")
