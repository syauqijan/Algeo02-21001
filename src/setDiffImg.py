# me-return set matriks hasil selisih dari mean set tersebut

from function import abssubmatrix
from meanSetImg import meanSetImg

def setDiffImg(setImg) :
    mean = meanSetImg(setImg)
    setDiff = setImg
    for i in range(len(setImg)) :
        setDiff[i] = abssubmatrix(setDiff[i],mean)
    return setDiff