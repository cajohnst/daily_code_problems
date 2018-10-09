"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def count_msg_combinations(abc_to_int_map, msg):
    """
    This function assumes the abc to integer map contains only integers < 100.
    Otherwise this code disincludes 3 digit codes
    
    dtype msg: str
    dtype abc_to_int_map: dict

    rtype: int 
    """

    num_combinations = 0

    for ix, code_num in enumerate(msg):
        if not ix == len(msg) - 1:
            two_dig_code = msg[ix:ix+2]

            if int(two_dig_code) in abc_to_int_map.values():
                num_combinations += 1

        if int(code_num) in abc_to_int_map.values():
            num_combinations += 1

    return num_combinations

if __name__ == "__main__":
    abc_to_int_map = {
    "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9,
    "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, 
    "r":18, "s":19, "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, 
    "z":26
    }

    msg = "1232192142"

    num_combinations = count_msg_combinations(abc_to_int_map, msg)

    print(f"total combinations: {num_combinations}")

    