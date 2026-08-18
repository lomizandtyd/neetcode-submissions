class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) <= 1:
            return len(position)

        stack = []

        for pos, spd in sorted(zip(position, speed), reverse=True):
            if not stack:
                stack.append((target-pos)/spd)
            else:
                ts = (target-pos) / spd
                if ts > stack[-1]:
                    stack.append(ts)

        return len(stack)

                


