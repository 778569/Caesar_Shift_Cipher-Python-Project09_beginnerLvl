# Caesar_Shift_Cipher-Python-Project

## Usage
The Shift (or Caesar) Cipher is another monoalphabetic substitution cipher. Although more secure than the Atbash Cipher, it is still an easy cipher to break, especially by today's standards. Originally, it was used by Julius Caesar for sending encrypted messages to his troops, as recorded by Suetonius

*If he had anything confidential to say, he wrote it in cipher, that is, by so changing the order of the letters of the alphabet, that not a word could be made out. If anyone wishes to decipher these, and get at their meaning, he must substitute the fourth letter of the alphabet, namely D, for A, and so with the others.
(Suetonius, The Twelve Caesars)*

This describes what we would now call a shift of 3, and describes the cipher that Caesar used quite well. That is, "a" was encrypted as "D", "b" as "E", etc. The table below gives the plaintext alphabet and the ciphertext alphabet to show how a shift of 3 could be depicted.
Picture

![190935_orig](https://github.com/778569/Caesar_Shift_Cipher-Python-Project/assets/52319671/f4a20fa0-0320-47c1-bf09-04d6e5805610)

A Caesar Shift of 3. This was the key that Caesar himself used.
For a Caesar shift we have a key, which makes the cipher stronger than the Atbash Cipher. The key is the number by which we shift the alphabet, since this provides a unique way to describe the ciphertext alphabet easily.

##Encryption
Encryption using the Shift Cipher is very easy. First we must create the ciphertext alphabet, which as discussed above is simply found by 'shifting' the alphabet to the left by the number of places given by the key. Thus a shift of 1 moves "A" to the end of the ciphertext alphabet, and "B" to the left one place into the first position. As the key gets bigger, the letters shift further along, until we get to a shift of 26, when "A" has found it's way back to the front. We have already seen a shift of 3 in  the table above, and below we have a shift of 15.
Picture
![5567092_orig](https://github.com/778569/Caesar_Shift_Cipher-Python-Project/assets/52319671/9527e70c-ddc3-4c6a-8eb0-c40020413f06)

The ciphertext alphabet for a Sihft of 15.
Once we have created the table, the encryption process is easy, as we just replace each occurence within the plaintext of a letter with the corresponding ciphertext letter as given by the ciphertext alphabet. Hence, if we wanted to encrypt the plaintext "julius caesar" with the key he himself used, namely 3, we look along the plaintext alphabet row in the first table to find "j", and note that this encrypts to "M". We then look for "u", and take the ciphertext letter "X". Continuing in this way, we finally encrypt to "MXOLXV FDHVDU".
##Decryption
Decryption by the intended recipient of a ciphertext received that has been encrypted using the Shift Cipher is also very simple. One can either use the table already created above, and find each letter of the ciphertext in the bottom row, and replace with the corresponding plaintext letter directly above it, or the recipient could create the inverse table, with the ciphertext alphabet on top, and using a shift of -3 on it, which gives the table below.
Picture
![5906642_orig](https://github.com/778569/Caesar_Shift_Cipher-Python-Project/assets/52319671/cf55d8ad-7be0-4897-a997-836283decc18)


To decrypt a message encoded with a Shift of 3, generate the plaintext alphabet using a shift of -3.
Clearly, the encryption table and its inverse are the same as each other, only reordered. If we have received the ciphertext "PDUFXV EUXWXV", and we know that it has been enciphered using the key 3, then we can use the table to decipher the message. We see that  "P" represents the plaintext letter  "m",  "D" represents  "a" and so on. Continuing in this way we retrieve the plaintext  "marcus brutus", the name of the famous conspiritor in the assassination of Julius Caesar.

## Installation

1. Clone this repository.
2. Navigate to the project directory.
3. Run the program using Python 3.x:


