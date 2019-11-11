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

7) Bob guess a card (user input)

8) Bob sign a message contains the guessed card

9) Bob send a message contains the guessed card and the signature.

10) Alice verify the received signature

11 Alice decide what car to reveal (user input)

12) Alice send a message contains the revealed card and the signature.

13) Bob verify the received signature

14) Bob verify that the hash of the received signature matches the previous signature hash

15) bob sends confirmation or rejection to Alice

16) Alice receive response

17) Alice print the winner

18) Bob prints the winner



### How to execute the code

Just run the `card_picker_exec.py` and then run the `card_guesser_exec.py` in your terminal. 

if you would like to change the name of the players or add/remove new cards. you can configure that in `library/config.py` . or if you would like to change the host or the port of the server `executables/config.py`



## Output Examples:

#### Example 1: Alice Wins fairly

**Alice Terminal:**

```cmd
Bob => Alice: {"message": "I am Bob, please receive my public_key", "name": "Bob", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAm+IkfQfM1FtmJFx4a8dy\nx8S9zA3pbSoqkqbA8suKTWLAlR5qZ2aPD5EyAodK+pznIgQ2bj3R8+9nIP3UidPf\nStg1qEIQyOoliOMDYxlCCT0+vbsgaAyvYT+PC3+sidEyWPfXmR2Bcn8oGj0uvjI2\n0Dd4OWWV9Y2LbU7At8dYYDYPVx30RPri8Bntv+U3lZK3zehfbkRY4grmd+JcM02J\nrBfyIcS5jSE6twDt59c9d3xjQq5x47TATMefxL63/26jIiO6Nt8VsIqJgC1k/nox\nqWObACXx2xo8ewsqwhBMI0uJlR6M80NM/nRPMzpT/Eh1uYFp7+jJsSqNfjcZK7d6\nC4DfnWoSEpGqVMvzLo6ylPcD43pQBTLthNwTNXCmzHkR273lXX/B/8yKMZEJN0CW\naJa9Mh4tV4yRIaTK2a3oyv63F09QwOSuZx9qBzWrwzwJHP7MPBi8IXMrOtd3GPle\n4pRkAsvu1/YLyf7YXPAkR+w9gSGOYeI8cHFujnAOEHiUGvGQNi/TWi6UNyw1Zutb\nRSN81dfvrPuP33ASL8uqtktv5FxJw98x1obSffJ/NyBa7wOpTj2EVGu9a0bBIIf+\nnVPjKAsrHIfdffqcG0Rva2A8h6S/DKURe4V6aXGbJg4lRKz61H9Ec5bGM7hbQb4h\nYTbH9dItdOKQWl0kXnmihFcCAwEAAQ==\n-----END PUBLIC KEY-----\n"}

Pick a card -> cards:('queen', 'king') (please enter a number from 0 to 1): 1

Alice => Bob: {"message": "I've chosen my card, I have revealed the hash of my signature so you can validate my honesty", "signature_hash": "n8Es+L6zmdKO7da9qhOhl9/c3x4Aa5crb8rxMsbsOjI="}

Bob is guessing a card...

Bob => Alice: {"message": "I guess the card is queen", "guessed_card": "queen", "signature": "IS+pLgET4kalPfL9QUN6XBBb07ZIFN/p44NyUmkxuY+Wrat1uiPO7zhmawoNXKDx0lkIFKciM/xD\nSTsXxpuYK7b4P7LsaFk/lE3b0RpVKJ0KaSZBS3MLwuFMjebGGO5hXHq6/SFeCnh00VyVXaGzGCBi\naaYZKwj1bmVSnsksNAYTXDVkwN72AbkAI6QPLIn1tLWuE7nHhXtYz9LwE00Ff1NyRhlDhLwhXo+t\noqN/zS8qi4+ai5Yt/ERCliTDSXthJdrP56DmuY0HATG/uDd4exhC4VIkJoTRr4kjKxaiK27Mbvvk\no3VxHtNdLtkiAWOSx/GGE53CG2zkLRW3MZA3D5Xo/5wJHyTSUYY9emtn1Slryye9P3d1qR9+qU1A\nh/rB0QYXAiQFeImoRpZaZSEU7GfUsWdFT2QziK0ovsZfs4VNCmNqyhro8wnfZ1jh4wYtF4/LKong\nn8dgOEE1LITIcUj+qGJ38+t/59zIcEWCGBc2XQKR88VNX7Ei/SCnFYm559XiqBA385sQqQ0YbE+D\nu9XjYIJEyZYdq8d9wUDWz1AkTSStM0RGQecNg0XMG/7OS3F3qmzgeztYzl7h3AtnDZhjFB3ZvagR\nNOTkcSzMRIr+nP+W4NNHuAQvn4OmSrAeNjS174EhtWCReOCIj1ggCrJnXfvM/j31ScdFKtNsQcU=\n"}

What card do you want to reveal? -> cards:('queen', 'king') (please enter a number from 0 to 1): 1

Alice => Bob: {"message": "The Card I have chosen is: king", "card": "king", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA0RJBCRtIu2ac7Uf4+sSU\ntmcWTMYckOPCrzF917J85Bx4mwWGOHZ2CisKuFB9FxP+doChE3KWkDOflOaod6/d\nKL5DdGh805wkAvJK5BK94JRDxMm/KFugDgKayewQ5JlZfl2PYxdgsxiwgpHWEsBU\n8AFHP5yjA8Z7OhAl3h/rsnS2lmoinfP7X/7ZMYIfpSYIIMXJDI9UEQQ+MGZs5e+F\npYRNTo2MCxla5hoIU8cTjNaGns6P+KZG+Gs/C/WFn264bmybz11kglG33wKA3DOB\nVhBVXz0LsGpOff3Djt4Y+938a1NNCl+dVSUXETE9eVc1ApnmCYmcBXyCbYjG5K6j\nmenl7wP55dqz/uydjg9ZsdYQEby7Ep4q1qLsPmndHWI1lQe2KxOs/UuSB1mGtUDV\nnrmJCaZAiwpwxIobP3sLOUiiM+YPy1pocXaHS0AB0goflS8qxHaHDvwWeTspdGmU\ntWCgx5FI5ckj+eOJ+D4EdmNO2Khj1WV47pHcM/8WyF8feB7fO7bKbfloJSI2F7PV\nUiC8fMDAjW/4VYQIRKeD3BSLQNlJ1oF8eucE5DCZmlm1a+wBTsninQ3bIofsbE5g\nUa+3WycEKa+9gT2ghqoYk2RLlQ6BPvMTk+wAFQLOgeo0Xre22lCBmaYNfuj31zD2\nPBVwMJCMT+6koL5kGvzSHX8CAwEAAQ==\n-----END PUBLIC KEY-----\n", "signature": "esvOddpn0fc6iADzd2obwAX1b0Ta758TsOYK75tiEGo7BcshYGNuBDbC4Yaphwr6eWPk1kk8XUux\nUdDZYIn+K0t8VfLgC8Y+uspSAb3bE2emIF/bhmI15MShYDksGocDMrpjwX/6nuL5QwUj6au6GG8f\nh85+ycVGDIdjZG18wqPpgypk/KQVu+LgqnsBoyI2BS7mfECk6243AkO/NI4+15kvj7Ak6fpk4Lgs\nIqus9cRqwirpEPsGLDX/uBAbGTaY6Wlr8/5r+lSjWH4sbY5J1lyhMuisvmuVTSfeEzVJdoFGsFJP\nUkSjd0JQmq+EQrNoH++K88szGqFUqzfGECh6Fi2/6HZNeqCsr2Fab9HUpFmT1ibG1Eaku3qowrJk\nGgPkrAA2rGOssGqlZr5bpTMW0mVIvJDW17LqrR9EnOROYsWMBfiG63pBvURPIe9UYiWG9mmsL0be\niYcsoFE5qb+Db4Qga/fhbcUGXos2YlMhPILIsv9LpFj2aguDzZ/RCPupdyj4veeRQipYstr9egX2\njKat5PuLtsKRw/VCArqIYfWDACCxpOnif4D6hbLvp4mfn0qu9OItPIedF0L8jtZOl6rIglmEnAx0\n2HhNNR9VLGYzBAlke0X0Gz+4BTTu0odYJQrLIlPHFTPi+tfZHHSXFgGYiKQ96Xg3feWeik9HJdI=\n"}

Bob => Alice: {"message": true}

Alice Wins!
```

