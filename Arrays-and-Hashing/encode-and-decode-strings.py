class Solution:
    def encode(strs):
        return('SHOULDBECSV'.join(strs));
    def decode(str):
        return(str.split('SHOULDBECSV'));

print(Solution.decode(Solution.encode(["neet","code","love","you"])));
