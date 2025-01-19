from flight import Flight

def comp(o1,o2):
    return (o1[0],o1[1].flight_no) < (o2[0],o2[1].flight_no)

positive_infinity = float('inf')
'''
Python Code to implement a heap with general comparison function
'''

class Heap:
    '''
    Class to implement a heap with general comparison function
    '''
    def swap(self,i,j):
        self.array[i], self.array[j] = self.array[j], self.array[i]

    def parent(self, i):
        if i<=0:
            return None
        return (i-1)//2

    def left_child(self, i):
        if(2*i + 1 < self.size):
            return 2*i + 1
        return None
    
    def right_child(self, i):
        if(2*i + 2 < self.size):
            return 2*i + 2
        return None
    
    def upheap(self, i):
        while (self.parent(i) is not None) and (self.comparison_function(self.array[i],self.array[self.parent(i)])):
            self.swap(self.parent(i),i)
            i = self.parent(i)
        return
    
    def downheap(self,i):
        while self.right_child(i) is not None:
            l = self.left_child(i)
            r = self.right_child(i)
            if self.comparison_function(self.array[l],self.array[r]):
                if self.comparison_function(self.array[l],self.array[i]):
                    self.swap(l,i)
                    i = l
                else:
                    return
            else:
                if self.comparison_function(self.array[r],self.array[i]):
                    self.swap(r,i)
                    i = r
                else:
                    return
        l = self.left_child(i)
        if l is not None:
            if self.comparison_function(self.array[l],self.array[i]):
                self.swap(l,i)
        return

    def __init__(self, comparison_function, init_array):
        '''
        Arguments:
            comparison_function : function : A function that takes in two arguments and returns a boolean value
            init_array : List[Any] : The initial array to be inserted into the heap
        Returns:
            None
        Description:
            Initializes a heap with a comparison function
            Details of Comparison Function:
                The comparison function should take in two arguments and return a boolean value
                If the comparison function returns True, it means that the first argument is to be considered smaller than the second argument
                If the comparison function returns False, it means that the first argument is to be considered greater than or equal to the second argument
        Time Complexity:
            O(n) where n is the number of elements in init_array
        '''
        
        # Write your code here
        self.comparison_function = comparison_function
        self.array = init_array
        self.size = len(init_array)
        if self.size<=1:
            return
        p_last = self.parent(self.size-1)
        for i in range(p_last,-1,-1):
            self.downheap(i)
        
    def insert(self, value):
        '''
        Arguments:
            value : Any : The value to be inserted into the heap
        Returns:
            None
        Description:
            Inserts a value into the heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        self.array.append(value)
        self.size += 1
        self.upheap(self.size-1)
    
    def extract(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value extracted from the top of heap
        Description:
            Extracts the value from the top of heap, i.e. removes it from heap
        Time Complexity:
            O(log(n)) where n is the number of elements currently in the heap
        '''
        
        # Write your code here
        if self.size < 1:
            return None
        self.swap(0,self.size-1)
        self.size -= 1
        temp = self.array.pop()
        if self.size > 0:
            self.downheap(0)
        return temp
    
    def top(self):
        '''
        Arguments:
            None
        Returns:
            Any : The value at the top of heap
        Description:
            Returns the value at the top of heap
        Time Complexity:
            O(1)
        '''
        
        # Write your code here
        if self.size < 1:
            return None
        return self.array[0]
    
    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    # You can add more functions if you want to

class Queue:
    def __init__(self,l):
        self.array = [None]*(l+10)
        self.front = 0
        self.rear = 0

    def isEmpty(self):
        if self.front == self.rear:
            return True
        return False

    def isFull(self):
        if (self.rear + 1)%len(self.array) == self.rear:
            return True
        return False

    def enqueue(self,i):
        if self.isFull():
            raise Exception("Queue full")
        self.array[self.rear] = i
        self.rear = (self.rear + 1)%len(self.array)
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue empty")
        p = self.array[self.front]
        self.front = (self.front + 1)%len(self.array)
        return p

