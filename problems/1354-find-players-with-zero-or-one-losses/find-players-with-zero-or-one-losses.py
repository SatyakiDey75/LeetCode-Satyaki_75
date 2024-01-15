class Solution(object):
    def findWinners(self, matches):
        z_l,o_l,m_l=set(),set(),set()
        for w,l in matches:
            if w not in o_l and w not in m_l:
                z_l.add(w)
            if l in z_l:
                z_l.remove(l)
                o_l.add(l)
            elif l in o_l:
                o_l.remove(l)
                m_l.add(l)
            elif l in m_l:
                continue
            else:
                o_l.add(l)          
        return [sorted(list(z_l)), sorted(list(o_l))]