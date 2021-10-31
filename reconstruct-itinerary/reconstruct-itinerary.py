from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.len_tic =0
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        self.len_tic = len(tickets)
        adj_list = defaultdict(list)
        visited_edge = defaultdict(list)
        for ticket in tickets:
            adj_list[ticket[0]].append(ticket[1])
            visited_edge[ticket[0]].append(False)
        for key, value in adj_list.iteritems():
            value.sort()
        path = []
        stack =[]
        stack.append('JFK')
        while(stack):
            #print(stack)
            a = stack.pop()
            place_list = adj_list[a]
            #print('placelist')
            #print(place_list)
            if not place_list:
                path.append(a)
            else:
                stack.append(a)
                stack.append(place_list[0])
                adj_list[a].remove(place_list[0])
    
        return path[::-1]
                