# 68. Text Justification
# Time: O(n * m) | Space: O(k) where k = maxWidth
# Greedy line packing + space distribution

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        current_line = []
        current_length = 0

        for word in words:
            neededLength = current_length + len(word) + len(current_line)
            
            if neededLength > maxWidth:
                result.append(self.justify_line(current_line, current_length, maxWidth))
                current_line = [word]
                current_length = len(word)
            else:
                current_line.append(word)
                current_length += len(word)
        
        last_line = " ".join(current_line)
        last_line += " " * (maxWidth - len(last_line))
        result.append(last_line)

        return result

    def justify_line(self, current_line, current_length, maxWidth):
        total_spaces = maxWidth - current_length
        gaps = len(current_line) - 1

        if gaps == 0:
            return current_line[0] + " " * total_spaces

        space_per_gap = total_spaces // gaps
        extra_spaces = total_spaces % gaps

        result = ""
        for i in range(len(current_line)):
            result += current_line[i]

            if i < len(current_line) - 1:
                result += " " * space_per_gap
                
                if i < extra_spaces:
                    result += " "

        return result