buffer1 = input("Buffer1: ")
buffer2 = input("Buffer2: ")
buffer1_int = int(buffer1, 16)
buffer2_int = int(buffer2, 16)
buffer1_xor_buffer2 = buffer1_int ^ buffer2_int
print(hex(buffer1_xor_buffer2))