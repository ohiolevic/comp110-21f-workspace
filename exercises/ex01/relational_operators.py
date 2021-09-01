"""Relational Operators"""
__author_ = "730234891"
num: str = input("Left-hand side : ")
num: str = input("Right-hand side : ")
x = 11
y = 5
t1_new = bool(x) < bool(y)
ro = str(t1_new)
print("11 < 5 " + "is " + ro)
t2_new = bool(x) >= bool(y)
r1 = str(t2_new)
print("11 >= 5 " + "is " + r1)
t3_new = bool(x) == bool(y)
r2 = str(t3_new)
print("11 == 5 " + "is " + r2)
t4_new = bool(x) != bool(y)
r3 = str(t4_new )
print("11 != 5 " + "is " + r3)