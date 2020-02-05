## Quantum Key Distribution

> Generate a key using Quantum Key Distribution (QKD) algorithm and decrypt the flag.

The challenge's server implements (a slightly modified)  [BB84](https://en.m.wikipedia.org/wiki/BB84), which is a simple algorithm to allow two entities to share a secret key. 

## Qubits, Basis and Measurements review

If you feel comfortable with these topics, feel free to jump to the solution.

### Qubits

In classical computing we the most basic unit of information so the "bit", which can hold two states. We traditionally mark them as 0 and 1.

Qubits are the basic unit of quantum information, which can be represented as a unit vectors of size 2 in an orthonormal basis.

For example: [0,1], [1,0], [1/root 2, 1/root 2]. 


### Basis

Vectors have no meaning without a basis. We can choose any two basis vectors as long as they are orthogonal and have unit length.

Although we can choose an arbitrary basis, two bases are common:

+: [ 1 0, 0 1]
x: [1/root 2 1/root 2, -1/root 2, 1/root 2]

For simplicity we call the first column vector "0" and the second column vector "1".

### Measurements

To convert qubits to bits we measure them. You can think of measurement as a function that takes a basis and a qubit and returns a bit.

For this challenge the only important thing to know about this function is that if the qubit is one of the basis vectors (ex: [0,1] in the + basis "1" or [1/root 2 1/root 2] in the x basis "0"), the function return their value. Otherwise it's unknown what the function will return (though it's probability is known). 

## BB84

Alice and Bob want to share a key. They have a Quantum channel (a way Alice can send qubits to Bob) and a classical channel.

Step 1:

Alice generates a predetermined number of random bits. Then for each bit she randomly generate the same number of basis (for our purposes she can choose + or x). Then she encodes the bits she created as qubits in the  basis she has chosen.

She send them to Bob.

Step 2:

Bob randomly chooses the same number of predetermined basis. He reads the qubits Alice sent him by measuring them using the basises he has generated. For every bit, Bob has a 50% chance of generating the same basis as Alice. I'd he happens to choose correctly, the measurement will result in the correct bit. Otherwise he has a 50% chance of getting the correct bit.

At the end of the exchange both Alice and Bob have a series of bits and basis. ~50% of the bits Alice has sent were decoded correctly by Bob.

Step 2:

Alice and Bob share their basis with each other. They get rid of every bit that was measured by different basis. 

Step 3: 

Alice and Bob send half of the bits that were left and check they are the same. If Eve has interfered with the quantum channel. They'd disagree due to the no cloning theorem.

Step 4:

Alice and Bob use the bits that were left as an OTP.


## The Challenge

The challenge's server requires us to send 512 qubits and basis (It does steps 1 and 2 together):

`

`

The response has the basis the server has chosen. We get rid of the basis that don't match:

`

`

We also get an announcement, which is not part of the original algorithm. I originally thought it was the server trying to perform step 3 but couldn't figure out what it's response ment). Then I figured out the server doesn't implement step 3 and just send the flag xored with the first 128 bits that agree.

We choose the useful bits


Xor the announcement with the OTP


And get the flag




-----

## A simpler solution

To make sure Eve can't know the OTP. Both the bits and the basis have to be chosen randomly. If She can figure out the basis used. If Eve knows the basis, she can perform MiTM attack. But the sever doesn't check that.

So let's generate a basis which is just +


And our OTP is 111....


We don't care which bits agree because they are all the same


NOT the announcement and get the flag 
