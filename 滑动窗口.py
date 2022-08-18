def slidingWindow(s,t):
    need=dict()
    window=dict()
    
    for c in t:
        need[c]=need.get(c,0)+1
    
    left = right = 0
    valid = 0
    while (right < len(s)):
        # c 是将移入窗口的字符
        c = s[right]
        # 增大窗口
        right+=1
        # 进行窗口内数据的一系列更新
        ...
        # debug 输出的位置
        print("window: [{},{})".format(left, right))
        
        # 判断左侧窗口是否要收缩
        while window needs shrink:
            # d 是将移出窗口的字符
            d = s[left]
            # 缩小窗口
            left+=1
            # 进行窗口内数据的一系列更新
            ...