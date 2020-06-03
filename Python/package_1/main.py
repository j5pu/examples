#!/usr/bin/env python3
print("----------------------------------------------------------------------------------")
print("main.py's __name__: {}".format(__name__))
print("main.py's __package__: {}".format(__package__))

from sub_package_1_1.sub_package_1_1_module_A import var_1_1_A
from sub_package_1_2.sub_package_1_2_module_A import var_1_2_A
from sub_package_1_2.sub_package_1_2_module_B import var_1_2_B
from sub_package_1_2.sub_sub_package_1_2_1 import sub_sub_package_1_2_1_module_A

var_1_main = "package_1_module_main"
print(f"var_1_main: {var_1_main}")

var_1_1_A = var_1_main + var_1_1_A
var_1_2_A = var_1_main + var_1_2_A
var_1_2_B = var_1_main + var_1_2_B
var_1_2_1_A = var_1_main + sub_sub_package_1_2_1_module_A.var_1_2_1_A

print(f"var_1_1_A: {var_1_1_A}")
print(f"var_1_2_A: {var_1_2_A}")
print(f"var_1_2_B: {var_1_2_B}")
print(f"var_1_2_1_A: {var_1_2_1_A}")

if __name__ == "__main__" and __package__ is None:
     print(var_1_1_A)
     print(var_1_2_A)
     print(var_1_2_B)
     print(var_1_2_1_A)
