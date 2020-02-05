## Quantum Key Distribution

> Generate a key using Quantum Key Distribution (QKD) algorithm and decrypt the flag.

The challenge's server implements (a slightly modified version of) [BB84](https://en.m.wikipedia.org/wiki/BB84), which is a simple algorithm to allow two entities to share a secret key. 

## Qubits, Basis and Measurements review

If you feel comfortable with these topics, feel free to jump to the solution.

### Qubits

In classical computing, the most basic unit of information is the "bit", which can hold two states. We traditionally mark them as 0 and 1.

Qubits are the basic unit of quantum information, which can be represented as a unit vectors of size 2 in an orthonormal basis.

For example: [0,1], [1,0], [1/root 2, 1/root 2]. 


### Basis

Vectors have no meaning without a basis. We can choose any two basis vectors as long as they are orthogonal and have unit length.

It's common to choose one of two basis:

+: [ 1 0, 0 1]
x: [1/root 2 1/root 2, -1/root 2, 1/root 2]

We call the first column vector "0" and the second column vector "1". So you can think of qubits as a linear combination of "0" and "1".

### Measurements

To convert qubits to bits we measure them. You can think of measurement as a function that takes a basis and a qubit and returns a bit.

For this challenge the only important thing to know about measurments is that if the qubit is one of the basis vectors (ex: [0,1] in the + basis or [1/root 2 1/root 2] in the x basis), the function returns their value ("0" or "1"). Otherwise it's unknown what the function will return (though its probability is known). 

## BB84

Alice and Bob want to share a key. They have a Quantum channel (a way Alice can send qubits to Bob) and a classical channel.

Step 1:

Alice generates a predetermined number (`N`) of random bits. Then she randomly generates `N` bases (for our purposes she can choose + or x). Then she encodes the bits she had generated as qubits in the bases she has chosen.

She sends all the qubits to Bob.

Step 2:

Bob randomly chooses N bases. He reads the qubits Alice sent him and measures them using the bases he has generated. For every bit, Bob has a 50% chance of generating the same basis as Alice. If he happens to choose correctly, the measurement will result in the correct bit. Otherwise he has a 50% chance of getting the correct bit.

At the end of the exchange both Alice and Bob have a series of bits and basis. On average 50% of the bits Alice has sent were decoded correctly by Bob.

Step 3:

Alice and Bob share their basis with each other. They get rid of every bit that was measured by different bases. 

At the end of this part (as long as no one interfered with the quantum channel), Alice and Bob share a secrets, which is the list of bits that were measured correctly by Bob.

Step 4: 

Alice and Bob send half of the bits to each other and verify they are the same. If Eve has interfered with the quantum channel. They'd disagree.

Step 5

Alice and Bob use the bits that were left as an OTP.


## The Challenge

The challenge's server requires us to send 512 qubits and bases (It does steps 1 and 2 together):

Let's generate them:

```python
import random
from math import sqrt

basis_vectors = {
    '+': [{'real': 0, 'imag': 1}, {'real': 1, 'imag': 0}],
    'x': [{'real': 1/sqrt(2), 'imag': 1/sqrt(2)}, {'real': 1/sqrt(2), 'imag': -1/sqrt(2)}]
}

bases = [random.choice('+x') for _ in range(512)]
qubits = [random.choice(basis_vectors[basis]) for basis in bases]
```

The response has the basis the server has chosen. We get rid of the basis that don't match:

```python
import requests

URL = 'https://cryptoqkd.web.ctfcompetition.com/qkd/qubits'

response = requests.post(
    URL,
    json={'basis': basis, 'qubits': qubits},
    verify=False
   ).json()
```

We get the following response:

