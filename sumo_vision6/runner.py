#!/usr/bin/env python
# Eclipse SUMO, Simulation of Urban MObility; see https://eclipse.org/sumo
# Copyright (C) 2009-2018 German Aerospace Center (DLR) and others.
# This program and the accompanying materials
# are made available under the terms of the Eclipse Public License v2.0
# which accompanies this distribution, and is available at
# http://www.eclipse.org/legal/epl-v20.html
# SPDX-License-Identifier: EPL-2.0

# @file    runner.py
# @author  Lena Kalleske
# @author  Daniel Krajzewicz
# @author  Michael Behrisch
# @author  Jakob Erdmann
# @date    2009-03-26
# @version $Id$

from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import optparse
import random
import xlsxwriter
from helpful import *


# we need to import python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("please declare environment variable 'SUMO_HOME'")

from sumolib import checkBinary  # noqa
import traci  # noqa



def run():
    """execute the TraCI control loop"""
    step = 0
    # we start with phase 2 where EW has green
    workbook = xlsxwriter.Workbook('trajectory.xlsx') 
    worksheet = workbook.add_worksheet('test1')
    ## create a excel sheet
    simulation_step = []
    begin_step = 20
    vehicle_store = []
    #initialize some parameters 
    EdgeListA_E = ['edge-AW2-AW1',"edge-AW1-AO0",'edge-AO0-BW1','edge-BW1-BO0','edge-BO0-CW1','edge-BW1-BO0','edge-CO0-DW1','edge-DW1-DO0','edge-DO0-EW1','edge-EW1-EO0','edge-EO0-EE2'] 
    EdgeListE_A = ['edge-EE2-EE1','edge-EE1-EO0','edge-EO0-DE1','edge-DE1-DO0','edge-DO0-CE1','edge-CE1-CO0','edge-CO0-BE1','edge-BE1-BO0','edge-BO0-AE1','edge-AE1-AO0','edge-AO0-AW2']
    # Edegs list which can help us locate the vehicle;
    RouteListA_E = ['AW-B-C-D-E-ST','AS-B-C-D-E-ST','AN-B-C-D-E-ST','BS-C-D-E-ST','BN-C-D-E-ST','CS-D-E-ST','CN-D-E-ST','DS-E-ST','DN-E-ST'] 
    RouteListE_A = ["EE-D-C-B-A-ST"]
    # Routes's ID list which we need to track.
    ####3################################################

    TrackDirection = 'A_E'
    #轨迹的方向： 'A_E' OR 'E_A'
    if TrackDirection == 'A_E':
        EdgeList = EdgeListA_E
        RouteList = RouteListA_E
    else:
        EdgeList = EdgeListE_A
        RouteList = RouteListE_A


    while traci.simulation.getMinExpectedNumber() > 0 and step <= 200:
        traci.simulationStep()
        if step >= begin_step:
            VehicleSet = traci.vehicle.getIDList() # get all Vehicle's ID
            #get vehicle's  ID which we want
            temp_vehicle = []
            simulation_step = step - begin_step
            for VehicleID in VehicleSet:
                JudgeValue = judge_needed(VehicleID,EdgeList,RouteList)
                # 选取从A交叉口西行驶至E交叉口东直行的车辆
                if JudgeValue:    
                    temp_vehicle.append(VehicleID)

            for temp_vehicleID in temp_vehicle:
                if temp_vehicleID not in vehicle_store:
                    vehicle_store.append(temp_vehicleID)
            #用Vehicle_store 来装路径为特定路径的车辆
            for VehicleID in temp_vehicle:
                travel_distance = get_distance(VehicleID,TrackDirection)
                worksheet.write(simulation_step,vehicle_store.index(VehicleID),travel_distance)
        step += 1
    workbook.close()
    traci.close()
    sys.stdout.flush()


def get_options():
    optParser = optparse.OptionParser()
    optParser.add_option("--nogui", action="store_true",
                         default=False, help="run the commandline version of sumo")
    options, args = optParser.parse_args()
    return options


# this is the main entry point of this script
if __name__ == "__main__":
    options = get_options()

    # this script has been called from the command line. It will start sumo as a
    # server, then connect and run
    if options.nogui:
        sumoBinary = checkBinary('sumo')
    else:
        sumoBinary = checkBinary('sumo-gui')

    # first, generate the route file for this simulation

    # this is the normal way of using traci. sumo is started as a
    # subprocess and then the python script connects and runs
    traci.start([sumoBinary, "-c", "b.sumocfg",
                             "--tripinfo-output", "tripinfo.xml"])
    run()
