class codec:
    def encode(self,strs):
        encode = " "
        for word in strs:
            encode += word + " "
        return encode.strip()
    def decode(self,encode):
        result = []
        i = 0
        while i < len(encode):
            j = i
            while j < len(encode) and encode[j] != " ":
                j += 1
            result.append(encode[i:j])
            i = j + 1
        return result
# Example usage:
codec_instance = codec()
encoded_string = codec_instance.encode(["hello", "world", "this", "is", "codec"])
print("Encoded String:", encoded_string)
'''✅ T.C ≈ O(L) (but technically could degrade toward O(n²·k) due to repeated concatenation).
✅ S.C = O(L)
'''