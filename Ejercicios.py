# Variables 
x = 0
y = 0
z = 0

# Función no.1 = (x*x')+(y*y')+z'

F1 = (x and (not x)) or (y and (not y)) or (not z)

# Función no.2 = (x*x') + (y*y') + z

F2 = (x and not x) or (y and not y) or z

# Tabla de verdad no.2

# Función no.1 = x'y'z + z'yz' + x'yz + + xy'z' 

F3 = ((not x) and (not y) and z) or ((not x) and y and (not z)) or ((not x) and y and z) or (x and (not y) and (not z))

# Tabla de verdad no.3

# Función no.1 = (x'*y') + (x*y) + (y*z') + (y'z')

F4 = (not x and not y) or (x and y) or (y and not z) or (not y and z) 

# Función no.2 (x'*y'*z')

F5 = (not x) and (not y) and (not z)

#Tabla de verdad no.4 

# Función no.1 = x'y'z' + x'yz' + x'yz + xy'z 

F6 = ((not x) and (not y) and (not z)) or ((not x) and y and (not z)) or ((not x) and y and z) or (x and (not y) and z) 

# Función no.2 = x'y'z + x'yz + xyz' 

F7 = ((not x) and (not y) and z) or ((not x) and y and z) or (x and y and (not z))

#Tabla de verdad no.5

# Función no.1 = (x'y'z' + (x+y+z)) + x'yz' + xy'z' + xy'z 

F8 = ((not z) and (not y) and (not z) or (x or y or z)) or ((not x) and y and (not z)) or (x and (not y) and (not z)) or (x and y and (not z))

# Función no.2 = x'y'z' + x'yz' + x'yz + xy'z' + xyz'

F9 = ((not x) and (not y) and (not z)) or ((not x) and y and (not z)) or ((not x) and y and z) or (x and (not y) and (not z)) or (x and y and (not z))

#Tabla de verdad no.6

# Función no.1 = x'y'z' + x'y'z + x'yz + xy'z'

F10 = ((not x) and (not y) and (not z)) or ((not x) and (not y) and z) or ((not x) and y and z) or (x and (not y) and (not z)) 

# Función no.2 = x'yz' + x'yz + xyz' + xyz

F11 = ((not x) and y and (not z)) or ((not x) and y and z) or (x and y and (not z)) or (x and y and z) 




