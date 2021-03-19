#importation
from math import *
from kandinsky import *
from ion import *
from time import *




#on dessine le cadre du tableau et les numéros de coordonnées
def colonnes():
  #les colonnes
  x_colonnes = 0
  for i in range(6):
    draw_line(x_colonnes, 0, x_colonnes, 222, color(0,0,0))
    x_colonnes = x_colonnes + 64

def lignes():
  #les lignes
  y_lignes = 0
  for i in range(11):
    draw_line(0, y_lignes, 340, y_lignes, color(0,0,0))
    y_lignes = y_lignes + 22
  draw_line(0, 221, 340, 221, color(0,0,0))

def texte():
  #les numéros
  x_texte = 0
  y_texte = 1
  for i in range(9):
    draw_string(str(y_texte),2,x_texte+25)
    x_texte = x_texte + 22
    y_texte = y_texte + 1
  x_texte = 0
  y_texte = 1
  for i in range(4):
    draw_string(str(y_texte),x_texte+66,2)
    x_texte = x_texte + 64
    y_texte = y_texte + 1

def quadrillage():
  #appelle toute les fonctions qui dessinent le quadrillage et les coordonnées
  fill_rect(0,0,320,222,color(255,255,255))
  texte()
  colonnes()
  lignes()




#on definit les fonctions pour passer des coordonnées de cases vers des coordonnées en pixels
def x_case_vers_x_sur_l_ecran(x):
  return x*64+1

def y_case_vers_y_sur_l_ecran(y):
  return y*22+1




#on definit la fonction qui permet de savoir ou stocker l'entrée
def ajout_d_un_caractere(touche):
  if selecteur.x == 1:
    colonne1[int(selecteur.y)] = colonne1[int(selecteur.y)] + touche
      
  elif selecteur.x == 2:
    colonne2[int(selecteur.y)] = colonne1[int(selecteur.y)] + touche
  
  elif selecteur.x == 3:
    colonne3[int(selecteur.y)] = colonne1[int(selecteur.y)] + touche

  elif selecteur.x == 4:
    colonne4[int(selecteur.y)] = colonne1[int(selecteur.y)] + touche
  
  print(colonne1)
  print(colonne2)
  print(colonne3)
  print(colonne4)
  sleep(0.15)



#on cree une classe "sélecteur"
class Selecteur():
  #on definit l'initialisation
  def __init__(self,x,y):
    self.x = x
    self.y = y
    fill_rect(x_case_vers_x_sur_l_ecran(self.x),y_case_vers_y_sur_l_ecran(self.y),63,21,color(225,225,225))


  #on definit la recuperation des coordonnées.
  def get_x(self):
    return self.x
  
  def get_y(self):
    return self.y

  #on definit la sélection puis la déselection
  def selectionner(self):
    fill_rect(x_case_vers_x_sur_l_ecran(self.x),y_case_vers_y_sur_l_ecran(self.y),63,21,color(220,220,220))

  def effacer_la_selection(self):
    fill_rect(x_case_vers_x_sur_l_ecran(self.x),y_case_vers_y_sur_l_ecran(self.y),63,21,color(255,255,255))  



      

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
  if keydown(KEY_DOWN):#↓
    if selecteur.y != 9:
      selecteur.effacer_la_selection()
      selecteur.y = selecteur.y + 1
      selecteur.selectionner()
      sleep(0.1)
      
  elif keydown(KEY_UP):#↑
    if selecteur.y != 1:
      selecteur.effacer_la_selection()
      selecteur.y = selecteur.y - 1
      selecteur.selectionner()
      sleep(0.1)
  
  elif keydown(KEY_LEFT):#←
    if selecteur.x != 1:
      selecteur.effacer_la_selection()
      selecteur.x = selecteur.x - 1
      selecteur.selectionner()
      sleep(0.15)
  
  elif keydown(KEY_RIGHT):#→
    if selecteur.x != 4:
      selecteur.effacer_la_selection()
      selecteur.x = selecteur.x + 1
      selecteur.selectionner()
      sleep(0.15)





  elif keydown(KEY_ZERO):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
    ajout_d_un_caractere("0")
  
  elif keydown(KEY_ONE):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
    ajout_d_un_caractere("1")
  
  elif keydown(KEY_TWO):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
    ajout_d_un_caractere("2")
  
  elif keydown(KEY_THREE):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
    ajout_d_un_caractere("3")
  
  elif keydown(KEY_FOUR):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
    ajout_d_un_caractere("4")
  
  elif keydown(KEY_FIVE):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
    ajout_d_un_caractere("5")
  
  elif keydown(KEY_SIX):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
    ajout_d_un_caractere("6")
  
  elif keydown(KEY_SEVEN):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
    ajout_d_un_caractere("7")
  
  elif keydown(KEY_EIGHT):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
    ajout_d_un_caractere("8")
  
  elif keydown(KEY_NINE):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
    ajout_d_un_caractere("9")
  
  
      
  draw_string(str(selecteur.x)+";"+str(selecteur.y),2,2)
