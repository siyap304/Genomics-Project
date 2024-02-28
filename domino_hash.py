# This code includes the hash function tested on a NCBI sequence, same test cases for smith-waterman

class HashNode:
    def __init__(self, key):
        """
        Initializes a node for the hash table, containing the key-value

        Args:
            key
        """
        self.key = key
        self.next = None

def binary_to_decimal(binary):
    """
    Converts a binary string to its decimal equivalent

    Args:
        binary: A string representing a binary number

    Returns:
        The decimal representation of the binary number
    """
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

class HashTable:
    def __init__(self, size):
        """
        Initializes a hash table with a given size

        Args:
            size: The size of the hash table
        """
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        """
        Computes the hash value for a given key (which is essentiatlly the binary representation of the k-mer)

        Args:
            key: The key to be hashed

        Returns:
            The hash value
        """
        return binary_to_decimal(key)

    def insert(self, key):
        """
        Inserts the key into the hash table

        Args:
            key
        """
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = HashNode(key)
        else:
            node = self.table[index]
            while node.next is not None:
                node = node.next
            node.next = HashNode(key)

    def search(self, key):
        """
        Searches for a key in the hash table and returns the index if found

        Args:
            key

        Returns:
            The index of the hash table if key is found, otherwise -1
        """
        index = self.hash(key)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return index
            node = node.next
        return -1

    def print_table(self):
        # Prints the contents of the hash table
        for index, node in enumerate(self.table):
            print(f'Index {index}: ', end='')
            while node is not None:
                print(f'({node.key}) -> ', end='')
                node = node.next
            print("None")

# Making a hash table of the required size
hash_table = HashTable(256)

def genome_to_binary(seq):
    """
    Converts the k-mer into a binary number following A=00, T=01, G=10, C=11

    Args:
      seq: the k-mer in a string form

    Returns:
      The binary version of the k-mer in a string form

    """
    binary=""
    for i in seq:
      if i == "A":
        binary = binary + "00"
      elif i == "T":
        binary = binary + "01"
      elif i == "G":
        binary = binary + "10"
      elif i == "C":
        binary = binary + "11"

    return binary

