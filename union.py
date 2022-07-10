from data_excel import fila_excel
from points import data_position, coordenadas ,input_estado_civil, input_genero, input_empresa
from functions import puntero, function_copy

data_excel_total = fila_excel()
coordenadas = data_position(coordenadas)


def union_iterador():
    for a, b in zip(coordenadas, data_excel_total):
        puntero(a)
        function_copy(b) 
