# me-return set matriks hasil selisih dari mean set tersebut

import numpy as np
from meanSetImg import meanSetImg

# def setDiffImg(setImg, mean) :
#     setDiff = []
#     print(len(setImg))
#     for i in range(len(setImg)) :
#         setDiff[i] = np.absolute(np.subtract(setDiff[i],mean))
#     return setDiff

def setDiffImg(setImg, mean) :
    setDiff = []
  
    for i in range(len(setImg)) :
        setDiff.append(np.absolute(np.subtract(setImg[i],mean)))
    return setDiff
