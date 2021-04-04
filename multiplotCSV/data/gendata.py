# #!/usr/bin/env python
# -*- coding: utf-8 -*-

# script permettant de générer des données artificielles

from random import randint

for i in range(20):
	print str(i)+","+str(i+randint(0,3))+","+str(i+4+randint(-1,2))
