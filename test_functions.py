from main import *

print(BSOption('P', 100, 100, 0.5, 0.05, 0.40).delta())
print(BSOption('C', 100, 100, 1, 0.05, 0.15).price())
print(BSOption('P', 100, 100, 0.5, 0.05, 0.40).gamma())
print(BSOption('C', 100, 100, 0.5, 0.05, 0.40).theta())
print(BSOption('C', 100, 100, 0.5, 0.05, 0.40).theta_bis())