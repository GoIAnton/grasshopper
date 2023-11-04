GF = [1, 2, 4, 8, 16, 32, 64, 128, 195, 69, 138, 215, 109, 218, 119,
      238, 31, 62, 124, 248, 51, 102, 204, 91, 182, 175, 157, 249, 49,
      98, 196, 75, 150, 239, 29, 58, 116, 232, 19, 38, 76, 152, 243,
      37, 74, 148, 235, 21, 42, 84, 168, 147, 229, 9, 18, 36, 72, 144,
      227, 5, 10, 20, 40, 80, 160, 131, 197, 73, 146, 231, 13, 26, 52,
      104, 208, 99, 198, 79, 158, 255, 61, 122, 244, 43, 86, 172, 155,
      245, 41, 82, 164, 139, 213, 105, 210, 103, 206, 95, 190, 191, 189,
      185, 177, 161, 129, 193, 65, 130, 199, 77, 154, 247, 45, 90, 180,
      171, 149, 233, 17, 34, 68, 136, 211, 101, 202, 87, 174, 159, 253,
      57, 114, 228, 11, 22, 44, 88, 176, 163, 133, 201, 81, 162, 135,
      205, 89, 178, 167, 141, 217, 113, 226, 7, 14, 28, 56, 112, 224,
      3, 6, 12, 24, 48, 96, 192, 67, 134, 207, 93, 186, 183, 173, 153,
      241, 33, 66, 132, 203, 85, 170, 151, 237, 25, 50, 100, 200, 83,
      166, 143, 221, 121, 242, 39, 78, 156, 251, 53, 106, 212, 107, 214,
      111, 222, 127, 254, 63, 126, 252, 59, 118, 236, 27, 54, 108, 216,
      115, 230, 15, 30, 60, 120, 240, 35, 70, 140, 219, 117, 234, 23,
      46, 92, 184, 179, 165, 137, 209, 97, 194, 71, 142, 223, 125, 250,
      55, 110, 220, 123, 246, 47, 94, 188, 187, 181, 169, 145, 225, 1]


PI = [
    252, 238, 221, 17, 207, 110, 49, 22, 251, 196, 250, 218, 35, 197, 4, 77,
	233, 119, 240, 219, 147, 46, 153, 186, 23, 54, 241, 187, 20, 205, 95, 193,
	249, 24, 101, 90, 226, 92, 239, 33, 129, 28, 60, 66, 139, 1, 142, 79, 5,
	132, 2, 174, 227, 106, 143, 160, 6, 11, 237, 152, 127, 212, 211, 31, 235,
	52, 44, 81, 234, 200, 72, 171, 242, 42, 104, 162, 253, 58, 206, 204, 181,
	112, 14, 86, 8, 12, 118, 18, 191, 114, 19, 71, 156, 183, 93, 135, 21, 161,
	150, 41, 16, 123, 154, 199, 243, 145, 120, 111, 157, 158, 178, 177, 50, 117,
	25, 61, 255, 53, 138, 126, 109, 84, 198, 128, 195, 189, 13, 87, 223, 245,
	36, 169, 62, 168, 67, 201, 215, 121, 214, 246, 124, 34, 185, 3, 224, 15,
	236, 222, 122, 148, 176, 188, 220, 232, 40, 80, 78, 51, 10, 74, 167, 151,
	96, 115, 30, 0, 98, 68, 26, 184, 56, 130, 100, 159, 38, 65, 173, 69, 70,
	146, 39, 94, 85, 47, 140, 163, 165, 125, 105, 213, 149, 59, 7, 88, 179, 64,
	134, 172, 29, 247, 48, 55, 107, 228, 136, 217, 231, 137, 225, 27, 131, 73,
	76, 63, 248, 254, 141, 83, 170, 144, 202, 216, 133, 97, 32, 113, 103, 164,
	45, 43, 9, 91, 203, 155, 37, 208, 190, 229, 108, 82, 89, 166, 116, 210, 230,
	244, 180, 192, 209, 102, 175, 194, 57, 75, 99, 182
]


