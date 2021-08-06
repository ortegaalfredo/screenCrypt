# screenCrypt

Encrypt an image using a symmetric key and generate the decryption mask (a paper print, regular 80g white paper works).

# Instructions

You will need python3 with PIL. Additionaly you might need numpy and randomgen packages. Install them with:

```
sudo pip install randomgen numpy
```


## 1) Usage

You will need a black and white 24-bit BMP of any resolution, but close to 100x100 work best on cell phones.


```
$ python3 screenCrypt.py
screenCrypt V0.1 by Alfredo Ortega https://github.com/ortegaalfredo/screenCrypt
Usage: screenCrypt.py <input.bmp> [key seed]
```

The optional key seed is used to encrypt images with the same key mask instead of autogenerating a new one every time. WARNING: Never distribute two encrypted images with the same key mask, as it's trivial to decrypt them by xoring them together.

## 2) Encrypt an image

Encryption is simple, just pass a BMP file as the first argument. The file must be black/white 24-bit with #000000 and #ffffff pixels.


```
$ python3 screenCrypt.py smiley.bmp
screenCrypt V0.1 by Alfredo Ortega https://github.com/ortegaalfredo/screenCrypt
Usage: screenCrypt.py <input.bmp> [key seed]
Loading examples/smiley.bmp
Input: <PIL.BmpImagePlugin.BmpImageFile image mode=RGB size=100x100 at 0x7FFBADCB5DF0>
Saving examples/smiley.bmp-key.bmp
Saving examples/smiley.bmp-encrypted.bmp
```

From the smiley.bmp the utility will generate two images:

 * smiley.bmp-key.bmp: This is the encrypted image that you distribute
 * smiley.bmp-encrypted.bmp: This is the key mask.

You must print the key mask with any color printer in regular white paper and must have the same size as the encrypted image. When laying the mask over the encrypted image on the screen (monitor or cellphone), you will be able to make-out the original image.

## 3) examples:

Original image:

![smiley.bmp](https://github.com/ortegaalfredo/screenCrypt/blob/main/examples/smiley.bmp?raw=true)


Encrypted image:

![smiley.bmp-encrypted.bmp](https://github.com/ortegaalfredo/screenCrypt/blob/main/examples/smiley.bmp-encrypted.bmp?raw=true)

Key mask image:

![smiley.bmp-key.bmp](https://github.com/ortegaalfredo/screenCrypt/blob/main/examples/smiley.bmp-key.bmp?raw=true)

Result (superposition of key over encrypted image):

![combination.jpg](https://github.com/ortegaalfredo/screenCrypt/blob/main/examples/combination.jpg?raw=true)

## 4) Demo video:

[![Demo Video](http://img.youtube.com/vi/OGSKrDhh4Og/0.jpg)](http://www.youtube.com/watch?v=OGSKrDhh4Og "screenCrypt demo")

## 5) Inner working:

The encryption is trivial. It's an one-time pad encryption scheme, with the key mask being the same size as the plaintext. Pseudo-Random generation utilizes the ChaCha algorithm. The algoritm is insecure if you encrypt several images with the same key, but if you generate a different key mask every time, OTP has the strongest provable security. It was inspired by the Monkey Island copy-protection wheel.
