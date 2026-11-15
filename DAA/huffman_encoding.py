import heapq

class Node:
    def __init__(self, symbol, freq, left=None, right=None):
        self.symbol = symbol
        self.freq = freq
        self.left = left
        self.right = right


def generate(root, code=""):
    if root.left is None and root.right is None:
        codes[root.symbol] = code or "0"
        return

    generate(root.left, code + "0")
    generate(root.right, code + "1")


n = int(input("Enter number of symbols: "))

if n <= 0:
    print("Invalid input")
else:
    pq = []
    symbols = []
    codes = {}
    unique = set()

    print("Enter symbols and frequencies (e.g. A 5):")

    for i in range(n):
        ch, f = input().split()
        f = int(f)

        if ch in unique or f <= 0:
            print("Invalid input")
            break

        unique.add(ch)
        symbols.append(ch)
        heapq.heappush(pq, (f, i, Node(ch, f)))

    else:
        # Build Huffman Tree
        while len(pq) > 1:
            f1, i1, left = heapq.heappop(pq)
            f2, i2, right = heapq.heappop(pq)

            parent = Node(None, f1 + f2, left, right)
            heapq.heappush(pq, (parent.freq, n + i1 + i2 + 1, parent))

        root = pq[0][2]

        generate(root)

        print("\nHuffman Codes:")
        for ch in symbols:
            print(ch, ":", codes[ch])

        # Encode Message
        message = input("\nEnter message to encode: ")

        if all(ch in codes for ch in message):
            encoded = "".join(codes[ch] for ch in message)
            print("Encoded message:", encoded)
        else:
            print("Message contains an unknown symbol")