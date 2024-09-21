from contacts import Contacts

contacts_list = Contacts("Lista_contactos.txt")

while True:
    print("Guía Telefónica 2024\n")
    print("1. Crear un nuevo contacto")
    print("2. Buscar un contacto")
    print("3. Modificar numero de contacto")
    print("4. Eliminar un contacto")
    print("5. Listar todos los contactos")
    print("6. Salir")

    option = int(input("Ingrese una opción: "))

    if option == 1:
        name = input("Nombre del contacto: ")
        number = input("Número de teléfono: ")
        contacts_list.add_contact(name, number)
    elif option == 2:
        name = input("Nombre del contacto a buscar: ")
        contact = contacts_list.search_contact(name)
        if contact:
            print(f"Contacto encontrado\nNombre: {contact[0]}\nNúmero: {contact[1]}")
        else:
            print(f"Contacto '{name}' no encontrado.")
    elif option == 3:
        name = input("Nombre del contacto a modificar: ")
        new_number = input("Nuevo número de teléfono: ")
        contacts_list.edit_contact(name, new_number)
    elif option == 4:
        name = input("Nombre del contacto a eliminar: ")
        contacts_list.delete_contact(name)
    elif option == 5:
        contacts_list.show_contacts()
    elif option == 6:
        print("Saliendo del programa...")
        break
    else:
        print("Intentelo de nuevo")