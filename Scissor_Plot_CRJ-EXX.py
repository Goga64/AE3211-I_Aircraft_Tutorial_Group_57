# CRJ-EXX

import numpy as np
from matplotlib import pyplot as plt


# Coefficients

# Stability at cruise
grad_s = 0.425208
int_s = -0.098444

# Neutral at cruise
grad_n = 0.425208
int_n = -0.119705

# Control at landing
grad_c = -0.48682
int_c = 0.226599

# CG Locations

x_cg_fore = 18.95/100
x_cg_aft = 72.30/100


ShS_CRJEXX = 21.5/77.4



# ShS_fore on the control curve
ShS_fore = grad_c * x_cg_fore + int_c

# ShS_aft on the stability curve

ShS_aft = grad_s * x_cg_aft + int_s


# Line from Control curve to y axis for min Sh/S
dt = 0.01
cg_line = np.arange(0, x_cg_aft+dt, dt)
ShS_line = np.ones_like(cg_line) * ShS_aft

# Dotted Lines for aft cg and fore cg

ShS_fore_dotted = np.arange(0, ShS_fore + dt, dt)

cg_fore_dotted = np.ones_like(ShS_fore_dotted) * x_cg_fore

plt.plot(cg_fore_dotted, ShS_fore_dotted,
         color = "gray",
         linestyle = "--",
         linewidth = "2") 

ShS_aft_dotted = np.arange(0, ShS_aft + dt, dt)

cg_aft_dotted = np.ones_like(ShS_aft_dotted) * x_cg_aft

plt.plot(cg_aft_dotted, ShS_aft_dotted,
         color = "gray",
         linestyle = "--",
         linewidth = "2") 







# straight line for the ShS stuff

cg_line = np.arange(0, x_cg_aft+dt, dt)


def curve(g, i, dt=0.01):   # smaller dt for smoother lines
    cg = np.arange(0, 1 + dt, dt)
    ShS = g * cg + i
    return cg, ShS


cg, ShS_stability = curve(grad_s, int_s)
cg, ShS_neutral = curve(grad_n, int_n)
cg, ShS_control = curve(grad_c, int_c)




plt.plot(
    cg, ShS_stability,
    color="#4C72B0",   # muted blue
    linewidth=2,
    label="Stability curve at cruise speed"
)

plt.plot(
    cg, ShS_control,
    color="#55A868",   # muted green
    linewidth=2,
    label="Control curve at landing speed"
)

plt.plot(
    cg, ShS_neutral,
    color="#C44E52",   # muted red
    linestyle="--",    # dashed (more visible than :)
    linewidth=2,
    label="Neutral point stability at cruise speed"
)

plt.plot(x_cg_aft, ShS_aft, marker="o", markersize = 7, markeredgecolor="black", markerfacecolor= "red")
plt.plot(x_cg_fore, ShS_fore, marker="o", markersize = 7, markeredgecolor="black", markerfacecolor="red")
plt.plot(cg_line, ShS_line, color = "black", label = "Minimum Sh/S")


ShS_CRJEXX_line = np.ones_like(cg) * ShS_CRJEXX

print(cg)

plt.plot(cg, ShS_CRJEXX_line, linestyle = "--", linewidth = 2, color = "purple", label = "Sh/S of CRJ-EXX")



# Set axis limits
plt.xlim(0, 1)
plt.ylim(0, 0.45)

plt.xlabel("c.g. position")
plt.ylabel(r"$S_h / S$")
plt.grid(True, alpha=0.3)
plt.title("CRJ-EXX Scissor Plot")
plt.legend()
plt.show()
