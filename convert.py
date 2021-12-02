import argparse
import re
from flp_convert import dec_to_flp 


def u1_to_u2(b: str):
    if b == '1' * len(b):
        print(f"U1: {b} -> U2: {'0' * len(b)}")
    else:
        print(f"U1: {b} -> U2: {bin(int(b, 2) + 1)[2:]}")


def u2_to_u1(b: str):
    if b[1:] == '0' * (len(b) - 1):
        print(f"Cannot convert to {len(b)} bit U1 binary")
    else:
        if b[0] == '1':
            print(f"U2: {b} -> U1: {bin(int(b, 2) - 1)[2:]}")
        else:
            print(f"U2: {b} -> U1: {b}")


def w_to_utf(word: str):
    int_representation = list(word.encode("utf-8"))
    print(f"""
    Given word {word}

    ------- UTF-8 ------- > 

    {" ".join([bin(x)[2:] for x in int_representation])}
          """)


def nbc_to_bcd(b: str):
    list_of_dec = [bin(int(x) + 32)[4:] for x in str(int(b))]
    print(f"NBC : {b} -> BCD: {' '.join(list_of_dec)}")


def bcd_to_nbc(b: str):
    new_decimal = [str(int(x, 2)) for x in re.findall('....', b)]
    dec_vaule = int(''.join(new_decimal))
    print(f"BCD: {b} -> NBC: {bin(dec_vaule)[2:]}")


def main():
    _parser = argparse.ArgumentParser("""
    Converts between different types of binary numbers
    and more ...

    MODES: 

    * U1toU2 - convert from U1 binary to U2 binary
    * U2toU1 - convert from U2 bianry to U1 binary

    * WtoUTF - convert String word to UTF-8 binary

    * NBCtoBCD - convert NaturalBinaryCode to BinaryCodedDecmal
    * BCDtoNBC - convert BinaryCodedDecimal to NaturalBinaryCode

    * DECtoFLP - convert Decimal float to FLP binary

    """)

    _parser.add_argument('mode', metavar="M", type=str, 
                         help="Select mode for convertion")
    _parser.add_argument('numbers', metavar="N", type=str,
                         help="Pass numbers to convert",
                         nargs="+")

    args = _parser.parse_args()
    mode = args.mode
    for word in args.numbers:
        if mode == "U1toU2":
            u1_to_u2(word)

        elif mode == "U2toU1":
            u2_to_u1(word)

        elif mode == "WtoUTF":
            w_to_utf(word)

        elif mode == "NBCtoBCD":
            nbc_to_bcd(word)

        elif mode == "BCDtoNBC":
            bcd_to_nbc(word)

        elif mode == "DECtoFLP":
            dec_to_flp(float(word))
            

if __name__ == '__main__':
   main()