**Bob Terminal:**

```cmd
Bob => Alice: {"message": "I am Bob, please receive my public_key", "name": "Bob", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAm+IkfQfM1FtmJFx4a8dy\nx8S9zA3pbSoqkqbA8suKTWLAlR5qZ2aPD5EyAodK+pznIgQ2bj3R8+9nIP3UidPf\nStg1qEIQyOoliOMDYxlCCT0+vbsgaAyvYT+PC3+sidEyWPfXmR2Bcn8oGj0uvjI2\n0Dd4OWWV9Y2LbU7At8dYYDYPVx30RPri8Bntv+U3lZK3zehfbkRY4grmd+JcM02J\nrBfyIcS5jSE6twDt59c9d3xjQq5x47TATMefxL63/26jIiO6Nt8VsIqJgC1k/nox\nqWObACXx2xo8ewsqwhBMI0uJlR6M80NM/nRPMzpT/Eh1uYFp7+jJsSqNfjcZK7d6\nC4DfnWoSEpGqVMvzLo6ylPcD43pQBTLthNwTNXCmzHkR273lXX/B/8yKMZEJN0CW\naJa9Mh4tV4yRIaTK2a3oyv63F09QwOSuZx9qBzWrwzwJHP7MPBi8IXMrOtd3GPle\n4pRkAsvu1/YLyf7YXPAkR+w9gSGOYeI8cHFujnAOEHiUGvGQNi/TWi6UNyw1Zutb\nRSN81dfvrPuP33ASL8uqtktv5FxJw98x1obSffJ/NyBa7wOpTj2EVGu9a0bBIIf+\nnVPjKAsrHIfdffqcG0Rva2A8h6S/DKURe4V6aXGbJg4lRKz61H9Ec5bGM7hbQb4h\nYTbH9dItdOKQWl0kXnmihFcCAwEAAQ==\n-----END PUBLIC KEY-----\n"}

Alice is picking a card...

Alice => Bob: {"message": "I've chosen my card, I have revealed the hash of my signature so you can validate my honesty", "signature_hash": "n8Es+L6zmdKO7da9qhOhl9/c3x4Aa5crb8rxMsbsOjI="}

Guess what is the card that Alice has picked -> cards:('queen', 'king') (please enter a number from 0 to 1): 0

Bob => Alice: {"message": "I guess the card is queen", "guessed_card": "queen", "signature": "IS+pLgET4kalPfL9QUN6XBBb07ZIFN/p44NyUmkxuY+Wrat1uiPO7zhmawoNXKDx0lkIFKciM/xD\nSTsXxpuYK7b4P7LsaFk/lE3b0RpVKJ0KaSZBS3MLwuFMjebGGO5hXHq6/SFeCnh00VyVXaGzGCBi\naaYZKwj1bmVSnsksNAYTXDVkwN72AbkAI6QPLIn1tLWuE7nHhXtYz9LwE00Ff1NyRhlDhLwhXo+t\noqN/zS8qi4+ai5Yt/ERCliTDSXthJdrP56DmuY0HATG/uDd4exhC4VIkJoTRr4kjKxaiK27Mbvvk\no3VxHtNdLtkiAWOSx/GGE53CG2zkLRW3MZA3D5Xo/5wJHyTSUYY9emtn1Slryye9P3d1qR9+qU1A\nh/rB0QYXAiQFeImoRpZaZSEU7GfUsWdFT2QziK0ovsZfs4VNCmNqyhro8wnfZ1jh4wYtF4/LKong\nn8dgOEE1LITIcUj+qGJ38+t/59zIcEWCGBc2XQKR88VNX7Ei/SCnFYm559XiqBA385sQqQ0YbE+D\nu9XjYIJEyZYdq8d9wUDWz1AkTSStM0RGQecNg0XMG/7OS3F3qmzgeztYzl7h3AtnDZhjFB3ZvagR\nNOTkcSzMRIr+nP+W4NNHuAQvn4OmSrAeNjS174EhtWCReOCIj1ggCrJnXfvM/j31ScdFKtNsQcU=\n"}

Alice is asking you to wait :) ...

Alice => Bob: {"message": "The Card I have chosen is: king", "card": "king", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA0RJBCRtIu2ac7Uf4+sSU\ntmcWTMYckOPCrzF917J85Bx4mwWGOHZ2CisKuFB9FxP+doChE3KWkDOflOaod6/d\nKL5DdGh805wkAvJK5BK94JRDxMm/KFugDgKayewQ5JlZfl2PYxdgsxiwgpHWEsBU\n8AFHP5yjA8Z7OhAl3h/rsnS2lmoinfP7X/7ZMYIfpSYIIMXJDI9UEQQ+MGZs5e+F\npYRNTo2MCxla5hoIU8cTjNaGns6P+KZG+Gs/C/WFn264bmybz11kglG33wKA3DOB\nVhBVXz0LsGpOff3Djt4Y+938a1NNCl+dVSUXETE9eVc1ApnmCYmcBXyCbYjG5K6j\nmenl7wP55dqz/uydjg9ZsdYQEby7Ep4q1qLsPmndHWI1lQe2KxOs/UuSB1mGtUDV\nnrmJCaZAiwpwxIobP3sLOUiiM+YPy1pocXaHS0AB0goflS8qxHaHDvwWeTspdGmU\ntWCgx5FI5ckj+eOJ+D4EdmNO2Khj1WV47pHcM/8WyF8feB7fO7bKbfloJSI2F7PV\nUiC8fMDAjW/4VYQIRKeD3BSLQNlJ1oF8eucE5DCZmlm1a+wBTsninQ3bIofsbE5g\nUa+3WycEKa+9gT2ghqoYk2RLlQ6BPvMTk+wAFQLOgeo0Xre22lCBmaYNfuj31zD2\nPBVwMJCMT+6koL5kGvzSHX8CAwEAAQ==\n-----END PUBLIC KEY-----\n", "signature": "esvOddpn0fc6iADzd2obwAX1b0Ta758TsOYK75tiEGo7BcshYGNuBDbC4Yaphwr6eWPk1kk8XUux\nUdDZYIn+K0t8VfLgC8Y+uspSAb3bE2emIF/bhmI15MShYDksGocDMrpjwX/6nuL5QwUj6au6GG8f\nh85+ycVGDIdjZG18wqPpgypk/KQVu+LgqnsBoyI2BS7mfECk6243AkO/NI4+15kvj7Ak6fpk4Lgs\nIqus9cRqwirpEPsGLDX/uBAbGTaY6Wlr8/5r+lSjWH4sbY5J1lyhMuisvmuVTSfeEzVJdoFGsFJP\nUkSjd0JQmq+EQrNoH++K88szGqFUqzfGECh6Fi2/6HZNeqCsr2Fab9HUpFmT1ibG1Eaku3qowrJk\nGgPkrAA2rGOssGqlZr5bpTMW0mVIvJDW17LqrR9EnOROYsWMBfiG63pBvURPIe9UYiWG9mmsL0be\niYcsoFE5qb+Db4Qga/fhbcUGXos2YlMhPILIsv9LpFj2aguDzZ/RCPupdyj4veeRQipYstr9egX2\njKat5PuLtsKRw/VCArqIYfWDACCxpOnif4D6hbLvp4mfn0qu9OItPIedF0L8jtZOl6rIglmEnAx0\n2HhNNR9VLGYzBAlke0X0Gz+4BTTu0odYJQrLIlPHFTPi+tfZHHSXFgGYiKQ96Xg3feWeik9HJdI=\n"}

Bob => Alice: {"message": true}

Alice Wins!

```

