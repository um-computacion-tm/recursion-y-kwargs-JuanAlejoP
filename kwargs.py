def write_name(*args, **kwargs):
    print('---------------------')
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(key, value)

write_name("Ludmila", primer_nombre="Luciano",
                   segundo_nombre="Cristian",
                   primer_apellido="Toneatti",
                   segundo_apellido="Gandolfo")

write_name(primer_nombre="Nehuen",
                   primer_apellido="Donozo",
                   segundo_apellido="Marquez")

write_name("Francisco", "Facundo", "Emiliano", primer_nombre="Celina",
                   segundo_nombre="Anahi",
                   primer_apellido="Guerra Diaz")

write_name("Raul", "Uva", "Antonio", "Pepe", "Yolanda", "Negra", primer_nombre="Eusebio",
                   primer_apellido="Quinteros")