# Numeral System Calculator

HEX_VALUES = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

# Convert binary to decimal
def bin2dec(num: str) -> int:
    result = 0
    # Iterating over the bits of the number
    for index, digit in enumerate(reversed(num)):
        result += 2**index * int(digit)
    return result

# Convert hexadecimal to decimal
def hex2dec(num: str) -> int:
    result = 0
    # Iterating over the characters of the number
    for index, digit in enumerate(reversed(str(num))):
        if digit.isdigit():
            result += 16**index * int(digit)
        else:
            # Finding letter's corresponding value in the HEX_VALUES dictionary
            result += 16**index * next(key for key, val in HEX_VALUES.items() if val == digit.upper())
    return result

# Convert decimal to hexadecimal
def dec2hex(num: str) -> str:
    num = int(num)
    result = ""
    # Iterating over the digits of the number
    while num > 0:
        remainder = num % 16
        # Use the letter representation from the HEX_VALUES dictionary
        if remainder > 9:
            result += HEX_VALUES[remainder]
        else:
            result += str(remainder)
        num //= 16
    return result[::-1]

# Convert decimal to binary
def dec2bin(num: str) -> int:
    num = int(num)
    result = ""
    # Iterating over the digits of the number
    while num > 0:
        result += str(num % 2)
        num //= 2
    return int(result[::-1])

# Convert a number with base from 1 to 9 to decimal
def uptonine2dec(num: str, base: int) -> int:
    num = [int(i) for i in num]
    result = 0
    # Iterating over the digits of the number
    for i in num:
        # 'Any' base conversion formula
        result += base**i * i
    return result

def main():
    print(bin2dec('1010111'))
    print(hex2dec('d125c'))
    print(dec2hex('29345'))
    print(dec2bin('91457'))
    print(uptonine2dec('2313', 4))


if __name__ == "__main__":
    main()