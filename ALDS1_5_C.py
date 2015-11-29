import math


def koch(n, p1x, p1y, p2x, p2y):
    if n == 0:
        return

    sx = (2*p1x + 1*p2x)/3
    sy = (2*p1y + 1*p2y)/3
    tx = (1*p1x + 2*p2x)/3
    ty = (1*p1y + 2*p2y)/3
    theta = math.pi/3
    ux = math.cos(theta)*(tx-sx) - math.sin(theta)*(ty-sy) + sx
    uy = math.sin(theta)*(tx-sx) + math.cos(theta)*(ty-sy) + sy

    koch(n-1, p1x, p1y, sx, sy)
    print("{:.5f} {:.5f}".format(sx, sy))
    koch(n-1, sx, sy, ux, uy)
    print("{:.5f} {:.5f}".format(ux, uy))
    koch(n-1, ux, uy, tx, ty)
    print("{:.5f} {:.5f}".format(tx, ty))
    koch(n-1, tx, ty, p2x, p2y)

n = int(input())

p1x, p1y = 0.0, 0.0
p2x, p2y = 100.0, 0.0

print("{:.5f} {:.5f}".format(p1x, p1y))
koch(n, p1x, p1y, p2x, p2y)
print("{:.5f} {:.5f}".format(p2x, p2y))
