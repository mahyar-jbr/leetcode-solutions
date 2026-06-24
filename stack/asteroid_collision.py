# 735. Asteroid Collision
# Time: O(n) | Space: O(n)
# Stack of surviving asteroids. Collision only when top > 0 and incoming < 0.
# On collision: bigger survives, equal -> both explode. Incoming keeps
# fighting (while loop) until it dies or clears the stack, then is pushed.

class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for a in asteroids:
            alive = True
            while alive and stack and a < 0 and stack[-1] > 0:
                if stack[-1] > abs(a):
                    alive = False
                elif stack[-1] == abs(a):
                    alive = False
                    stack.pop()
                else:
                    stack.pop()
            if alive:
                stack.append(a)

        return stack