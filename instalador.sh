#!/bin/bash

##############################################
###########-Projeto: instalador-##############
##############################################
## Este ptojeto que traz um instalador      ##
## rapido e seguro para seu linux.          ##
## O projeto instala:                       ##
##
## ClipGrab
## Audacity
## RetroArch 
##
##
##
##
##
##############################################
##############################################
##############################################
#++++++++++++++++++++++++++++++++++++++++++++#
##############################################
#########-Configuração do Programa-###########
##############################################
#                                            #
#-Use 0 (zero) para não instalar o programa  #
#                                            #
#-Use 1 (um) para instalar o programa        #
#                                            #
#-O padrão é 1 (um) para todos os programas  #
#
#
INSTALAR_CLIPGRAB=1 #-Instalar ClipGrab?
INSTALAR_RETROARCH=1 #-Instalar RetroArch?
INSTALAR_AUDACITY=1  #-Instalar Audacity? 
#
#
#
#
#
#
#
#
##############################################
########-Fim da configuração, não edite-######
##############################################

#-Mensagem inicial
dialog --title "Confirmação" \
 --infobox "Nos iremos instalar tudo para você...digite sua senha de root e tome seu café!!!" \
 0 0
#-Dorme 10s
sleep 5
echo
sudo apt-get update 2>&1&> /dev/null
#-Mensagem de Refresh
dialog --title "Refresh no sistema" \
 --infobox "Realizado com sucesso!! " \
 0 0
#-Dorme 5s
sleep 5

#-Instala ClipGrab
if test $INSTALAR_CLIPGRAB -eq 1
then
	#Mostra mensagem de instalação
	dialog --title "ClipGrab" \
	 --infobox "\nInstalando ClipGrab..." \
	  0 0  
	#Dorme 5s
	sleep 5
	#Comandos de instalação + barra de progresso
	(echo 25; sudo add-apt-repository ppa:noobslab/apps -y 2>&1&> /dev/null; \
		echo 50; sudo add-apt-repository ppa:clipgrab-team/ppa -y 2>&1&> /dev/null; \
		echo 75; sudo apt-get update -y 2>&1&> /dev/null; \
		echo 85; sudo apt-get install clipgrab -y 2>&1&> /dev/null; echo 100 ) | dialog --gauge 'Instalando ClipGrab' 8 70 0
	#Mostra mensagem de pós instalação
	dialog --title "ClipGrab" \
	 --infobox "\nInstalação Bem Sucedia!!!" \
	  0 0
	#Dorme 5s
	sleep 5
fi

#-Instala RetroArch
if test $INSTALAR_RETROARCH -eq 1 
then
	#Mostra mensagem de instalação
	dialog --title "RetroArch" \
	 --infobox "\nInstalando RetroArch..." \
	 0 0
	#Dorme 5s
	sleep 5
	#Comandos de instalação + barra de progresso 
	(echo 25; sudo add-apt-repository ppa:libretro/stable  -y 2>&1&> /dev/null; \
		echo 50; sudo apt-get update -y  2>&1&> /dev/null; \
		echo 75; sudo apt-get install retroarch retroarch-* libretro-* -y 2>&1&> /dev/null; echo 100 ) | dialog --gauge 'Instalando RetroArch' 8 70 0
	#Mostra mensagem de pós instalação
	dialog --title "RetroArch" \
	 --infobox "\nInstalação Bem Sucedida!!!" \
	 0 0
	#Dorme 5s
	sleep 5
fi 

#-Instala Audacity
if test $INSTALAR_AUDACITY -eq 1
then
	#Mostra mensagem de instalação
	dialog --title "Audacity" \
	 --infobox "\nInstalando Audacity" \
	 0 0
	#Dorme 5s
	sleep 5
    #Comandos de instalação + barra de progresso 
    (echo 50; sudo apt-get update -y 2>&1&> /dev/null; \

    	echo 75; sudo apt-get install audacity -y 2>&1&> /dev/null; echo 100 ) | dialog --gauge 'Instalando Audacity' 8 70 0
	#Mostra mensagem de pós instalação
	dialog --title "Audacity" \
	 --infobox "Intalação Bem Sucedida!!!" \
	 0 0 
	#Dorme 5s
	sleep 5
fi

sleep 5
exit 


	
  

 

