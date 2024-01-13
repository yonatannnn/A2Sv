import collections

class Solution:
    def balancedString(self, input_string: str) -> int:
        char_count = collections.Counter(input_string)
        target_length = len(input_string) // 4
        extra_chars = {}

        for key in char_count:
            if char_count[key] > target_length:
                extra_chars[key] = char_count[key] - target_length
        
        if not extra_chars:
            return 0

        start_index = 0
        result_length = len(input_string)

        for end_index in range(len(input_string)):
            if input_string[end_index] in extra_chars:
                extra_chars[input_string[end_index]] -= 1
            
            while max(extra_chars.values()) <= 0:
                result_length = min(result_length, end_index - start_index + 1)
                
                if input_string[start_index] in extra_chars:
                    extra_chars[input_string[start_index]] += 1
                
                start_index += 1
                
        return result_length
