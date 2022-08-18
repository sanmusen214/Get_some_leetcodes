class TimeMap:
    def __init__(self):
        self.totalset={}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.totalset:
            self.totalset[key][timestamp]=value
        else:
            self.totalset[key]={timestamp:value}

    def get(self, key: str, timestamp: int) -> str:
        if(key not in self.totalset):
            return ""
        else:
            if(timestamp in self.totalset[key]):
                return self.totalset[key][timestamp]
            m=-1
            for eachtime in self.totalset[key]:
                if(eachtime>m and eachtime<timestamp):
                    m=eachtime
            if(m==-1):
                return ""
            else:
                return self.totalset[key][m]
                
            
         
                    

