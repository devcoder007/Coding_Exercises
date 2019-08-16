Fecth out the integers without hyphen and integers
import re


str = "11-22-33-44 trdtyj yutuyik"

d=(re.findall('\d+',str))
print(''.join(d))
