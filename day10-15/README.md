# 10. Cathode-Ray Tube

That was so much easier than the previous 3 puzzles. Part 1 took only a few minutes, part 2 was a bit harder but not a challenge either. Still, I had
some logic errors, mostly coming from not reading the instructions carefuly enough. All those commented out "print" commands are a result of this.
It was also my favourite puzzle so far!

# 11. Monkey in the Middle

Toughest so far. I admit I had to look up hints for part 2. I also for the first time felt the need to use type hints and non-trivial comments in my Python
code, avoid global variables and generally follow some good practices. Also for the first time I used lambda and list comprehensions (I usually avoid them,
making code longer but more readable - I believe this time they were justified).

SPOILERS BELOW:

The trick for part 2: as the author wrote, you need another way to keep your worry level managable. Which means: prevent it from getting bigger than your
computer's integer variable can hold (some languages support big integers, Python included, but the operations on them are much slower). Now, we don't
really need the exact value of the worry level. We only need to be able to perform every monkey's test - which means checking if the number is divisible
by every monkey. So, that means every turn we can do modulo by least common multiple of all monkey's test values.

# 12. Hill Climbing Algorithm

### Version 1: Brute force

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


### Version 2: A bit more subtle force

All right, I don't need to keep all possible paths through the map, only those that lead to the end point. With that modification, my program was able to find the route from start to end - just not the shortest route.


### Version 3: Dijkstra algorithm

Why am I trying to brute force anyway? After all, I learned about graph searching algorithms back at the Uni. I haven't needed them for years and obviously wouldn't remeber them, but at least I know what to look for. I compared a few, [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) looked well suited for the task and easy to implement.


**Data structures needed for the algorithm**

- one holding a distance between the start node and any other node in the graph (in that case, between start point and any other point on the map) - a 2D array, so a vector of vectors of integers was OK,
- list of nodes already checked - a set 
- list of nodes to be checked with their distance from the starting point - there are a few variations of Dijkstra algorithm, I chose one using priority queue.
- I also needed a helper list to keep track of points in the queue, as C++'s priority queue doesn't support checking if an element is already present - a set was again the best choice,
- and finally, the elevation map - another 2D array, so a vector of vector of char... wait, that might as well be a vector of strings,
- I also defined the point on map as a pair of 16-bit integers, I'll be passing and storing a few of those.

I rewrote the program to proper, modern C++. No need to worry about the size of my data structures now. I only needed one of each, so it's going to be orders of magnitude smaller and faster anyway. And I could surely use STL for all those sets and queues.

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

## Part 2

So, now I have to find the shortest path not from a given start point, but any point with elevation 'a'. The brute force approach would be to get a list of all such points and run the algorithm for each of them. The smart way would be to realise that Dijkstra algorithm calculates the distance for all points on the map, not only the one given. So, let's reverse the search:
- the program searches from the end point now, it only required changing the line comparing the elevation of neighbouring points,
- I checked that it gaves the same result for part 1,
- then, I got a list of all points with elevation 'a',
- iterated over it, read distance for all of them and found the smallest one.

It took me days to write part 1, but only a few minutes to get to part 2.


# 13. Distress Signal

I'm now convinced that the Advent's author is a Python developer. Input data was exactly the format of Python list, so simply doing:
literal_eval(newline.strip()) was enough to read the input. Then, the first part wasn't particularly hard either, and second was even easier. The key was to realise that I need to use a 3-value logic, eg.:
* -1 means the left item is smaller
* +1 means the right item is smaller
* 0 means they are equal and I need to check the next item
Part 2 was something completely different - it required sorting the packets. Incidentally, many sort functions expect a comparison function using
exactly the logic above.

# 14. Regolith Reservoir

It was the opposite of Day 12. At first I decided **not** to do the obvious solution of calculating each successive position of each grain of sand. 
Instead, considered it a problem of finding distance on a map, with Dijkstra's algorithm again, but this time in Python:
- create 2D array for the map
- calculate distance from the start point to every point, using the rules given (which means many points will be inaccessible)
- then count how many points accessible points there are between the start point and the lowest rock.
But I couldn't get right results. Rules of finding the next possible point need to be modified of course, I tried a few ways but I always got
either too little or too much accessible points. I can now see that it would work for part 2 though. Pity, I even had a visualization:

![screenshot](https://github.com/igorwaw/advent22/blob/main/img/day14.png)

So instead I thought: what's the size of the brute force solution? There's no exponential growth here, even on the large map 
it's only thousands of iterations, not billions. Plus, I don't need to store the map. I used sets to store rock and sand positions only
(fast and easy checking if the position is in the set). It worked great for part 1. Part 2 only required adding a layer of rock and a new stop condition.

I'm adding both versions anyway. 14-regolith.py is the grain-by-grain simulation that works, 14-regolith-pathfinding.py is the fancy version with Dijkstra's algorithm and pygame that doesn't.
