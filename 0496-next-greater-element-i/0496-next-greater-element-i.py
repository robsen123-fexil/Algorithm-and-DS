class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        [-1 , -1 ,-1 , -1]
        from nums2= 4  -> -1
                nums1 4 = -1
            
            
            nums2 1 -> 3 
               nums1 1 -> 3
      
            nums2 2 -> -1
                nums1 2>=-1

         
         res1=[-1 , -1 ,-1 , -1 ]
           empty->  stack =[]
            stack.appeneded([1  , 0])
            
            not empty  -> stack[[1 ,0]]
                value 4
                while loop ,.. if there is stack also if stack[-1][0]<value
                    stack.pop()
                    hsh={stack[-1][0]:value}
        
                
                
            stack.apppend([value ,ind])
           if stack:
            [4 , 2]
            hsh[4]:-1


            [3 , 4 , -1 ,-1]
            hsh={}
         res2=[]
           [4 , 1 , 2]
           for loop res2->
              res.append(hsh[4])
        '''

        hsh={}
        stack=[]
        result=[]
        for i in range(len(nums2)):
            if stack:
                while stack and stack[-1][0]<nums2[i]:
                    a  , b =stack.pop()
                    hsh[a]=nums2[i]
                stack.append([nums2[i] , i])
            else:
                stack.append([nums2[i] , i])
        print(stack)
        for a , b in stack:
            hsh[a]=-1
        
        
        for i in nums1:
            if i in hsh:

               result.append(hsh[i])
        return result

