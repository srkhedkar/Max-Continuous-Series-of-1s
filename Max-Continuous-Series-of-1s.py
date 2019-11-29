class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
        start = -1
        end = -1
        TempStart = -1       
        TempEnd = -1
        count = 0
        maxCount = 0
        chances = B
        i = 0

        zeroList = []
        listInxed = 0
        for j in range(len(A)):
            if A[j] == 0:
                zeroList.append(j)

        while i < len(A):
            if A[i] == 1:
                count += 1
                if (TempStart == -1):
                    TempStart = i
            else:
                if (chances > 0):
                    if (TempStart == -1):
                        TempStart = i
                    chances -= 1
                    count += 1
                    
                else:
                    TempEnd = i - 1
                    if (count > maxCount):
                        maxCount = count
                        start = TempStart
                        end = TempEnd

                    
                    i = i -1
                    count = i - zeroList[listInxed]
                    TempStart =  zeroList[listInxed]  + 1
                    chances = 1                    
                    listInxed += 1
                   
            i += 1
            
        if count > maxCount:
            start = TempStart
            end = len(A) -1 
                    
        lst1 = [i for i in range(start,end+1)]

        return lst1