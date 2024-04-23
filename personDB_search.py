database = {
            1:{
                'nombre1':'Pablo',
                'nombre2':'Diego',
                'apellido1':'Ruiz',
                'apellido2':'Picasso'
            },
            2:{
                'nombre1':'Elio',
                'apellido1':'Anci'
            },
            3:{
                'nombre1':'Elias',
                'nombre2':'Marcos',
                'nombre3':'Luciano',
                'apellido1':'Marcelo',
                'apellido2':'Gonzalez'
            },
}
database = {str(id): value for id, value in database.items()}

def personDB_search(*args, **database):
    for person_id, person_data in database.items():
        if len(args) != len(person_data):
            continue
        match = True
        for arg in args:
            found_match = False
            for value in person_data.values():
                if arg == value:
                    found_match = True
                    break
            if not found_match:
                match = False
                break
        if match:
            return person_id
    return None