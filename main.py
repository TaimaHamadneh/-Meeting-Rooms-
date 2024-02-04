"""
    Definition of interval.
"""

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
             
class solution:
    def minMeetingRooms(Self, intervals):
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        
        res, count = 0,0
        s, e = 0,0
        while s < len(intervals):
            if start[s] < end[e]:
                s+= 1
                count +=1 
            else:
                e+=1
                count -=1    
            res = max(res, count)    
        return res     
    
def main():
    # Creating sample intervals
   intervals = [
        Interval(5, 30),
        Interval(5, 10), 
        Interval(10, 15)
        ## Example: 
        ## Interval(5, 30),
        ## Interval(5, 10), 
        ## Interval(10, 15)
        ### 5*****||***||**********************30
        ### 5*****||10 ||  
        ### ------||10*||****15
      
        ## Example: 
        ## Interval(5, 10),
        ## Interval(15, 30), 
        ### 5*****10||    
        ###  -------||---15***************30

    ]
    
    sol = solution()
    result = sol.minMeetingRooms(intervals)

    print("Minimum number of meeting rooms required:", result)

if __name__ == "__main__":
    main()