REVERSE_PI = [0xA5, 0x2D, 0x32,  0x8F, 0x0E, 0x30, 0x38,  0xC0,
              0x54,  0xE6,  0x9E, 0x39, 0x55, 0x7E, 0x52,  0x91,
              0x64, 0x03, 0x57, 0x5A, 0x1C, 0x60, 0x07, 0x18,
              0x21, 0x72,  0xA8,  0xD1, 0x29,  0xC6,  0xA4, 0x3F,
              0xE0, 0x27,  0x8D, 0x0C,  0x82,  0xEA,  0xAE,  0xB4,
              0x9A, 0x63, 0x49,  0xE5, 0x42,  0xE4, 0x15,  0xB7,
              0xC8, 0x06, 0x70,  0x9D, 0x41, 0x75, 0x19,  0xC9,
              0xAA,  0xFC, 0x4D,  0xBF, 0x2A, 0x73,  0x84,  0xD5,
              0xC3,  0xAF, 0x2B,  0x86,  0xA7,  0xB1,  0xB2, 0x5B,
              0x46,  0xD3,  0x9F,  0xFD,  0xD4, 0x0F,  0x9C, 0x2F,
              0x9B, 0x43,  0xEF,  0xD9, 0x79,  0xB6, 0x53, 0x7F,
              0xC1,  0xF0, 0x23,  0xE7, 0x25, 0x5E,  0xB5, 0x1E,
              0xA2,  0xDF,  0xA6,  0xFE,  0xAC, 0x22,  0xF9,  0xE2,
              0x4A,  0xBC, 0x35,  0xCA,  0xEE, 0x78, 0x05, 0x6B,
              0x51,  0xE1, 0x59,  0xA3,  0xF2, 0x71, 0x56, 0x11,
              0x6A,  0x89,  0x94, 0x65,  0x8C,  0xBB, 0x77, 0x3C,
              0x7B, 0x28,  0xAB,  0xD2, 0x31,  0xDE,  0xC4, 0x5F,
              0xCC,  0xCF, 0x76, 0x2C,  0xB8,  0xD8, 0x2E, 0x36,
              0xDB, 0x69,  0xB3, 0x14,  0x95,  0xBE, 0x62,  0xA1,
              0x3B, 0x16, 0x66,  0xE9, 0x5C, 0x6C, 0x6D,  0xAD,
              0x37, 0x61, 0x4B,  0xB9,  0xE3,  0xBA,  0xF1,  0xA0,
              0x85,  0x83,  0xDA, 0x47,  0xC5,  0xB0, 0x33,  0xFA,
              0x96, 0x6F, 0x6E,  0xC2,  0xF6, 0x50,  0xFF, 0x5D,
              0xA9,  0x8E, 0x17, 0x1B,  0x97, 0x7D,  0xEC, 0x58,
              0xF7, 0x1F,  0xFB, 0x7C, 0x09, 0x0D, 0x7A, 0x67,
              0x45,  0x87,  0xDC,  0xE8, 0x4F, 0x1D, 0x4E, 0x04,
              0xEB,  0xF8,  0xF3, 0x3E, 0x3D,  0xBD,  0x8A,  0x88,
              0xDD,  0xCD, 0x0B, 0x13,  0x98, 0x02,  0x93,  0x80,
              0x90,  0xD0, 0x24, 0x34,  0xCB,  0xED,  0xF4,  0xCE,
              0x99, 0x10, 0x44, 0x40,  0x92, 0x3A, 0x01, 0x26,
              0x12, 0x1A, 0x48, 0x68,  0xF5,  0x81,  0x8B,  0xC7,
              0xD6, 0x20, 0x0A, 0x08, 0x00, 0x4C,  0xD7, 0x74]


L_VEC = [1, 148, 32, 133, 16, 194, 192, 1, 251, 1, 192, 194, 16, 133, 32, 148]


