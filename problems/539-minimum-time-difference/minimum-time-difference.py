def to_minutes(time):
    hour, minute = map(int, time.split(':'))
    return hour * 60 + minute

class Solution:
    def findMinDifference(self, tp: List[str]) -> int:
        minutes = [to_minutes(time) for time in tp]
        minutes.sort()
        min_diff = 10**20
        for i in range(len(minutes)):
            diff = minutes[(i + 1) % len(minutes)] - minutes[i]
            if diff < 0:
                diff += 1440
            min_diff = min(min_diff, diff)
    
        return min_diff