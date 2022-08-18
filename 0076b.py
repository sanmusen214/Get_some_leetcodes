class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need=dict()
        window=dict()
        lenres=[float("inf"),-1,-1]
        def needs():
            for each in need:
                if need[each]>0:
                    return False
            return True
        for c in t:
            need[c]=need.get(c,0)+1
        
        left = right = 0
        valid = 0
        while right < len(s):
            # c 是将移入窗口的字符
            c = s[right]
            # 增大窗口
            right+=1
            # 进行窗口内数据的一系列更新
            if(c in need):
                need[c]=need.get(c,0)-1

            # debug 输出的位置
            # print("window: [{},{})".format(left, right),need)
            
            # 判断左侧窗口是否要收缩
            while needs():
                lenres=min(lenres,[right-left,left,right])
                # d 是将移出窗口的字符
                if(left>=len(s)):
                    break
                d = s[left]
                # 缩小窗口
                left+=1
                # 进行窗口内数据的一系列更新
                if(d in need):
                    need[d]=need.get(d,0)+1
        return s[lenres[1]:lenres[2]]

a=Solution()
print(a.minWindow("ADOBECODEBANC","ABC"))