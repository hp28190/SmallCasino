#!/usr/bin/python3.6
#-*-coding:Utf-8 -*

import os
from random import randrange
from math import ceil

#Programme de simulation de jeu de roulette de casino
wallet = 50
while wallet > 0 :
#Variables
	somme = 0
	numero = -1

	#début du programme
	while somme > wallet or somme < 1:	
		somme = input('Combien voulez vous miser ?\n')
		somme = int(somme)
		

	while numero < 0 or numero > 49:
		numero = input('Sur quel numéro ? (entre 0 et 49)\n')
		numero = int(numero)
	
	tire = randrange (50)
	print('La bille s\'arrète sur le',tire) 	

	if tire == numero : #Numéros égaux
		print('Vous avez le bon numéro\n')
		wallet += 3*somme

	elif tire%2 == numero%2 :	#Même couleur
		print('vous avez miser sur la bonne couleur\n')		
		wallet += ceil(somme/2)
	else :
		print('vous avez perdu\n')
		wallet -= somme
	
	if wallet > 0:
		print("Vous avez encore:", wallet, "$\n") 
	else :
		print('Game Over\n')
