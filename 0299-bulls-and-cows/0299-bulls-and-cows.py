class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        dig_secret = {}
        dig_guess = {}
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                dig_secret[secret[i]] = dig_secret.get(secret[i], 0) + 1
                dig_guess[guess[i]] = dig_guess.get(guess[i], 0) + 1
        
        for d in dig_secret:
            if d in dig_guess:
                cows += min(dig_secret[d], dig_guess[d])

        return f"{bulls}A{cows}B"
        