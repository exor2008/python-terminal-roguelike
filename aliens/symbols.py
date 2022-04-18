import numpy as np

SYMB_EMPTY = 31 * 16 + 15
SYMB_BOX = 27 * 16+3
SYMB_FIRST_TUBE = 27 * 16 + 3
SYMB_LAST_TUBE = 29 * 16 + 11
SYMB_MARINE = 16 * 16
SYMB_FLOOR = 18 * 16 #27 * 16
SYMB_DOT = 31 * 16 + 10
SYMB_CAMERA = 16 * 16 + 8
SYMB_ALIEN = 24 * 16
SYMB_HIVE = 25 * 16

SYMB_DL, SYMB_L, SYMB_UL, SYMB_U = np.arange(24 * 16 + 12, 24 * 16 + 16)
SYMB_UR, SYMB_R, SYMB_DR, SYMB_D = np.arange(25 * 16 + 12, 25 * 16 + 16)

def random_tubes(shape):
    return np.random.randint(SYMB_FIRST_TUBE, SYMB_LAST_TUBE, size=shape)