
def isAnagram(s: str, t: str) -> bool:
    class Solution:
        def isAnagram(self, s: str, t: str) -> bool:
            smap, tmap = {}, {}

            # check if same length
            if len(s) == len(t) and len(s) != 0:
                # two pointers
                for i in range(0, (len(s))):
                    scount = 1 + smap.get(s[i], 0)  # set the default val to 0
                    tcount = 1 + tmap.get(t[i], 0)  # set the default val to 0
                    smap[s[i]] = scount
                    tmap[t[i]] = tcount

                # compare key values
                for key in smap:
                    if smap[key] != tmap.get(key, 0):
                        return False

                for key in tmap:
                    if tmap[key] != smap.get(key, 0):
                        return False

                return True
            return False

s = 'racecar'
t = 'carrace'
isAnagram(s,t)