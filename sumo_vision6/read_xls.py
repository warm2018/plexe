# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 09:55:26 2018

@author: hanxintong
"""
# 读取excel数据
from __future__ import print_function
import xlrd #Python读取Excel的模块

def generate_routefile():

    data = xlrd.open_workbook(r'C:\Users\hanxintong\Desktop\third-year master\Offset Optimization\sumo_vision6\vehicle_OD.xlsx') #读取Excel
    table = data.sheet_by_index(0) #读取此Excel中的第一页，从0开始
    nrows = table.nrows #读取表格中的行数
    ncols = table.ncols #读取表格中的列数
    rouNum = 0 #设置循环变量
    beginTime = 0 #每一轮开始时间
    endTime = 600 #每一轮结束时间
    rouReal = ('AW-LE','AW-RI','AW-B-LE','AW-B-RI','AW-B-C-LE','AW-B-C-RI','AW-B-C-D-RI','AW-B-C-D-E-LE','AW-B-C-D-E-ST','AW-B-C-D-E-RI',\
               'AS-LE','AS-ST','AS-B-LE','AS-B-RI','AS-B-C-LE','AS-B-C-RI','AS-B-C-D-RI','AS-B-C-D-E-LE','AS-B-C-D-E-ST','AS-B-C-D-E-RI',\
               'AN-RI','AN-ST','AN-B-LE','AN-B-RI','AN-B-C-LE','AN-B-C-RI','AN-B-C-D-RI','AN-B-C-D-E-LE','AN-B-C-D-E-ST','AN-B-C-D-E-RI',\
               'BS-A-LE','BS-A-ST','BS-A-RI','BS-ST','BS-C-LE','BS-C-RI','BS-C-D-RI','BS-C-D-E-LE','BS-C-D-E-ST','BS-C-D-E-RI',\
               'BN-A-LE','BN-A-ST','BN-A-RI','BN-ST','BN-C-LE','BN-C-RI','BN-C-D-RI','BN-C-D-E-LE','BN-C-D-E-ST','BN-C-D-E-RI',\
               'CS-B-A-LE','CS-B-A-ST','CS-B-A-RI','CS-B-LE','CS-B-RI','CS-ST','CS-D-RI','CS-D-E-LE','CS-D-E-ST','CS-D-E-RI',\
               'CN-B-A-LE','CN-B-A-ST','CN-B-A-RI','CN-B-LE','CN-B-RI','CN-ST','CN-D-RI','CN-D-E-LE','CN-D-E-ST','CN-D-E-RI',\
               'DS-C-B-A-LE','DS-C-B-A-ST','DS-C-B-A-RI','DS-C-B-LE','DS-C-B-RI','DS-C-LE','DS-C-RI','DS-ST','DS-E-LE','DS-E-ST','DS-E-RI',\
               'DN-C-B-A-LE','DN-C-B-A-ST','DN-C-B-A-RI','DN-C-B-LE','DN-C-B-RI','DN-C-LE','DN-C-RI','DN-ST','DN-E-LE','DN-E-ST','DN-E-RI',\
               'ES-D-C-B-A-LE','ES-D-C-B-A-ST','ES-D-C-B-A-RI','ES-D-C-B-LE','ES-D-C-B-RI','ES-D-C-LE','ES-D-C-RI','ES-D-LE','ES-D-RI','ES-ST','ES-RI',\
               'EN-D-C-B-A-LE','EN-D-C-B-A-ST','EN-D-C-B-A-RI','EN-D-C-B-LE','EN-D-C-B-RI','EN-D-C-LE','EN-D-C-RI','EN-D-LE','EN-D-RI','EN-LE','EN-ST',\
               'EE-D-C-B-A-LE','EE-D-C-B-A-ST','EE-D-C-B-A-RI','EE-D-C-B-LE','EE-D-C-B-RI','EE-D-C-LE','EE-D-C-RI','EE-D-LE','EE-D-RI','EE-LE','EE-RI'
               ) #设置Excel中需要用的变量名,例如N_S就是北到南

    #这里的语句相当于routes=open("data/cross.rou.xml","w"),打开文件并赋值
    #创建并将以下内容写入新的rou.xml文件中
    with open("b.rou.xml", "w") as routes:
        print("""<?xml version="1.0" encoding="UTF-8"?>
