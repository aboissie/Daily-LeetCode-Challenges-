class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        h1v = len([_ for _ in s[:len(s)//2] if _ in vowels])
        h2v = len([_ for _ in s[len(s)//2:] if _ in vowels])
        return h1v == h2v