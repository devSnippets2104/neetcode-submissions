"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervalLength=len(intervals)

        for i in range(intervalLength):
            meetA=intervals[i]

            for j in range(i+1,intervalLength):
                meetB=intervals[j]

                if min(meetA.end,meetB.end) > max(meetA.start,meetB.start):
                    return False
        return True

