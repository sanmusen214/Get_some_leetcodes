
class Solution:
    def pathInZigZagTree(self, label: int):
        temp=label
        track=[]
        while(temp>=1):
            track.insert(0,temp)
            temp=int(temp/2)
        for i in range(len(track)-1):
            if(i%2==1-(len(track)-1)%2):
                track[i]=2**i+2**(i+1)-1-track[i]
        return track
a=Solution()
print(a.pathInZigZagTree(26))