class Planner:
    def __init__(self, flights):
        """The Planner

        Args:
            flights (List[Flight]): A list of information of all the flights (objects of class Flight)
        """
        self.incoming_flights = []
        self.outgoing_flights = []
        for i in range(2*len(flights)):
            self.incoming_flights.append([])
            self.outgoing_flights.append([])
        for flight in flights:
            self.incoming_flights[flight.end_city].append(flight)
            self.outgoing_flights[flight.start_city].append(flight)
        self.in_connection = []
        self.out_connection = []
        for i in range(len(flights)):
            self.in_connection.append([])
            self.out_connection.append([])
        for flight in flights:
            for j in self.outgoing_flights[flight.end_city]:
                if j.departure_time >= flight.arrival_time + 20:
                    self.out_connection[flight.flight_no].append(j)
            for j in self.incoming_flights[flight.start_city]:
                if flight.departure_time >= j.arrival_time + 20:
                    self.in_connection[flight.flight_no].append(j)
    
    def least_flights_earliest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        arrives the earliest
        """
        n = len(self.incoming_flights)
        color = [0]*n
        prev = [None]*n
        level = [0]*n
        q = Queue(n)
        q.enqueue(start_city)
        color[start_city] = 1
        while not q.isEmpty():
            p = q.dequeue()
            if p != start_city and level[p] == level[end_city]:
                break
            if p == start_city:
                for i in self.outgoing_flights[p]:
                    if (i.departure_time >= t1) and (i.arrival_time <= t2):
                        if color[i.end_city] == 0:
                            q.enqueue(i.end_city)
                            prev[i.end_city] = i
                            color[i.end_city] = 1
                            level[i.end_city] = level[p] + 1
                        else:
                            if (level[i.end_city] == level[p] + 1) and (prev[i.end_city].arrival_time > i.arrival_time):
                                prev[i.end_city] = i
            else:
                for i in self.outgoing_flights[p]:
                    if (i.departure_time >= prev[p].arrival_time + 20) and (i.arrival_time <= t2):
                        if color[i.end_city] == 0:
                            q.enqueue(i.end_city)
                            prev[i.end_city] = i
                            color[i.end_city] = 1
                            level[i.end_city] = level[p] + 1
                        else:
                            if (level[i.end_city] == level[p] + 1) and (prev[i.end_city].arrival_time > i.arrival_time):
                                prev[i.end_city] = i
        if color[end_city] == 0:
            return []
        ans = []
        j = end_city
        while prev[j] is not None:
            ans.append(prev[j])
            j = prev[j].start_city
        ans.reverse()
        return ans
    
    def cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route is a cheapest route
        """
        if start_city == end_city:
            return []
        cost = positive_infinity
        ans = []
        for flight in self.outgoing_flights[start_city]:
            if flight.departure_time < t1 or flight.arrival_time > t2:
                continue
            n = len(self.out_connection)
            estimated_cost = [positive_infinity]*n
            h = Heap(comp,[])
            prev = [None]*n
            visited = [False]*n
            h.insert((0,flight))
            estimated_cost[flight.flight_no] = 0
            flag = 0
            cur = None
            while not h.isEmpty():
                p = h.extract()
                cur = p[1]
                if visited[cur.flight_no] == True:
                    continue
                if cur.end_city == end_city:
                    flag = 1
                    break
                visited[cur.flight_no] = True
                for i in self.out_connection[cur.flight_no]:
                    if (i.departure_time >= t1) and (i.arrival_time <= t2):
                        if estimated_cost[i.flight_no] > (estimated_cost[cur.flight_no] + i.fare):
                            estimated_cost[i.flight_no] = estimated_cost[cur.flight_no] + i.fare
                            h.insert((estimated_cost[i.flight_no],i))
                            prev[i.flight_no] = cur
            if flag == 0:
                continue
            cur_cost = 0
            cur_path = []
            while cur is not None:
                cur_cost += cur.fare
                cur_path.append(cur)
                cur = prev[cur.flight_no]
            if cur_cost < cost:
                cost = cur_cost
                cur_path.reverse()
                ans = cur_path
        return ans

    def least_flights_cheapest_route(self, start_city, end_city, t1, t2):
        """
        Return List[Flight]: A route from start_city to end_city, which departs after t1 (>= t1) and
        arrives before t2 (<=) satisfying: 
        The route has the least number of flights, and within routes with same number of flights, 
        is the cheapest
        """
        if start_city == end_city:
            return []
        final = (positive_infinity,positive_infinity)
        ans = []
        for flight in self.outgoing_flights[start_city]:
            if flight.departure_time < t1 or flight.arrival_time > t2:
                continue
            n = len(self.out_connection)
            estimated_cost = [(positive_infinity,positive_infinity)]*n
            h = Heap(comp,[])
            prev = [None]*n
            visited = [False]*n
            level = [0]*n
            h.insert(((0,0),flight))
            estimated_cost[flight.flight_no] = (0,0)
            flag = 0
            cur = None
            while not h.isEmpty():
                p = h.extract()
                cur = p[1]
                if visited[cur.flight_no] == True:
                    continue
                if cur.end_city == end_city:
                    flag = 1
                    break
                visited[cur.flight_no] = True
                for i in self.out_connection[cur.flight_no]:
                    if (i.departure_time >= t1) and (i.arrival_time <= t2):
                        if estimated_cost[i.flight_no] > (estimated_cost[cur.flight_no][0]+1,estimated_cost[cur.flight_no][1]+i.fare):
                            estimated_cost[i.flight_no] = (estimated_cost[cur.flight_no][0]+1,estimated_cost[cur.flight_no][1]+i.fare)
                            level[i.flight_no] = level[cur.flight_no] + 1
                            h.insert(((level[i.flight_no], estimated_cost[i.flight_no]),i))
                            prev[i.flight_no] = cur
            if flag == 0:
                continue
            cur_cost = 0
            cur_path = []
            l = level[cur.flight_no]
            while cur is not None:
                cur_cost += cur.fare
                cur_path.append(cur)
                cur = prev[cur.flight_no]
            temp = (l,cur_cost)
            if temp < final:
                final = temp
                cur_path.reverse()
                ans = cur_path
        return ans