# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 23:43:22 2021

@author: sarah sakinah
"""
print("@@@@ @@@ @@@@ @@@  @ @")
print("@    @ @ @  @ @ @  @ @")
print("@    @@@ @@@@ @@@  @ @")
print("@@@@ @@@ @@   @ @  @@@")
print("   @ @ @ @ @  @ @  @ @")
print("   @ @ @ @  @ @ @  @ @")
print("@@@@ @ @ @   @@ @  @ @")
def hitung_jarak_tempuh(kecepatan_awal,waktu, percepatan):
    jarak_tempuh=(v0*t)+(0.5*(a*t**2))
    print("kecepatan awal=",v0,"waktu=",t,"dan percepatan:",a,"hasil",jarak_tempuh)
    return jarak_tempuh

v0=int(input("masukkan v0: "))
t=int(input("masukkan t: "))
a=int(input("masukkan a: "))
hitung_jarak_tempuh(v0,t,a)
