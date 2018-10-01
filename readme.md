Ali Taqvi amt3597
Hassaan Raza hr7233

Readme for AES project for CS361 Fall 2018

Algorithm was implemented by following the AES documentation (https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.197.pdf)
We took time to closely understand the key components of the algorithm detailed in section 5 of the document.
Our approach to creating the encryption algorithm was to follow the pseudocode described in the text and for the 128 bit key
encryption. We chose to take it step by step by implementing functions and verifiying that the program was working up to that
point by running the sample key and input given by in Appendix B of the document. Here is the path we took to implement the
functions:

1. Complete input file reading and storage in a list of strings containing "bytes" (techically they were strings but with a
byte format)
2. Create a layout for functions that would be used in the cipher/encryption functions and fill them in in the order shown
in the pseudocode given in the AES documentation
3. Roundkey, subbytes, shiftrows were implemented first. At this time, we did not implement key expansion and only verified
that our functions worked for the first block.
4. Mixcolumns was difficult to implement and we did reference resources that described Rijndael Galois Fields. We were able to
discover a trick that allows for the use of two multiplication in the field and extrapolated that to the 3 multiplication as well
5. Next we tackled key extension which was fairly straightforward by looking at both the pseudocode and the Appendix A of the
AES document
6. Finally, we implemented the inverse cipher, or decryption, algorithm by following the pseudocode and choosing the inverse
cipher instead of the equivalent inverse cipher route described because we did not want to generate another key. In the process
of writing the decryption algorithm, we ran into issues with the inverse mixcolumns function again and had to resort to using
Mul tables that were provided on Piazza. The key schedule also had to be used in reverse, block by block, which was another
issue we ran into and were able to find fairly quickly through some quick debugging.
7. Once encryption and decryption were completed, we made some slight modificaitons (mostly to number of rounds and key expansion)
to accomodate for and validate 256 bit keys. We had no issues with this, and the encryption worked on the first attempt.
8. The last thing was converting our list of hex strings to a bytearray in the output file specified. We did this by opening
and writing into the file each of the bytes in the array.

Although we do not have any sample files in this repo, we did test several inputs and outputs both forwards and backwards
and were excited to see that our encryption and decryption works as expected. The file can be run using the method specified
in the project description from canvas, ie:

python aes.py --keysize 128 --keyfile keyfile.txt --inputfile input.txt --outputfile output.txt --mode encrypt
