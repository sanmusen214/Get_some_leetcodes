class Solution:
    def fullJustify(self, words, maxWidth: int):
        results=[]
        thislayer=[]
        ptr=0
        thislayer_len=0
        def normalizy(str_list:list,remain_space):
            '''
            将str_list按照remain_space数量等距离插入空格，多出来的空格放到第一个间隙处
            '''
            if(len(str_list)==1):
                str_list.append(remain_space*" ")
            else:
                # 此处注意str_list要去掉间隙数量，也就是-1/2
                if(remain_space<((len(str_list)-1)/2)):
                    for i in range(remain_space):
                        str_list[i*2+1]+=" "
                else:
                    everypich=int(remain_space/((len(str_list)-1)/2))
                    first_pich_plus=int(remain_space%((len(str_list)-1)/2))
                    for i in range(len(str_list)-1,-1,-1):
                        if(i%2==1):
                            str_list[i]+=(everypich*" ")
                    str_list[1]+=(first_pich_plus*" ")
            return str_list
        while(ptr<len(words)):
            #可添加
            if(thislayer_len==0 and len(words[ptr])+thislayer_len<=maxWidth):
                thislayer.append(words[ptr])
                thislayer_len+=(len(words[ptr]))
                ptr+=1
            elif(len(words[ptr])+thislayer_len+1<=maxWidth):
                thislayer.append(" ")
                thislayer.append(words[ptr])
                thislayer_len+=(len(words[ptr])+1)
                ptr+=1
            else:
                #对齐thislayer所有元素,添加到results
                print("for :{}, spaces is{}".format(thislayer,thislayer_len))
                thislayer=normalizy(thislayer,maxWidth-thislayer_len)
                results.append("".join(thislayer))
                thislayer=[]
                thislayer_len=0
        #最后一行特殊处理，多余空格全放右边
        thislayer.append((maxWidth-thislayer_len)*" ")
        results.append("".join(thislayer))
        return results
                
a=Solution()
print(a.fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20))
print(a.fullJustify(["Listen","to","many,","speak","to","a","few."],6))
            