import re

s = 'PHP123JAVA890PYTHON67GO'

r = re.findall('\D', s, re.I)
print(r)
