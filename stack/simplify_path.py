# 71. Simplify Path
# Time: O(n) | Space: O(n)
# Split path by '/', use stack to track directories.
# Skip '' and '.', pop on '..', push real names. Join with '/' at end.

class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []
        for piece in path.split('/'):
            if piece == '' or piece == '.':
                continue
            elif piece == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(piece)
        return '/' + '/'.join(stack)