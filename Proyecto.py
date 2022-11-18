import math

a = 0
f = 0
b = 0
e1 = 0
e2 = 0
e = 0
E =0
m = 0
n = 0
f1 = 0
gradosLatitud = 0
minutosLatitud = 0
segundosLatitud = 0
gradosLongitud = 0
minutosLongitud = 0
segundosLongitud = 0
h = 0
latitud = 0
latitudRad = 0
longitud = 0
longitudRad = 0
sen = 0
N = 0
X = 0
Y = 0
Z = 0
opcion = 0


def sign (parametro):
        if parametro < 0:
            return -1
        elif parametro == 0:
            return 0
        else:
            return 1


print("Seleccione el sistema de referencia")
print("1.- SIRGAS")
print("2.- WGS84")
print("3.- Psad56")
print("4.- SAD69")

opcion = int(input())

if opcion == 1:
    a = 6378137
    f = 0.003352810681
    b = a-a*f
    e1 = (math.sqrt(a*a-b*b)/a)*(math.sqrt(a*a-b*b)/a)
    e2 = (math.sqrt(a*a-b*b)/b)*(math.sqrt(a*a-b*b)/b)
    e = math.sqrt(e1)
    E = e*a
    m = ((a*a)-(b*b))/((a*a)+(b*b))
    n = (a-b)/(a+b)
    f1 = 1/f

    gradosLatitud = float(input("Ingrese los grados de la latitud :"))
    minutosLatitud = float(input("Ingrese los minutos de la latitud :"))
    segundosLatitud = float(input("Ingrese los segundos de la latitud :"))
    gradosLongitud = float(input("Ingrese los grados de la Longitud :"))
    minutosLongitud = float(input("Ingrese los minutos de la Longitud :"))
    segundosLongitud = float(input("Ingrese los segundos de la Longitud :"))
    h = float(input("Ingrese la ACHE :"))

    latitud = sign(gradosLatitud)*(abs(gradosLatitud)+(segundosLatitud/60+minutosLatitud)/60)
    latitudRad = math.radians(latitud)
    longitud = (sign(gradosLongitud))*(abs(gradosLongitud)+((segundosLongitud/60)+minutosLongitud)/60)
    longitudRad = math.radians(longitud)
    sen = math.sin(latitudRad)*math.sin(latitudRad)
    N = a/math.sqrt(1-e1*sen)

    X = (N+h)*math.cos(latitudRad)*math.cos(longitudRad)
    Y = (N+h)*math.cos(latitudRad)*math.sin(longitudRad)
    Z = (((1-e1)*N)+h)*math.sin(latitudRad)

    print("X ="+str(X))
    print("Y ="+str(Y))
    print("Z ="+str(Z))

elif opcion == 2:
    a= 6378137
    f= 0.003352810665
    b = a-a*f
    e1 = (math.sqrt(a*a-b*b)/a)*(math.sqrt(a*a-b*b)/a)
    e2 = (math.sqrt(a*a-b*b)/b)*(math.sqrt(a*a-b*b)/b)
    e = math.sqrt(e1)
    E = e*a
    m = ((a*a)-(b*b))/((a*a)+(b*b))
    n = (a-b)/(a+b)
    f1 = 1/f
elif opcion == 3:
    a= 6378388
    f= 0.003367003367
    b = a-a*f
    e1 = (math.sqrt(a*a-b*b)/a)*(math.sqrt(a*a-b*b)/a)
    e2 = (math.sqrt(a*a-b*b)/b)*(math.sqrt(a*a-b*b)/b)
    e = math.sqrt(e1)
    E = e*a
    m = ((a*a)-(b*b))/((a*a)+(b*b))
    n = (a-b)/(a+b)
    f1 = 1/f
elif opcion == 4:
    a=6378160
    f=0.003352891869
    b = a-a*f
    e1 = (math.sqrt(a*a-b*b)/a)*(math.sqrt(a*a-b*b)/a)
    e2 = (math.sqrt(a*a-b*b)/b)*(math.sqrt(a*a-b*b)/b)
    e = math.sqrt(e1)
    E = e*a
    m = ((a*a)-(b*b))/((a*a)+(b*b))
    n = (a-b)/(a+b)
    f1 = 1/f


