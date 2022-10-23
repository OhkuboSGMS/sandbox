from PIL import ImageDraw
import string
import  numpy as np
def main():
    ascii_str = string.ascii_lowercase
    unicode_tbl = [hex(ord(c)) for c in ascii_str]
    np_u_tbl = np.array(unicode_tbl)
    print(np_u_tbl.dtype)

    print(unicode_tbl)


if __name__ == '__main__':
    main()