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
    

elif opcion == 2:
    a= 6378137
    f= 0.003352810665
    

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

    X = float(input("Ingrese el valor de X : "))
    Y = float(input("Ingrese el valor de Y : "))
    Z = float(input("Ingrese el valor de Z : "))
    
    raizXY = math.sqrt((X*X)+(Y*Y))
    e1rara = 1-e1
    longitud = (math.atan(Y/X))*180/math.pi
    longitudABS = abs(longitud)

    phiRadianCero = (math.pi/2)-(math.atan(Z/raizXY)*(1/e1rara))
    phiCero = 90-(phiRadianCero*180/math.pi)
    NCero = a/math.sqrt(1-e1*(math.sin(e))*(math.sin(e)))
    hCero = raizXY/math.cos(math.radians(phiCero))-NCero
    tanFi = math.tan(math.radians(phiCero))
    gradoCero = sign(phiCero)*int(abs(phiCero))
    minutosCero = int((abs(phiCero)-abs(gradoCero))*60)
    segundosCeros = (((abs(phiCero)-abs(gradoCero))*60)-minutosCero)*60


    phiRadian1 = math.atan((Z/raizXY)*(1/(1-e1*(NCero/(NCero+hCero)))))
    phi1 = (phiRadian1 * 180/math.pi)
    N1 = a/math.sqrt(1-e1*(math.sin(math.radians(phi1)))*(math.sin(math.radians(phi1))))
    h1 = (raizXY/math.cos(math.radians(phi1)))-N1
    tanfi1 = math.tan(math.radians(phi1))
    grado1 = sign(phi1)*int(abs(phi1))
    minutos1 = int((abs(phi1)-abs(grado1))*60)
    segundos1 = (((abs(phi1)-abs(grado1))*60)-minutos1)*60


    phiRadian2 = math.atan((Z/raizXY)*(1/(1-e1*(N1/(N1+h1)))))
    phi2 = (phiRadian2 * 180/math.pi)
    N2 = a/math.sqrt(1-e1*(math.sin(math.radians(phi2)))*(math.sin(math.radians(phi2))))
    h2 = (raizXY/math.cos(math.radians(phi2)))-N2
    tanfi2 = math.tan(math.radians(phi2))
    grado2 = sign(phi2)*int(abs(phi2))
    minutos2 = int((abs(phi2)-abs(grado2))*60)
    segundos2 = (((abs(phi2)-abs(grado2))*60)-minutos2)*60


    phiRadian3 = math.atan((Z/raizXY)*(1/(1-e1*(N2/(N2+h2)))))
    phi3 = (phiRadian3 * 180/math.pi)
    N3 = a/math.sqrt(1-e1*(math.sin(math.radians(phi3)))*(math.sin(math.radians(phi3))))
    h3 = (raizXY/math.cos(math.radians(phi3)))-N3
    tanfi3 = math.tan(math.radians(phi3))
    grado3 = sign(phi3)*int(abs(phi3))
    minutos3 = int((abs(phi3)-abs(grado3))*60)
    segundos3 = (((abs(phi3)-abs(grado3))*60)-minutos3)*60


    longitudGrados = sign(Y)*int(abs(longitudABS))
    longitudMinutos = int((abs(longitudABS)-abs(longitudGrados))*60)
    longitudSegundos = (((abs(longitudABS)-abs(longitudGrados))*60)-longitudMinutos)*60


    diferencia1 = segundosCeros - segundos1
    diferencia2 = segundos1 - segundos2
    diferencia3 = segundos2 - segundos3

    print("Escoja la diferencia mas cercana a cero")
    print("Diferencia 1 : "+str(diferencia1))
    print("Diferencia 2 : "+str(diferencia2))
    print("Diferencia 3 : "+str(diferencia3))

    eleccion = int(input())

    if eleccion == 1:
        print("Latitud Gados : "+  str(gradoCero))
        print("Latitud minutos : "+  str(minutosCero))
        print("Latitud segundos : "+  str(segundosCeros))
        print("Longitud Gados : "+  str(longitudGrados))
        print("Longitud minutos : "+  str(longitudMinutos))
        print("Longitud segundos : "+  str(longitudSegundos))
        print("El ACHE es : "+  str(hCero))
    elif eleccion == 2:
        print("Latitud Gados : "+  str(grado1))
        print("Latitud minutos : "+  str(minutos1))
        print("Latitud segundos : "+  str(segundos1))
        print("Longitud Gados : "+  str(longitudGrados))
        print("Longitud minutos : "+  str(longitudMinutos))
        print("Longitud segundos : "+  str(longitudSegundos))
        print("El ACHE es : "+  str(h1))
    elif eleccion == 3:
        print("Latitud Gados : "+  str(grado2))
        print("Latitud minutos : "+  str(minutos2))
        print("Latitud segundos : "+  str(segundos2))
        print("Longitud Gados : "+  str(longitudGrados))
        print("Longitud minutos : "+  str(longitudMinutos))
        print("Longitud segundos : "+  str(longitudSegundos))
        print("El ACHE es : "+  str(h2))

elif opcion == 4:
    a=6378160
    f=0.003352891869
    