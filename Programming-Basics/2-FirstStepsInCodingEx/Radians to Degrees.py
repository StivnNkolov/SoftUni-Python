# чете ъгъл в радиани (rad) и го преобразува в градуси (deg).
# градуси = радиани * 180 / π.

from math import pi
from math import floor

rad = float(input())
deg = rad * 180 / pi
print(floor(deg))