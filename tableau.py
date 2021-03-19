#importation
from math import *
from kandinsky import *
from ion import *
from time import *

#on dessine le cadre du tableau
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
  #le texte
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

def selectionner():
  fill_rect(x_selecteur,y_selecteur,63,21,color(220,220,220))
      
def quadrillage():
  fill_rect(0,0,320,222,color(255,255,255))
  texte()
  colonnes()
  lignes()

def effacer_la_selection():
  fill_rect(x_selecteur,y_selecteur,63,21,color(255,255,255))  

quadrillage()

x_selecteur = 65
y_selecteur = 23
sel()

while True:
  if keydown(KEY_DOWN):#↓
    if y_selecteur != 199:
      effacer_la_selection()
      y_selecteur = y_selecteur + 22
      sel()
      sleep(0.1)
      
  elif keydown(KEY_UP):#↑
    if y_selecteur != 23:
      effacer_la_selection()
      y_selecteur = y_selecteur - 22
      sel()
      sleep(0.1)
  
  elif keydown(KEY_LEFT):#←
    if x_selecteur != 65:
      effacer_la_selection()
      x_selecteur = x_selecteur - 64
      sel()
      sleep(0.15)
  
  elif keydown(KEY_RIGHT):#→
    if x_selecteur != 257:
      effacer_la_selection()
      x_selecteur = x_selecteur + 64
      sel()
      sleep(0.15)
   elif keydown(KEY_ONE):
    #j'aimerai ici que ca ajoute un au string de la case selectionnée à savoir de coordonnées x, y
  
  draw_string(str(x_selecteur)+";"+str(y_selecteur),2,2)