#### Example 2: Bob wins fairly

**Alice Terminal:**

```cmd
Bob => Alice: {"message": "I am Bob, please receive my public_key", "name": "Bob", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAzH0QE0KgK7YLkyJy9Frz\nT9gV5WPcb6D0I6yx3sJu6iHoOSHgvD7Ij2WisEccfJmoQLEeTiJJJOHZJo3De9Pi\nT6nmp+xnDzJHRQNoXBsrO016U53IpXiuVnkTthZsk5f9I+Y4OrK1kPKu2aLZK7ab\nybfZD1V88/tsfh+r3oDCjkphC2v5ThAQugONEa1pXqridFotLpE0PefF9xaj2TM6\nqSX1fzmYWa/4T9Ht7gZ5pPS36wyWsCHw83JCqNxh1VjRriSFoUQFfSqXHCb9AWLM\noJJT85xUEaLRm49Lky6gwSzWfLuyFG8ezLuTERNWlc6dpFdF27UXWw6D2D3n9VMX\ntBDL0BchwioYOM04CsdmWpJlFmJWqLOPvGiBVMO4HsHYjBw0EDV+hehhHOUxI0Mf\neMZpuNAP1yLPp66am145P9ndo2pOGw7sDIG3nBLMVU50cpnlfENdioWDpyTo8CA2\nDXe7qlnUaTYOqjmo9ZGk2QpvFiYm7AUrCvm8UIrIA8ZUhtkeupUBJv4F5O7xEEAp\nJ9HjEWaYl8xXmqZLnFPf3kuo9JDrI5ILPAPcULdkhU5EJo3ibfCf+/gTqW5mWYMQ\n18lBXC6LvbnY9WmvqhRQsC5QPr2FEBPJg5a103xXcMGM+izIpR3yJ2y2c30X4PD9\nS6SWieyupXuhizQ6WEMuhiECAwEAAQ==\n-----END PUBLIC KEY-----\n"}

Pick a card -> cards:('queen', 'king') (please enter a number from 0 to 1): 0

Alice => Bob: {"message": "I've chosen my card, I have revealed the hash of my signature so you can validate my honesty", "signature_hash": "JBeZZRbOdoGUCm+Ptg9DvtHFZRYFvMYJrD6Q62hjXRE="}

Bob is guessing a card...

Bob => Alice: {"message": "I guess the card is queen", "guessed_card": "queen", "signature": "DCh3JKJWC4afO86ptNB+z7Ufl5S2g7sVLn/NvcWmtn6X4hjXGEKF4XLIQXGjHbhrDgdawpP5Br6w\nI581gBYEAAk+BLm9ZnPlwp21cinrcBx3J15i1szKh5c0JS7FCzdS71PjAw0tDcv5tZJWmwp7ybfi\nr31uekcqY+mAHQmy9zQVzuBzE+PckDiFIbEYp8DWF20tcQ6aSslBw20TnmrYft/jDA6Z+z2z6yPb\nMJTvJuKcUaaWCiMq5aIanzUFyUC7bgnrSY6oO6VUK0SuO0A5VLNycpni+IFbu3w3XizgRbE0v8JG\ndolRHiz6XLnb+5whngQgFUH6auhjko/nOdp5nfFGsPI7mkFrLJAEoeUB1EUPeo8r2ZclIslC8UPM\nEvCHeHn0PX4jDf/9bYNTG3hW2t1oet79VBgMmC3QgwA1a+oaywveO0MsacGThuRHFCuzhF5EeUd4\nRQ2s7V05zsJgFMlzTy0rjxpzM7p04ocjLSODPHvmffQiQ+skmOBA87r+QPytKT/ZpqQQ+6Sp/eWU\nlXE7lnTeD5OeYQCPVVmsQyH/4RnV6LjoVJyd8Iai6bixCOfqwlVrPGZaY4VdPwXngGzpWX+fk7es\nqx/DLyOcqR1ac7IwAjeX499bj/mAaBP8wx1zWphXiKQrOoG5N4Hvm4FUivgmGkTVoXH83DTVb54=\n"}

What card do you want to reveal? -> cards:('queen', 'king') (please enter a number from 0 to 1): 0

Alice => Bob: {"message": "The Card I have chosen is: queen", "card": "queen", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAuuG1w8egoUpYStE4mh8O\nx5rWjCTCS/VgQlYEjM23gEy6ZlWRwgeYuCfBffOxk1Mk8nQ9F5oQIbSXV6YIJHUs\n6vvanEbcCrl3YSpQQVXdFWRLIOH8Hy+l6OyUO5B7g10AUzDT1eFCLXzajhJdUg2w\nYK7n28JN6o3Yx7hMgmci6rrJ+F5Nc6QJABH2C4IUGY24s69vu4wrqZxiqNoz/ZFK\nQqmwboqlNdzQ2Y5Zu2NIDCrMgxlqOX5dHX9CcqmY/hksXzOymBjJwoEVDPg8gl8z\nqW5GK/koMmkiQIp/5JBJOTVx40gsMLALbxojmuBmMXov6d+ojkTcSj3nUxN+AO3A\nTV8xVFgQG91SahQ/0mgNsrmZrNP18RiJH4cmebBhhZ467lDP9fNLxRNalkIYaTIu\nmbycCc0KEJkvdZbHkamsAo5W/c5rukXT9EU1okT1fa18AcIdGFqUvlGJtvKyMnBd\nv9S9OC6a0Ygj5046i/B9Nqwqcwv9Ll9c7ml+cayIxGawJL3Oydx6kE0XQS2GggrA\n8Dmrfks8aZugqypAfTrUjM07yNLOxHCLib8zR4hS6hIsqzDPKgqO8MpvyQr78YVQ\nlF1t1AsiMXBpUkkrk8ShAs+ieTsSdG9lZrsGCYYXZbypbRQ/s1ysCRx9mULImWfv\nRoXpqsiVRwBSShrtg7XCqhUCAwEAAQ==\n-----END PUBLIC KEY-----\n", "signature": "fNa4RNsZov4jDsoj7oK21eY+cIxArO2z8+0FLlVrachHQzlrHrK+3FP5U08b24ZruQ/z8to8ycb+\nHQ2IK4KtwBvME70NgHcDgnHQJTsOJ3BRzy3k7t/MaaXS8DnAo/PUMveD4Kj4B+WYxLxI1MRgNtvt\nUrn/bt47hgmy9w67t7uUOj6JO2QcnJze5iYxqqfvFQCAGugqqeKI2YDLDOcvEwMBkDzL60zTAAGo\nIT3D+BmKgY0Yd94bvHwI4/8Mr4xxzp7mZQydQxqZNp7MKXzNvv59RzioqUzEgNZzp1tPxBDo+1nm\nZz/rQ2NIt6ZPn29oWYL5E4MdaRtqmhq1x8nxKdnz+2FSBoD+JI3E/jDt9o4oNdFuYYWWBgU+CueR\nhKpszjT6ucVxjvRxyMHjLBxx4MJJcSdmN5Hd7/3MB+wpgXIXS+ajYC+AWUTvTDBN624J5yBN+5U9\nV9nsejuQP9ez2WNTY4vXPsjMyZ3skwpikTm3GEkoouwzwF8vk8QHnJ6hsOUN0IfVHwydyqlgk3b4\n9tJnIX7w774RFM2pEj2WC1Gn2gQfwikcZLNJ6DEEbLw1OCqqi/+SAcQ1eGYMYotc1aNhRdwKOKpd\nnHDaLpBbLMZk9spvX95LoIByPfbGg0m89L2UD3MG8yLdpP6/90Hh1NYwNwqzQ+k5cge7y0cT21Y=\n"}

Bob => Alice: {"message": true}

Bob Wins!
```

