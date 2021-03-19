#importation
from math import *
from kandinsky import *
from ion import *
from time import *

#on dessine le cadre du tableau
def vertic():
  #les colonnes
  xv = 0
  for i in range(6):
    draw_line(xv, 0, xv, 222, color(0,0,0))
    xv = xv + 64

def horyzo():
  #les lignes
  xh = 0
  for i in range(11):
    draw_line(0, xh, 340, xh, color(0,0,0))
    xh = xh + 22
  draw_line(0, 221, 340, 221, color(0,0,0))

def txt():
  #le texte
  xt = 0
  yt = 1
  for i in range(9):
    draw_string(str(yt),2,xt+25)
    xt = xt + 22
    yt = yt + 1
  xt = 0
  yt = 1
  for i in range(4):
    draw_string(str(yt),xt+66,2)
    xt = xt + 64
    yt = yt + 1

def sel():
  fill_rect(xsel,ysel,63,21,color(220,220,220))
      
def quadrillage():
  fill_rect(0,0,320,222,color(255,255,255))
  txt()
  vertic()
  horyzo()

def white():
  fill_rect(xsel,ysel,63,21,color(255,255,255))  

quadrillage()

xsel = 65
ysel = 23
sel()

while True:
  if keydown(KEY_DOWN):
    if ysel != 199:
      white()
      ysel = ysel + 22
      sel()
      sleep(0.1)
      
  if keydown(KEY_UP):
    if ysel != 23:
      white()
      ysel = ysel - 22
      sel()
      sleep(0.1)
  
  if keydown(KEY_LEFT):
    if xsel != 65:
      white()
      xsel = xsel - 64
      sel()
      sleep(0.15)
  
  if keydown(KEY_RIGHT):
    if xsel != 257:
      white()
      xsel = xsel + 64
      sel()
      sleep(0.15)
