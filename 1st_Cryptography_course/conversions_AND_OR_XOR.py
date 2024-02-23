a = int('10110011', 2)
b = int('11011100', 2)

AxorB = a ^ b
AorB = a | b
AandB = a & b

print(a,'XOR', b, '=', AxorB)
print(a, 'OR', b, '=', AorB)
print(a, 'AND', b, '=', AandB)