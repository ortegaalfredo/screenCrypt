import sys
import numpy as np
from randomgen import ChaCha
from PIL import Image

print("screenCrypt V0.1 by Alfredo Ortega https://github.com/ortegaalfredo/screenCrypt")
print("Usage: %s <input.bmp> [key seed]" % sys.argv[0])
if len(sys.argv)<2:
    exit(0)

#Load plaintext image
imagefile=sys.argv[1]
print("Loading %s" % imagefile)
plain = Image.open(imagefile)
print("Input: "+repr(plain))
plainp = plain.load() # Load plaintext image
#Create encrypted image
crypt = Image.new( 'RGB', (plain.size[0],plain.size[1]), "white") 
cryptp = crypt.load() 
#Create key image
key   = Image.new( 'RGB', (plain.size[0],plain.size[1]), "white") 
keyp = key.load() 


#Read optional seed
if len(sys.argv)>2:
    seed=int(sys.argv[2])
    print("Using seed: %d WARNING: Never use the same key mask twice." % seed)
    rg = np.random.Generator(ChaCha(seed=seed, rounds=8))
else:
    rg = np.random.Generator(ChaCha())

#Color constants
whitePixel=(255,255,255)
blackPixel=(0,0,0)
encryptedBlack=(0,0,255) 
keyBlack=(160,160,0)

#generate key image and xor
for i in range(crypt.size[0]):    # for every col:
    for j in range(crypt.size[1]):    # For every row
        # Draw a black border, useful for alignment
        if i==0 or j==0 or i==crypt.size[0]-1 or j==crypt.size[1]-1:
            keyp[i,j]=cryptp[i,j]=blackPixel
            continue
        # Xor pixel with key stream
        keybit=rg.integers(0,2)
        plainbit=0 if plainp[i,j][0]==0 else 1
        cryptbit = keybit ^ plainbit
        keyp[i,j]=keyBlack if keybit==0 else whitePixel
        cryptp[i,j]=encryptedBlack if cryptbit==0 else whitePixel

# Save key image
keyname="%s-key.bmp" % imagefile
print("Saving %s" % keyname)
key.resize((plain.size[0]*5,plain.size[1]*5),Image.NEAREST).save(keyname)
# Save encrypted image
encryptedname="%s-encrypted.bmp" % imagefile
print("Saving %s" % encryptedname)
crypt.resize((plain.size[0]*5,plain.size[1]*5),Image.NEAREST).save(encryptedname)
