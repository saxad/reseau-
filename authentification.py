#! /usr/bin/env python
# -*- coding: utf8 -*-

from getpass import getpass
from  database import *
import socket
import time

"""
def deconnexion(client, clients_a_lire,clients_connectes):
	client.close()
	clients_a_lire.remove(client)
	clients_connectes.remove(client)
"""

def authentificationserveur(client):

	identification = 0
	buf = 1024
	client.send("=====================================\n----Authentification ---\n=====================================\n")

	while identification == 0:

		nom = client.recv(buf)
		print "message recu : ",nom
		data = "recu"
		client.send(data)

		prenom = client.recv(buf)
		print "message recu : ",prenom
		client.send(data)

		mdp = client.recv(buf)
		print "message recu : ", mdp
		################################################################

		client.send(data)
		# identification return 0 pour false, et 1 pour true
		identification = isintable(nom,prenom,mdp,"employees")

		if identification == 0 :
			client.send("nok")

		else:
			data = "entre une action ..."
			client.send(data)
		##################################################################

			data = client.recv(buf)
			while 1:

				print(data)
				if data.upper() == 'FIN':
					break
				client.send("action traité... \n(pas vraiment j'ai pas encore codé cette partie mais\nbon bref entre une autre ou fin pour finir)")
				data = client.recv(buf)

			client.send("envoie < F > pour confirmer")
			data = client.recv(buf)
			
			if data.upper() == 'F':
				client.send("fin")
				print("\n---- deconnecxion du client ------\n" )
				break
			else:
				print("coucou")
	print("c'est fini molami")

	return 0



def authentificationclient(client):



	buf = 1024
	identification = 'nok'

	print(client.recv(buf))

	while identification == 'nok' :
		print("\n")
		data = raw_input("entre ton nom : ")
		client.send(data)

		data = client.recv(buf)#ack recu
		print "serveur : ", data#ack recu

		data = raw_input("entre ton prenom : ")
		client.send(data)

		data = client.recv(buf)#ack recu
		print "serveur : ", data#ack recu

		data = getpass("entre ton mot de passe : ")
		###### Faut chiffrer le mot de passe avant de l'envoyer ######
		client.send(data)
		data = client.recv(buf)#ack recu
#############################################" blempro"
		print "serveur : ", data #ack recu       il lit deux send


		identification = client.recv(buf)

		if identification == 'nok':
			print("==================================================\nerreur d'enthentification entrez votre Id a nouveau")
		else:

			print("\n=============================\nvous etes connecté au serveur")
			print "serveur : ", identification

#########################################################


			print("\n==============================\nCONSOLE DES ACTIONS : \n")

			while 1:
				data = raw_input("C> ")
				client.send(data)
				data = client.recv(buf)
				print(data)
				if data.upper() == "FIN":
					break
