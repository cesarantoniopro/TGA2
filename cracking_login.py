# -*- coding: utf-8 -*-
"""Cracking.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dmwO51uukUMtD1TXAX_AKAiCGz0Ka2AQ
"""

def login(usuario, contrasena):
    # En un sistema real, nunca debes almacenar contraseñas en texto plano.
    usuarios = {
        'usuario1': 'contrasena1',
        'usuario2': 'contrasena2'
    }

    if usuario in usuarios and usuarios[usuario] == contrasena:
        return "Acceso concedido"
    else:
        return "Acceso denegado"

print(login('usuario1', 'contrasena1'))  # Acceso concedido
print(login('usuario1', 'contrasenaIncorrecta'))  # Acceso denegado