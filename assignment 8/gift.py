import os
import imageio
import numpy as np
n=sorted(os.listdir("New folder (8)"))
ima=[]
for i in n:
    path="New folder (8)/"+i
    c=imageio.imread(path)
    ima.append(c)
imageio.mimsave("out.gif",ima)
