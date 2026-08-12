class Solution(object):
    def oddCells(self, m, n, indices):
       row = [0]*m
       col = [0]*n

       for r,c in indices:

        row[r] += 1
        col[c] += 1

       count = 0


       for r in range(m):

          for c in range(n):

            if(row[r]+col[c])%2==1:
                count += 1
       return count

        