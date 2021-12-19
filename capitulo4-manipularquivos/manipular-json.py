import json
import os
if os.path.exists("inventariojson.json"):
    with open("inventariojson.json", "r") as arqjson:
        inventario = json.load(arqjson)
else:
    inventario={}
opcao=int(input("Digite:\n "
                      
"<1> para registrar ativo\n"
                      
"<2> para exibir ativos armazenados: "))
while opcao>0 and opcao<3:
    if opcao==1:
        resp = "S"
        while resp == "S":
            inventario[input("Digite o número patrimonial: ")] = [
                input("Digite a data da última atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")]
            resp = input("Digite <S> para continuar.").upper()
        with open("inventariojson.json", "w") as arqjson:
            json.dump(inventario, arqjson)
        print("JSON gerado!!!!")
    elif opcao==2:
            with open("inventariojson.json", "r") as arqjson:
    		 resultado = json.load(arqjson)
    		 for chave, dado in resultado.items():
                	print("Data.........: ", dado[0])
                	print("Descrição....: ", dado[1])
                	print("Departamento.: ", dado[2])
    opcao = int(input("Digite:\n "
                
"<1> para registrar ativo\n"

"<2> para exibir ativos armazenados: " ) )
