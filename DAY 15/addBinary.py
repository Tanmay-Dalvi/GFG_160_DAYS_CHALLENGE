class Solution:
    def addBinary(self, s1, s2):
        i, j = len(s1) - 1, len(s2) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            bit1 = int(s1[i]) if i >= 0 else 0
            bit2 = int(s2[j]) if j >= 0 else 0

            total = bit1 + bit2 + carry
            carry = total // 2
            result.append(str(total % 2))

            i -= 1
            j -= 1

        result_str = ''.join(reversed(result))
        return result_str.lstrip('0') or '0'