**Bob Terminal:**

```cmd
Bob => Alice: {"message": "I am Bob, please receive my public_key", "name": "Bob", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAzH0QE0KgK7YLkyJy9Frz\nT9gV5WPcb6D0I6yx3sJu6iHoOSHgvD7Ij2WisEccfJmoQLEeTiJJJOHZJo3De9Pi\nT6nmp+xnDzJHRQNoXBsrO016U53IpXiuVnkTthZsk5f9I+Y4OrK1kPKu2aLZK7ab\nybfZD1V88/tsfh+r3oDCjkphC2v5ThAQugONEa1pXqridFotLpE0PefF9xaj2TM6\nqSX1fzmYWa/4T9Ht7gZ5pPS36wyWsCHw83JCqNxh1VjRriSFoUQFfSqXHCb9AWLM\noJJT85xUEaLRm49Lky6gwSzWfLuyFG8ezLuTERNWlc6dpFdF27UXWw6D2D3n9VMX\ntBDL0BchwioYOM04CsdmWpJlFmJWqLOPvGiBVMO4HsHYjBw0EDV+hehhHOUxI0Mf\neMZpuNAP1yLPp66am145P9ndo2pOGw7sDIG3nBLMVU50cpnlfENdioWDpyTo8CA2\nDXe7qlnUaTYOqjmo9ZGk2QpvFiYm7AUrCvm8UIrIA8ZUhtkeupUBJv4F5O7xEEAp\nJ9HjEWaYl8xXmqZLnFPf3kuo9JDrI5ILPAPcULdkhU5EJo3ibfCf+/gTqW5mWYMQ\n18lBXC6LvbnY9WmvqhRQsC5QPr2FEBPJg5a103xXcMGM+izIpR3yJ2y2c30X4PD9\nS6SWieyupXuhizQ6WEMuhiECAwEAAQ==\n-----END PUBLIC KEY-----\n"}

Alice is picking a card...

Alice => Bob: {"message": "I've chosen my card, I have revealed the hash of my signature so you can validate my honesty", "signature_hash": "JBeZZRbOdoGUCm+Ptg9DvtHFZRYFvMYJrD6Q62hjXRE="}

Guess what is the card that Alice has picked -> cards:('queen', 'king') (please enter a number from 0 to 1): 0

Bob => Alice: {"message": "I guess the card is queen", "guessed_card": "queen", "signature": "DCh3JKJWC4afO86ptNB+z7Ufl5S2g7sVLn/NvcWmtn6X4hjXGEKF4XLIQXGjHbhrDgdawpP5Br6w\nI581gBYEAAk+BLm9ZnPlwp21cinrcBx3J15i1szKh5c0JS7FCzdS71PjAw0tDcv5tZJWmwp7ybfi\nr31uekcqY+mAHQmy9zQVzuBzE+PckDiFIbEYp8DWF20tcQ6aSslBw20TnmrYft/jDA6Z+z2z6yPb\nMJTvJuKcUaaWCiMq5aIanzUFyUC7bgnrSY6oO6VUK0SuO0A5VLNycpni+IFbu3w3XizgRbE0v8JG\ndolRHiz6XLnb+5whngQgFUH6auhjko/nOdp5nfFGsPI7mkFrLJAEoeUB1EUPeo8r2ZclIslC8UPM\nEvCHeHn0PX4jDf/9bYNTG3hW2t1oet79VBgMmC3QgwA1a+oaywveO0MsacGThuRHFCuzhF5EeUd4\nRQ2s7V05zsJgFMlzTy0rjxpzM7p04ocjLSODPHvmffQiQ+skmOBA87r+QPytKT/ZpqQQ+6Sp/eWU\nlXE7lnTeD5OeYQCPVVmsQyH/4RnV6LjoVJyd8Iai6bixCOfqwlVrPGZaY4VdPwXngGzpWX+fk7es\nqx/DLyOcqR1ac7IwAjeX499bj/mAaBP8wx1zWphXiKQrOoG5N4Hvm4FUivgmGkTVoXH83DTVb54=\n"}

Alice is asking you to wait :) ...

Alice => Bob: {"message": "The Card I have chosen is: queen", "card": "queen", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAuuG1w8egoUpYStE4mh8O\nx5rWjCTCS/VgQlYEjM23gEy6ZlWRwgeYuCfBffOxk1Mk8nQ9F5oQIbSXV6YIJHUs\n6vvanEbcCrl3YSpQQVXdFWRLIOH8Hy+l6OyUO5B7g10AUzDT1eFCLXzajhJdUg2w\nYK7n28JN6o3Yx7hMgmci6rrJ+F5Nc6QJABH2C4IUGY24s69vu4wrqZxiqNoz/ZFK\nQqmwboqlNdzQ2Y5Zu2NIDCrMgxlqOX5dHX9CcqmY/hksXzOymBjJwoEVDPg8gl8z\nqW5GK/koMmkiQIp/5JBJOTVx40gsMLALbxojmuBmMXov6d+ojkTcSj3nUxN+AO3A\nTV8xVFgQG91SahQ/0mgNsrmZrNP18RiJH4cmebBhhZ467lDP9fNLxRNalkIYaTIu\nmbycCc0KEJkvdZbHkamsAo5W/c5rukXT9EU1okT1fa18AcIdGFqUvlGJtvKyMnBd\nv9S9OC6a0Ygj5046i/B9Nqwqcwv9Ll9c7ml+cayIxGawJL3Oydx6kE0XQS2GggrA\n8Dmrfks8aZugqypAfTrUjM07yNLOxHCLib8zR4hS6hIsqzDPKgqO8MpvyQr78YVQ\nlF1t1AsiMXBpUkkrk8ShAs+ieTsSdG9lZrsGCYYXZbypbRQ/s1ysCRx9mULImWfv\nRoXpqsiVRwBSShrtg7XCqhUCAwEAAQ==\n-----END PUBLIC KEY-----\n", "signature": "fNa4RNsZov4jDsoj7oK21eY+cIxArO2z8+0FLlVrachHQzlrHrK+3FP5U08b24ZruQ/z8to8ycb+\nHQ2IK4KtwBvME70NgHcDgnHQJTsOJ3BRzy3k7t/MaaXS8DnAo/PUMveD4Kj4B+WYxLxI1MRgNtvt\nUrn/bt47hgmy9w67t7uUOj6JO2QcnJze5iYxqqfvFQCAGugqqeKI2YDLDOcvEwMBkDzL60zTAAGo\nIT3D+BmKgY0Yd94bvHwI4/8Mr4xxzp7mZQydQxqZNp7MKXzNvv59RzioqUzEgNZzp1tPxBDo+1nm\nZz/rQ2NIt6ZPn29oWYL5E4MdaRtqmhq1x8nxKdnz+2FSBoD+JI3E/jDt9o4oNdFuYYWWBgU+CueR\nhKpszjT6ucVxjvRxyMHjLBxx4MJJcSdmN5Hd7/3MB+wpgXIXS+ajYC+AWUTvTDBN624J5yBN+5U9\nV9nsejuQP9ez2WNTY4vXPsjMyZ3skwpikTm3GEkoouwzwF8vk8QHnJ6hsOUN0IfVHwydyqlgk3b4\n9tJnIX7w774RFM2pEj2WC1Gn2gQfwikcZLNJ6DEEbLw1OCqqi/+SAcQ1eGYMYotc1aNhRdwKOKpd\nnHDaLpBbLMZk9spvX95LoIByPfbGg0m89L2UD3MG8yLdpP6/90Hh1NYwNwqzQ+k5cge7y0cT21Y=\n"}

Bob => Alice: {"message": true}

Bob Wins!
```



