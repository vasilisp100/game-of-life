import sys

size = int(sys.argv[1])
f = open("/home/msi/projects/CLionProjects/game-of-life/mpi/input/input.txt", "r")
buffer = ""
buffer += f.read()
f.close()
newBuffer = ""
c = 0
for i in buffer:
    c += 1
    if i == "0":
        newBuffer += "\u2B1C "
    else:
        newBuffer += "\u2B1B "

    if c % int(size) == 0:
        newBuffer += "\n"

f = open("/home/msi/projects/CLionProjects/game-of-life/mpi/input/input-boxes.txt", "w")
f.write(newBuffer)
f.close()
