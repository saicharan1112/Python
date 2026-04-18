file = open("emails.py", "r")

emails = []

for line in file:
    emails.append(line.strip())

file.close()

result = ";".join(emails)

print(result)
