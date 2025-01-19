# Flight Planner

## Project Overview
The **Flight Planner** is designed for effective flight trip planning especially when travelers have specific requirements. Many aim to reach their destinations quickly by minimizing connections, while others prioritize the **lowest fare** or **timely arrivals**.

It is capable of finding optimized routes for these parameters:
- Fewest Flights and Earliest
- Cheapest Trip
- Fewest Flights and Cheapest

### Key Features:
- Multiple flights between any two cities.
- Models real world situation of layover time for connecting flights.
- Optimized for selecting trips based on people's diverse needs.

### Complexity:
- **Time complexity**:
-  O(m) : __init__ and least_flights_ealiest_route
-  O(m*log(m)) : cheapest_route and least_flights_cheapest_route
- **Space complexity**: O(n + m), where `n` is the number of cities and `m` is the number of flights.

### Algorithms:
- **Modified Dijkstra**: Used in cheapest_route and least_flights_cheapest_route
- **Modified BFS**: Used in least_flights_ealiest_route

### Technologies Used:
- Python
- Graphs
- OOPS Concept

---
