class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        nums_occu = []
        for idx, digits in enumerate(nums):
			# getting the index and the value from the list
            if digits == 1:
				# checking whether there are 2 indexes or one because we need 2 to compare the distance between them
                if len(nums_occu) == 0:
                    nums_occu.append(idx)
				# if we already have 1 in the list then we can append the other and check the distance between the indices.
                elif len(nums_occu) == 1:
                    nums_occu.append(idx)
					# if they are less than k+1(k+1 because when finding distance we calculate the position of last 1 also, so to nullify that +1 is added)
                    if (nums_occu[1] - nums_occu[0]) < k+1:
                        return False
                    else:
						# if we dont get the error then we are good to go and now we need the latest index of 1 for comparision so we discard the last index of first 1.
                        nums_occu = nums_occu[1:]
        return True
        