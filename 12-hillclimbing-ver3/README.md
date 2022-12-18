# 12. Hill Climbing Algorithm

## Version 1: Brute force

My first idea was to brute force the solution: create a tree of all possible paths from the starting point. How much data would that be?
Every node can point to 4 further nodes (top, bottom, left and right), but in practice much less than that:
- no sense going back to the previous node, so each node except the first one can only have 3 children,
- some nodes would have children outside of the map,
- some nodes would lead too high,
- I also kept track of visited nodes not to visit them again.

My guesstimate was each node would, on average, lead to between 1 or 2 other nodes. Closer to one 1 or 2? Well, that makes a big difference:
- if it's close to 1, there's almost no increase in the tree breadth,
- if it's close to 2, we get about 1000 nodes at level 10 (fine, that's nothing), 16 milion at level 24 (that's still managable), 4 billion at level 32 (uh oh)...

So, I hoped it's closer to 1 and made sure my data structures were small. I used 16-bit integers and my code was more "C with classes" than a proper C++ - I used almost no standard library and only really needed C++ for some basic encapsulation.

The solution worked fine for the sample data. For the full input, it worked for a few minutes and got terminated by the Out Of Memory Killer. OK, that wasn't a good idea.


## Version 2: A bit more subtle force

All right, I don't need to keep all possible paths through the map, only those that lead to the end point. With that modification, my program was able to find the route from start to end - just not the shortest route.


## Version 3: Dijkstra algorithm

Why am I trying to brute force anyway? After all, I learned about tree and graph searching algorithms back at the Uni. I haven't needed them for years and obviously wouldn't remeber them, but at least I know what to look for. I compared a few, [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) looked well suited for the task and easy to implement.


**Data structures needed for the algorithm**

- one holding a distance between the start node and any other node in the graphs (in that case, between start point and any other point on the map) - a 2D array, so a vector of vectors of integers was OK,
- list of nodes already checked - a set 
- list of nodes to be checked with their distance from the starting point - there are a few variations of Dijkstra algorithm, I chose one using priority queue.
- I also needed a helper list to keep track of points in the queue, as C++'s priority queue doesn't support checking if an element is already present - a set was again the best choice,
- and finally, the elevation map - another 2D array, so a vector of vector of char... wait, that might as well be a vector of strings,
- I also defined the point on map as a pair of 16-bit integers, I'll be passing and storing a few of those.

I rewrote the program to proper, modern C++. No need to worry about the size of my data structures now. I only needed one of each, so it's going to be orders of magnitude smaller and faster anyway. And I could surely use STL.

**First steps**

- set the initial distance: 0 for the start node, infinity for all others (in practice, any value larger than whatever can appear is OK and can serve as a sanity check, eg. if my calculated distance exceeded 10000, clearly there's something wrong with my calculation)
- add start point with distance 0 to the priority queue

**The Loop**
- get the point with the shortest distance from the queue (this is why the priority queue is useful - it just keeps the required point on top)
- add it to the list of visited nodes
- check all 4 neighbours of the current point, each of them is a possible next point:
 * if it's outside of map or too high from the current elevation, skip it,
 * if it's already visited, skip it,
 * calculate the distance as: distance of the current point + 1
 * if the new next point's distance is smaller than the one already stored, store the new distance (it's possible we see the same point again, but from another direction)
 * if the next point is not already in the queue of points to be checked, add it to the queue

And that's it. Just let it loop until it runs out of points to check, then read the distance of the end point. Worked like a charm for both example and full input data.

#### Part 2

So, now I have to find the shortest path not from a given start point, but any point with elevation 'a'. The brute force approach would be to get a list of all such points and run the algorithm for each of them. The smart way would be to realise that Dijkstra algorithm calculates the distance for all points on the map, not only the one given. So, let's reverse the search:
- the program searches from the end point now, it only required changing the line comparing the elevation of neighbouring points,
- I checked that it gaves the same result for part 1,
- then, I got a list of all points with elevation 'a',
- iterated over it, read distance for all of them and found the smallest one.

It took me days to write part 1, but only a few minutes to get to part 2.
