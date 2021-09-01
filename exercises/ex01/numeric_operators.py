"""Numeric Operators"""
__author__ = "730234891"
num_1: str = input("Left-hand side : ")
num_2: str = input("Right-hand side : ")
x = 11
y = 5
t1_new = int(x)**int(y)
ro = str(t1_new)
print("11 ** 5 " + "is " + ro)
t2_new = int(x) / int(y)
r1 = str(t2_new)
print("11 / 5 " + "is " + r1)
t3_new = int(x) // int(y)
r2 = str(t3_new)
print("11 // 5 " + "is " + r2)
t4_new = int(x) % int(y)
r3 = str(t4_new)
print("11 % 5 " + "is " + r3)