ITER_C = [[0x01, 0x94, 0x84, 0xdd, 0x10, 0xbd, 0x27, 0x5d, 0xb8, 0x7a, 0x48, 0x6c, 0x72, 0x76, 0xa2, 0x6e],
          [0x02, 0xeb, 0xcb, 0x79, 0x20, 0xb9, 0x4e, 0xba, 0xb3, 0xf4, 0x90, 0xd8, 0xe4, 0xec, 0x87, 0xdc],
          [0x03, 0x7f, 0x4f, 0xa4, 0x30, 0x04, 0x69, 0xe7, 0x0b, 0x8e, 0xd8, 0xb4, 0x96, 0x9a, 0x25, 0xb2],
          [0x04, 0x15, 0x55, 0xf2, 0x40, 0xb1, 0x9c, 0xb7, 0xa5, 0x2b, 0xe3, 0x73, 0x0b, 0x1b, 0xcd, 0x7b],
          [0x05, 0x81, 0xd1, 0x2f, 0x50, 0x0c, 0xbb, 0xea, 0x1d, 0x51, 0xab, 0x1f, 0x79, 0x6d, 0x6f, 0x15],
          [0x06, 0xfe, 0x9e, 0x8b, 0x60, 0x08, 0xd2, 0x0d, 0x16, 0xdf, 0x73, 0xab, 0xef, 0xf7, 0x4a, 0xa7],
          [0x07, 0x6a, 0x1a, 0x56, 0x70, 0xb5, 0xf5, 0x50, 0xae, 0xa5, 0x3b, 0xc7, 0x9d, 0x81, 0xe8, 0xc9],
          [0x08, 0x2a, 0xaa, 0x27, 0x80, 0xa1, 0xfb, 0xad, 0x89, 0x56, 0x05, 0xe6, 0x16, 0x36, 0x59, 0xf6],
          [0x09, 0xbe, 0x2e, 0xfa, 0x90, 0x1c, 0xdc, 0xf0, 0x31, 0x2c, 0x4d, 0x8a, 0x64, 0x40, 0xfb, 0x98],
          [0x0a, 0xc1, 0x61, 0x5e, 0xa0, 0x18, 0xb5, 0x17, 0x3a, 0xa2, 0x95, 0x3e, 0xf2, 0xda, 0xde, 0x2a],
          [0x0b, 0x55, 0xe5, 0x83, 0xb0, 0xa5, 0x92, 0x4a, 0x82, 0xd8, 0xdd, 0x52, 0x80, 0xac, 0x7c, 0x44],
          [0x0c, 0x3f, 0xff, 0xd5, 0xc0, 0x10, 0x67, 0x1a, 0x2c, 0x7d, 0xe6, 0x95, 0x1d, 0x2d, 0x94, 0x8d],
          [0x0d, 0xab, 0x7b, 0x08, 0xd0, 0xad, 0x40, 0x47, 0x94, 0x07, 0xae, 0xf9, 0x6f, 0x5b, 0x36, 0xe3],
          [0x0e, 0xd4, 0x34, 0xac, 0xe0, 0xa9, 0x29, 0xa0, 0x9f, 0x89, 0x76, 0x4d, 0xf9, 0xc1, 0x13, 0x51],
          [0x0f, 0x40, 0xb0, 0x71, 0xf0, 0x14, 0x0e, 0xfd, 0x27, 0xf3, 0x3e, 0x21, 0x8b, 0xb7, 0xb1, 0x3f],
          [0x10, 0x54, 0x97, 0x4e, 0xc3, 0x81, 0x35, 0x99, 0xd1, 0xac, 0x0a, 0x0f, 0x2c, 0x6c, 0xb2, 0x2f],
          [0x11, 0xc0, 0x13, 0x93, 0xd3, 0x3c, 0x12, 0xc4, 0x69, 0xd6, 0x42, 0x63, 0x5e, 0x1a, 0x10, 0x41],
          [0x12, 0xbf, 0x5c, 0x37, 0xe3, 0x38, 0x7b, 0x23, 0x62, 0x58, 0x9a, 0xd7, 0xc8, 0x80, 0x35, 0xf3],
          [0x13, 0x2b, 0xd8, 0xea, 0xf3, 0x85, 0x5c, 0x7e, 0xda, 0x22, 0xd2, 0xbb, 0xba, 0xf6, 0x97, 0x9d],
          [0x14, 0x41, 0xc2, 0xbc, 0x83, 0x30, 0xa9, 0x2e, 0x74, 0x87, 0xe9, 0x7c, 0x27, 0x77, 0x7f, 0x54],
          [0x15, 0xd5, 0x46, 0x61, 0x93, 0x8d, 0x8e, 0x73, 0xcc, 0xfd, 0xa1, 0x10, 0x55, 0x01, 0xdd, 0x3a],
          [0x16, 0xaa, 0x09, 0xc5, 0xa3, 0x89, 0xe7, 0x94, 0xc7, 0x73, 0x79, 0xa4, 0xc3, 0x9b, 0xf8, 0x88],
          [0x17, 0x3e, 0x8d, 0x18, 0xb3, 0x34, 0xc0, 0xc9, 0x7f, 0x09, 0x31, 0xc8, 0xb1, 0xed, 0x5a, 0xe6],
          [0x18, 0x7e, 0x3d, 0x69, 0x43, 0x20, 0xce, 0x34, 0x58, 0xfa, 0x0f, 0xe9, 0x3a, 0x5a, 0xeb, 0xd9],
          [0x19, 0xea, 0xb9, 0xb4, 0x53, 0x9d, 0xe9, 0x69, 0xe0, 0x80, 0x47, 0x85, 0x48, 0x2c, 0x49, 0xb7],
          [0x1a, 0x95, 0xf6, 0x10, 0x63, 0x99, 0x80, 0x8e, 0xeb, 0x0e, 0x9f, 0x31, 0xde, 0xb6, 0x6c, 0x05],
          [0x1b, 0x01, 0x72, 0xcd, 0x73, 0x24, 0xa7, 0xd3, 0x53, 0x74, 0xd7, 0x5d, 0xac, 0xc0, 0xce, 0x6b],
          [0x1c, 0x6b, 0x68, 0x9b, 0x03, 0x91, 0x52, 0x83, 0xfd, 0xd1, 0xec, 0x9a, 0x31, 0x41, 0x26, 0xa2],
          [0x1d, 0xff, 0xec, 0x46, 0x13, 0x2c, 0x75, 0xde, 0x45, 0xab, 0xa4, 0xf6, 0x43, 0x37, 0x84, 0xcc],
          [0x1e, 0x80, 0xa3, 0xe2, 0x23, 0x28, 0x1c, 0x39, 0x4e, 0x25, 0x7c, 0x42, 0xd5, 0xad, 0xa1, 0x7e],
          [0x1f, 0x14, 0x27, 0x3f, 0x33, 0x95, 0x3b, 0x64, 0xf6, 0x5f, 0x34, 0x2e, 0xa7, 0xdb, 0x03, 0x10],
          [0x20, 0xa8, 0xed, 0x9c, 0x45, 0xc1, 0x6a, 0xf1, 0x61, 0x9b, 0x14, 0x1e, 0x58, 0xd8, 0xa7, 0x5e],]
