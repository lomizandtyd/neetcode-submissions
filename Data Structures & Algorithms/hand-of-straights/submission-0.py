class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False


        hand.sort()
        cnt = Counter(hand)

        start = hand[0]

        for num in hand:
            if cnt[num]:
                for i in range(num, num+groupSize):
                    if i not in cnt or cnt[i] <= 0:
                        return False
                    
                    cnt[i] -= 1

        return True
