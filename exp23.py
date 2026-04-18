file1 = open("temps.txt", "r")
file2 = open("ftemps.txt", "w")

for line in file1:
    c = float(line.strip())        
    f = (c * 9/5) + 32             
    file2.write(str(f) + "\n")     

file1.close()
file2.close()
