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
 
import serial

porta = 'COM7'
baud_rate    = 115200 # VELOCIDADE DO CALAMP PADRÃO
at           = b'at\r\n'
apnVivo      = b'AT$APP PARAM 2306,0,trixlog.vivo.com.br\r\n'
loginVivo    = b'AT$APP PARAM 2314,0,vivo\r\n'
senhaVivo    = b'AT$APP PARAM 2315,0,vivo\r\n'

apnClaro     = b'AT$APP PARAM 2306,0,trix.claro.com.br\r\n'
loginClaro   = b'AT$APP PARAM 2314,0,claro\r\n'
senhaClaro   = b'AT$APP PARAM 2315,0,claro\r\n'

manterSerial = b'ats130=0\r\n' 
atic         = b'ATIC\r\n'     
 
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
def conectar_porta(numCom, at):
   flag = 0
   valor = 'NADA'
   
   try:
       numCom = 'COM%d' %numCom
       Obj_porta = serial.Serial(numCom, baud_rate)
       
       if Obj_porta.is_open == True:
           while flag != 1:
               Obj_porta.write(at)
               valor = str(Obj_porta.readline())
               test = valor.find('OK');
               if(valor[2:(len(valor)-5)] != ''):
                   print ("Valor lido da Serial: " ,valor[2:(len(valor)-5)])
               if (test > -1):
                   flag = 1
       Obj_porta.close()

   except serial.SerialException:
       print ("ERRO: Verifique se ha algum dispositivo conectado na porta!")
 
   return flag 

################################ MAIN ####################################
if __name__=='__main__':
    var = 1
    portCom = -1
    print("Numero da porta | Nome da Porta")
    while var != 0:
        for numero,portas_ativas in verifica_portas():
            print("      %d         |    %s" % (numero,portas_ativas))
            if (conectar_porta(numero, at) == 1):
                portCom = numero
        if(portCom != -1):
            print("CALAMP CONECTADO NA PORTA: ", portCom)
            print("===========================================")
            print("========= 1 - ALTERAR APN PARA CLARO ======")
            print("========= 2 - ALTERAR APN PARA VIVO =======")
            print("===========================================")
            opcao = int (input("Digite a Opcao: "))
         
            if opcao == 1:
                print("====== CLARO: ======")
                if conectar_porta(portCom, apnClaro) == 1:
                    print("APN ALTERADA")
                if conectar_porta(portCom, loginClaro) == 1:
                    print("LOGIN ALTERADO")
                if conectar_porta(portCom, senhaClaro) == 1:
                    print("SENHA ALTERADA")
                

            elif opcao == 2:
                print("====== VIVO: ======")
                if conectar_porta(portCom, apnVivo) == 1:
                    print("APN ALTERADA")
                if conectar_porta(portCom, loginVivo) == 1:
                    print("LOGIN ALTERADO")
                if conectar_porta(portCom, senhaVivo) == 1:
                    print("SENHA ALTERADA")            

            else:
               print ("Entrada Invalida!!")

            print ("===========================")
            print ("===== 0 - Finalizar   =====")
            print ("===== 1 - Continuar   =====")
            print ("===========================")
            var = int (input("Digite a Opcao: "))
