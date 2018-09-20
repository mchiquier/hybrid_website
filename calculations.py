import numpy
from numpy.fft import fft2, ifft2, fftshift, ifftshift
from scipy import misc
from scipy import ndimage
import math
import cv2

def scaleSpectrum(A):
   return numpy.real(numpy.log10(numpy.absolute(A) + numpy.ones(A.shape)))


# sample values from a spherical gaussian function from the center of the image
def makeGaussianFilter(numRows, numCols, sigma, highPass=True):
   centerI = int(numRows/2) + 1 if numRows % 2 == 1 else int(numRows/2)
   centerJ = int(numCols/2) + 1 if numCols % 2 == 1 else int(numCols/2)
   
   def gaussian(i,j):
        coefficient = math.exp(-1.0 * ((i - centerI)**2 + (j - centerJ)**2) / (2 * sigma**2))
      
        return 1 - coefficient if highPass else coefficient

   return numpy.array([[gaussian(i,j) for j in range(numCols)] for i in range(numRows)])


def filterDFT(imageMatrix, filterMatrix):
   shiftedDFT = fftshift(fft2(imageMatrix))
   misc.imsave("images/dft.png", scaleSpectrum(shiftedDFT))

   filteredDFT = shiftedDFT * filterMatrix
   misc.imsave("images/filtered-dft.png", scaleSpectrum(filteredDFT))
   return ifft2(ifftshift(filteredDFT))


def lowPass(imageMatrix, sigma):
   n,m = imageMatrix.shape
   return filterDFT(imageMatrix, makeGaussianFilter(n, m, sigma, highPass=False))


def highPass(imageMatrix, sigma):
   n,m = imageMatrix.shape
   return filterDFT(imageMatrix, makeGaussianFilter(n, m, sigma, highPass=True))



def hybridImage(highFreqPath, lowFreqPath, sigmaHigh, sigmaLow):
    highFreqImg = ndimage.imread(highFreqPath, flatten=True)
    lowFreqImg = ndimage.imread(lowFreqPath, flatten=True)
    img = cv2.imread(highFreqPath)
    new = cv2.resize(img, dsize=(450, 450), interpolation=cv2.INTER_CUBIC)
    highPassed = highPass(highFreqImg, sigmaHigh)
    lowPassed = lowPass(lowFreqImg, sigmaLow)
    print("enw")
    print(new)
    return highPassed + lowPassed

if __name__ == "__main__":
   hybrid = hybridImage("uploads/einstein.png", "images/marilyn.png", 25, 10)
   print("ok!!!")
   misc.imsave("images/ok.png", numpy.real(hybrid))
