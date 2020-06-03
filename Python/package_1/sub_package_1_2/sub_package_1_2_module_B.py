print("----------------------------------------------------------------------------------")
print("sub_sub_package_1_2_1_module_B.py's __name__: {}".format(__name__))
print("sub_sub_package_1_2_1_module_B.py's __package__: {}".format(__package__))

from sub_package_1_1 import sub_package_1_1_module_A
# from sub_package_1_2 import sub_package_1_2_module_A as sub_package_1_2_module_A_en_1_2_B
from sub_package_1_2.sub_sub_package_1_2_1 import sub_sub_package_1_2_1_module_A

var_1_2_B = "sub_package_1_2_module_B"
print(f"var_1_2_B: {var_1_2_B}")


var_1_1_A = var_1_2_B + sub_package_1_1_module_A.var_1_1_A
# var_1_2_A = var_1_2_B + sub_package_1_2_module_A_en_1_2_B.var_1_2_A
var_1_2_1_A = var_1_2_B + sub_sub_package_1_2_1_module_A.var_1_2_1_A

print(f"var_1_1_A: {var_1_1_A}")
# print(f"var_1_2_A: {var_1_2_A}")
print(f"var_1_2_1_A: {var_1_2_1_A}")

