from function import submatrix
from meanSetImg import meanSetImg

def setDiffImg(setImg) :
    mean = meanSetImg(setImg)
    setDiff = setImg
    for i in range(len(setImg)) :
        setDiff[i] = submatrix(setDiff[i],mean)
    return setDiff