class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0 # pointer on which the repeatition is found
        right = 0 # pointer for the current position
        temp_list=[] # temporary list for every substring 
        temp_dict={} # dictionary for storing the indices of the character
        length = 0 # length of the longest substring

        for c in s:
            if c in temp_list:
                left = temp_dict[c] + 1
                temp_dict[c] = right # updating the indices if any repeatition is found
                right = right + 1

            else:
                temp_dict[c] = right
                right = right + 1
            temp_list = s[left : right]
            length = length if length > len(temp_list) else len(temp_list)
            # print(temp_list)
        return length
