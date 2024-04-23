def write_name(*args, **kwargs):
    print('---------------------')
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

write_name('Ludmila', first_name = 'Luciano',
                   second_name = 'Cristian',
                   first_surname = 'Toneatti',
                   second_surname = 'Gandolfo')

write_name(first_name = 'Nehuen',
                   first_surname = 'Donozo',
                   second_surname = 'Marquez')

write_name('Francisco', 'Facundo', 'Emiliano', first_name = 'Celina',
                   second_name = 'Anahi',
                   first_surname = 'Guerra Diaz')

write_name('Raul', 'Uva', 'Antonio', 'Pepe', 'Yolanda', 'Negra', first_name = 'Eusebio',
                   first_surname = 'Quinteros')