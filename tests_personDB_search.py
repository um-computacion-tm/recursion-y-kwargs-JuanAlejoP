import unittest
from personDB_search import personDB_search

class TestPersonDBSearch(unittest.TestCase):
    def setUp(self):
        self.database = {
            '1': {
                'nombre1': 'Pablo',
                'nombre2': 'Diego',
                'apellido1': 'Ruiz',
                'apellido2': 'Picasso'
            },
            '2': {
                'nombre1': 'Elio',
                'apellido1': 'Anci'
            },
            '3': {
                'nombre1': 'Elias',
                'nombre2': 'Marcos',
                'nombre3': 'Luciano',
                'apellido1': 'Marcelo',
                'apellido2': 'Gonzalez'
            },
            '4': {
                'nombre1': 'María', 'nombre2': 'José', 'apellido1': 'García López'
            }
        }

    def test_personFound(self):
        self.assertEqual(personDB_search('Pablo', 'Diego', 'Ruiz', 'Picasso', **self.database), ['1'])
        self.assertEqual(personDB_search('Elio', 'Anci', **self.database), ['2'])
        self.assertEqual(personDB_search('Elias', 'Marcos', 'Luciano', 'Marcelo', 'Gonzalez', **self.database), ['3'])

    def test_unordered_info(self):
        self.assertEqual(personDB_search('Diego', 'Picasso', 'Ruiz', 'Pablo', **self.database), ['1'])
        self.assertEqual(personDB_search('Anci', 'Elio', **self.database), ['2'])
        self.assertEqual(personDB_search('Elias', 'Marcelo', 'Marcos', 'Gonzalez', 'Luciano', **self.database), ['3'])

    def test_compoundNames(self):
        self.assertEqual(personDB_search('María', 'José', 'García', 'López', **self.database), None)
        dynamic_database = self.database.copy()
        dynamic_database['4'] = {'nombre1': 'María', 'nombre2': 'José', 'apellido1': 'García López'}
        self.assertEqual(personDB_search('María', 'José', 'García López', **dynamic_database), ['4'])

    def test_sameNames(self):
        self.assertEqual(personDB_search('Pablo', 'Diego', 'Ruiz', 'Picasso', **self.database), ['1'])
        dynamic_database = self.database.copy()
        dynamic_database['5'] = {'nombre1': 'Pablo', 'nombre2': 'Diego', 'apellido1': 'Ruiz', 'apellido2': 'Picasso'}
        self.assertEqual(personDB_search('Pablo', 'Diego', 'Ruiz', 'Picasso', **dynamic_database), ['1', '5'])

    def test_personNotFound(self):
        self.assertIsNone(personDB_search('Rubén', 'Carolini', **self.database))
        self.assertIsNone(personDB_search('Rodolfo', 'Coria', **self.database))
        self.assertIsNone(personDB_search('Leonardo', 'Salgado', **self.database))

    def test_partial_info(self):
        self.assertIsNone(personDB_search('Pablo', 'Ruiz', **self.database))
        self.assertIsNone(personDB_search('Elio', 'Anci', 'Hernández', **self.database))
        self.assertIsNone(personDB_search('Elias', 'Luciano', **self.database))

    def test_emptyDB(self):
        self.assertIsNone(personDB_search('Pablo', 'Diego', 'Ruiz', 'Picasso'))

    def test_emptyArgs(self):
        self.assertIsNone(personDB_search(**self.database))

    def test_invalidInput(self):
        self.assertIsNone(personDB_search('Pablo', 123, **self.database))
        self.assertIsNone(personDB_search(123, **self.database))

unittest.main()