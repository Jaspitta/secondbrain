```
class Solution {

    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> map = new HashMap<Integer, Integer>();

        for(int i = 0; i < nums.length; i++){

            if(map.containsKey(nums[i])) return new int[]{map.get(nums[i]), i};

            map.put(target - nums[i], i);

        }

        return new int[]{0, 0};

    }

}
```

As much as this seemed like a simple problem at first, jumping too fast into it without making sure I understood the constrains was a big mistake.
I did not notice the possibility of negative numbers and that caused me 2 wrong submissions, I definitely need to be more careful and also remember that the aim is to get them right first try.

This problem involved an [[hash table]] to solve properly, otherwise [[time complexity]] would have been exponential.
With this solution we have
TC = O(n) because it grows at the same rate as the input
SC = O(n) because it grows at the same rate as the input
