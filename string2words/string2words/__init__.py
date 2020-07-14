import ctypes
import os

gDLL = ctypes.CDLL(os.path.split(__file__)[0]+'/encodeDecode.so')

def encode(inputString):
   asciiBuffer = [ord(ch) for ch in inputString]
   while (len(asciiBuffer) % 4) != 0:
      asciiBuffer.append(0)
   encodedWords = []
   for i in range(0,len(asciiBuffer),4):
      inputWord = asciiBuffer[i+3] << 24 | \
               asciiBuffer[i+2] << 16 | \
               asciiBuffer[i+1] << 8 | \
               asciiBuffer[i]
      encodedWords.append(gDLL.encodeWord(inputWord))
   return encodedWords
   
def decode(wordBuffer):
   decodedChars = ""
   for word in wordBuffer:
      decoded = gDLL.decodeWord(word)
      decodedChars += chr((decoded & 0x000000FF))
      decodedChars += chr((decoded & 0x0000FF00) >> 8)
      decodedChars += chr((decoded & 0x00FF0000) >> 16)
      decodedChars += chr((decoded & 0xFF000000) >> 24)      
   return decodedChars.strip('\x00')
