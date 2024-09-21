import os
class Contacts:
    def __init__(self, file):
        self.file = file

    # Método para agregar archivos
    def add_contact(self, name, number):
        with open(self.file, "a") as file:
            file.write(f"{name}, {number}\n")
        print(f"Contacto {name} agregado")

    # Método para buscar un contacto
    def search_contact(self, name):
        with open(self.file, 'r') as file:
            for line in file:
                contact_name, contact_number = line.strip().split(",")
                if contact_name == name:
                    return  contact_name, contact_number
        return None

    # Método para modificar un contacto
    def edit_contact(self, name, new_number):
        contacts = []
        founded = None
        with open(self.file, 'r') as file:
            for line in file:
                contact_name, contacto_number = line.strip().split(',')
                if contact_name == name:
                    contacts.append(f"{name},{new_number}\n")
                    founded = True
                else:
                    contacts.append(f"{contact_name},{contacto_number}\n")

            if founded:
                with open(self.file, 'w') as file:
                    file.writelines(contacts)
                print(f"Contacto '{name}' actualizado con el nuevo número '{new_number}'.")
            else:
                print(f"Contacto '{name}' no encontrado.")

    # Método para eliminar un contacto
    def delete_contact(self, name):
        contacts = []
        founded = False
        with open(self.file, 'r') as file:
            for line in file:
                contact_name, contact_number = line.strip().split(',')
                if contact_name != name:
                    contacts.append(f"{contact_name},{contact_number}\n")
                else:
                    founded = True

        if founded:
            with open(self.file, 'w') as file:
                file.writelines(contacts)
            print(f"Contacto '{name}' eliminado.")
        else:
            print(f"Contacto '{name}' no encontrado.")

    # Método para listar todos los contactos
    def show_contacts(self):
        if os.path.exists(self.file):
            with open(self.file, 'r') as file:
                print("Lista de contactos:")
                for line in file:
                    contact_name, contact_number = line.strip().split(',')
                    print(f"Nombre: {contact_name}\nNúmero: {contact_number}\n")
        else:
            print("No hay contactos en la agenda.")