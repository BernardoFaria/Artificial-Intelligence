import sys
import os

os.system("mkdir tests")
os.system("cd tests/ && rm *.out && cd ..")

for i in range(int(sys.argv[1])):
  filename = "tests/test" + str(i) + ".out"
  os.system("python3 ruagomesfreiregame2.py >" + filename)


n_not_20 = 0
acc = 0
for i in range(int(sys.argv[1])):
  filename = "tests/test" + str(i) + ".out"
  with open(filename, 'r') as filehandle:
    filecontent = filehandle.readlines()

    for line in filecontent:
      acc += int(line)

grade = acc/int(sys.argv[1])

print("Average Grade: " + str(grade))
