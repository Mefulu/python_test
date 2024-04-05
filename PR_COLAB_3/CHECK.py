def decode_data(hex_string):
    data = int(hex_string, 16)

    r1 = data & 0b11
    r2 = (data >> 4) & 0b111111111
    r3 = (data >> 13) & 0b111
    r4 = (data >> 16) & 0b111
    r5 = (data >> 19) & 0b111111

    return [
        ("R1", str(r1)),
        ("R2", str(r2)),
        ("R3", str(r3)),
        ("R4", str(r4)),
        ("R5", str(r5))
    ]


hex_string = "0x6a9f6"
decoded_data = decode_data(hex_string)
print(decoded_data)