#### Example 3: Alice is not honest

**Alice Terminal:**

```cmd
Bob => Alice: {"message": "I am Bob, please receive my public_key", "name": "Bob", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAzad4DpzdzjQLxmkYeNb/\n8K5ns5Z2uaDJS7iapLxD6E81laoFrSROKEfWFLpLhhDI/8EAK4QDb8jSs//1CwQp\nYnl1a35I5lLirHslUOBH+SUimpXKI7hFduv/25dh4BX/GuiI3el5QLcx19s1cygc\n7snr7Dqw6u+TeOf8BDBEtk6Ixft6l0nT/GASmUDGMOXUdCHQxJ+q6ZWaxEmz9EfD\nv6WwEV4vTVgUQ8phiLY1oBwZOj1z5nQw5ivl1ErfKeiRd3iQ9ZpAaOu8hJHqN5MQ\nMjCZh8V2GMvF7BhA4UO7c2XzPCIvoteMS36cKNVScs4MWGj1WS0dYykLNI/ZHABQ\nYRCK9jQbcUSE7zN+koG9M4qEcHQgRygOwBNN4QcDUJTgHrA3GQrKZqQO4jBb3CFY\nDdrSn55QsUjzQY0D4HtReli+PVMDlLusolk8vxwDoTKX4c8CQOu6Cz+iNYjXmr/n\nC/wlMDGISlR3oo0v10+AODNqvdmQAVzXf0TC1cHPO50Rg2VXVzqx8mpYdLmKxLeF\nDmai8mE9/1DQdIoNC6d6jR5X9MNYHmFE/ajrh+HNKv5lBe/tgkzKy9wCExdNm9yt\neSVUFfv0pUWgVzDfmMFlAWZ1kMB0CCaGefAeTUuGaWTUAyF8q4PzC2rLbLn4oawJ\nesQtHYekj480SgZPQsoVr9kCAwEAAQ==\n-----END PUBLIC KEY-----\n"}

Pick a card -> cards:('queen', 'king') (please enter a number from 0 to 1): 0
Alice => Bob: {"message": "I've chosen my card, I have revealed the hash of my signature so you can validate my honesty", "signature_hash": "xGvCy6ojuLTbRBjydcpwKnGaZMbs82G9uc5qhvFXSJc="}

Bob is guessing a card...

Bob => Alice: {"message": "I guess the card is queen", "guessed_card": "queen", "signature": "hMkZeHweTLRd9Khb0zl4d/M9WKnydcqEhbqpipHcjGxgjBBb6qnR0wDgAG6s/Z0mwhFRjZU9c1hA\n9zFR3R+3TkuZOMq4UWMvfSLzj2N6EcDJjMry2VxE+cq+e2y4WAReKgh9QiR8CBI/0fGP7JjI5UAW\nj7Alqh2y8CX8LQpDe7DPIkwMR8HnAekQ+2aGNSQVayyIPy8nu7JRkiKE5XygmdpD7CixLMTjJHvu\nK/vwJhGm55Bq3ddJH2Ydq0xUEOyB7Gm28dAxarW0yRt+1BRsst2fwn6z1Ue6kcm7BpfvvwRdWrnn\n4jBnp2yXMJB1JenvU5zIlJ6CcM6LDx3wdq8u7ky6H0TLRiPQBXa5kcDvNZkqsyI8xZVNw6vDEgLQ\nhnSOpVCCKe7A2NkPmGzCH6KJqat7hZTVyvBSukzPdqX0QzpE/S7ShgWlregqEa16kH3nt/olhooT\nQUYbM4ccF3LRhMgG7MXRhAMPhcckS2O8JY8v+D0M34KK7femLYwDoDx4InSP+Eyp8tIdYEGkqnKg\nHabOezh/Z4iNXtVwnwZjVWc7LMn0QLcNWONeGcI2qt4W/oKvovxenhS64sGBMtjqNDTat4PYnC6m\nLfdEw0+lF2IyJes3g5G2VbD7S9yqdMIelF45W0ELMjWBs186XadyaV75eowe/JDTbZ3lJHwmRvQ=\n"}

What card do you want to reveal? -> cards:('queen', 'king') (please enter a number from 0 to 1): 1

Alice => Bob: {"message": "The Card I have chosen is: king", "card": "king", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqqwR0SA5VbrXNkjgC1e0\no2kt0zIbsUq9VSSYXKyKgtG8BJFB/eV/h7zIvreRh1dGF5tdzvYC48MIS5gU7yHQ\nKotaYJbGJGPaPJrXEHLEpzzx0ZhncLJXNgl1SBD47Ea/3tArINIpyJ/Ri36WOY9q\ncPwcBVSG/nC3ieKTlVNBQI6ll1oCNPXk4tHheFgIWwCqAiveR72WMlsnG8xwOsZ2\nJ77l0B+Ug9+Y4CGO35+gNg0Ii+FYx8XaISUaRCs7hTLf30hNVS7+deKSlBwLwPnt\nNBhOwfhpMqSpsWchwvLQsldIumLHkERqfqzbxUGKKqWJm1i6AU/If2ONkSnXI/2i\nQsio5eMpN94NpUDnokaESaCXQu8ShuQFbv0G1Xlek4e29UHX3LxXOYF6+CrxPcL0\nacME/QGjSPw39d5tEynRA0OlR4D8kXXk/kT98GK/qNRbvb4OWEqBjUXQx1xMQrEb\nJ8qugz5dcA4+2jf2Ym5/h7gHHOvzGbcpMLkKjmdLOnX33ksglsZpKX5fsqbW77Ql\n4MefWUrzGpUAkX36XhZoL/UKRw1s52Ufc0Qo/xc1Gy/NbPQ5fIpKOekv/23XEI3w\nJ6vm8FXUhhF+4hW6ufRob0qQBVUKcRR+MzvVVVWo/rdetpOE8mNUJLIPcwL1/uKH\nYQRA92FwTGFua2Zx9rTnTKkCAwEAAQ==\n-----END PUBLIC KEY-----\n", "signature": "UbfZafja/09KMeGZz+SHc805Lkz3L47TFdBnphy/MWddNYVi3fm1ELbKiOe6mXiaQAtD3fuJ2jEW\nXYSJ0r2gtvW69D3tCnjmslpp9Zcgdzx9GadB7JVvZMQXqxUTf09rPVkezEu9aj3STNYdGMxzi4PB\nHYytrqJ4Re8/3AB0Z6CMMhpeq/Ec41/tfNFM4FtGrvY5EtEgSBih3w5A3+IbB2JpHaTHy/PN9MhL\ncdivQvV1V+2ffm8o1pvTFNPqrdGPSCLuG6M/atUfmqFYGLRJY+qRQBVjC1x3BWjvqRWPEpfGyRIz\nwXf0ePFQfSK9siIgovyWiJuCeoIPcDCb8Pbipj6MTydgWq4tiydsrTxbqashj9uIZl5Ce4SNvpEp\nrPR9PzyLGa6R0aiy4e5AvHEwkH2D0YiYEP8Wa1iz0WFTpjmS0gSCZr6faBCmKcrmmmrlPCorc0oR\nVESZ5wCNVbOJa1V5rudJu+b2cKEs2e926smua5dwdVSIP60e3kII7iRyERf/8+GRvVy4w88vLYnF\nHrbmVuq6ETYo1cn1Oj+LL9xQUXu/0gK/rGecvpR9Oy0+0HB4w+6vDa0bjWjwqiNIgTrIpytLeq3L\nC2yFuGaPtLKd07oSmfYkaC6+y/asQ0s62hv684+ruyQbkCT2DAT1DvuHw1N3Nyxa9uqSJjHqbhM=\n"}

Bob => Alice: {"message": false}

Alice is not Honest :(, Bob Wins!
```

