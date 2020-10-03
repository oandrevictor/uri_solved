# -*- coding: utf-8 -*-

categorias = {}
vertebrado = {}
invertebrado = {}
ave = {}
mamifero = {}
inseto = {}
anelideo = {}

categorias["vertebrado"] = vertebrado
categorias["invertebrado"] = invertebrado

vertebrado["ave"] = ave
vertebrado["mamifero"] = mamifero

invertebrado["inseto"] = inseto
invertebrado["anelideo"] = anelideo

ave["carnivoro"] = "aguia"
ave["onivoro"] = "pomba"

mamifero["onivoro"] = "homem"
mamifero["herbivoro"] = "vaca"

inseto["hematofago"] = "pulga"
inseto["herbivoro"] = "lagarta"

anelideo["hematofago"] = "sanguessuga"
anelideo["onivoro"] = "minhoca"

c1 = raw_input()
c2 = raw_input()
c3 = raw_input()

print categorias.get(c1).get(c2).get(c3)