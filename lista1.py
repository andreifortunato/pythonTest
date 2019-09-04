minha_string = "O rato roeu a roupa do rei de Roma"
## eliminar strings pelo metodo split:
minha_lista = minha_string.split("r")
print(minha_string)
## buscar por uma palavra pelo metodo find:
busca = minha_string.find("rei")
print(busca)
## busca a partir da palavra rei: 
print(minha_string[busca:])

