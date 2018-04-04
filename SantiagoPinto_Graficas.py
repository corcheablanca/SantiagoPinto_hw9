import numpy as np
import matplotlib.pyplot as plt
py = np.genfromtxt("times_python.csv")
cpp = np.genfromtxt("times_cpp.csv")

plt.plot(py[:,0],py[:,1])

plt.plot(cpp[:,0],cpp[:,1])


plt.savefig("cpp_vs_python.png")
