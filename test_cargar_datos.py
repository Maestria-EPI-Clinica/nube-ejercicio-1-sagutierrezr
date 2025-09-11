import unittest
import pandas as pd
from nube import cargar_datos

class TestCargarDatos(unittest.TestCase):
    def test_cargar_datos_csv(self):
        # Usar el archivo expectativas.csv incluido en el workspace
        df = cargar_datos('expectativas.csv')
        # Verificar que se cargue correctamente y tenga las columnas esperadas
        self.assertIsInstance(df, pd.DataFrame)
        self.assertIn('Nombre', df.columns)
        self.assertIn('expectativa', df.columns)
        
if __name__ == '__main__':
    unittest.main()