ITER_KEY = [[0] * 64 for i in range(10)]


BLOCK_SIZE = 16


def XOR(a, b):
    c = [0] * BLOCK_SIZE
    for i in range(BLOCK_SIZE):
        c[i] = a[i] ^ b[i]
    return c


def GF_mul(a, b):
    if a == 0 or b == 0:
        return 0
    GF_a = GF.index(a)
    GF_b = GF.index(b)
    GF_c = (GF_a + GF_b) % 255
    return GF[GF_c]


def nonlinear(in_data):
    out_data = [0] * len(in_data)
    for i in range(BLOCK_SIZE):
        data = in_data[i]
        if data < 0:
            data = data + 256	
        out_data[i] = PI[data]
    return out_data


def iter(state):
    a_15 = 0
    internal = [0] * 16
    for i in range(15, 0, -1):
        internal[i - 1] = state[i]
        a_15 ^= GF_mul(state[i], L_VEC[i])
    a_15 ^= GF_mul(state[0], L_VEC[0])
    internal[15] = a_15
    return internal


def linear(in_data):
    internal = in_data;
    for i in range(16):
        internal = iter(internal)
    return internal


def nonlinear_reverse(in_data):
    out_data = [0] * len(in_data)
    for i in range(BLOCK_SIZE):
        data = in_data[i]
        if data < 0:
            data = data + 256
        out_data[i] = REVERSE_PI[data]
    return out_data


