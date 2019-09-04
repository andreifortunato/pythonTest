# -*- coding:utf-8 -*-

from math import sqrt
a = input("Dê um valor para a:")
b = input("Dê um valor para b:")
c = input("Dê um valor para c:")

delta = b**2-4*a*c
raiz_delta = sqrt(delta)

x1 =(-b + raiz_delta)/(2*a)
x2 =(-b - raiz_delta)/(2*a)

print("x1 =%d" %x1)
print("x2 =%d" %x2)