class Solution:
    def displayTable(self, orders):
        records={}
        table=[]
        foods=[]
        for each in orders:
            #未出现的桌号
            if each[1] not in records:
                table.append(each[1])
                records[each[1]]={}
            #未出现的食物名字
            if each[2] not in foods:
                foods.append(each[2])
            #桌号里未出现的食物
            if each[2] not in records[each[1]]:
                records[each[1]][each[2]]=1
            #桌号里已出现的食物
            else:
                records[each[1]][each[2]]+=1
        table.sort(key=int)
        foods.sort()
        biglist=[["Table"]+foods]
        for dex in table:
            tlist=[dex]
            for food in foods:
                if food not in records[dex]:
                    tlist.append("0")
                else:
                    tlist.append(str(records[dex][food]))
            biglist.append(tlist)
        return biglist
                
    
a=Solution()
print(a.displayTable([["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]))
            