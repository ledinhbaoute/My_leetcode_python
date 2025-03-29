#https://leetcode.com/problems/roman-to-integer/
#Ý tưởng: Duyệt qua str, nếu kí tự hiện tại là I, X, C thì kiểm tra giá trị sau đó coi có tạo thành cặp hợp lệ,
#nếu có thì nhận giá trị của cặp ký tự và bỏ qua ký tự kế tiếp (i+=2) 
#nếu không lấy giá trị bình thường và kiểm tra ký tự kế tiếp (i+=1)
class Solution:
    def romanToInt(self, s: str) -> int:
        ref = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = 0
        i = 0
        while i < len(s):
            value = 0
            if i+1 < len(s):
                if s[i] == "I":
                    if s[i+1] == "V":
                        value = 4
                        i+=2
                    elif s[i+1] == "X":
                        value = 9
                        i+=2
                    else:
                        value = ref[s[i]]
                        i+=1
                elif s[i] == "X":
                    if s[i+1] == "L":
                        value = 40
                        i+=2
                    elif s[i+1] == "C":
                        value = 90
                        i+=2
                    else:
                        value = ref[s[i]]
                        i+=1
                elif s[i] == "C":
                    if s[i+1] == "D":
                        value = 400
                        i+=2
                    elif s[i+1] == "M":
                        value = 900
                        i+=2
                    else:
                        value = ref[s[i]]
                        i+=1
                else:
                    value = ref[s[i]]
                    i+=1
            else:
                value = ref[s[i]]
                i+=1
            num+=value
        return num