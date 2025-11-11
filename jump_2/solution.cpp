#include <iostream>

int JumpGameTwo(vector<int> nums)
{
    int furthest_index = 0;
    int hops = 0;
    int boundary = 0;
    if (nums.size() == 1) return 0;
    for (int i = 0; i < nums.size() - 1; i++) {
        furthest_index = (nums[i] + i > furthest_index) ? nums[i] + i: furthest_index;
        if (i == boundary) {
            hops++;
            boundary = furthest_index;
        }
    }
    return hops;
}
/*
Idea for the algo: we use a greedy algorithm to solve this
meaning we need to find the key heuristic. looking at this problem we can observe
that for a given index we care about how far we can possible go in the current jump.
the furthest we can go for a certain jump is what we always want. if we imagine each hop as an
iteration of bfs, we can see that really we are looking at "layers" and a layer is dictated by what the furthest
possible index is for a given jump. if we jump 3 from the starting index - then the next layer is going to include all 
indexes up to 3. if the final index isn't there, then we we will keep iterating on the next layer boundary and repeat -
only increasing the hops once we reach the end of a "layer"
*/
