import matplotlib.pyplot as plt
import math


with open("COLVAR-driver", "r") as f:
    time, dist, coord = [], [], []
    f.readline()
    for line in f:
        data = [float(i) for i in line.split()]
        time.append(data[0])
        dist.append(data[1])
        coord.append(data[2])

plt.figure(1)
N, bins, _ = plt.hist(dist, bins=80, density=True)
plt.xlabel("Distance [nm]")
plt.ylabel("Count (normalized)")
plt.title("Distance histogram")
plt.savefig("histogram.png")

F = []
last_non_zero = N[0]
for i in range(len(N)):
    if N[i] != 0:
        F.append(-math.log(N[i]))
        last_non_zero = N[i]
    else:
        F.append(-math.log(last_non_zero))

plt.figure(2)
plt.plot(bins[1:], F)
plt.ylabel("Free Energy [kT]")
plt.xlabel("Distance [nm]")
plt.title("Free Energy graph")
plt.savefig("free_energy.png")

plt.figure(3)
plt.plot(time, dist)
plt.xlabel("Time [ps]")
plt.ylabel("Distance [nm]")
plt.title("Distance between Na and Cl atoms")
plt.savefig("distance-time.png")

plt.figure(4)
Ncoord, bins, _ = plt.hist(coord, bins=80, density=True)
plt.xlabel("Coordination number")
plt.ylabel("Count (normalized)")
plt.title("Coordination number histogram")
plt.savefig("histogram_coord.png")

Fcoord = []
last_non_zero = Ncoord[0]
for i in range(len(Ncoord)):
    if Ncoord[i] != 0:
        Fcoord.append(-math.log(Ncoord[i]))
        last_non_zero = Ncoord[i]
    else:
        Fcoord.append(-math.log(last_non_zero))

plt.figure(5)
plt.plot(bins[1:], Fcoord)
plt.ylabel("Free Energy [kT]")
plt.xlabel("Coordination number")
plt.title("Free Energy of the coordination number")
plt.savefig("free_energy_coord.png")

plt.figure(6)
plt.plot(time, coord)
plt.xlabel("Time [ps]")
plt.ylabel("Coordination number")
plt.title("Coordination number in time")
plt.savefig("coord-time.png")

#plt.tight_layout
#plt.show()
