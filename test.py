class Solution:
    def bagOfTokensScore(self, tokens: list[int], power: int) -> int:
        tokens.sort()
        scores = []
        if len(tokens) > 2:
            i = len(tokens)-1
            j = len(tokens)-2

            while j >= 0:
                temp_power = power
                score = 0
                if tokens[j] <= temp_power:
                    temp_power -= tokens[j]
                    temp_power += tokens[i]

                    k = 0
                    while k < j and temp_power > 0:
                        temp_power -= tokens[k]
                        score += 1
                    
                    scores.append(score)      
                else:
                    scores.append(score)

                j -= 1
        elif len(tokens) == 2:
            for value in tokens:
                if value <= power:
                    return 1
            return 0
        else:
            if tokens[0] <= power:
                return 1
            return 0

        return max(scores)
s = Solution()

print(s.bagOfTokensScore([100,200,300,400], 200))
