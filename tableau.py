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

def y_case_vers_x_sur_l_ecran(y):
  return y*22+1




def selectionner():
  #colorise le rectangle qui est sélectionné
  fill_rect(x_case_vers_x_sur_l_ecran(x_selecteur),y_case_vers_x_sur_l_ecran(y_selecteur),63,21,color(220,220,220))

def effacer_la_selection():
  #efface l'ancienne sélection
  fill_rect(x_case_vers_x_sur_l_ecran(x_selecteur),y_case_vers_x_sur_l_ecran(y_selecteur),63,21,color(255,255,255))  

      

#on initialise le tableau
quadrillage()

#on donne la première position du tableau
x_selecteur = 1
y_selecteur = 1
#on affiche la selection
sel()

while True:
  #on teste les touches de navigation
  if keydown(KEY_DOWN):#↓
    if y_selecteur != 9:
      effacer_la_selection()
      y_selecteur = y_selecteur + 1
      sel()
      sleep(0.1)
      
  elif keydown(KEY_UP):#↑
    if y_selecteur != 1:
      effacer_la_selection()
      y_selecteur = y_selecteur - 1
      sel()
      sleep(0.1)
  
  elif keydown(KEY_LEFT):#←
    if x_selecteur != 1:
      effacer_la_selection()
      x_selecteur = x_selecteur - 1
      sel()
      sleep(0.15)
  
  elif keydown(KEY_RIGHT):#→
    if x_selecteur != 4:
      effacer_la_selection()
      x_selecteur = x_selecteur + 1
      sel()
      sleep(0.15)
   elif keydown(KEY_ONE):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
  
  draw_string(str(x_selecteur)+";"+str(y_selecteur),2,2)
