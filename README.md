# CoBloX Programming Challenge

**Name:** Abdel Rahman Hussein Alharahsheh

**Date:** November 11th, 2019



## Problem Solution

The CardPicker or the Server is Alice. The CardGuesser or the Client is Bob: 

1) Bob send the public key to Alice, so Alice can verify Bob messages.

2) Alice receive the public key

3) Alice pick a card (user input)

4) Alice sign a message contains the picked card (create signature)

5) Alice send the hash of signature to bob

Alice sends only the signature hash because if Bob gets the signature, he can try all the possible cards that verify the signature and guess the card. 

6) Bob receive only the hash of the signature

7) Bob guess a card

8) Bob sign a message contains the guessed card

9) Bob send a message contains the guessed card and the signature.

10) Alice verify the received signature

11) Alice send a message contains the picked card and the signature.

12) Bob verify the received signature

13) Bob verify that the hash of the received signature matches the previous signature hash

14) bob sends confirmation to Alice

15) Alice receive confirmation

16) Alice print the winner

17) Bob prints the winner