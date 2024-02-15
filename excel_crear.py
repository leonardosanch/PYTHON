import pandas as pd
from pandas import ExcelWriter
import os

ruta = os.path.dirname(os.path.abspath(__file__))

datos = pd.DataFrame({'id':[1,2,3,4],
                      'nombre':["Juan", "Yelimar", "Maria", "Pedro"],
                      'apellido':["Martinez", "Pérez", "Barceló", "Moncada"]

                      })

datos = datos [['id', 'nombre', 'apellido']]

writer = ExcelWriter(ruta+"/archivo.xlsx")

datos.to_excel(writer, sheet_name="Hoja 1", index=False)

writer._save()