sequence = "GCATCTCCTCCTCCCTCTCCCCGGGCTCCTACTGGCCTGAGGTTGAGGGCGGCTGGGGGCTCGGGGCAGGCTCCGCGGCGTTCCCCTCCCCACCCCGGCCCTCCGTTCAGCCGCGCTCCTCCGGGGCTGCGGTTCCTACTGCGCGAGCTGCCAGTGGATTCGCTCTTTTCCTCCGTCCGTGGCCCGCCTGGGCGGCCTTGTTCTTTCCGCAGCAGCCAGATAACCTTCTGTTCGGTGATGAAATTATCACTAATGGTTTTCATTCCTGTGAAAGTGATGAGGAGGATAGAGCCTCACATGCAAGCTCTAGTGACTGGACTCCAAGGCCACGGATAGGTCCATATACTTTTGTTCAGCAACATCTTATGATTGGCACAGATCCTCGAACAATTCTTAAAGATTTATTGCCGGAAACAATACCTCCACCTGAGTTGGATGATATGACACTGTGGCAGATTGTTATTAATATCCTTTCAGAACCACCAAAAAGGAAAAAAAGAAAAGATATTAATACAATTGAAGATGCTGTGAAATTACTGCAAGAGTGCAAAAAAATTATAGTTCTAACTGGAGCTGGGGTGTCTGTTTCATGTGGAATACCTGACTTCAGGTCAAGGGATGGTATTTATGCTCGCCTTGCTGTAGACTTCCCAGATCTTCCAGATCCTCAAGCGATGTTTGATATTGAATATTTCAGAAAAGATCCAAGACCATTCTTCAAGTTTGCAAAGAAGAAACAGCATTGAAGCATTATTTGGGGGGAAAAACACACACACAAAATCCAGCAACTCAGCATTCATGAGCAACTCTATACTATACCAGTATGTGCCTGTGCAGTGGAAGGAAAACAATTTTGGAAATATATCCTGGACAATTCCAGCCATCTCTCTGTCACAAATTCATAGCCTTGTCAGATAAGGAAGGAAAACTACTTCGCAACTATACCCAGAACATAGACACGCTGGAACAGGTTGCGGGAATCCAAAGGATAATTCAGTGTCATGGTTCCTTTGCAACAGCATCTTGCCTGATTTGTAAATACAAAGTTGACTGTGAAGCTGTACGAGGAGATATTTTTAATCAGGTAGTTCCTCGATGTCCTAGGTGCCCAGCTGATGAACCGCTTGCTATCATGAAACCAGAGATTGTGTTTTTTGGTGAAAATTTACCAGAACAGTTTCATAGAGCCATGAAGTATGACAAAGATGAAGTTGACCTCCTCATTGTTATTGGGTCTTCCCTCAAAGTAAGACCAGTAGCACTAATTCCAAGTTCCATACCCCATGAAGTGCCTCAGATATTAATTAATAGAGAACCTTTGCCTCATCTGCATTTTGATGTAGAGCTTCTTGGAGACTGTGATGTCATAATTAATGAATTGTGTCATAGGTTAGGTGGTGAATATGCCAAACTTTGCTGTAACCCTGTAAAGCTTTCAGAAATTACTGAAAAACCTCCACGAACACAAAAAGAATTGGCTTATTTGTCAGAGTTGCCACCCACACCTCTTCATGTTTCAGAAGACTCAAGTTCACCAGAAAGAACTTCACCACCAGATTCTTCAGTGATTGTCACACTTTTAGACCAAGCAGCTAAGAGTAATGATGATTTAGATGTGTCTGAATCAAAAGGTTGTATGGAAGAAAAACCACAGGAAGTACAAACTTCTAGGAATGTTGAAAGTATTGCTGAACAGATGGAAAATCCGGATTTGAAGAATGTTGGTTCTAGTACTGGGGAGAAAAATGAAAGAACTTCAGTGGCTGGAACAGTGAGAAAATGCTGGCCTAATAGAGTGGCAAAGGAGCAGATTAGTAGGCGGCTTGATGGTAATCAGTATCTGTTTTTGCCACCAAATCGTTACATTTTCCATGGCGCTGAGGTATATTCAGACTCTGAAGATGACGTCTTATCCTCTAGTTCTTGTGGCAGTAACAGTGATAGTGGGACATGCCAGAGTCCAAGTTTAGAAGAACCCATGGAGGATGAAAGTGAAATTGAAGAATTCTACAATGGCTTAGAAGATGAGCCTGATGTTCCAGAGAGAGCTGGAGGAGCTGGATTTGGGACTGATGGAGATGATCAAGAGGCAATTAATGAAGCTATATCTGTGAAACAGGAAGTAACAGACATGAACTATCCATCAAACAAATCATAGTGTAATAATTGTGCAGGTACAGGAATTGTTCCACCAGCATTAGGAACTTTAGCATGTCAAAATGAATGTTTACTTGTGAACTCGATAGAGCAAGGAAACCAGAAAGGTGTAATATTTATAGGTTGGTAAAATAGATTGTTTTTCATGGATAATTTTTAACTTCATTATTTCTGTACTTGTACAAACTCAACACTAACTTTTTTTTTTTTAAAAAAAAAAAGGTACTAAGTATCTTCAATCAGCTGTTGGTCAAGACTAACTTTCTTTTAAAGGTTCATTTGTATGATAAATTCATATGTGTATATATAATTTTTTTTGTTTTGTCTAGTGAGTTTCAACATTTTTAAAGTTTTCAAAAAGCCATCGGAATGTTAAATTAATGTAAAGGGAACAGCTAATCTAGACCAAAGAATGGTATTTTCACTTTTCTTTGTAACATTGAATGGTTTGAAGTACTCAAAATCTGTTACGCTAAACTTTTGATTCTTTAACACAATTATTTTTAAACACTGGCATTTTCCAAAACTGTGGCAGCTAACTTTTTAAAATCTCAAATGACATGCAGTGTGAGTAGAAGGAAGTCAACAATATGTGGGGAGAGCACTCGGTTGTCTTTACTTTTAAAAGTAATACTTGGTGCTAAGAATTTCAGGATTATTGTATTTACGTTCAAATGAAGATGGCTTTTGTACTTCCTGTGGACATGTAGCAATGTCTATATTGGCTCATAAAACTAACCTGAAAAACAAATAAATGCTTTGGAAATGTTTCAGTTGCTTTAGAAACATTAGTGCCTGCCTGGATCCCCTTAGTTTTGAAATATTTGCCATTGTTGTTTAAATACCTATCACTGTGGTAGAGCTTGCATTGATCTTTTCCACAAGTATTAAACTGCCAAAATGTGAATATGCAAAGCCTTTCTGAATCTATAATAATGGTACTTCTACTGGGGAGAGTGTAATATTTTGGACTGCTGTTTTCCATTAATGAGGAGAGCAACAGGCCCCTGATTATACAGTTCCAAAGTAATAAGATGTTAATTGTAATTCAGCCAGAAAGTACATGTCTCCCATTGGGAGGATTTGGTGTTAAATACCAAACTGCTAGCCCTAGTATTATGGAGATGAACATGATGATGTAACTTGTAATAGCAGAATAGTTAATGAATGAAACTAGTTCTTATAATTTATCTTTATTTAAAAGCTTAGCCTGCCTTAAAACTAGAGATCAACTTTCTCAGCTGCAAAAGCTTCTAGTCTTTCAAGAAGTTCATACTTTATGAAATTGCACAGTAAGCATTTATTTTTCAGACCATTTTTGAACATCACTCCTAAATTAATAAAGTATTCCTCTGTTGCTTTAGTATTTATTACAATAAAAAGGGTTTGAAATATAGCTGTTCTTTATGCATAAAACACCCAGCTAGGACCATTACTGCCAGAGAAAAAAATCGTATTGAATGGCCATTTCCCTACTTATAAGATGTCTCAATCTGAATTTATTTGGCTACACTAAAGAATGCAGTATATTTAGTTTTCCATTTGCATGATGTTTGTGTGCTATAGATGATATTTTAAATTGAAAAGTTTGTTTTAAATTATTTTTACAGTGAAGACTGTTTTCAGCTCTTTTTATATTGTACATAGTCTTTTATGTAATTTACTGGCATATGTTTTGTAGACTGTTTAATGACTGGATATCTTCCTTCAACTTTTGAAATACAAAACCAGTGTTTTTTACTTGTACACTGTTTTAAAGTCTATTAAAATTGTCATTTGACTTTTTTCTGTT"
seq = "CTGAGCTACTATC"

k = 0
while k < len(sequence):
    current = sequence[k:k+4]
    k = k + 4
    # print(current)
    # print(genome_to_binary(current))
    hash_table.insert(genome_to_binary(current))

hash_table.print_table()

k = 0
while k < len(seq):
    current = seq[k:k+4]
    k = k + 4
    print(current)
    print(hash_table.search(genome_to_binary(current)))
