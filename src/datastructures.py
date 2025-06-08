"""
Update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- get_member: Should return a member from the self._members list
"""

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1 # Este es el ID que se usará
        self._members = [
            {
                "id": self._generate_id(),
                "first_name": "John",
                "last_name": last_name,
                "age": 33,
                "lucky_numbers": [7, 13, 22]
            }
        ]

    # Este método genera un ID incremental único
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id
    
    # Agregamos un nuevo miembro a la familia
    def add_member(self, member):
        # Si no tiene ID, se lo asignamos automáticamente
        if "id" not in member:
            member["id"] = self._generate_id()

        # Aseguramos que el apellido sea el correcto
        member["last_name"] = self.last_name

        # Agregamos a la lista
        self._members.append(member)

    # Eliminamos a un miembro por ID
    def delete_member(self, id):
        # Recorremos la lista y eliminamos al que coincida con el ID
        self._members = [m for m in self._members if m["id"] != id]

    def get_member(self, id):
        # Obtenemos a un miembro por el ID
        for member in self._members:
            if member["id"] == id:
                return member
        return None

    # Este método está hecho, devuelve una lista con todos los miembros de la familia.
    def get_all_members(self):
        return self._members