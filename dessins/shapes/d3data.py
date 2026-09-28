import math
import turtle


def draw_d3data(DC: int = 2, 
                TC: int = 2,
                O: list[float] = [5, -2, 1.3], 
                A: list[float] = [3*math.pi/4, 0, 0], 
                Q: list[float] = [0, 1, 0],
                NP: int = 480):
    OX, OY, OZ = O
    AZ, AY, AX = A
    QX, QY, QZ = Q
    
    C1, S1 = math.cos(AZ), -math.sin(AZ)
    C2, S2 = math.cos(AY), -math.sin(AY)
    C3, S3 = math.cos(AX), -math.sin(AX)
    
    DATA = [
        0,0,0, 0,0,2, 1,0,3, 1,0,4, 2,0,4,
        2,0,3, 3,0,2, 3,0,0, 3,1,0, 3,1,2,
        2,1,3, 2,1,4, 2,0,4, 1.5,.5,5.5, 1,0,4, 1000,
        0,0,0, 3,0,0, 1000,
        1,0,0, 1,0,1, 1.25,0,1.3, 1.75,0,1.3, 2,0,1, 2,0,0, 1000,
        3,0,2, 3,1,2, 1000,
        2,0,3, 2,1,3, 1000,
        2,1,4, 1.5,.5,5.5, 2000,
        1,1,4, 1,1,3, 0,1,2, 0,1,0, 3,1,0, 1000,
        0,0,0, 0,1,0, 1000,
        0,0,2, 0,1,2, 1000,
        1,0,3, 1,1,3, 1000,
        1,0,4, 1,1,4, 2,1,4, 2000
    ]
    
    data_index = 0
    B1 = 0
    
    def read_data():
        nonlocal data_index
        value = DATA[data_index]
        data_index += 1
        return value
    
    def perspective_transform(MX, MY, MZ):
        nonlocal B1
        MX, MY, MZ = MX-OX, MY-OY, MZ-OZ
        
        UU = MX
        MX = C1*UU - S1*MY
        MY = S1*UU + C1*MY
        
        UU = MX
        MX = C2*UU - S2*MZ
        MZ = S2*UU + C2*MZ
        
        UU = MY
        MY = C3*UU - S3*MZ
        MZ = S3*UU + C3*MZ
        
        MX, MY, MZ = MX-QX, MY-QY, MZ-QZ
        
        KP = DC/MX
        XX, YY = -KP*MY, KP*MZ
        X_ = int(NP * (0.5 + XX/TC))
        Y_ = int(NP * (0.5 + YY/TC))
        
        if B1 == 1:
            turtle.pendown()

        else:
            turtle.penup()
            B1 = 1
        
        turtle.goto(X_, Y_)
    
    turtle.clear()

    while True:
        MX = read_data()

        if MX == 2000:
            break

        if MX == 1000:
            B1 = 0
            MX = read_data()

        MY = read_data()
        MZ = read_data()
        
        perspective_transform(MX, MY, MZ)