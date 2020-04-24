print ("Bem Vindo ao RSA_Vazamentos")
print ("ADM, a seguir preencha os e-mails vazados")
vaz = []
re = "SIM"

while re == "SIM":
    vaz.append(input("Preencha o e-mail: "))
    rewhile = ""
    while rewhile != "SIM" and rewhile != "NAO":
        rewhile = input("Existe mais enderecos vazados? ").upper()
        re = rewhile
for elemento in vaz:
    print(elemento)

print ("\n_-__-__-__-__-__-__-__-__-__-__-__-_")

print ("\n DESCUBRA SE SEU E-MAIL FOI VAZADO")

print ("_-__-__-__-__-__-__-__-__-__-__-__-_")

meuemail = input("\n Digite seu e-mail: ")

for elemento in vaz:
    if elemento == meuemail:
        print("E-mail vazado, vai dar ruim!")
    else:
        print("Fique em paz!")
