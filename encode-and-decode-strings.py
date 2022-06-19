# Encode and Decode Strings
# join/split string by chr(257),  return chr(258) for empty string
# time: O(1), space: O(1)/O(N) en/decode
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # 256 valid ascii chars, use non-ascii as delimiter
        if len(strs) == 0:
            return chr(258)
        return chr(257).join(strs)
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if s == chr(258):
            return []
        return s.split(chr(257))


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
