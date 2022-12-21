
Extra Python libraries:
* treelib for task 7
* pygame for task 9


# 1. Calorie counting

Nothing special here, quick and dirty Python.

# 2. Rock Paper Scissors

I can think of many ways to solve this. I went with the most naive one, reading the file line by line and doing a nested case/if for every line. Effective for a simple case like this.

# 3. Rucksack Reorganization

Very simple with Python using sets.

# 4. Camp Cleanup

I could have used sets again, but this time I decided to care about performance: we are only really intested in beginnings and ends of two ranges,
not the whole contents. A simple comparison of several integers is thousands time faster than set operations (even if we can't see the difference
on a small data). And in my opinion it's only slightly harder to write and equaly readable.

# 5. Supply Stacks

Parsing the input file was interesting, because the format was better suited to be read by human than a machine. The rest was simple, Python lists work great as stacks.

# 6. Tuning Trouble

Python seemed like a natural choice. String slicing for parsing input data, set operations to check for repeating characters. So, to make it more interesting, I decided to use pure C and pointer arithmetics.

# 7. No Space Left On Device

That one was tough. I decided to reconstruct the directory structure, traverse it recursively and calculate the sizes. It turned out I also needed two other data structures, a dict with directory name as a key and size as a value and another dict with size as a key and name as a value. I don't really like my code, it's neither very fast nor very readable, but I didn't have time to rewrite it.

I used a non-standard library: treelib.

# 8. Treetop Tree House

I used C and pointer arithmetics instead of a 2D array. Parsing input was easy. Calculations initially suffered from some off-by-one errors and "is this a character 4 or number 4" problems. Well, I wanted to do it low-level, I got what I deserved. 

I chose an inefficient way for solving the first part: created another data structure to store information from how many directions the tree is visible. It also meant I traversed the whole
data structure 4 times: left, right, top and bottom. It wasn't really neded, but I tried to guess what part 2 would be. Well, I was wrong, for part 2 I had to calculate a completely different
score. This time I used a more efficient way, checking only parts of the forest for each tree and without allocationg more data structures. In the hindsight, I should have done something
similar as in part 2: for every tree, try to check in each direction if it's visible, if it is - increment the visible counter and skip other directions.

# 9. Rope Bridge

At first I thought it was so easy that I decided to add visualization with pygame. Turned out that calculating tail position was prone to strange logic errors which meant it worked in ALMOST all circumstances. Which means it wasn't as easy as I thought, but at least the visualization helped with debugging. And moving from part
1 to part 2 wasn't hard.

