
import matplotlib.pyplot as plt
import xlrd
from xlrd import open_workbook


ValueX=[]
ValueY=[]
BookFile= open_workbook('trajectory.xlsx')
 
'''
### 读取每一列的数据，分别绘制，最后统一绘出图形
###思路是用一个循环数为列数的循环，里面定义X坐标和Y坐标
'''


for SheetValue in BookFile.sheets():
	print ('Sheet:',SheetValue.name)
	for col in range(SheetValue.ncols):
		print ('the col is:',col)
		RowLength = SheetValue.nrows
		print('the RowLength IS',RowLength)
		ValueY = []
		ValueX = [] 
		for row in range(RowLength):
			value = SheetValue.cell(row,col).value
			if value != '':
				ValueX.append(row)
				ValueY.append(value)
		print(len(ValueX))
		print(len(ValueY))
		plt.plot(ValueX, ValueY, linestyle='-',linewidth=0.3)



plt.title(u"Space-Time diagram")
plt.xlabel(u"Simulation Step(s)")
plt.ylabel(u"Spce(m)")
 
 
plt.show()
print ('over!')