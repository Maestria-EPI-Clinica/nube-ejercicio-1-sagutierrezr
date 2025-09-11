import unittest
import os
import pandas as pd
from nube import generar_nube_palabras

data = {
    'Nombre': ['juan pajaro', 'tank', 'neo'],
    'expectativa': [
        'Espero entender como usar redes neuronales y transformers en los datos de historía clínica',
        'Deseo usar los algoritmos de redes',
        'Es importante en mi campo de aprendizaje usar las redes neuronales'
    ]
}

class TestGenerarNubePalabras(unittest.TestCase):
    def setUp(self):
        self.df = pd.DataFrame(data)
        self.output_file = 'test_nube_palabras.png'

    def tearDown(self):
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generar_nube_palabras_crea_archivo(self):
        generar_nube_palabras(self.df, 'expectativa', self.output_file)
        self.assertTrue(os.path.exists(self.output_file))
        # Opcional: Verificar que el archivo no esté vacío
        self.assertGreater(os.path.getsize(self.output_file), 0)

if __name__ == '__main__':
    unittest.main()
