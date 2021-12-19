from funcoes.fucoesjson import  *

inventario = ler_arquivo("inventariojson.json")
opcao=chamarMenu()
while opcao>0 and opcao<3:
    if opcao==1:
        print(registrar(inventario, "inventariojson.json"))
    elif opcao==2:
        exibir("inventariojson.json")
    opcao = chamarMenu()