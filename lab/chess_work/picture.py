from ntpath import join
from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    new = []
    num = len(self.img) - 1
    while (num >= 0):
      new.append(self.img[num])
      num = num - 1
    return new

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    new = []
    num = 0
    for x in self.img:
      str = self.img[num]
      reversed = []
      i = len(str)
      while i > 0: 
        reversed += str[i-1]
        i = i - 1
      num = num + 1
      str = "".join(reversed)
      new.append(str)
    return new

  def negative(self):
    """ Devuelve un negativo de la imagen """
    return Picture(None)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    new = []
    num = 0
    for x in self.img:
      new.append(self.img[num])
      new[num] = new[num] + p.img[num] 
      num = num + 1
    return new

  def up(self, p):
    """ Devuelve una nueva figura poniendo la figura p debajo de la
        figura actual """
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    new = []
    num = 0
    for x in self.img:
      new.append(self.img[num])
      iter = 0
      while(iter < n-1):
        new[num] = new[num] + self.img[num] 
        iter = iter +1
      num = num + 1
    return new

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual por debajo de
        la cantidad de veces que indique el valor de n """
    new = []
    iter = 0
    while(iter < n):
      num = 0
      for x in self.img:
        new.append(self.img[num])
        num = num + 1
      iter = iter + 1
    return new

  #Extra: Sólo para realmente viciosos 
  def rotate(self):
    """Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario"""
    return Picture(None)

