"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda i: i.start)

        for i in range(len(intervals)-1):
            m1 = intervals[i]
            m2 = intervals[i+1]

            if m2.start < m1.end:
                return False

        return True
            