```javascript
{
'basis': ['x', '+', '+', 'x', '+', '+', '+', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', '+', '+', 'x', '+', '+', '+', '+', '+', 'x', 'x', 
'+', '+', '+', '+', 'x', 'x', 'x', '+', '+', '+', 'x', '+', 'x', 'x', '+', '+', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', '+', 'x', '+', 'x', '+', 'x', '+', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', '+', 'x', 'x', 'x', 'x', 'x', 'x', '+', 'x', 'x', '+', '+', '+', 'x', 'x', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', '+', '+', '+', 'x', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', '+', '+', '+', 'x', '+', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', '+', '+', '+', '+', 'x', '+', 'x', 'x', 'x', '+', 'x', '+', '+', '+', 'x', 'x', '+', '+', '+', '+', '+', '+', 'x', 'x', 'x', 'x', '+', 'x', '+', 'x', '+', '+', '+', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', '+', 'x', '+', '+', 'x', '+', '+', '+', '+', 'x', '+', '+', 'x', '+', '+', '+', '+', '+', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '+', 'x', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', '+', '+', 'x', 'x', 'x', 'x', 'x', '+', '+', 'x', '+', '+', '+', '+', '+', 'x', 'x', 'x', '+', '+', '+', '+', '+', 'x', '+', 'x', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', '+', '+', 'x', 'x', '+', 'x', 'x', '+', 'x', '+', '+', 'x', '+', '+', 'x', 'x', 'x', 'x', '+', '+', 'x', '+', 'x', '+', 'x', '+', 'x', '+', '+', '+', '+', 'x', 'x', '+', '+', '+', 'x', 'x', 'x', 'x', '+', '+', '+', '+', '+', '+', 'x', '+', '+', '+', 'x', 'x', 'x', '+', '+', '+', 'x', '+', '+', 'x', '+', '+', 'x', 'x', 'x', 'x', 'x', '+', '+', '+', '+', 'x', 'x', 'x', '+', '+', '+', '+', 'x', 'x', 'x', 'x', '+', '+', '+', '+', '+', '+', 'x', 'x', 'x', '+', 'x', 'x', '+', '+', 'x', '+', 'x', 'x', 'x', '+', '+', 'x', '+', 'x', '+', '+', '+', '+', '+', 'x', 'x', '+', '+', 'x', 'x', '+', 'x', '+', '+', '+', '+', 'x', '+', 'x', 'x', 'x', '+', 'x', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', '+', '+', '+', '+', '+', '+', 'x', '+', '+', '+', 'x', 'x', '+', '+', 'x', '+', 'x', 'x', 'x', 'x', 'x', '+', '+', '+', 'x', '+', 'x', 'x', '+', '+', '+', '+', 'x', '+', 'x', 'x', 'x', 'x', '+', '+', '+', '+', 'x', '+', 'x', 'x', '+', 'x', '+', 'x', '+', '+', 'x', '+', '+', '+', 'x', 'x', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', '+', 'x', 'x', 'x', 'x', 'x', 'x', '+', '+', 'x', '+', '+', '+', '+', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '+', '+', '+', 'x', 'x', '+', 'x', 'x', 'x', 'x', '+', '+', '+', 'x', 'x', '+'],
'announcement': '909c84644d36c14650f032b29d1dc48a'
}
```

The response contains two fields:

* `basis`: the list of bases that the server used to decode the qubits we've sent
* `announcement`:  Not a part of the original algorithm. I originally thought it was the server trying to perform step 3 but couldn't figure out what it's response ment). Then I figured out the server doesn't implement step 3 and just send the flag xored with the first 128 bits that agree.

Xor the announcement with the OTP:

```python
key = 0
for i in range(len(bases)):
    if bases[i] == server_bases[i]:
        key *= 2
        key += basis_vectors[bases[i]].index(qubits[i])
```


And get the flag

```python
key = ''
for i in range(len(bases)):
    if bases[i] == server_bases[i]:
        key += str(basis_vectors[bases[i]].index(qubits[i]))
        
key = int(key[:128],2)
announcement = int(response['announcement'],16)

print(hex(key^announcement))        
```

result:

`0x946cff6c9d9efed002233a6a6c7b83b1`

-----

## A simpler solution

To make sure Eve can't know the OTP. Both the bits and the basis have to be chosen randomly. If She can figure out the basis used. If Eve knows the basis, she can perform MiTM attack. But the sever doesn't check that.

So let's generate a basis which is just +


And our OTP is 111....


We don't care which bits agree because they are all the same


NOT the announcement and get the flag 