def iter_reverse(state):
    a_0 = state[15]
    internal = [0] * 16
    for i in range(1, 16):
        internal[i] = state[i - 1]
        a_0 ^= GF_mul(internal[i], L_VEC[i])
    internal[0] = a_0
    return internal


def linear_reverse(in_data):
    internal = in_data
    for i in range(16):
        internal = iter_reverse(internal)
    return internal


def create_C():
    iter_num = [[0] * 16 for i in range(32)]
    for i in range(32):
        for j in range(BLOCK_SIZE):
            iter_num[i][j] = 0
        iter_num[i][0] = i + 1
    for i in range(32):
    	ITER_C[i] = linear(iter_num[i])


def one_iter_create_key(in_key_1, in_key_2, iter_const):
    out_key_2 = in_key_1;
    internal = XOR(in_key_1, iter_const)
    internal = nonlinear(internal)
    internal = linear(internal)
    out_key_1 = XOR(internal, in_key_2)
    key = []
    key.append(out_key_1)
    key.append(out_key_2)
    return key;


def create_iter_key(key_1, key_2):
    create_C()
    iter12 = [key_1, key_2]
    ITER_KEY[0] = key_1
    ITER_KEY[1] = key_2
    for i in range(4):
        iter34 = one_iter_create_key(iter12[0], iter12[1], ITER_C[0 + 8 * i])
        iter12 = one_iter_create_key(iter34[0], iter34[1], ITER_C[1 + 8 * i])
        iter34 = one_iter_create_key(iter12[0], iter12[1], ITER_C[2 + 8 * i])
        iter12 = one_iter_create_key(iter34[0], iter34[1], ITER_C[3 + 8 * i])
        iter34 = one_iter_create_key(iter12[0], iter12[1], ITER_C[4 + 8 * i])
        iter12 = one_iter_create_key(iter34[0], iter34[1], ITER_C[5 + 8 * i])
        iter34 = one_iter_create_key(iter12[0], iter12[1], ITER_C[6 + 8 * i])
        iter12 = one_iter_create_key(iter34[0], iter34[1], ITER_C[7 + 8 * i])
        
        ITER_KEY[2 * i + 2] = iter12[0]
        ITER_KEY[2 * i + 3] = iter12[1]


def kuznechik_ecrypt(blk):
    out_blk = [int(blk[i:i+2], 16) for i in range(0, 32, 2)]
    for i in range(9):
        out_blk = XOR(ITER_KEY[i], out_blk)
        out_blk = nonlinear(out_blk)
        out_blk = linear(out_blk)
    out_blk = XOR(out_blk, ITER_KEY[9])
    for i in range(16):
        out_blk[i] = '{:02x}'.format(out_blk[i])
    return ''.join(out_blk)


def kuznechik_derypt(blk):
    out_blk = [int(blk[i:i+2], 16) for i in range(0, 32, 2)]
    out_blk = XOR(out_blk, ITER_KEY[9])
    for i in range(8, -1, -1):
        out_blk = linear_reverse(out_blk)
        out_blk = nonlinear_reverse(out_blk)
        out_blk = XOR(ITER_KEY[i], out_blk)
    for i in range(16):
        out_blk[i] = '{:02x}'.format(out_blk[i])
    return ''.join(out_blk)


def show_C():
    print('[', end='')
    for i in range(10):
        print('[', end='')
        for j in range(64):
            print('0x{:02x}, '.format(ITER_C[i][j]), end='')
        print('0x{:02x}],'.format(ITER_C[i][15]))
    print(']', end='')


if __name__ == "__main__":
    key_1 = [0x27, 0x66, 0x55, 0x44, 0x33, 0x22, 0x11, 0x00, 0xff, 0xee,
             0xdd, 0xcc, 0x2b, 0x3a, 0x99, 0x88]
    key_2 = [0xef, 0x4d, 0xab, 0x89, 0x67, 0xe5, 0xa3, 0xd1, 0x10, 0x32,
             0x54, 0x76, 0x98, 0xfa, 0xdc, 0xfe]
    message = '8899aabbccddeeff0077665544332211'
    print(message)
    create_iter_key(key_1, key_2)
    message = kuznechik_ecrypt(message)
    print(message)
    message = kuznechik_derypt(message)
    print(message)
