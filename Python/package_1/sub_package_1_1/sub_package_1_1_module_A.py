print("----------------------------------------------------------------------------------")
print("sub_package_1_1_module_A.py's __name__: {}".format(__name__))
print("sub_package_1_1_module_A.py's __package__: {}".format(__package__))


# from sub_package_1_2 import sub_package_1_2_module_A as sub_package_1_2_module_A_en_1_1_A
# from sub_package_1_2.sub_package_1_2_module_B import var_1_2_B as var_1_2_B_en_1_1_A
from sub_package_1_2.sub_sub_package_1_2_1 import sub_sub_package_1_2_1_module_A

var_1_1_A = "sub_package_1_1_module_A"
print(f"var_1_1_A {var_1_1_A}")

# var_1_2_A = var_1_1_A + sub_package_1_2_module_A_en_1_1_A.var_1_2_A
# var_1_2_B = var_1_1_A + var_1_2_B_en_1_1_A
var_1_2_1_A = var_1_1_A + sub_sub_package_1_2_1_module_A.var_1_2_1_A

# print(f"var_1_2_A: {var_1_2_A}")
# print(f"var_1_2_B: {var_1_2_B}")
print(f"var_1_2_1_A: {var_1_2_1_A}")