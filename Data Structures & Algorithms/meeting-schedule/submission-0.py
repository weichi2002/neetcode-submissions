"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res = self.sort(intervals)
        for i in range(1, len(res)):
            e1 = res[i-1][1]
            s2 = res[i][0]
            if s2 < e1:
                return False
        
        return True



    def sort(self, intervals):
        #we want to make an array of tuples tracking the volume
        array = []
        for i in intervals:
            start = i.start
            end = i.end
            array.append([start, end])

        array.sort()

        return array
        



        
        #if this meeting is inside the other meeting
        #the first time is greater than the second one 




        
