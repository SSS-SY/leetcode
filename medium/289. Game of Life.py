import numpy as np
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m,n=len(board),len(board[0])
        res=np.zeros((m,n),int)
        count=0
        adjoining=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
        for i in range(m):
        	for j in range(n):
        		count=0
        		for neighbor in adjoining:
        			if i+neighbor[0]<0 or i+neighbor[0]>=m or j+neighbor[1]<0 or j+neighbor[1]>=n:
        				continue
        			if board[i+neighbor[0]][j+neighbor[1]]==1:
        				count+=1
        		if board[i][j]==1:
        			if count<2:
        				res[i][j]=0
        			elif count<=3:
        				res[i][j]=1
        			else:
        				res[i][j]=0
        		else:
        			if count==3:
        				res[i][j]=1
        			else:
        				res[i][j]=0
        for i in range(m):
        	for j in range(n):
        		board[i][j]=res[i][j]