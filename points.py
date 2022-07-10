import pyautogui as main

EMPRESA_A = "EMPRESA_A"
EMPRESA_B = "EMPRESA_B"
EMPRESA_C = "EMPRESA_C"


estado_civil= [(551,344),(599,345),(567,345)]
genero_sexo = [(693,344),(704,344)]
posiciones = [(447,345),(341,376),(454,375),(631,346),(344,390),(506,373),(344,415)]
coordenadas = []

def empresa():
    if input_empresa == "EMPRESA_A":
        main.write(EMPRESA_A)   
    elif input_empresa == "EMPRESA_B":
        main.write(EMPRESA_B)
    elif input_empresa == "EMPRESA_C":
        main.write(EMPRESA_C)

def estado(a,b): 
    if input_estado_civil == "Soltero":
        a.append(b[0])
        return a[0]
    elif input_estado_civil == "Unión L.":
        a.append(b[1]) 
        return a[0]
    elif input_estado_civil == "Casado":
        a.append(b[2])
        return a[0]


def genero(a,b):
    if input_genero == "Masculino":
        a.append(b[0])
        return a[1]
    elif input_genero == "Femenino":
        a.append(b[1])
        return a[1]  

def data_position(a):
    estado(a, estado_civil)
    genero(a, genero_sexo)
    return_ubicacion = a + posiciones
    return return_ubicacion

input_empresa = main.confirm('Empresa', buttons=['EMPRESA_A', 'EMPRESA_B', 'EMPRESA_C'])   
input_estado_civil = main.confirm('Estado Civil', buttons=['Soltero', 'Unión L.', 'Casado'])
input_genero = main.confirm('GENERO', buttons=['Femenino', 'Masculino'])
