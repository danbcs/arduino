# Autor: Fernando Krein Pinheiro
# Data: 07/09/2011
# Linguagem: Python

# PROGRAMA ATUALIZADO PARA PYTHON 3.x
# Modificado por: Daniel Bento - @DBent0
# Data: 19/12/2017
 
# ========= IMPORTANTE ===========
# O codigo esta livre para usar,
# citar e compartilhar desde que
# mantida sua fonte e seu autor.
# Obrigado.
 
#! /usr/bin/env python
 
import serial
porta = 'COM7'
baud_rate = 115200 # VELOCIDADE DO CALAMP PADRÃO
at           = 'at/r/n'               # ALTERAR COMANDO PARA HEXADECIMAL
manterSerial = 'ats130=0/r/n' # ALTERAR COMANDO PARA HEXADECIMAL
atic         = 'ATIC/r/n'     # ALTERAR COMANDO PARA HEXADECIMAL
 
###################### FUNCAO PARA VERIFICAR PORTAS ATIVAS ###############
def verifica_portas():
 
    portas_ativas = []
    for numero in range(10):
 
        try:
            num = 'COM%d' %numero
            objeto_verifica = serial.Serial( num,baud_rate )
            portas_ativas.append((numero, objeto_verifica.portstr))
            objeto_verifica.close()
 
        except serial.SerialException:
            pass
    return portas_ativas
 
################## FUNCAO PARA ESCREVER NA PORTA ####################
def escrever_porta(numCom, comandAt):
 
   try:
       port   = numCom
       numCom = 'COM%d' %numCom
       #comandAt = b'%s' %comandAt
       #~ valor = (input("Digite o valor a ser enviado: "))
       Obj_porta = serial.Serial(numCom, baud_rate)
       Obj_porta.write(at)
       Obj_porta.close()
       
 
   except serial.SerialException:
       print ("ERRO: Verifique se ha algum dispositivo conectado na porta!")
 
   return ler_porta(port)
 
########################## FUNCAO PARA LER A PORTA #######################
def ler_porta(numCom):
    flag = 0
    try:
        numCom = 'COM%d' %numCom
        valor = 'NADA RECEBIDO'
        Obj_porta = serial.Serial(numCom, baud_rate)
        Obj_porta.write(at)
        if Obj_porta.is_open == True:
            while valor != "b'OK\r\n'" or flag == 1:
                valor = Obj_porta.readline()
                print ("Valor lido da Serial: ",valor)
                if valor == "b'at\r\n'":
                    flag = 1
           #while flag != 0A:
           #valor.append(Obj_porta.read())
           #print ("Valor lido da Serial: ",valor)
           #Obj_porta.close()
        else:
            print ("PORTA ESTÁ OCUPADA!")
        #print ("Valor lido da Serial: ",valor)
    except serial.SerialException:
       print ("ERRO: Verifique se ha algum dispositivo conectado na porta!")
    return flag
 
################################ MAIN ####################################
if __name__=='__main__':
    var = 1
    while var != 0:
    
        print("===========================================")
        print("===== 1 - Verificar Portas Existentes =====")
        print("===== 2 - Ler Valor da Porta Serial   =====")
        print("===== 3 - Escrever Valor na Porta Serial ==")
        print("===========================================")
        opcao = int (input("Digite a Opcao: "))
     
        if opcao == 1:
            print("Numero da porta | Nome da Porta")
            for numero,portas_ativas in verifica_portas():
                print("      %d         |    %s" % (numero,portas_ativas))
                if escrever_porta(numero, at) == 1:
                    portCom = numero
                
     
        #elif opcao == 2:
            #ler_porta()
     
       # elif opcao == 3:
            #escrever_porta()
     
        else:
           print ("Entrada Invalida!!")

        print ("===========================")
        print ("===== 0 - Finalizar   =====")
        print ("===== 1 - Continuar   =====")
        print ("===========================")
        var = int (input("Digite a Opcao: "))
