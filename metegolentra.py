#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  metegolentra.py
#  
#  Copyright 2015 Alumno <alumno@huayra>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import pilasengine

pilas = pilasengine.iniciar()
fondo = pilas.fondos.Fondo()
fondo.imagen = pilas.imagenes.cargar('imagenes/cancha.png')



class Jugador(pilasengine.actores.Actor):

    def iniciar(self):
        self.imagen = 'imagenes/jugador.png'
        self.x = 0
        self.y = -200
        self.figura_de_colision = pilas.fisica.Rectangulo(0,0, 100, 20, False)

    def actualizar(self):
        if self.pilas.control.izquierda:
            self.x -= 5

        elif self.pilas.control.derecha:
            self.x += 5

        if self.x <= -265:
            self.x = -265
        elif self.x >= 265:
            self.x = 265


class Arco(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = 'imagenes/arco.png'
        #~ self.figura_de_colision = pilas.fisica.Rectangulo(0, 0, 60, 30, False)
		

def crear_arco(grupo_arcos, x, y):
    arco = Arco(pilas)
    arco.x = x
    arco.y = y
    grupo_arcos.agregar(arco)


def empujar_pelota(jugador, pelota):
    pelota.empujar((pelota.x - jugador.x) / 5.0, 30)

# Creamos un jugador
jugador = Jugador(pilas)

# El arco es un grupo por si en algún momento 
# el juego cambia y hay dos arcos
arcos = pilas.actores.Grupo()
crear_arco(arcos, 0, 230)

# Ahora se mete la bocha
pelota = pilas.actores.Pelota()
pelota.figura.escala_de_gravedad = 0
pelota.empujar(0, -10)
# La línea siguiente es por si tiramos con el dedo desde el pad
#pelota.aprender(pilas.habilidades.Arrastrable)
pelota.imagen = 'imagenes/pelota.png'
pilas.colisiones.agregar(jugador, pelota, empujar_pelota)
#~ pilas.colisiones.agregar(pelota, arcos, eliminar_arco)
# Para que la bocha no se vaya nunca
#~ pilas.fisica.eliminar_suelo()

pilas.ejecutar()

