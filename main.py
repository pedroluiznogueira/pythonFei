valor = int( input("Digite o valor:") )
esp = 0
while valor > 0 :
    d=valor%10
    esp=esp*10+d
    valor=valor//10
print("Resultado:", esp)