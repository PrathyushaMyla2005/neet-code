class Solution:
    def encode(self, strs):
        """Encode a list of strings to a single string."""
        encoded = ""
        for s in strs:
            # Prefix each string with its length and a special separator '#'
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, encoded):
        """Decode a single string back into a list of strings."""
        result = []
        i = 0
        while i < len(encoded):
            # Find the '#' which separates length from string
            j = i
            while encoded[j] != "#":
                j += 1
            length = int(encoded[i:j])
            # Extract the string of that length
            result.append(encoded[j+1:j+1+length])
            i = j + 1 + length
        return result

# Example usage:
solution = Solution()
encoded_str = solution.encode(["hello", "world"])
print("Encoded:", encoded_str)