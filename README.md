# STEGANOGRAPHY
STEGANOGRAPHY
Definition
Steganography (/ˌstɛɡəˈnɒɡrəfi/ STEG-ə-NOG-rə-fee) is the practice of concealing a file, message, image, or video within another file, message, image, or video. The word steganography comes from New Latin steganographia, which combines the Greek words steganós (στεγανός), meaning "covered or concealed", and -graphia (γραφή) meaning "writing".
Steganography, Wikipedia

The advantage of steganography over cryptography alone is that the intended secret message does not attract attention to itself as an object of scrutiny. Plainly visible encrypted messages, no matter how unbreakable they are, arouse interest and may in themselves be incriminating in countries in which encryption is illegal.
Steganography, Wikipedia

IMAGE STEGANOGRAPHY
Explanation
As the name suggests, Image Steganography refers to the process of hiding data within an image file. The image selected for this purpose is called the cover-image and the image obtained after steganography is called the stego-image.


An image is represented as an N*M (in case of greyscale images) or N*M*3 (in case of colour images) matrix in memory, with each entry representing the intensity value of a pixel. In image steganography, a message is embedded into an image by altering the values of some pixels, which are chosen by an encryption algorithm. The recipient of the image must be aware of the same algorithm in order to known which pixels he or she must select to extract the message.


Detection of the message within the cover-image is done by the process of steganalysis . This can be done through comparison with the cover image, histogram plotting, or by noise detection. While efforts are being invested in developing new algorithms with a greater degree of immunity against such attacks, efforts are also being devoted towards improving existing algorithms for steganalysis, to detect exchange of secret information between terrorists or criminal elements.



Encode the data :
Every byte of data is converted to its 8-bit binary code using ASCII values. Now pixels are read from left to right in a group of 3 containing a total of 9 values. The first 8-values are used to store the binary data. The value is made odd, if 1 occurs and even, if 0 occurs.

Decode the data :
To decode, three pixels are read at a time, till the last value is odd, which means the message is over. Every 3-pixels contain a binary data, which can be extracted by the same encoding logic. If the value if odd the binary bit is 1 else 0.

CIPHERS
Definition
A system of writing that prevents most people from understanding the message.
Cipher, Cambridge Dictionary

In cryptography, a cipher (or cypher) is an algorithm for performing encryption or decryption—a series of well-defined steps that can be followed as a procedure. An alternative, less common term is encipherment. To encipher or encode is to convert information into cipher or code. In common parlance, "cipher" is synonymous with "code", as they are both a set of steps that encrypt a message; however, the concepts are distinct in cryptography, especially classical cryptography.
Cipher, Wikipedia

A cipher is a method of hiding words or text with encryption by replacing original letters with other letters, numbers and symbols through substitution or transposition. A combination of substitution and transposition is also often employed.
Cipher, techopidia

Along the course of history, there were plenty different types of cipher used varying in how they operate or whether they use a single key or multiple keys. Historical chiphers were done using pen and paper and are usually known as classical chiphers. Some examples are the well-known Caesar's cipher or Vigenere's cipher.


Types
Classic:
Caesar Cipher
Vigenere Cipher
ROT13
Scytale
Modern:
Feistel Cipher
RC4
RSA
Enigma Machine's Cipher
Caeser's cipher
In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. The method is named after Julius Caesar, who used it in his private correspondence.

The encryption step performed by a Caesar cipher is often incorporated as part of more complex schemes, such as the Vigenère cipher, and still has modern application in the ROT13 system. As with all single-alphabet substitution ciphers, the Caesar cipher is easily broken and in modern practice offers essentially no communications security.
Caesar Cipher, Wikipedia


Vigenere's Cipher
Vigenère cipher, type of substitution cipher invented by the 16th-century French cryptographer Blaise de Vigenère and used for data encryption in which the original plaintext structure is somewhat concealed in the ciphertext by using several different monoalphabetic substitution ciphers rather than just one; the code key specifies which particular substitution is to be employed for encrypting each plaintext symbol. Such resulting ciphers, known generically as polyalphabetics, have a long history of usage. The systems differ mainly in the way in which the key is used to choose among the collection of monoalphabetic substitution rules.
Vigenere Cipher, Encyclopædia Britannica

Vigenere Cipher is a method of encrypting alphabetic text. It uses a simple form of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution, using multiple substitution alphabets .The encryption of the original text is done using the Vigenère square or Vigenère table.


Reference:
1. https://www.geeksforgeeks.org/image-based-steganography-using-python
2. https://www.npmjs.com/package/file-system
3. https://www.youtube.com/watch?v=A01KtJTv1oc
4. https://github.com/desudesutalk/f5stegojs 
5. https://docs.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-nodejs
