
import traci
import math

def judge_needed(VehicleID,EdgeID,RouteID):
	specific_route = traci.vehicle.getRouteID(VehicleID)	
	specific_edge = traci.vehicle.getRoadID(VehicleID)
	###得到该车辆的routID和所在车道ID
	JudgeEdge = False
	if specific_edge in EdgeID or specific_edge.find(':') != -1:
		JudgeEdge = True
	if specific_route in  RouteID and JudgeEdge:
		return 	True
	else:
		return False
	'''
	#如果车辆的车道ID和RouteID都在我们要求的范围内
	#，可判断此车辆就是我们要跟踪的车辆
	'''


def get_distance(vehcieID,trackdirection):
	'''
	获取车辆离参照点的水平距离（因为路网是水平的，
	用x坐标的差值来表示其离参考点的距离）
	'''
	vehicle_pos = traci.vehicle.getPosition(vehcieID)
	#get the vehicle's coordination
	cor_x,cor_y = vehicle_pos
	if trackdirection == 'A_E':
		origin_x = 0
		origin_y = 0
	else:
		origin_x = 0
		origin_y = 0
	#the origin's (start) coordination
	distance = abs(cor_x - origin_x)
	return distance
