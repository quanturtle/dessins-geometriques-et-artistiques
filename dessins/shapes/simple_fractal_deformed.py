import math
import turtle
from typing import Callable

def default_deformation_subroutine(X0: int, 
                                   Y0: int,
                                   NP: int = 480) -> tuple[int, int]:
    XH = X0/NP*2 - 1
    YH = Y0/NP*2 - 1
    DH = math.sqrt(XH*XH + YH*YH)
    
    if XH != 0:
        AH = math.atan(YH/XH) - math.pi*(math.copysign(1, XH)-1)/2*math.copysign(1, YH)
    else:
        AH = math.pi/2*math.copysign(1, YH)
        
    DH = pow(DH, 2)
    AH = AH
    
    X1 = int((DH*math.cos(AH) + 1)*NP/2)
    Y1 = int((DH*math.sin(AH) + 1)*NP/2)

    return X1, Y1

    
def draw_simple_fractal_deformed(M: int = 3,
                                 N: int = 4,
                                 K: int = 4,
                                 X: list[int] = None,
                                 Y: list[int] = None,
                                 L: list[float] = None,
                                 A: list[float] = None,
                                 deformation_func: Callable = default_deformation_subroutine,
                                 NP: int = 480) -> list[tuple[int, int]]:
    pts = []

    if X is None:    
        X = [NP/2 * (1 + math.sin(2 * i * math.pi / 3)) for i in range(M+1)]
    if Y is None:
        Y = [NP/2 * (1 + math.cos(2 * i * math.pi / 3)) for i in range(M+1)]
    if L is None:
        L = [1/3] * N
    if A is None:
        A = [0, math.pi/3, -math.pi/3, 0][:N]
    
    for II in range(M):
        XD, YD = X[II], Y[II]
        XA, YA = X[II + 1], Y[II + 1]
        X0, Y0 = XD, YD
        
        X1, Y1 = deformation_func(X0, Y0, NP)
        
        turtle.penup()
        turtle.goto(X1, Y1)
        turtle.pendown()
        pts.append((X1, Y1))
        
        if XA != XD:
            A0 = math.atan((YA - YD)/(XA - XD))
        
        else:
            A0 = math.pi/2 * math.copysign(1, YA - YD)
        
        if (XA - XD) < 0:
            A0 += math.pi
            
        L0 = math.sqrt((XA - XD)**2 + (YA - YD)**2)
        
        for I in range(N**K):
            LL, AA = L0, A0
            T1 = I
            
            for J in range(K-1, -1, -1):
                R = N**J
                T2 = T1 // R
        
                if T2 < N:
                    AA += A[T2]
                    LL *= L[T2]
        
                T1 -= T2 * R
                
            X0 = X0 + LL * math.cos(AA)
            Y0 = Y0 + LL * math.sin(AA)
        
            X1, Y1 = deformation_func(X0, Y0, NP)
        
            turtle.goto(X1, Y1)
            pts.append((X1, Y1))
            
    return pts