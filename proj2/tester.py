import sys
import os

os.system("mkdir tests")
os.system("cd tests/ && rm *.out && cd ..")

for i in range(int(sys.argv[1])):
  filename = "tests/test" + str(i) + ".out"
  os.system("python3 ruagomesfreiregame2.py >" + filename)


n_not_20 = 0
for i in range(int(sys.argv[1])):
  filename = "tests/test" + str(i) + ".out"
  with open(filename, 'r') as filehandle:
    filecontent = filehandle.readlines()
    for line in filecontent:
      if int(line) != 20:
        print("ERROR: " + str(line))
        n_not_20 += 1

success = int(sys.argv[1]) - n_not_20
print("Number of test with grade 20: " + str(success) + " of " + sys.argv[1])
