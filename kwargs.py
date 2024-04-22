def write_name(*args, **kwargs):
    print('---------------------')
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print('key', key, 'value', value)

write_name('Ludmila', first_name = 'Luciano',
    second_name = 'Cristian',
    first_lastname = 'Toneatti',
    second_lastname ='Gandolfo'
    )
write_name(
    first_name = 'Nehuen',
    first_lastname = 'Donoso',
    second_lastname = 'Marquez'
    )
write_name(
    'Facundo', 'Emiliano',
    first_name = 'Celina',
    second_name =  'Anahi',
    first_lastname = 'Guerra Diaz'
    )
write_name(
    'Raul', 'Uva', 'Antonio', 'Pepe', 'Yolanda', 'Negra',
    first_name = 'Eusebio',
    first_lastname =  'Quinteros'
    )