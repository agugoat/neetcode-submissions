class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        '''
        go through replace val with inf
        then do a sort a in place min sort(selection sort)
        '''
        
        write = 0


        for read in range(len(nums)):
            if nums[read] != val:

                nums[write] = nums[read]
                write +=1
        
        return write
      


        