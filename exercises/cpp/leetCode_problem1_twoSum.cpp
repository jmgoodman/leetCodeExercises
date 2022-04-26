using namespace std; // probably already done implicitly but I like to be explicit...
// what's the pipeline for using this file?
// since we're defining a class here, I'd think that would go in a .h header file
// but since we have an explicit implementation... it seems to belong in a .cpp code file after all!
// but there's no main() method here... so compiling this alone would not work
// I wonder if the way leetcode runs this is by stuffing this in a header file after all, importing that header file in the test code, then in the main() method the twoSum method is called!

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // ampersand = pass-by-reference
        // basically, it means changes to it in the function are global in scope
        // in exchange for not needing to instantiate a local copy
        // vectors are inherently pointers anyway, and a lot of that juggling is abstracted away from you no matter what
        // it's really just about the scope of the modifications of the input, and whether data copies are created in memory
        unordered_map<int, int> hashmap; // unordered map for that sweet O(1) access time
        int i = 0;
        vector<int> output;
        for(vector<int>::iterator it=nums.begin(); it != nums.end(); it++,i++) {
            unordered_map<int,int>::iterator got = hashmap.find(target - *it); // funny way of doing hashmap lookup - "find" generates an iterator that returns an object which points to the sought key if it's present, otherwise returns the "past-the-end" iterator (meaning we "overshot" the end of the array)
            if( got == hashmap.end() ) {
                hashmap.insert({*it,i});
            } else {
                output.push_back(hashmap[target - *it]); // funny vector methods, this expands the vector by 1 (should probably preallocate to save time) and sticks a new value in the new last index. What throws me, though, is that *it works, but *got does NOT (because *got returns a key-value PAIR whereas *it just returns the value referenced to that position in the array) (note: (*got).second gets you the value from the <int,int> pair pointed to by the iterator pointer got... seems to be no faster, maybe even a bit slower, though) (note: you NEED that * tho! iterators are pointers so you need to specify "points to" when usin' em) (indeed: https://home.csulb.edu/~pnguyen/cecs282/lecnotes/iterators.pdf)
                output.push_back(i);
                break;
            }

        }
        return output;
    }
};

/* a simpler solution:
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int>ans;
        unordered_map<int, int> mp;
        for(int i=0; i<nums.size(); i++) // here is where things get simplified, instead of doing an iterator, we just deal with an accumulating int that is used to pull elements from the vector (which I ultimately do *anyway*)
        {
            if(mp.find(target-nums[i])!= mp.end())
            {
                ans.push_back(mp[target-nums[i]]);
                ans.push_back(i);
                return ans;
            }
            else mp[nums[i]] = i;
        }
        return ans;
    }
};
*/