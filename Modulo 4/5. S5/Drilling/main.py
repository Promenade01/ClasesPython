from persona import Persona
from departamento import Departamento
from trabajador import Trabajador

trabajador1 = Trabajador("Juan", "Perez", "2005", "Ingenieria de software", "IS", "20000")

# print(trabajador1.nombre)
# print(trabajador1.apellido)
# print(trabajador1.nombre_dpto)
# print(trabajador1.salario)

#! Drilling

print(trabajador1.__dict__)
print("Es trabajador instancia de Persona: ",isinstance(trabajador1, Persona))
print("Es trabajador instancia de Departamento: ",isinstance(trabajador1, Departamento))
print("Es trabajador instancia de Trabajador: ",isinstance(trabajador1, Trabajador))