import re


croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

inputs = input()

for i in range(len(croatia)):
    inputs = inputs.replace(croatia[i], '#')

# for i in range(len(croatia)):
#     inputs = re.sub(croatia[i], '#', inputs)

print(inputs)
print(len(inputs))