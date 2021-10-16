# PLAYFUL CIPHER

WHAT IS THIS?

The Playful Cipher was started as a learning project. I am currently learning Python 3 and I wanted a fun project to work through instead of just following a set program. Although I am sure I will complete a course of instruction on Python at some point. The playful cipher is a hybrid cipher. Yes, a hybrid cipher is not a technical term however it is two encryption systems put into one system. The first part of the Playful Cipher is a Vigener cipher with the results of the vigenere cipher put through an SHA3 512 algorithm.

"BUT WHY DO THAT?"

When attempting to use online tools like crackstation or Cyber Chef because the results of the vigener are not normal words found in the dictionary, online hash cracking tools can not identify or crack the hash.

"CAN I USE THIS CIPHER TO ENCRYPT MY INFORMATION?

Yes, but I would not recommend it. While online tools such as crackstation and Cyber Chef are not able to crack the hash; tools like hashcat with enough time could eventually crack the hash. The results from hashcat would be the vigenere cipher which if you have enough experience with other forms of encryption easily solved with pen and paper, such as a caesar cipher or a vigenere cipher, you could crack the code.

"OK, SO WHAT CAN I USE THIS CIPHER FOR?"

My recommendation would be for the creation of Capture the Flag challenges where the emphasis is on encryption and cryptography. You could also use the cipher for passing messages between friends if you like using fun ciphers to pass unimportant information between you and a friend.

DECODE WARNING: 
I have not created a tool that will automaticaly decode the cipher. Right now the only way to decode the cipher is by using hashcat and vigenere cipher cracking tool. 
#authors note: This readme file will be updated as necessary.