**Bob Terminal**

```cmd
Bob => Alice: {"message": "I am Bob, please receive my public_key", "name": "Bob", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAzad4DpzdzjQLxmkYeNb/\n8K5ns5Z2uaDJS7iapLxD6E81laoFrSROKEfWFLpLhhDI/8EAK4QDb8jSs//1CwQp\nYnl1a35I5lLirHslUOBH+SUimpXKI7hFduv/25dh4BX/GuiI3el5QLcx19s1cygc\n7snr7Dqw6u+TeOf8BDBEtk6Ixft6l0nT/GASmUDGMOXUdCHQxJ+q6ZWaxEmz9EfD\nv6WwEV4vTVgUQ8phiLY1oBwZOj1z5nQw5ivl1ErfKeiRd3iQ9ZpAaOu8hJHqN5MQ\nMjCZh8V2GMvF7BhA4UO7c2XzPCIvoteMS36cKNVScs4MWGj1WS0dYykLNI/ZHABQ\nYRCK9jQbcUSE7zN+koG9M4qEcHQgRygOwBNN4QcDUJTgHrA3GQrKZqQO4jBb3CFY\nDdrSn55QsUjzQY0D4HtReli+PVMDlLusolk8vxwDoTKX4c8CQOu6Cz+iNYjXmr/n\nC/wlMDGISlR3oo0v10+AODNqvdmQAVzXf0TC1cHPO50Rg2VXVzqx8mpYdLmKxLeF\nDmai8mE9/1DQdIoNC6d6jR5X9MNYHmFE/ajrh+HNKv5lBe/tgkzKy9wCExdNm9yt\neSVUFfv0pUWgVzDfmMFlAWZ1kMB0CCaGefAeTUuGaWTUAyF8q4PzC2rLbLn4oawJ\nesQtHYekj480SgZPQsoVr9kCAwEAAQ==\n-----END PUBLIC KEY-----\n"}

Alice is picking a card...

Alice => Bob: {"message": "I've chosen my card, I have revealed the hash of my signature so you can validate my honesty", "signature_hash": "xGvCy6ojuLTbRBjydcpwKnGaZMbs82G9uc5qhvFXSJc="}

Guess what is the card that Alice has picked -> cards:('queen', 'king') (please enter a number from 0 to 1): 0

Bob => Alice: {"message": "I guess the card is queen", "guessed_card": "queen", "signature": "hMkZeHweTLRd9Khb0zl4d/M9WKnydcqEhbqpipHcjGxgjBBb6qnR0wDgAG6s/Z0mwhFRjZU9c1hA\n9zFR3R+3TkuZOMq4UWMvfSLzj2N6EcDJjMry2VxE+cq+e2y4WAReKgh9QiR8CBI/0fGP7JjI5UAW\nj7Alqh2y8CX8LQpDe7DPIkwMR8HnAekQ+2aGNSQVayyIPy8nu7JRkiKE5XygmdpD7CixLMTjJHvu\nK/vwJhGm55Bq3ddJH2Ydq0xUEOyB7Gm28dAxarW0yRt+1BRsst2fwn6z1Ue6kcm7BpfvvwRdWrnn\n4jBnp2yXMJB1JenvU5zIlJ6CcM6LDx3wdq8u7ky6H0TLRiPQBXa5kcDvNZkqsyI8xZVNw6vDEgLQ\nhnSOpVCCKe7A2NkPmGzCH6KJqat7hZTVyvBSukzPdqX0QzpE/S7ShgWlregqEa16kH3nt/olhooT\nQUYbM4ccF3LRhMgG7MXRhAMPhcckS2O8JY8v+D0M34KK7femLYwDoDx4InSP+Eyp8tIdYEGkqnKg\nHabOezh/Z4iNXtVwnwZjVWc7LMn0QLcNWONeGcI2qt4W/oKvovxenhS64sGBMtjqNDTat4PYnC6m\nLfdEw0+lF2IyJes3g5G2VbD7S9yqdMIelF45W0ELMjWBs186XadyaV75eowe/JDTbZ3lJHwmRvQ=\n"}
Alice is asking you to wait :) ...

Alice => Bob: {"message": "The Card I have chosen is: king", "card": "king", "public_key": "-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAqqwR0SA5VbrXNkjgC1e0\no2kt0zIbsUq9VSSYXKyKgtG8BJFB/eV/h7zIvreRh1dGF5tdzvYC48MIS5gU7yHQ\nKotaYJbGJGPaPJrXEHLEpzzx0ZhncLJXNgl1SBD47Ea/3tArINIpyJ/Ri36WOY9q\ncPwcBVSG/nC3ieKTlVNBQI6ll1oCNPXk4tHheFgIWwCqAiveR72WMlsnG8xwOsZ2\nJ77l0B+Ug9+Y4CGO35+gNg0Ii+FYx8XaISUaRCs7hTLf30hNVS7+deKSlBwLwPnt\nNBhOwfhpMqSpsWchwvLQsldIumLHkERqfqzbxUGKKqWJm1i6AU/If2ONkSnXI/2i\nQsio5eMpN94NpUDnokaESaCXQu8ShuQFbv0G1Xlek4e29UHX3LxXOYF6+CrxPcL0\nacME/QGjSPw39d5tEynRA0OlR4D8kXXk/kT98GK/qNRbvb4OWEqBjUXQx1xMQrEb\nJ8qugz5dcA4+2jf2Ym5/h7gHHOvzGbcpMLkKjmdLOnX33ksglsZpKX5fsqbW77Ql\n4MefWUrzGpUAkX36XhZoL/UKRw1s52Ufc0Qo/xc1Gy/NbPQ5fIpKOekv/23XEI3w\nJ6vm8FXUhhF+4hW6ufRob0qQBVUKcRR+MzvVVVWo/rdetpOE8mNUJLIPcwL1/uKH\nYQRA92FwTGFua2Zx9rTnTKkCAwEAAQ==\n-----END PUBLIC KEY-----\n", "signature": "UbfZafja/09KMeGZz+SHc805Lkz3L47TFdBnphy/MWddNYVi3fm1ELbKiOe6mXiaQAtD3fuJ2jEW\nXYSJ0r2gtvW69D3tCnjmslpp9Zcgdzx9GadB7JVvZMQXqxUTf09rPVkezEu9aj3STNYdGMxzi4PB\nHYytrqJ4Re8/3AB0Z6CMMhpeq/Ec41/tfNFM4FtGrvY5EtEgSBih3w5A3+IbB2JpHaTHy/PN9MhL\ncdivQvV1V+2ffm8o1pvTFNPqrdGPSCLuG6M/atUfmqFYGLRJY+qRQBVjC1x3BWjvqRWPEpfGyRIz\nwXf0ePFQfSK9siIgovyWiJuCeoIPcDCb8Pbipj6MTydgWq4tiydsrTxbqashj9uIZl5Ce4SNvpEp\nrPR9PzyLGa6R0aiy4e5AvHEwkH2D0YiYEP8Wa1iz0WFTpjmS0gSCZr6faBCmKcrmmmrlPCorc0oR\nVESZ5wCNVbOJa1V5rudJu+b2cKEs2e926smua5dwdVSIP60e3kII7iRyERf/8+GRvVy4w88vLYnF\nHrbmVuq6ETYo1cn1Oj+LL9xQUXu/0gK/rGecvpR9Oy0+0HB4w+6vDa0bjWjwqiNIgTrIpytLeq3L\nC2yFuGaPtLKd07oSmfYkaC6+y/asQ0s62hv684+ruyQbkCT2DAT1DvuHw1N3Nyxa9uqSJjHqbhM=\n"}

Bob => Alice: {"message": false}

Alice is not honest :(, Bob Wins!
```

