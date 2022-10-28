/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var kLengthApart = function(nums, k) {
    let currentIndex = -Infinity;
    
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 1) {
            if (i - currentIndex <= k) {
                return false;
            } else {
                currentIndex = i;
            }
        }
    }
    
    return true;
    
};