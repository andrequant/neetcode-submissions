class Solution:
    def transformArray(self, arr: List[int]) -> List[int]:
        condition = True

        while condition:
            new_arr = arr.copy()
            for i in range(1,len(arr)-1):
                if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
                    new_arr[i] = arr[i] + 1
                elif arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                    new_arr[i] = arr[i] - 1
            
            if new_arr == arr:
                return new_arr
            else:
                arr = new_arr.copy()