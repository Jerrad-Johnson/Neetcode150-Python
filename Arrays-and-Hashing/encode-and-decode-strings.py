class Solution:
    def encode(strs):
        return('SHOULDBECSV'.join(strs));
    def decode(str):
        return(str.split('SHOULDBECSV'));


encoded = Solution.encode(["neet","code","love","you"]);
print(Solution.decode(encoded));