import math


def frequency_bit_test(bit_string: str) -> float:
    """
    Performs frequency bit test.

    The frequency bit test is a statistical test used to determine whether a sequence of bits is random.
    The test is based on the assumption that the probability of a 0 or 1 bit occurring is equal.
    The test statistic is the sum of the differences between the number of 0s and 1s in the sequence.
    The p-value is the probability of obtaining a test statistic as extreme as, or more extreme than,
    the observed test statistic, assuming that the sequence is random.

    Args:
        bit_string (str): The bit sequence to test.

    Returns:
        float: The p-value of the test. 
        If the value tends to 1, then it is said that the generator tends to be ideal.
        If the P-value tends to 0, the generator is completely predictable.

    Raises:
        ValueError: the input string is not a bitstring.
    """

    if any([symbol not in ['0','1'] for symbol in bit_string]):
        raise ValueError("This is not a bitstring")

    sum = 0
    for bit in bit_string:
        if bit == '1':
            sum += 1
        else:
            sum += -1

    p_value = math.erfc(abs(sum / math.sqrt(len(bit_string)) / math.sqrt(2)))
    return p_value


def consecutive_bits_test(bit_string: str) -> float:
    """
    Performs consecutive bits test.

    The test is about finding all sequences of the same bits. 
    Then the number and sizes of these sequences are analyzed for compliance with a truly random
    reference sequence. The main task of this test is to determine how often the change from "1" to "0" and back occurs.

    Args:
        bit_string (str): The bit sequence to test.

    Returns:
        float: The p-value of the test. 
        If the value tends to 1, then it is said that the generator tends to be ideal.
        If the P-value tends to 0, the generator is completely predictable.

    Raises:
        ValueError: the input string is not a bitstring.
    """

    if any([symbol not in ['0','1'] for symbol in bit_string]):
        raise ValueError("This is not a bitstring")

    ones_ratio = bit_string.count('1') / len(bit_string)

    if abs(ones_ratio - 0.5) < (2 / math.sqrt(len(bit_string))):
        sign_alteration_count = sum(
            [0 if bit_string[i] == bit_string[i + 1] else 1
            for i in range(len(bit_string) - 1)]
            )

        p_value = math.erfc(
            abs(sign_alteration_count - 2 * len(bit_string) * ones_ratio * (1 - ones_ratio)) / (
                2 * math.sqrt(2 * len(bit_string)) * ones_ratio * (1 - ones_ratio))
            )
    else:
        p_value = 0
    
    return p_value


def main() -> None:
    paths = read_json("paths.json")
    task1_paths = paths["task1"]

    russian_alphabet = dict(read_json(task1_paths["key"])["alphabet"]).keys()
    set_new_cypher_parameters(task1_paths["key"], new_alphabet=russian_alphabet, new_key="панграмма")
    
    write_txt(task1_paths["result"], cypher_text(read_txt(task1_paths["message"]), read_json(task1_paths["key"])))
    write_txt(task1_paths["result_decypher"], decypher_text(read_txt(task1_paths["result"]), read_json(task1_paths["key"])))


if __name__ == '__main__':
    main() 