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


#~ class Ladrillo(pilasengine.actores.Actor):
#~ 
    #~ def iniciar(self):
        #~ self.imagen = 'imagenes/ladrillo.png'
        #~ self.figura_de_colision = pilas.fisica.Rectangulo(0, 0, 60, 30, False)
		

#~ def crear_ladrillo(grupo_ladrillos, x, y):
    #~ ladrillo = Ladrillo(pilas)
    #~ ladrillo.x = x
    #~ ladrillo.y = y
    #~ grupo_ladrillos.agregar(ladrillo)


#~ def eliminar_ladrillo(pelota, ladrillo):
    #~ ladrillo.eliminar()
#~ 
def empujar_pelota(jugador, pelota):
    pelota.empujar((pelota.x - jugador.x) / 5.0, 30)


jugador = Jugador(pilas)


#~ ladrillos = pilas.actores.Grupo()
#~ 
#~ crear_ladrillo(ladrillos, -200, 100)
#~ crear_ladrillo(ladrillos, -100, 100)
#~ crear_ladrillo(ladrillos,    0, 100)
#~ crear_ladrillo(ladrillos,  100, 100)
#~ crear_ladrillo(ladrillos,  200, 100)

# ladrillos.aprender(pilas.habilidades.Arrastrable)


pelota = pilas.actores.Pelota()
pelota.figura.escala_de_gravedad = 0
pelota.empujar(0, -10)
pelota.aprender(pilas.habilidades.Arrastrable)
pelota.imagen = 'imagenes/pelota.png'

pilas.colisiones.agregar(jugador, pelota, empujar_pelota)
#~ pilas.colisiones.agregar(pelota, ladrillos, eliminar_ladrillo)

#~ pilas.fisica.eliminar_suelo()

pilas.ejecutar()

