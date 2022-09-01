from veiculo import Veiculo  #importando o objeto
from carro import Carro      #importanto o objeto

caminhao_preto = Veiculo("Preto", 8 , "Ford", 10)     #passando os argumentos caminhão preto
carro_azul = Veiculo("Azul", 4, "BMW", 6)             #passando os argumentos carro azul

#imprimindo os objetos

print("CAMINHÃO PRETO")
print("Cor: ", caminhao_preto.cor)
print("Marca: ", caminhao_preto.marca)
print("Rodas: ", caminhao_preto.rodas)
print("Tanque: ", caminhao_preto.tanque)

print(" ")

print("CARRO AZUL")
print("Cor: ", carro_azul.cor)
print("Marca: ", carro_azul.marca)
print("Rodas: ", carro_azul.rodas)
print("Tanque: ", carro_azul.tanque)
print(" ")

#Abastecendo o veiculo

print("Tanque: ", caminhao_preto.tanque)
caminhao_preto.abastecer(35)
print("Tanque: ", caminhao_preto.tanque)
print(" ")

#usando o segundo objeto

carro_verde = Carro("Verde", "Fiat", 10)
print("Carro VERDE")
print("Cor: ", carro_verde.cor)
print("Marca: ", carro_verde.marca)
print("Rodas: ", carro_verde.rodas)
print("Tanque: ", carro_verde.tanque)
print(" ")

#ABASTECENDO COM LIMITE

print("Tanque: ", carro_verde.tanque)
carro_verde.abastecer(35)
print("Tanque: ", carro_verde.tanque)
carro_verde.abastecer(20)
print("Tanque: ", carro_verde.tanque)
print(" ")
