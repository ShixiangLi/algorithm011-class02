class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct = {}
        s_lst = []
        new = 1
        for i in s:
            if i in dct:
                s_lst.append(dct[i])
            else:
                dct[i] = new
                s_lst.append(new)
                new += 1

        dct = {}
        t_lst = []
        new = 1
        for i in t:
            if i in dct:
                t_lst.append(dct[i])
            else:
                dct[i] = new
                t_lst.append(new)
                new += 1

        return s_lst == t_lst