def cacheit(func):
    func_name = func.__name__
    
    def memoize_wrapper(self, *args):
        key = func_name,args
        pos = self.mark()
        memo = self.memos.get(pos)
        if memo is None:
            memo = self.memos[pos] = {}
        key = (func, args)
        if key in memo:
            res, endpos = memo[key]
            self.reset(endpos)
        else:
            res = func(self, *args)
            endpos = self.mark()
            memo[key] = res, endpos
        return res
    memoize_wrapper = func_name
    return memoize_wrapper