import os

byte = bytearray(1)
bytes_95 = bytearray(95)
try:
    out_stream = open("file.bin", "wb")
    for i in range(32,127):
        byte[0] = i;
        out_stream.write(byte)
    out_stream.close();
    in_stream = open("file.bin", "rb")
    read_in = in_stream.readinto(bytes_95)
    in_stream.close()
    print(read_in,"byte(s) read in")
    for i in range(95):
        print(chr(bytes_95[i]), end='')
except IOError as exception:
    print("I/O error occurred:", os.strerror(exception.errno))