<routes>
    <route id="AW-LE" edges="edge-AW2-AW1 edge-AW1-AO0 edge-AO0-AN2"/>
    <route id="AW-RI" edges="edge-AW2-AW1 edge-AW1-AO0 edge-AO0-AS2"/>
    <route id="AW-B-LE" edges="edge-AW2-AW1 edge-AW1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-BN2"/>
	<route id="AW-B-RI" edges="edge-AW2-AW1 edge-AW1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-BS2"/>
	<route id="AW-B-C-LE" edges="edge-AW2-AW1 edge-AW1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-CN2"/>
	<route id="AW-B-C-RI" edges="edge-AW2-AW1 edge-AW1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-CS2"/>
	<route id="AW-B-C-D-RI" edges="edge-AW2-AW1 edge-AW1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-DS2"/>
	<route id="AW-B-C-D-E-LE" edges="edge-AW2-AW1 edge-AW1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EN2"/>
	<route id="AW-B-C-D-E-ST" edges="edge-AW2-AW1 edge-AW1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EE2"/> 	
	<route id="AW-B-C-D-E-RI" edges="edge-AW2-AW1 edge-AW1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-ES2"/>  
	
	<route id="AS-LE" edges="edge-AS2-AS1 edge-AS1-AO0 edge-AO0-AW2"/>
	<route id="AS-ST" edges="edge-AS2-AS1 edge-AS1-AO0 edge-AO0-AN2"/>
	<route id="AS-B-LE" edges="edge-AS2-AS1 edge-AS1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-BN2"/>  
	<route id="AS-B-RI" edges="edge-AS2-AS1 edge-AS1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-BS2"/>     
	<route id="AS-B-C-LE" edges="edge-AS2-AS1 edge-AS1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-CN2"/>     
	<route id="AS-B-C-RI" edges="edge-AS2-AS1 edge-AS1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-CS2"/>     
	<route id="AS-B-C-D-RI" edges="edge-AS2-AS1 edge-AS1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-DS2"/>  
	<route id="AS-B-C-D-E-LE" edges="edge-AS2-AS1 edge-AS1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EN2"/> 
	<route id="AS-B-C-D-E-ST" edges="edge-AS2-AS1 edge-AS1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EE2"/> 		
	<route id="AS-B-C-D-E-RI" edges="edge-AS2-AS1 edge-AS1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-ES2"/>  
	
	<route id="AN-RI" edges="edge-AN2-AN1 edge-AN1-AO0 edge-AO0-AW2"/>	
	<route id="AN-ST" edges="edge-AN2-AN1 edge-AN1-AO0 edge-AO0-AS2"/>
	<route id="AN-B-LE" edges="edge-AN2-AN1 edge-AN1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-BN2"/>  
	<route id="AN-B-RI" edges="edge-AN2-AN1 edge-AN1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-BS2"/>     
	<route id="AN-B-C-LE" edges="edge-AN2-AN1 edge-AN1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-CN2"/>     
	<route id="AN-B-C-RI" edges="edge-AN2-AN1 edge-AN1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-CS2"/>     
	<route id="AN-B-C-D-RI" edges="edge-AN2-AN1 edge-AN1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-DS2"/>  
	<route id="AN-B-C-D-E-LE" edges="edge-AN2-AN1 edge-AN1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EN2"/>  
	<route id="AN-B-C-D-E-ST" edges="edge-AN2-AN1 edge-AN1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EE2"/>
	<route id="AN-B-C-D-E-RI" edges="edge-AN2-AN1 edge-AN1-AO0 edge-AO0-BW1 edge-BW1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-ES2"/>  

	<route id="BS-A-LE" edges="edge-BS2-BS1 edge-BS1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AS2"/>
	<route id="BS-A-ST" edges="edge-BS2-BS1 edge-BS1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AW2"/>
	<route id="BS-A-RI" edges="edge-BS2-BS1 edge-BS1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AN2"/>
	<route id="BS-ST" edges="edge-BS2-BS1 edge-BS1-BO0 edge-BO0-BN2"/>
	<route id="BS-C-LE" edges="edge-BS2-BS1 edge-BS1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-CN2"/>
	<route id="BS-C-RI" edges="edge-BS2-BS1 edge-BS1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-CS2"/>
	<route id="BS-C-D-RI" edges="edge-BS2-BS1 edge-BS1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-DS2"/>
	<route id="BS-C-D-E-LE" edges="edge-BS2-BS1 edge-BS1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EN2"/>
	<route id="BS-C-D-E-ST" edges="edge-BS2-BS1 edge-BS1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EE2"/>
	<route id="BS-C-D-E-RI" edges="edge-BS2-BS1 edge-BS1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-ES2"/>
	
	<route id="BN-A-LE" edges="edge-BN2-BN1 edge-BN1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AS2"/>
	<route id="BN-A-ST" edges="edge-BN2-BN1 edge-BN1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AW2"/>
	<route id="BN-A-RI" edges="edge-BN2-BN1 edge-BN1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AN2"/>
	<route id="BN-ST" edges="edge-BN2-BN1 edge-BN1-BO0 edge-BO0-BS2"/>
	<route id="BN-C-LE" edges="edge-BN2-BN1 edge-BN1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-CN2"/>
	<route id="BN-C-RI" edges="edge-BN2-BN1 edge-BN1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-CS2"/>
	<route id="BN-C-D-RI" edges="edge-BN2-BN1 edge-BN1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-DS2"/>
	<route id="BN-C-D-E-LE" edges="edge-BN2-BN1 edge-BN1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EN2"/>
	<route id="BN-C-D-E-ST" edges="edge-BN2-BN1 edge-BN1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EE2"/>
	<route id="BN-C-D-E-RI" edges="edge-BN2-BN1 edge-BN1-BO0 edge-BO0-CW1 edge-CW1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-ES2"/>

	<route id="CS-B-A-LE" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AS2"/>
	<route id="CS-B-A-ST" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AW2"/>
	<route id="CS-B-A-RI" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AN2"/>
	<route id="CS-B-LE"	edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BS2"/>
	<route id="CS-B-RI" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BN2"/>
	<route id="CS-ST" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-CN2"/>
	<route id="CS-D-RI" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-DS2"/>
	<route id="CS-D-E-LE" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EN2"/>
	<route id="CS-D-E-ST" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EE2"/>
	<route id="CS-D-E-RI" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-ES2"/>	
	
	<route id="CN-B-A-LE" edges="edge-CN2-CN1 edge-CN1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AS2"/>
	<route id="CN-B-A-ST" edges="edge-CN2-CN1 edge-CN1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AW2"/>
	<route id="CN-B-A-RI" edges="edge-CN2-CN1 edge-CN1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AN2"/>
	<route id="CN-B-LE"	edges="edge-CN2-CN1 edge-CN1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BS2"/>
	<route id="CN-B-RI" edges="edge-CN2-CN1 edge-CN1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BN2"/>
	<route id="CN-ST" edges="edge-CN2-CN1 edge-CN1-CO0 edge-CO0-CS2"/>
	<route id="CN-D-RI" edges="edge-CN2-CN1 edge-CN1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-DS2"/>
	<route id="CN-D-E-LE" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EN2"/>
	<route id="CN-D-E-ST" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EE2"/>
	<route id="CN-D-E-RI" edges="edge-CS2-CS1 edge-CS1-CO0 edge-CO0-DW1 edge-DW1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-ES2"/>

	<route id="DS-C-B-A-LE" edges="edge-DS2-DS1 edge-DS1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AS2"/>
	<route id="DS-C-B-A-ST" edges="edge-DS2-DS1 edge-DS1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AW2"/>
	<route id="DS-C-B-A-RI" edges="edge-DS2-DS1 edge-DS1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AN2"/>
	<route id="DS-C-B-LE" edges="edge-DS2-DS1 edge-DS1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BS2"/>
	<route id="DS-C-B-RI" edges="edge-DS2-DS1 edge-DS1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BN2"/>
	<route id="DS-C-LE" edges="edge-DS2-DS1 edge-DS1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-CS2"/>
	<route id="DS-C-RI" edges="edge-DS2-DS1 edge-DS1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-CN2"/>
	<route id="DS-ST" edges="edge-DS2-DS1 edge-DS1-DO0 edge-DO0-DN1"/>
	<route id="DS-E-LE" edges="edge-DS2-DS1 edge-DS1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EN2"/>
	<route id="DS-E-ST" edges="edge-DS2-DS1 edge-DS1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EE2"/>
	<route id="DS-E-RI" edges="edge-DS2-DS1 edge-DS1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-ES2"/>
	
	<route id="DN-C-B-A-LE" edges="edge-DN1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AS2"/>
	<route id="DN-C-B-A-ST" edges="edge-DN1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AW2"/>
	<route id="DN-C-B-A-RI" edges="edge-DN1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AN2"/>
	<route id="DN-C-B-LE" edges="edge-DN1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BS2"/>
	<route id="DN-C-B-RI" edges="edge-DN1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BN2"/>
	<route id="DN-C-LE" edges="edge-DN1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-CS2"/>
	<route id="DN-C-RI" edges="edge-DN1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-CN2"/>
	<route id="DN-ST" edges="edge-DN1-DO0 edge-DO0-DS2"/>
	<route id="DN-E-LE" edges="edge-DN1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EN2"/>
	<route id="DN-E-ST" edges="edge-DN1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-EE2"/>
	<route id="DN-E-RI" edges="edge-DN1-DO0 edge-DO0-EW1 edge-EW1-EO0 edge-EO0-ES2"/>
		
	<route id="EE-D-C-B-A-LE" edges="edge-EE2-EE1 edge-EE1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AS2"/>
	<route id="EE-D-C-B-A-ST" edges="edge-EE2-EE1 edge-EE1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AW2"/>
	<route id="EE-D-C-B-A-RI" edges="edge-EE2-EE1 edge-EE1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AN2"/>
	<route id="EE-D-C-B-LE" edges="edge-EE2-EE1 edge-EE1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BS2"/>
	<route id="EE-D-C-B-RI" edges="edge-EE2-EE1 edge-EE1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BN2"/>
	<route id="EE-D-C-LE" edges="edge-EE2-EE1 edge-EE1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-CS2"/>
	<route id="EE-D-C-RI" edges="edge-EE2-EE1 edge-EE1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-CN2"/>
	<route id="EE-D-LE" edges="edge-EE2-EE1 edge-EE1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-DS2"/>
	<route id="EE-D-RI" edges="edge-EE2-EE1 edge-EE1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-DN1"/>
	<route id="EE-LE" edges="edge-EE2-EE1 edge-EE1-EO0 edge-EO0-ES2"/>
	<route id="EE-RI" edges="edge-EE2-EE1 edge-EE1-EO0 edge-EO0-EN2"/>
	
	<route id="ES-D-C-B-A-LE" edges="edge-ES2-ES1 edge-ES1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AS2"/>
	<route id="ES-D-C-B-A-ST" edges="edge-ES2-ES1 edge-ES1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AW2"/>
	<route id="ES-D-C-B-A-RI" edges="edge-ES2-ES1 edge-ES1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AN2"/>
	<route id="ES-D-C-B-LE" edges="edge-ES2-ES1 edge-ES1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BS2"/>
	<route id="ES-D-C-B-RI" edges="edge-ES2-ES1 edge-ES1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BN2"/>
	<route id="ES-D-C-LE" edges="edge-ES2-ES1 edge-ES1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-CS2"/>
	<route id="ES-D-C-RI" edges="edge-ES2-ES1 edge-ES1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-CN2"/>
	<route id="ES-D-LE" edges="edge-ES2-ES1 edge-ES1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-DS2"/>
	<route id="ES-D-RI" edges="edge-ES2-ES1 edge-ES1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-DN1"/>
	<route id="ES-ST" edges="edge-ES2-ES1 edge-ES1-EO0 edge-EO0-EN2"/>
	<route id="ES-RI" edges="edge-ES2-ES1 edge-ES1-EO0 edge-EO0-EE2"/>
	
	<route id="EN-D-C-B-A-LE" edges="edge-EN2-EN1 edge-EN1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AS2"/>
	<route id="EN-D-C-B-A-ST" edges="edge-EN2-EN1 edge-EN1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AW2"/>
	<route id="EN-D-C-B-A-RI" edges="edge-EN2-EN1 edge-EN1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-AE1 edge-AE1-AO0 edge-AO0-AN2"/>
	<route id="EN-D-C-B-LE" edges="edge-EN2-EN1 edge-EN1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BS2"/>
	<route id="EN-D-C-B-RI" edges="edge-EN2-EN1 edge-EN1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-BE1 edge-BE1-BO0 edge-BO0-BN2"/>
	<route id="EN-D-C-LE" edges="edge-EN2-EN1 edge-EN1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-CS2"/>
	<route id="EN-D-C-RI" edges="edge-EN2-EN1 edge-EN1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-CE1 edge-CE1-CO0 edge-CO0-CN2"/>
	<route id="EN-D-LE" edges="edge-EN2-EN1 edge-EN1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-DS2"/>
	<route id="EN-D-RI" edges="edge-EN2-EN1 edge-EN1-EO0 edge-EO0-DE1 edge-DE1-DO0 edge-DO0-DN1"/>
	<route id="EN-LE" edges="edge-EN2-EN1 edge-EN1-EO0 edge-EO0-EE2"/>
	<route id="EN-ST" edges="edge-EN2-EN1 edge-EN1-EO0 edge-EO0-ES2"/>"""'\n', file=routes)

        #循环读取Excel中的数据，并带入到需要设置的车流中，例如就是先从第一行开始读，第一行第一列，第一行第二列。。。。。。
        for i in range(1,nrows):#此处示例的时候先用第二行的数据，如果想用全部的改成rang(0,nrows)
            for j in range(1,ncols):
                if table.row_values(i)[j] > 0:
                    #if j in [0,5,10,13]:continue
                    print('    <flow id="%s" route="%s" begin="%d" end="%d" number="%d" type="private" departLane="best"/>' % (rouNum,str(rouReal[j-1]),beginTime,endTime,table.row_values(i)[j]),file=routes)
                    rouNum += 1 #车辆id
            beginTime = endTime #第一行数据读取运行完，下一行数据的车流开始运行的时间
            endTime += 600 #下一行结束的时间

        #至此，写完了rou.xml文件
        print("</routes>", file=routes)

if __name__ == '__main__':
    generate_routefile()
