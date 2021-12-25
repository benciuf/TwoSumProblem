#The two sum problem is a common interview question, and it is a variation of the
#subset sum problem. For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7,
#your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7.

x = (3,5,2,-4,8,11)
sumSearch = 7
def getTwoSum_Vone():
    for i in range (0,len(x)):
        for j in range (i+1,len(x)):
            #print("i = ",i)
            #print("j = ",j)
            sumTemp = x[i] + x[j]
            #print("sumTemp = ",x[i], " + ",x[j], " = ", sumTemp)
            if(sumTemp == sumSearch):
                print("[",x[i],", ",x[j],"],", end=' ')
getTwoSum_Vone()

def getTwoSum_Vtwo():
	return()
getTwoSum_Vtwo()
