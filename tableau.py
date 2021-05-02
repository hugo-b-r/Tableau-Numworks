#importation
from math import *
import kandinsky as kdk
import ion as ion
from time import *



#on définit les couleurs ici
BLANC = kdk.color(255,255,255)
NOIR = kdk.color(0,0,0)
GRIS = kdk.color(220,220,220)


#on dessine le cadre du tableau et les numéros de coordonnées
def colonnes():
  #les colonnes
  x_colonnes = 0
  for i in range(6):
    kdk.draw_line(x_colonnes, 0, x_colonnes, 222, NOIR)
    x_colonnes = x_colonnes + 64

def lignes():
  #les lignes
  y_lignes = 0
  for i in range(11):
    kdk.draw_line(0, y_lignes, 340, y_lignes, NOIR)
    y_lignes = y_lignes + 22
  kdk.draw_line(0, 221, 340, 221, NOIR)

def texte():
  #les numéros
  x_texte = 0
  y_texte = 1
  for i in range(9):
    kdk.draw_string(str(y_texte),2,x_texte+25)
    x_texte = x_texte + 22
    y_texte = y_texte + 1
  x_texte = 0
  y_texte = 1
  for i in range(4):
    kdk.draw_string(str(y_texte),x_texte+66,2)
    x_texte = x_texte + 64
    y_texte = y_texte + 1

def quadrillage():
  #appelle toute les fonctions qui dessinent le quadrillage et les coordonnées
  kdk.fill_rect(0,0,320,222,BLANC)
  texte()
  colonnes()
  lignes()




#on definit les fonctions pour passer des coordonnées de cases vers des coordonnées en pixels
def x_case_vers_x_sur_l_ecran(x):
  return x*64+1

def y_case_vers_y_sur_l_ecran(y):
  return y*22+1




#on definit la fonction qui permet de savoir où stocker l'entrée
def ajout_d_un_caractere(touche):

  def stockage_d_une_entree_en(x):
    if selecteur.x == x:
      colonne1[int(selecteur.y) - 1] = colonne1[int(selecteur.y) - 1] + touche
      
      #on essaye d'écrire la nouvelle valeur
      try:
        print("ecriture")
        kdk.draw_string(str(colonne1[selecteur.y]), x_case_vers_x_sur_l_ecran(selecteur.x), y_case_vers_y_sur_l_ecran(selecteur.y))
      except:
        print("erreur d'affichage\réssayez.")
  
  for i in range(5):
    stockage_d_une_entree_en(i+1)
  
  sleep(0.15)



#on cree une classe "sélecteur"
class Selecteur():
  #on definit l'initialisation
  def __init__(self,x,y):
    self.x = x
    self.y = y
    kdk.fill_rect(x_case_vers_x_sur_l_ecran(self.x),y_case_vers_y_sur_l_ecran(self.y),63,21,GRIS)


  #on definit la recuperation des coordonnées.
  def get_x(self):
    return self.x
  
  def get_y(self):
    return self.y

  #on definit la sélection puis la déselection
  def selectionner(self):
    kdk.fill_rect(x_case_vers_x_sur_l_ecran(self.x),y_case_vers_y_sur_l_ecran(self.y),63,21,GRIS)

  def effacer_la_selection(self):
    kdk.fill_rect(x_case_vers_x_sur_l_ecran(self.x),y_case_vers_y_sur_l_ecran(self.y),63,21,BLANC)  



      

#on initialise le tableau
quadrillage()

#on crée le selecteur
selecteur = Selecteur(1, 1)

#on crée les listes pour chaque colonne
colonne1 = ["","","","","","","","",""]
colonne2 = ["","","","","","","","",""]
colonne3 = ["","","","","","","","",""]
colonne4 = ["","","","","","","","",""]




#boucle principale
while True:
  #on teste les touches de navigation
  if ion.keydown(ion.KEY_DOWN):#↓
    if selecteur.y != 9:
      selecteur.effacer_la_selection()
      selecteur.y = selecteur.y + 1
      selecteur.selectionner()
      sleep(0.1)
      
  elif ion.keydown(ion.KEY_UP):#↑
    if selecteur.y != 1:
      selecteur.effacer_la_selection()
      selecteur.y = selecteur.y - 1
      selecteur.selectionner()
      sleep(0.1)
  
  elif ion.keydown(ion.KEY_LEFT):#←
    if selecteur.x != 1:
      selecteur.effacer_la_selection()
      selecteur.x = selecteur.x - 1
      selecteur.selectionner()
      sleep(0.15)
  
  elif ion.keydown(ion.KEY_RIGHT):#→
    if selecteur.x != 4:
      selecteur.effacer_la_selection()
      selecteur.x = selecteur.x + 1
      selecteur.selectionner()
      sleep(0.15)





  elif ion.keydown(ion.KEY_ZERO):
    #on teste la touche 0
    ajout_d_un_caractere("0")
  
  elif ion.keydown(ion.KEY_ONE):
    #on teste la touche 1
    ajout_d_un_caractere("1")
  
  elif ion.keydown(ion.KEY_TWO):
    #on teste la touche 2
    ajout_d_un_caractere("2")
  
  elif ion.keydown(ion.KEY_THREE):
    #on teste la touche 3
    ajout_d_un_caractere("3")
  
  elif ion.keydown(ion.KEY_FOUR):
    #on teste la touche 4
    ajout_d_un_caractere("4")
  
  elif ion.keydown(ion.KEY_FIVE):
    #on teste la touche 5
    ajout_d_un_caractere("5")
  
  elif ion.keydown(ion.KEY_SIX):
    #on teste la touche 6
    ajout_d_un_caractere("6")
  
  elif ion.keydown(ion.KEY_SEVEN):
    #on teste la touche 7
    ajout_d_un_caractere("7")
  
  elif ion.keydown(ion.KEY_EIGHT):
    #on teste la touche 8
    ajout_d_un_caractere("8")
  
  elif ion.keydown(ion.KEY_NINE):
    #on teste la touche 9
    ajout_d_un_caractere("9")
  
  
      
  kdk.draw_string(str(selecteur.x)+";"+str(selecteur.y),2,2)
