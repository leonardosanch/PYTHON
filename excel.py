import pandas as pd
from pandas import ExcelWriter
import xlrd2
import os

ruta = os.path.dirname(os.path.abspath(__file__))

documento = xlrd2.open_workbook(ruta+"/archivo.xlsx")
datos = documento.sheet_by_index(0)
for i in range(datos.nrows):
    if i >=1:
        print(f"ID={datos.cell_value(i,0)} | Nombre:{datos.cell_value(i,1)} | Apellido:{datos.cell_value(i,2)}")



