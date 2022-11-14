# me-return set matriks hasil selisih dari mean set tersebut

import numpy as np
from meanSetImg import meanSetImg

def setDiffImg(setImg) :
    mean = meanSetImg(setImg)
    setDiff = setImg
    for i in range(len(setImg)) :
        setDiff[i] = np.absolute(np.subtract(setDiff[i],mean))
    return setDiff