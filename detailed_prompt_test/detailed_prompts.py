detailed_prompt_1_1 = f"""
Simulate a 8 story U-shaped building with a gable roof.
The height of story 1 is 14.8 meters.
The height of story 2 is 8.3 meters.
The height of story 3 is 8.0 meters.
The height of story 4 is 7.4 meters.
The height of story 5 is 7.4 meters.
The height of story 6 is 3.5 meters.
The height of story 7 is 3.5 meters.
The height of story 8 is 3.5 meters.
The horizontal segment is 136.36 meters long and 22.7 meters wide.
The left vertical segment is 78.84 meters long and 98.26 meters wide.
The right vertical segment is 69.55 meters long and 55 meters wide.
The attic height is 26.17 meters.
The building orientation is 298 degrees to the north.
Each story has 3 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.52 for the north, 0.76 for the south, 0.47 for the west, and 0.22 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 8, 9, 10, 11, 12. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 1, 2, 3, 4, 5, 6, 7. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16 the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 17, 18, 19, 20, 21, 22, 23, 24 the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 13, zone 14, zone 15, zone 16, zone 17, zone 18.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 19, zone 20, zone 21, zone 22, zone 23, zone 24.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_2 = f"""
Simulate a 3 story U-shaped building.
The height of story 1 is 3.31 meters.
The height of story 2 is 12.68 meters.
The height of story 3 is 2.71 meters.
The horizontal segment is 431.28 meters long and 11.15 meters wide.
The left vertical segment is 65.23 meters long and 170.26 meters wide.
The right vertical segment is 166.45 meters long and 40 meters wide.
The attic height is 29.55 meters.
The building orientation is 2 degrees to the north.
Each story has 3 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.82 for the north, 0.32 for the south, 0.78 for the west, and 0.25 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5, 6, 7. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 8, 9. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 4, zone 5.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 6, zone 7, zone 8.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 9.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_3 = f"""
Simulate a 5 story T-shaped building with a gable roof.
The height of story 1 is 7.09 meters.
The height of story 2 is 8.49 meters.
The height of story 3 is 2.99 meters.
The height of story 4 is 4.89 meters.
The height of story 5 is 10.93 meters.
The horizontal segment is 217.84 meters long and 101.11 meters wide.
The vertical segment is 70.07 meters long and 214.88 meters wide.
The vertical segment is 28.02 meters to the edge of the horizontal segment.
The attic height is 15.85 meters.
The building orientation is 154 degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.40 for the north, 0.36 for the south, 0.28 for the west, and 0.48 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3, 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5, 6, 7, 8, 9, 10. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 4, zone 5.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 6, zone 7, zone 8.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 9, zone 10.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_4 = f"""
Simulate a 6 story T-shaped building.
The height of story 1 is 1.82 meters.
The height of story 2 is 1.60 meters.
The height of story 3 is 3.29 meters.
The height of story 4 is 8.56 meters.
The height of story 5 is 1.55 meters.
The height of story 6 is 13.27 meters.
The horizontal segment is 260.44 meters long and 352.84 meters wide.
The vertical segment is 116.02 meters long and 393.36 meters wide.
The vertical segment is 51.12 meters to the edge of the horizontal segment.
The building orientation is 167 degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.13 for the north, 0.78 for the south, 0.45 for the west, and 0.59 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 5, 6, 7. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 8, 9, 10, 11, 12. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3 , 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 8, 9, 10, 11, 12, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 4, zone 5.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 6, zone 7, zone 8.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 9, zone 10, zone 11, zone 12.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_5 = f"""
Simulate a 18 story L-shaped building with a gable roof.
The height of story 1 is 9.62 meters.
The height of story 2 is 3.62 meters.
The height of story 3 is 13.18 meters.
The height of story 4 is 6.39 meters.
The height of story 5 is 13.72 meters.
The height of story 6 is 13.78 meters.
The height of story 7 is 12.49 meters.
The height of story 8 is 7.32 meters.
The height of story 9 is 5.95 meters.
The height of story 10 is 1.76 meters.
The height of story 11 is 1.72 meters.
The height of story 12 is 8.66 meters.
The height of story 13 is 12.15 meters.
The height of story 14 is 14.03 meters.
The height of story 15 is 13.54 meters.
The height of story 16 is 14.53 meters.
The height of story 17 is 12.00 meters.
The height of story 18 is 6.57 meters.
The horizontal segment is 386.38 meters long and 318.15 meters wide.
The vertical segment is 247.53 meters long and 354.02 meters wide.
The attic height is 57.72 meters.
The building orientation is 48 degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.42 for the north, 0.33 for the south, 0.46 for the west, and 0.59 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 28, 29, 30, 31, 32, 33, 34, 35, 36, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zon 28, zone 29, zone 30, zone 31, zone 32, zone 33, zone 34, zone 35, zone 36.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_6 = f"""
Simulate a 3 story L-shaped building.
The height of story 1 is 10.10 meters.
The height of story 2 is 13.69 meters.
The height of story 3 is 4.10 meters.
The horizontal segment is 221.61 meters long and 37.02 meters wide.
The vertical segment is 177.6 meters long and 95.06 meters wide.
The building orientation is 301 degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.14 for the north, 0.23 for the south, 0.64 for the west, and 0.61 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 6. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 3, zone 4.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 5.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 6.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_7 = f"""
Simulate a 12 story hollow square, courtyard building with a gable roof.
The height of story 1 is 6.94 meters.
The height of story 2 is 14.70 meters.
The height of story 3 is 12.10 meters.
The height of story 4 is 3.86 meters.
The height of story 5 is 5.88 meters.
The height of story 6 is 4.02 meters.
The height of story 7 is 10.34 meters.
The height of story 8 is 14.93 meters.
The height of story 9 is 12.80 meters.
The height of story 10 is 5.27 meters.
The height of story 11 is 10.54 meters.
The height of story 12 is 7.56 meters.
The horizontal segments are 207.17 meters long and 72.17 meters wide.
The vertical segments are 46.85 meters long and 456.78 meters wide.
The attic height is 4.19 meters.
The building orientation is 240 degrees to the north.
Each story has 4 thermal zones in each orientation.
The window-to-wall ratio is 0.73 for the north, 0.40 for the south, 0.71 for the west, and 0.86 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zon 28, zone 29, zone 30, zone 31, zone 32, zone 33, zone 34, zone 35, zone 36, zone 37, zone 38, zone 39, zone 40, zone 41, zone 42, zone 43, zone 44, zone 45, zone 46, zone 47, zone 48.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_8 = f"""
Simulate a 1 story hollow square, courtyard building.
The height of story 1 is 3.53 meters.
The horizontal segments are 48.46 meters long and 40.11 meters wide.
The vertical segments are 2.78 meters long and 315.35 meters wide.
The attic height is 12.53 meters.
The building orientation is 297 degrees to the north.
Each story has 4 thermal zones in each orientation.
The window-to-wall ratio is 0.77 for the north, 0.18 for the south, 0.28 for the west, and 0.38 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 2, 3. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 4. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 2, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 2.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 3.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 4.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_9 = f"""
Simulate a 10 story building that is 219.25 meters long, 157.95 meters wide.
The height of story 1 is 8.40 meters.
The height of story 2 is 13.70 meters.
The height of story 3 is 3.41 meters.
The height of story 4 is 4.21 meters.
The height of story 5 is 13.81 meters.
The height of story 6 is 3.53 meters.
The height of story 7 is 11.72 meters.
The height of story 8 is 13.32 meters.
The height of story 9 is 14.15 meters.
The height of story 10 is 10.06 meters.
The building orientation is 126 degrees to the north.
The window-to-wall ratio is 0.70 for the north, 0.33 for the south, 0.36 for the west, and 0.78 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 6, 7, 8, 9, 10. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, 9, 10 the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 3, zone 4, zone 5, zone 6.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 7, zone 8.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 9, zone 10.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_10 = f"""
Simulate a 5 story building that is 287.29 meters long, 426.48 meters wide, with a hip roof.
The height of story 1 is 6.40 meters.
The height of story 2 is 3.35 meters.
The height of story 3 is 12.01 meters.
The height of story 4 is 7.13 meters.
The height of story 5 is 8.04 meters.
The attic height is 31.81 meters.
The building orientation is 85 degrees to the north.
The window-to-wall ratio is 0.56 for the north, 0.46 for the south, 0.73 for the west, and 0.78 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 4, 5. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 3.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 4.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 5.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_11 = f"""
Simulate a 16 story building that is 72.88 meters long, 167.94 meters wide, with a gable roof.
The height of story 1 is 13.33 meters.
The height of story 2 is 2.77 meters.
The height of story 3 is 11.64 meters.
The height of story 4 is 11.21 meters.
The height of story 5 is 2.90 meters.
The height of story 6 is 8.68 meters.
The height of story 7 is 9.22 meters.
The height of story 8 is 12.24 meters.
The height of story 9 is 12.76 meters.
The height of story 10 is 3.26 meters.
The height of story 11 is 6.01 meters.
The height of story 12 is 6.11 meters.
The height of story 13 is 14.20 meters.
The height of story 14 is 6.14 meters.
The height of story 15 is 13.66 meters.
The height of story 16 is 13.48 meters.
The attic height is 19.09 meters.
The building orientation is 273 degrees to the north.
The window-to-wall ratio is 0.68 for the north, 0.18 for the south, 0.49 for the west, and 0.10 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 5, 6, 7. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 8, 9, 10, 11, 12, 13, 14, 15, 16. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3 , 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 8, 9, 10, 11, 12, 13, 14, 15, 16 the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 4, zone 5.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 6, zone 7, zone 8.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_12 = f"""
Simulate a 3 story building that is 202.15 meters long, 257.05 meters wide.
The height of story 1 is 6.18 meters.
The height of story 2 is 2.94 meters.
The height of story 3 is 9.77 meters.
The attic height is 43.78 meters.
The building orientation is 202 degrees to the north.
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.
The depth of exterior thermal zone is 20.29 meters.
The window-to-wall ratio is 0.71 for the north, 0.56 for the south, 0.21 for the west, and 0.22 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 5, 6, 7. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 8, 9, 10, 11, 12, 13, 14, 15. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3 , 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 8, 9, 10, 11, 12, 13, 14, 15, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 4, zone 5.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 6, zone 7, zone 8.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_13 = f"""
Simulate a 2 story building that is 53.37 meters long, 31.97 meters wide, with a hip roof.
The height of story 1 is 10.77 meters.
The height of story 2 is 1.88 meters..
The attic height is 0.86 meters.
The building orientation is 167 degrees to the north.
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.
The depth of exterior thermal zone is 7.25 meters.
The window-to-wall ratio is 0.16 for the north, 0.69 for the south, 0.37 for the west, and 0.87 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 5, 6, 7. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 8, 9, 10. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3 , 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 8, 9, 10, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 4, zone 5.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 6, zone 7, zone 8.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 9, zone 10.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_1_14 = f"""
Simulate a 3 story building that is 281.17 meters long, 210.20 meters wide, with a gable roof.
The height of story 1 is 3.67 meters.
The height of story 2 is 6.06 meters.
The height of story 3 is 7.38 meters.
The attic height is 13.24 meters.
The building orientation is 89 degrees to the north.
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.
The depth of exterior thermal zone is 26.38 meters.
The window-to-wall ratio is 0.48 for the north, 0.77 for the south, 0.52 for the west, and 0.34 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 5, 6, 7. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 8, 9, 10, 11, 12, 13, 14, 15. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3 , 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 8, 9, 10, 11, 12, 13, 14, 15the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with electric heater for heating.
The unit 1 serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is 41378 W for cooling and Autosize W for heating.
The rated cooling COP is 3.8 and the heating efficiency is 0.75.
The supply air temperature for cooling is 14.3 Celsius, and for heating is 40.7 Celsius.
The outdoor ventilation rate is 3.69 ACH.
The fan efficiency is 0.78, the pressure rise is 1770 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 4, zone 5.
The rated capacity is Autosize W for cooling and 36963 W for heating.
The rated cooling COP is 3.96 and the heating efficiency is 0.87.
The supply air temperature for cooling is 18.6 Celsius, and for heating is 49.0 Celsius.
The outdoor ventilation rate is 1.18 ACH.
The fan efficiency is 0.64, the pressure rise is 1536 Pa, and the maximum flow rate is 130.08 m3/s.
The unit 3 serves zone 6, zone 7, zone 8.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.47 and the heating efficiency is 0.78.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 44.7 Celsius.
The outdoor ventilation rate is 1.35 ACH.
The fan efficiency is 0.88, the pressure rise is 1140 Pa, and the maximum flow rate is Autosize m3/s.
The unit 4 serves zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is 32141 W for cooling and Autosize W for heating.
The rated cooling COP is 4.89 and the heating efficiency is 0.68.
The supply air temperature for cooling is 16.4 Celsius, and for heating is 43.1 Celsius.
The outdoor ventilation rate is 2.71 ACH.
The fan efficiency is 0.61, the pressure rise is 1160 Pa, and the maximum flow rate is 5.26 m3/s.
"""

detailed_prompt_2_1 = f"""
Simulate a 4 story U-shaped building with a gable roof.
The height of story 1 is 12.61 meters.
The height of story 2 is 10.03 meters.
The height of story 3 is 12.68 meters.
The height of story 4 is 11.75 meters.
The horizontal segment is 389.33 meters long and 85.62 meters wide.
The left vertical segment is 282.67 meters long and 206.4 meters wide.
The right vertical segment is 186.16 meters long and 217 meters wide.
The attic height is 69.84 meters.
The building orientation is 30 degrees to the north.
Each story has 3 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.39 for the north, 0.86 for the south, 0.14 for the west, and 0.31 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 6, 7, 8, 9. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 1, 2, 3, 4, 5. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 10, 11, 12. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12 the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 7, zone 8, zone 9.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 10.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
The unit 4 serves zone 11, zone 12.
The fuel type is natural gas.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.04 and the heating efficiency is 0.89.
The supply air temperature for cooling is 18.2 Celsius, and for heating is 42.2 Celsius.
The outdoor ventilation rate is 3.29 ACH.
The fan efficiency is 0.78, the pressure rise is 1668 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_2_2 = f"""
Simulate a 8 story U-shaped building.
The height of story 1 is 3.53 meters.
The height of story 2 is 1.84 meters.
The height of story 3 is 13.29 meters.
The height of story 4 is 10.76 meters.
The height of story 5 is 7.92 meters.
The height of story 6 is 8.10 meters.
The height of story 7 is 8.96 meters.
The height of story 8 is 8.23 meters.
The horizontal segment is 269.51 meters long and 79.21 meters wide.
The left vertical segment is 120.31 meters long and 485.89 meters wide.
The right vertical segment is 159.06 meters long and 168 meters wide.
The attic height is 7.08 meters.
The building orientation is 307 degrees to the north.
Each story has 3 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.26 for the north, 0.21 for the south, 0.22 for the west, and 0.80 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 9, 10, 11, 12, 13, 14, 15, 16. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 17, 18, 19, 20, 21, 22, 23, 24. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 13, zone 14, zone 15, zone 16, zone 17, zone 18.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 19, zone 20.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
The unit 4 serves zone 21, zone 22, zone 23, zone 24.
The fuel type is natural gas.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.04 and the heating efficiency is 0.89.
The supply air temperature for cooling is 18.2 Celsius, and for heating is 42.2 Celsius.
The outdoor ventilation rate is 3.29 ACH.
The fan efficiency is 0.78, the pressure rise is 1668 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_2_3 = f"""
Simulate a 2 story T-shaped building with a gable roof.
The height of story 1 is 6.31 meters.
The height of story 2 is 1.80 meters.
The horizontal segment is 101.11 meters long and 27.37 meters wide.
The vertical segment is 45.66 meters long and 106.71 meters wide.
The vertical segment is 57.16 meters to the edge of the horizontal segment.
The attic height is 4.90 meters.
The building orientation is 290 degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.46 for the north, 0.66 for the south, 0.58 for the west, and 0.85 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 4. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 4, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 3.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 2.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
The unit 4 serves zone 4.
The fuel type is natural gas.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.04 and the heating efficiency is 0.89.
The supply air temperature for cooling is 18.2 Celsius, and for heating is 42.2 Celsius.
The outdoor ventilation rate is 3.29 ACH.
The fan efficiency is 0.78, the pressure rise is 1668 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_2_4 = f"""
Simulate a 6 story T-shaped building.
The height of story 1 is 6.04 meters.
The height of story 2 is 12.39 meters.
The height of story 3 is 14.71 meters.
The height of story 4 is 5.69 meters.
The height of story 5 is 8.07 meters.
The height of story 6 is 10.62 meters.
The horizontal segment is 492.5 meters long and 91.99 meters wide.
The vertical segment is 395.35 meters long and 306.99 meters wide.
The vertical segment is 187.65 meters to the edge of the horizontal segment.
The building orientation is 135 degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.59 for the north, 0.63 for the south, 0.46 for the west, and 0.37 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 6, 7, 8, 9. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 1, 2, 3, 4, 5. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 10, 11, 12. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12 the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 5, zone 6, zone 7.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 8, zone 9, zone 10.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
The unit 4 serves zone 11, zone 12.
The fuel type is natural gas.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.04 and the heating efficiency is 0.89.
The supply air temperature for cooling is 18.2 Celsius, and for heating is 42.2 Celsius.
The outdoor ventilation rate is 3.29 ACH.
The fan efficiency is 0.78, the pressure rise is 1668 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_2_5 = f"""
Simulate a 21 story building that is 333.03 meters long, 19.29 meters wide, with a hip roof.
The height of story 1 is 4.47 meters.
The height of story 2 is 11.50 meters.
The height of story 3 is 3.62 meters.
The height of story 4 is 13.02 meters.
The height of story 5 is 7.59 meters.
The height of story 6 is 9.10 meters.
The height of story 7 is 7.93 meters.
The height of story 8 is 8.69 meters.
The height of story 9 is 3.76 meters.
The height of story 10 is 12.19 meters.
The height of story 11 is 11.36 meters.
The height of story 12 is 11.58 meters.
The height of story 13 is 14.74 meters.
The height of story 14 is 9.93 meters.
The height of story 15 is 11.15 meters.
The height of story 16 is 11.20 meters.
The height of story 17 is 10.30 meters.
The height of story 18 is 1.66 meters.
The height of story 19 is 13.74 meters.
The height of story 20 is 5.45 meters.
The height of story 21 is 14.80 meters.
The attic height is 7.54 meters.
The building orientation is 135 degrees to the north.
The window-to-wall ratio is 0.19 for the north, 0.72 for the south, 0.52 for the west, and 0.34 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 9, 10, 11, 12, 13, 14, 15, 16. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 17, 18, 19, 20, 21. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 13, zone 14, zone 15, zone 16, zone 17, zone 18.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 19, zone 20.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
The unit 4 serves zone 21.
The fuel type is natural gas.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.04 and the heating efficiency is 0.89.
The supply air temperature for cooling is 18.2 Celsius, and for heating is 42.2 Celsius.
The outdoor ventilation rate is 3.29 ACH.
The fan efficiency is 0.78, the pressure rise is 1668 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_2_6 = f"""
Simulate a 7 story building that is 110.33 meters long, 60.11 meters wide, with a gable roof.
The height of story 1 is 8.26 meters.
The height of story 2 is 6.58 meters.
The height of story 3 is 2.29 meters.
The height of story 4 is 7.85 meters.
The height of story 5 is 4.29 meters.
The height of story 6 is 13.50 meters.
The height of story 7 is 4.98 meters.
The attic height is 2.61 meters.
The building orientation is 126 degrees to the north.
The window-to-wall ratio is 0.15 for the north, 0.44 for the south, 0.61 for the west, and 0.78 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 5, 6. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 7. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 3, zone 4.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 5.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
The unit 4 serves zone 6, zone 7.
The fuel type is natural gas.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.04 and the heating efficiency is 0.89.
The supply air temperature for cooling is 18.2 Celsius, and for heating is 42.2 Celsius.
The outdoor ventilation rate is 3.29 ACH.
The fan efficiency is 0.78, the pressure rise is 1668 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_2_7 = f"""
Simulate a 3 story building that is 307.22 meters long, 344.14 meters wide.
The height of story 1 is 9.90 meters.
The height of story 2 is 14.02 meters.
The height of story 3 is 6.31 meters.
The building orientation is 205 degrees to the north.
The window-to-wall ratio is 0.27 for the north, 0.80 for the south, 0.33 for the west, and 0.28 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 2. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 3. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 2, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 3, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 2.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 3.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
"""

detailed_prompt_2_8 = f"""
Simulate a 6 story building that is 136.60 meters long, 153.72 meters wide, with a hip roof.
The height of story 1 is 5.11 meters.
The height of story 2 is 6.39 meters.
The height of story 3 is 3.09 meters.
The height of story 4 is 14.90 meters.
The height of story 5 is 3.34 meters.
The height of story 6 is 7.18 meters.
The attic height is 40.59 meters.
The building orientation is 50 degrees to the north.
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.
The depth of exterior thermal zone is 53.86 meters.
The window-to-wall ratio is 0.58 for the north, 0.87 for the south, 0.24 for the west, and 0.56 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 9, 10, 11, 12, 13, 14, 15, 16. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 17, 18, 19, 20, 21, 22, 23, 24. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 13, zone 14, zone 15, zone 16, zone 17, zone 18.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 19, zone 20.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
The unit 4 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30.
The fuel type is natural gas.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.04 and the heating efficiency is 0.89.
The supply air temperature for cooling is 18.2 Celsius, and for heating is 42.2 Celsius.
The outdoor ventilation rate is 3.29 ACH.
The fan efficiency is 0.78, the pressure rise is 1668 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_2_9 = f"""
Simulate a 4 story building that is 496.40 meters long, 400.53 meters wide, with a gable roof.
The height of story 1 is 11.93 meters.
The height of story 2 is 14.44 meters.
The height of story 3 is 6.08 meters.
The height of story 4 is 5.82 meters.
The attic height is 134.36 meters.
The building orientation is 286 degrees to the north.
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.
The depth of exterior thermal zone is 107.60 meters.
The window-to-wall ratio is 0.79 for the north, 0.11 for the south, 0.34 for the west, and 0.54 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 9, 10, 11, 12, 13, 14, 15, 16. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 17, 18, 19, 20. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 13, zone 14, zone 15, zone 16, zone 17.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 18.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
The unit 4 serves zone 19, zone 20.
The fuel type is natural gas.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.04 and the heating efficiency is 0.89.
The supply air temperature for cooling is 18.2 Celsius, and for heating is 42.2 Celsius.
The outdoor ventilation rate is 3.29 ACH.
The fan efficiency is 0.78, the pressure rise is 1668 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_2_10 = f"""
Simulate a 3 story building that is 383.64 meters long, 190.44 meters wide.
The height of story 1 is 12.63 meters.
The height of story 2 is 7.88 meters.
The height of story 3 is 10.46 meters.
The attic height is 113.06 meters.
The building orientation is 354 degrees to the north.
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.
The depth of exterior thermal zone is 81.77 meters.
The window-to-wall ratio is 0.36 for the north, 0.86 for the south, 0.88 for the west, and 0.86 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 9, 10, 11,. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 12, 13, 14, 15. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 8, zone 9, zone 10, zone 11, zone 12.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 13, zone 14, zone 15.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
"""

detailed_prompt_2_11 = f"""
Simulate a 5 story L-shaped building with a gable roof.
The height of story 1 is 13.59 meters.
The height of story 2 is 2.72 meters.
The height of story 3 is 12.26 meters.
The height of story 4 is 8.59 meters.
The height of story 5 is 10.28 meters.
The horizontal segment is 326.41 meters long and 163.48 meters wide.
The vertical segment is 241.54 meters long and 443.81 meters wide.
The attic height is 45.23 meters.
The building orientation is 14 degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.71 for the north, 0.81 for the south, 0.88 for the west, and 0.40 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 5, 6, 7, 8. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 9, 10. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2, zone 3.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 4, zone 5, zone 6, zone 7.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 8, zone 9, zone 10.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
"""

detailed_prompt_2_12 = f"""
Simulate a 18 story L-shaped building.
The height of story 1 is 11.02 meters.
The height of story 2 is 9.37 meters.
The height of story 3 is 7.19 meters.
The height of story 4 is 7.02 meters.
The height of story 5 is 5.20 meters.
The height of story 6 is 4.33 meters.
The height of story 7 is 6.50 meters.
The height of story 8 is 11.21 meters.
The height of story 9 is 8.91 meters.
The height of story 10 is 13.08 meters.
The height of story 11 is 14.85 meters.
The height of story 12 is 5.51 meters.
The height of story 13 is 2.17 meters.
The height of story 14 is 9.05 meters.
The height of story 15 is 7.77 meters.
The height of story 16 is 8.90 meters.
The height of story 17 is 7.81 meters.
The height of story 18 is 6.35 meters.
The horizontal segment is 169.89 meters long and 80.65 meters wide.
The vertical segment is 68.89 meters long and 228.61 meters wide.
The building orientation is 88 degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.80 for the north, 0.38 for the south, 0.19 for the west, and 0.20 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 11, 12, 13, 14, 15, 16, 17, 18. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 29, 30, 31, 32, 33, 34, 35, 36, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
"""

detailed_prompt_2_13 = f"""
Simulate a 5 story hollow square, courtyard building with a gable roof.
The height of story 1 is 6.39 meters.
The height of story 2 is 12.67 meters.
The height of story 3 is 8.64 meters.
The height of story 4 is 3.70 meters.
The height of story 5 is 6.55 meters.
The horizontal segments are 418.62 meters long and 6.36 meters wide.
The vertical segments are 107.73 meters long and 88.70 meters wide.
The attic height is 19.85 meters.
The building orientation is 249 degrees to the north.
Each story has 4 thermal zones in each orientation.
The window-to-wall ratio is 0.30 for the north, 0.37 for the south, 0.35 for the west, and 0.13 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 9, 10, 11,. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 8, zone 9, zone 10, zone 11, zone 12.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
"""

detailed_prompt_2_14 = f"""
Simulate a 4 story hollow square, courtyard building.
The height of story 1 is 11.13 meters.
The height of story 2 is 11.17 meters.
The height of story 3 is 6.65 meters.
The height of story 4 is 8.02 meters.
The horizontal segments are 178.21 meters long and 10.45 meters wide.
The vertical segments are 8.85 meters long and 126.91 meters wide.
The attic height is 13.48 meters.
The building orientation is 296 degrees to the north.
Each story has 4 thermal zones in each orientation.
The window-to-wall ratio is 0.35 for the north, 0.25 for the south, 0.33 for the west, and 0.80 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 9, 10, 11,. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 12, 13, 14, 15, 16. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with fuel burner for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 4599 W for heating.
The rated cooling COP is 3.61 and the heating efficiency is 0.84.
The supply air temperature for cooling is 13.2 Celsius, and for heating is 47.5 Celsius.
The outdoor ventilation rate is 3.01 ACH.
The fan efficiency is 0.62, the pressure rise is 862 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 8, zone 9, zone 10, zone 11, zone 12.
The fuel type is coal.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and 49254 W for heating.
The rated cooling COP is 3.55 and the heating efficiency is 0.82.
The supply air temperature for cooling is 18.7 Celsius, and for heating is 41.9 Celsius.
The outdoor ventilation rate is 1.46 ACH.
The fan efficiency is 0.85, the pressure rise is 346 Pa, and the maximum flow rate is 138.49 m3/s.
The unit 3 serves zone 13, zone 14, zone 15, zone 16.
The fuel type is natural gas.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.22 and the heating efficiency is 0.72.
The supply air temperature for cooling is 13.0 Celsius, and for heating is 54.4 Celsius.
The outdoor ventilation rate is 0.79 ACH.
The fan efficiency is 0.87, the pressure rise is 1707 Pa, and the maximum flow rate is 89.2 m3/s.
"""

detailed_prompt_3_1 = f"""
Simulate a 9 story U-shaped building with a gable roof.
The height of story 1 is 2.34 meters.
The height of story 2 is 5.76 meters.
The height of story 3 is 10.88 meters.
The height of story 4 is 1.79 meters.
The height of story 5 is 3.57 meters.
The height of story 6 is 2.91 meters.
The height of story 7 is 7.32 meters.
The height of story 8 is 4.81 meters.
The height of story 9 is 7.82 meters.
The horizontal segment is 335.27 meters long and 20.19 meters wide.
The left vertical segment is 157.89 meters long and 325.78 meters wide.
The right vertical segment is 77.09 meters long and 53 meters wide.
The attic height is 52.89 meters.
The building orientation is 144 degrees to the north.
Each story has 3 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.22 for the north, 0.70 for the south, 0.22 for the west, and 0.83 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 21, 22, 23, 24, 25, 26, 27. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 5, zone 6, zone 7, zone 8, zone 9.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, 
zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_2 = f"""
Simulate a 2 story U-shaped building.
The height of story 1 is 9.87 meters.
The height of story 2 is 11.84 meters.
The horizontal segment is 50.9 meters long and 23.15 meters wide.
The left vertical segment is 40.7 meters long and 74.72 meters wide.
The right vertical segment is 13.78 meters long and 267 meters wide.
The attic height is 6.65 meters.
The building orientation is 114 degrees to the north.
Each story has 3 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.17 for the north, 0.34 for the south, 0.18 for the west, and 0.80 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3, 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5, 6. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 3, zone 4.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 5, zone 6.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_3 = f"""
Simulate a 13 story T-shaped building with a gable roof.
The height of story 1 is 14.36 meters.
The height of story 2 is 7.17 meters.
The height of story 3 is 2.73 meters.
The height of story 4 is 2.53 meters.
The height of story 5 is 14.80 meters.
The height of story 6 is 11.92 meters.
The height of story 7 is 5.91 meters.
The height of story 8 is 4.44 meters.
The height of story 9 is 12.30 meters.
The height of story 10 is 10.63 meters.
The height of story 11 is 9.78 meters.
The height of story 12 is 13.61 meters.
The height of story 13 is 9.96 meters.
The horizontal segment is 327.42 meters long and 84.28 meters wide.
The vertical segment is 143.42 meters long and 105.96 meters wide.
The vertical segment is 111.60 meters to the edge of the horizontal segment.
The attic height is 35.24 meters.
The building orientation is 24 degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.77 for the north, 0.54 for the south, 0.72 for the west, and 0.42 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 21, 22, 23, 24, 25, 26. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 5, zone 6, zone 7, zone 8, zone 9.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, 
zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_4 = f"""
Simulate a 4 story T-shaped building.\n
The height of story 1 is 14.07 meters.\n
The height of story 2 is 9.81 meters.\n
The height of story 3 is 6.20 meters.\n
The height of story 4 is 9.33 meters.\n
The horizontal segment is 54.85 meters long and 248.3 meters wide.\n
The vertical segment is 47.06 meters long and 466.82 meters wide.\n
The vertical segment is 0.80 meters to the edge of the horizontal segment.\n
The building orientation is 265 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.87 for the north, 0.28 for the south, 0.73 for the west, and 0.87 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3, 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5, 6, 7, 8. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 3, zone 4.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 5, zone 6, zone 7, zone 8.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_5 = f"""
Simulate a 15 story building that is 452.34 meters long, 68.64 meters wide, with a hip roof\n
The height of story 1 is 2.11 meters.\n
The height of story 2 is 7.19 meters.\n
The height of story 3 is 3.36 meters.\n
The height of story 4 is 8.56 meters.\n
The height of story 5 is 8.33 meters.\n
The height of story 6 is 6.62 meters.\n
The height of story 7 is 14.06 meters.\n
The height of story 8 is 4.33 meters.\n
The height of story 9 is 10.52 meters.\n
The height of story 10 is 8.46 meters.\n
The height of story 11 is 3.30 meters.\n
The height of story 12 is 12.10 meters.\n
The height of story 13 is 13.79 meters.\n
The height of story 14 is 8.12 meters.\n
The height of story 15 is 2.94 meters.\n
The attic height is 61.43 meters.\n
The building orientation is 16 degrees to the north.\n
The window-to-wall ratio is 0.73 for the north, 0.10 for the south, 0.72 for the west, and 0.24 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 7, 8 ,9, 10. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 11, 12, 13, 14, 15. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 5, zone 6, zone 7, zone 8, zone 9.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 10, zone 11, zone 12, zone 13, zone 14, zone 15.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_6 = f"""
Simulate a 16 story building that is 283.19 meters long, 74.82 meters wide, with a gable roof\n
The height of story 1 is 6.75 meters.\n
The height of story 2 is 3.29 meters.\n
The height of story 3 is 14.58 meters.\n
The height of story 4 is 3.06 meters.\n
The height of story 5 is 11.84 meters.\n
The height of story 6 is 6.93 meters.\n
The height of story 7 is 6.63 meters.\n
The height of story 8 is 1.87 meters.\n
The height of story 9 is 3.92 meters.\n
The height of story 10 is 8.62 meters.\n
The height of story 11 is 7.04 meters.\n
The height of story 12 is 12.72 meters.\n
The height of story 13 is 13.22 meters.\n
The height of story 14 is 9.59 meters.\n
The height of story 15 is 5.50 meters.\n
The height of story 16 is 14.57 meters.\n
The attic height is 20.25 meters.\n
The building orientation is 115 degrees to the north.\n
The window-to-wall ratio is 0.76 for the north, 0.59 for the south, 0.48 for the west, and 0.22 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 7, 8 ,9, 10. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 11, 12, 13, 14, 15, 16. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 5, zone 6, zone 7, zone 8, zone 9.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_7 = f"""
Simulate a 20 story building that is 369.55 meters long, 256.33 meters wide.\n
The height of story 1 is 14.79 meters.\n
The height of story 2 is 8.20 meters.\n
The height of story 3 is 4.13 meters.\n
The height of story 4 is 1.78 meters.\n
The height of story 5 is 8.20 meters.\n
The height of story 6 is 13.78 meters.\n
The height of story 7 is 6.46 meters.\n
The height of story 8 is 11.93 meters.\n
The height of story 9 is 4.47 meters.\n
The height of story 10 is 3.70 meters.\n
The height of story 11 is 4.56 meters.\n
The height of story 12 is 2.73 meters.\n
The height of story 13 is 13.25 meters.\n
The height of story 14 is 11.59 meters.\n
The height of story 15 is 4.45 meters.\n
The height of story 16 is 10.91 meters.\n
The height of story 17 is 9.23 meters.\n
The height of story 18 is 3.29 meters.\n
The height of story 19 is 5.54 meters.\n
The height of story 20 is 3.66 meters.\n
The building orientation is 253 degrees to the north.\n
The window-to-wall ratio is 0.75 for the north, 0.19 for the south, 0.54 for the west, and 0.70 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 7, 8 ,9, 10. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 5, zone 6, zone 7, zone 8, zone 9.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16 zone 17, zone 18, zone 19, zone 20.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_8 = f"""
Simulate a 2 story building that is 53.37 meters long, 31.97 meters wide, with a hip roof\n
The height of story 1 is 10.77 meters.\n
The height of story 2 is 1.88 meters.\n
The attic height is 0.86 meters.\n
The building orientation is 167 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 7.25 meters.\n
The window-to-wall ratio is 0.16 for the north, 0.69 for the south, 0.37 for the west, and 0.87 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3, 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5, 6, 7, 8, 9, 10. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, 9, 10 the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 3, zone 4.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_9 = f"""
Simulate a 4 story building that is 330.69 meters long, 205.46 meters wide, with a gable roof.\n
The height of story 1 is 4.78 meters.\n
The height of story 2 is 13.82 meters.\n
The height of story 3 is 3.25 meters.\n
The height of story 4 is 11.87 meters.\n
The attic height is 13.39 meters.\n
The building orientation is 194 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 62.62 meters.\n
The window-to-wall ratio is 0.24 for the north, 0.27 for the south, 0.13 for the west, and 0.58 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 7, 8 ,9, 10. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 5, zone 6, zone 7, zone 8, zone 9.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16 zone 17, zone 18, zone 19, zone 20.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_10 = f"""
Simulate a 2 story building that is 304.46 meters long, 47.43 meters wide.\n
The height of story 1 is 5.04 meters.\n
The height of story 2 is 4.67 meters.\n
The attic height is 84.96 meters.\n
The building orientation is 61 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 9.41 meters.\n
The window-to-wall ratio is 0.25 for the north, 0.58 for the south, 0.54 for the west, and 0.15 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3, 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5, 6, 7, 8, 9, 10. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, 9, 10 the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 3, zone 4.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_11 = f"""
Simulate a 3 story L-shaped building with a gable roof.\n
The height of story 1 is 4.98 meters.\n
The height of story 2 is 11.68 meters.\n
The height of story 3 is 13.48 meters.\n\n
The horizontal segment is 161.95 meters long and 76.57 meters wide.\n
The vertical segment is 34.43 meters long and 149.3 meters wide.\n
The attic height is 12.72 meters.\n
The building orientation is 203 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.59 for the north, 0.29 for the south, 0.36 for the west, and 0.54 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3, 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5, 6. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 3, zone 4.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 5, zone 6.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_12 = f"""
Simulate a 3 story L-shaped building.\n
The height of story 1 is 10.10 meters.\n
The height of story 2 is 13.69 meters.\n
The height of story 3 is 4.10 meters.\n\n
The horizontal segment is 221.61 meters long and 37.02 meters wide.\n
The vertical segment is 177.6 meters long and 95.06 meters wide.\n
The building orientation is 301 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.14 for the north, 0.23 for the south, 0.64 for the west, and 0.61 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3, 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5, 6. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 3, zone 4.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 5, zone 6.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_13 = f"""
Simulate a 5 story hollow square, courtyard building with a gable roof.\n
The height of story 1 is 6.39 meters.\n
The height of story 2 is 12.67 meters.\n
The height of story 3 is 8.64 meters.\n
The height of story 4 is 3.70 meters.\n
The height of story 5 is 6.55 meters.\n
The horizontal segments are 418.62 meters long and 6.36 meters wide.\n
The vertical segments are 107.73 meters long and 88.70 meters wide.\n
The attic height is 19.85 meters.\n
The building orientation is 249 degrees to the north.\n
Each story has 4 thermal zones in each orientation.\n
The window-to-wall ratio is 0.30 for the north, 0.37 for the south, 0.35 for the west, and 0.13 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 7, 8 ,9, 10. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 5, zone 6, zone 7, zone 8, zone 9.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16 zone 17, zone 18, zone 19, zone 20.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_3_14 = f"""
Simulate a 9 story hollow square, courtyard building.\n
The height of story 1 is 14.64 meters.\n
The height of story 2 is 11.39 meters.\n
The height of story 3 is 7.73 meters.\n
The height of story 4 is 6.98 meters.\n
The height of story 5 is 4.55 meters.\n
The height of story 6 is 13.12 meters.\n
The height of story 7 is 1.63 meters.\n
The height of story 8 is 4.94 meters.\n
The height of story 9 is 11.62 meters.\n
The horizontal segments are 298.43 meters long and 28.52 meters wide.\n
The vertical segments are 54.11 meters long and 130.70 meters wide.\n
The attic height is 65.16 meters.\n
The building orientation is 234 degrees to the north.\n
Each story has 4 thermal zones in each orientation.\n
The window-to-wall ratio is 0.38 for the north, 0.28 for the south, 0.79 for the west, and 0.71 for the east.
The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8 ,9, 10. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 
The HVAC system in this building is packaged air conditioning unit, rooftop unit, DX system with heat pump for heating.
The unit 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9.
It includes an economizer, which operates based on differential enthalpy.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.97 and the heating efficiency is 6.14.
The supply air temperature for cooling is 15.3 Celsius, and for heating is 46.4 Celsius.
The outdoor ventilation rate is 1.51 ACH.
The fan efficiency is 0.64, the pressure rise is 873 Pa, and the maximum flow rate is Autosize m3/s.
The unit 2 serves zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16 zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential dry bulb.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 5.68 and the heating efficiency is 5.59.
The supply air temperature for cooling is 17.7 Celsius, and for heating is 44.5 Celsius.
The outdoor ventilation rate is 2.23 ACH.
The fan efficiency is 0.86, the pressure rise is 489 Pa, and the maximum flow rate is Autosize m3/s.
The unit 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31, zone 32, zone 33, zone 34, zone 35, zone 36.
The rated capacity is Autosize W for cooling and Autosize W for heating.
The rated cooling COP is 4.86 and the heating efficiency is 6.19.
The supply air temperature for cooling is 12.3 Celsius, and for heating is 51.3 Celsius.
The outdoor ventilation rate is 1.5 ACH.
The fan efficiency is 0.71, the pressure rise is 1888 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_4_1 = f"""
Simulate a 1 story U-shaped building with a gable roof.\n
The height of story 1 is 2.93 meters.\n
The horizontal segment is 97.08 meters long and 4.04 meters wide.\n
The left vertical segment is 20.23 meters long and 12.6 meters wide.\n
The right vertical segment is 42.19 meters long and 215 meters wide.\n
The attic height is 9.35 meters.\n
The building orientation is 202 degrees to the north.\n
Each story has 3 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.13 for the north, 0.22 for the south, 0.84 for the west, and 0.24 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 2. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 3. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 2, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 3, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_4_2 = f"""
Simulate a 2 story U-shaped building.\n
The height of story 1 is 12.82 meters.\n
The height of story 2 is 5.47 meters.\n
The horizontal segment is 213.83 meters long and 33.08 meters wide.\n
The left vertical segment is 190.57 meters long and 96.69 meters wide.\n
The right vertical segment is 46.43 meters long and 250 meters wide.\n
The attic height is 7.14 meters.\nThe building orientation is 198 degrees to the north.\n
Each story has 3 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.37 for the north, 0.41 for the south, 0.59 for the west, and 0.82 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3, 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5, 6. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_4_3 = f"""
Simulate a 9 story T-shaped building with a gable roof.\n
The height of story 1 is 10.96 meters.\n
The height of story 2 is 9.07 meters.\n
The height of story 3 is 7.74 meters.\n
The height of story 4 is 5.31 meters.\n
The height of story 5 is 2.10 meters.\n
The height of story 6 is 11.31 meters.\n
The height of story 7 is 8.83 meters.\n
The height of story 8 is 3.25 meters.\n
The height of story 9 is 10.60 meters.\n
The horizontal segment is 237.8 meters long and 122.84 meters wide.\n
The vertical segment is 117.97 meters long and 365.23 meters wide.\n
The vertical segment is 39.09 meters to the edge of the horizontal segment.\n
The attic height is 30.36 meters.\nThe building orientation is 265 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.12 for the north, 0.29 for the south, 0.36 for the west, and 0.47 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 7, 8 ,9, 10, 11, 12, 13, 14. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 15, 16, 17, 18. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_4_4 = f"""
Simulate a 3 story T-shaped building.\n
The height of story 1 is 3.34 meters.\n
The height of story 2 is 11.27 meters.\n
The height of story 3 is 2.72 meters.\n
The horizontal segment is 234.68 meters long and 171.93 meters wide.\n
The vertical segment is 143.95 meters long and 420.97 meters wide.\n
The vertical segment is 49.24 meters to the edge of the horizontal segment.\n
The building orientation is 322 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.75 for the north, 0.46 for the south, 0.20 for the west, and 0.77 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3, 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5, 6. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_4_5 = f"""
Simulate a 18 story building that is 340.33 meters long, 155.33 meters wide, with a hip roof\n
The height of story 1 is 2.68 meters.\n
The height of story 2 is 8.23 meters.\n
The height of story 3 is 13.96 meters.\n
The height of story 4 is 12.58 meters.\n
The height of story 5 is 9.21 meters.\n
The height of story 6 is 6.75 meters.\n
The height of story 7 is 13.88 meters.\n
The height of story 8 is 5.60 meters.\n
The height of story 9 is 8.60 meters.\n
The height of story 10 is 4.02 meters.\n
The height of story 11 is 13.49 meters.\n
The height of story 12 is 13.23 meters.\n
The height of story 13 is 2.21 meters.\n
The height of story 14 is 7.20 meters.\n
The height of story 15 is 7.87 meters.\n
The height of story 16 is 6.31 meters.\n
The height of story 17 is 13.90 meters.\n
The height of story 18 is 2.88 meters.\n
The attic height is 63.58 meters.\n
The building orientation is 273 degrees to the north.\n
The window-to-wall ratio is 0.23 for the north, 0.88 for the south, 0.50 for the west, and 0.16 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 7, 8 ,9, 10, 11, 12, 13, 14. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 15, 16, 17, 18. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""
detailed_prompt_4_6 = f"""
Simulate a 20 story building that is 339.55 meters long, 336.77 meters wide, with a gable roof\n
The height of story 1 is 3.76 meters.\n
The height of story 2 is 5.40 meters.\n
The height of story 3 is 10.55 meters.\n
The height of story 4 is 14.52 meters.\n
The height of story 5 is 13.53 meters.\n
The height of story 6 is 13.01 meters.\n
The height of story 7 is 13.28 meters.\n
The height of story 8 is 13.16 meters.\n
The height of story 9 is 10.85 meters.\n
The height of story 10 is 1.70 meters.\n
The height of story 11 is 14.18 meters.\n
The height of story 12 is 12.19 meters.\n
The height of story 13 is 6.29 meters.\n
The height of story 14 is 4.12 meters.\n
The height of story 15 is 13.83 meters.\n
The height of story 16 is 12.63 meters.\n
The height of story 17 is 10.28 meters.\n
The height of story 18 is 14.24 meters.\n
The height of story 19 is 3.09 meters.\n
The height of story 20 is 14.44 meters.\n
The attic height is 1.37 meters.\n
The building orientation is 193 degrees to the north.\n
The window-to-wall ratio is 0.50 for the north, 0.24 for the south, 0.13 for the west, and 0.58 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 7, 8 ,9, 10, 11, 12, 13, 14. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 15, 16, 17, 18, 19, 20. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""
detailed_prompt_4_7 = f"""
Simulate a 15 story building that is 77.80 meters long, 293.49 meters wide.\n
The height of story 1 is 6.19 meters.\n
The height of story 2 is 6.21 meters.\n
The height of story 3 is 3.96 meters.\n
The height of story 4 is 9.79 meters.\n
The height of story 5 is 7.68 meters.\n
The height of story 6 is 2.38 meters.\n
The height of story 7 is 5.96 meters.\n
The height of story 8 is 13.02 meters.\n
The height of story 9 is 6.46 meters.\n
The height of story 10 is 3.50 meters.\n
The height of story 11 is 9.69 meters.\n
The height of story 12 is 10.82 meters.\n
The height of story 13 is 12.29 meters.\n
The height of story 14 is 8.21 meters.\n
The height of story 15 is 10.31 meters.\n
The building orientation is 354 degrees to the north.\n
The window-to-wall ratio is 0.84 for the north, 0.59 for the south, 0.12 for the west, and 0.83 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 7, 8 ,9, 10, 11, 12, 13, 14. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 15. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 13, 14, 15, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""
detailed_prompt_4_8 = f"""
Simulate a 2 story building that is 424.34 meters long, 69.87 meters wide, with a hip roof\n
The height of story 1 is 11.06 meters.\n
The height of story 2 is 11.57 meters.\n
The attic height is 49.93 meters.\n
The building orientation is 6 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 13.08 meters.\n
The window-to-wall ratio is 0.16 for the north, 0.15 for the south, 0.31 for the west, and 0.19 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 7, 8. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 9, 10. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 9, 10, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_4_9 = f"""
Simulate a 7 story building that is 234.18 meters long, 151.94 meters wide, with a gable roof.\n
The height of story 1 is 3.40 meters.\n
The height of story 2 is 13.21 meters.\n
The height of story 3 is 12.94 meters.\n
The height of story 4 is 7.21 meters.\n
The height of story 5 is 8.68 meters.\n
The height of story 6 is 10.85 meters.\n
The height of story 7 is 2.28 meters.\n
The attic height is 0.93 meters.\n
The building orientation is 331 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 29.58 meters.\n
The window-to-wall ratio is 0.47 for the north, 0.52 for the south, 0.29 for the west, and 0.72 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 26, 27, 28, 29, 30, 31, 32, 33, 34, 35. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 29, 30, 31, 32, 33, 34, 35, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31, zone 32, zone 33, zone 34, zone 35.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""
detailed_prompt_4_10 = f"""
Simulate a 2 story building that is 356.85 meters long, 82.00 meters wide.\n
The height of story 1 is 6.24 meters.\n
The height of story 2 is 10.70 meters.\n
The attic height is 103.84 meters.\n
The building orientation is 314 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 37.46 meters.\n
The window-to-wall ratio is 0.51 for the north, 0.65 for the south, 0.48 for the west, and 0.65 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3, 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5, 6, 7, 8, 9, 10. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, 9, 10, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""
detailed_prompt_4_11 = f"""
Simulate a 2 story L-shaped building with a gable roof.\n
The height of story 1 is 12.05 meters.\n
The height of story 2 is 5.52 meters.\n\n
The horizontal segment is 159.34 meters long and 28.48 meters wide.\n
The vertical segment is 97.46 meters long and 32.05 meters wide.\
nThe attic height is 22.88 meters.\n
The building orientation is 230 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.81 for the north, 0.43 for the south, 0.75 for the west, and 0.68 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 4. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 4, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""
detailed_prompt_4_12 = f"""
Simulate a 17 story L-shaped building.
The height of story 1 is 7.62 meters.
The height of story 2 is 4.43 meters.
The height of story 3 is 5.54 meters.
The height of story 4 is 12.89 meters.
The height of story 5 is 13.20 meters.
The height of story 6 is 14.74 meters.
The height of story 7 is 5.13 meters.
The height of story 8 is 8.76 meters.
The height of story 9 is 2.98 meters.
The height of story 10 is 14.47 meters.
The height of story 11 is 14.35 meters.
The height of story 12 is 11.97 meters.
The height of story 13 is 14.75 meters.
The height of story 14 is 6.04 meters.
The height of story 15 is 4.68 meters.
The height of story 16 is 9.32 meters.
The height of story 17 is 6.48 meters.
The horizontal segment is 161.67 meters long and 66.8 meters wide.
The vertical segment is 144.06 meters long and 144.35 meters wide.
The building orientation is 320 degrees to the north.
Each story has 2 thermal zones with each segment as one thermal zone.
The window-to-wall ratio is 0.65 for the north, 0.20 for the south, 0.11 for the west, and 0.37 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 26, 27, 28, 29, 30, 31, 32, 33, 34. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 29, 30, 31, 32, 33, 34, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31, zone 32, zone 33, zone 34.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_4_13 = f"""
Simulate a 2 story hollow square, courtyard building with a gable roof.\n
The height of story 1 is 5.36 meters.\n
The height of story 2 is 11.69 meters.\n
The horizontal segments are 256.93 meters long and 88.05 meters wide.\n
The vertical segments are 54.52 meters long and 408.39 meters wide.\n
The attic height is 29.05 meters.\n
The building orientation is 285 degrees to the north.\n
Each story has 4 thermal zones in each orientation.\n
The window-to-wall ratio is 0.50 for the north, 0.11 for the south, 0.44 for the west, and 0.20 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3, 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5, 6, 7, 8. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""
detailed_prompt_4_14 = f"""
Simulate a 1 story hollow square, courtyard building.\n
The height of story 1 is 11.42 meters.\n
The horizontal segments are 144.24 meters long and 19.33 meters wide.\n
The vertical segments are 29.80 meters long and 390.88 meters wide.\n
The attic height is 26.60 meters.\n
The building orientation is 352 degrees to the north.\n
Each story has 4 thermal zones in each orientation.\n
The window-to-wall ratio is 0.80 for the north, 0.58 for the south, 0.17 for the west, and 0.78 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 3. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 4. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 4, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system, which serves zone 1, zone 2, zone 3, zone 4.
The rated capacity is 26976 W for cooling and 28118 W for heating.
The rated cooling COP is 4.23 and the heating COP is 4.95.
The supply air temperature for cooling is 13.8 Celsius, and for heating is 47.1 Celsius.
The outdoor ventilation rate is 2.56 ACH.
The fan efficiency of fan coil units, FCUs, is 0.78, the pressure rise is 1886 Pa, and the maximum flow rate is Autosize m3/s.
"""


detailed_prompt_5_1 = f"""
Simulate a 12 story U-shaped building with a gable roof.
The height of story 1 is 5.41 meters.
The height of story 2 is 3.29 meters.
The height of story 3 is 4.37 meters.
The height of story 4 is 8.33 meters.
The height of story 5 is 8.22 meters.\n
The height of story 6 is 3.11 meters.\n
The height of story 7 is 8.47 meters.\n
The height of story 8 is 14.81 meters.\n
The height of story 9 is 10.25 meters.\n
The height of story 10 is 10.44 meters.\n
The height of story 11 is 10.44 meters.\n
The height of story 12 is 14.97 meters.\n
The horizontal segment is 71.22 meters long and 8.05 meters wide.\n
The left vertical segment is 13.26 meters long and 464.3 meters wide.\n
The right vertical segment is 29.38 meters long and 32 meters wide.\n
The attic height is 13.60 meters.\n
The building orientation is 3 degrees to the north.\n
Each story has 3 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.79 for the north, 0.44 for the south, 0.74 for the west, and 0.41 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 32, zone 33, zone 34, zone 35, zone 36.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_5_2 = f"""
Simulate a 3 story U-shaped building.\n
The height of story 1 is 13.82 meters.\n
The height of story 2 is 8.50 meters.\n
The height of story 3 is 13.35 meters.\n
The horizontal segment is 362.02 meters long and 121.27 meters wide.\n
The left vertical segment is 88.68 meters long and 257.4 meters wide.\n
The right vertical segment is 37.72 meters long and 272 meters wide.\n
The attic height is 33.94 meters.\n
The building orientation is 250 degrees to the north.\n
Each story has 3 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.41 for the north, 0.51 for the south, 0.25 for the west, and 0.46 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 4, 5, 6, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 7, 8, 9, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 4, zone 5.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 8, zone 9.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""
detailed_prompt_5_3 = f"""
Simulate a 17 story T-shaped building with a gable roof.\n
The height of story 1 is 8.78 meters.\n
The height of story 2 is 4.90 meters.\n
The height of story 3 is 2.27 meters.\n
The height of story 4 is 4.72 meters.\n
The height of story 5 is 3.62 meters.\n
The height of story 6 is 3.26 meters.\n
The height of story 7 is 2.69 meters.\n
The height of story 8 is 6.13 meters.\n
The height of story 9 is 13.21 meters.\n
The height of story 10 is 9.44 meters.\n
The height of story 11 is 12.19 meters.\n
The height of story 12 is 13.00 meters.\n
The height of story 13 is 14.27 meters.\n
The height of story 14 is 4.89 meters.\n
The height of story 15 is 14.63 meters.\n
The height of story 16 is 11.63 meters.\n
The height of story 17 is 10.63 meters.\n
The horizontal segment is 228.91 meters long and 139.37 meters wide.\n
The vertical segment is 31.44 meters long and 441.59 meters wide.\n
The vertical segment is 31.32 meters to the edge of the horizontal segment.\n
The attic height is 5.88 meters.\n
The building orientation is 240 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.45 for the north, 0.45 for the south, 0.33 for the west, and 0.52 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 25, 26, 27, 28, 29, 30, 31, 32, 33, 34. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 32, zone 33, zone 34.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""
detailed_prompt_5_4 = f"""
Simulate a 18 story T-shaped building.\n
The height of story 1 is 7.65 meters.\n
The height of story 2 is 9.82 meters.\n
The height of story 3 is 12.57 meters.\n
The height of story 4 is 2.78 meters.\n
The height of story 5 is 1.69 meters.\n
The height of story 6 is 3.46 meters.\n
The height of story 7 is 12.39 meters.\n
The height of story 8 is 13.42 meters.\n
The height of story 9 is 10.02 meters.\n
The height of story 10 is 9.98 meters.\n
The height of story 11 is 10.32 meters.\n
The height of story 12 is 7.70 meters.\n
The height of story 13 is 7.64 meters.\n
The height of story 14 is 10.53 meters.\n
The height of story 15 is 8.35 meters.\n
The height of story 16 is 6.76 meters.\n
The height of story 17 is 8.90 meters.\n
The height of story 18 is 13.52 meters.\n
The horizontal segment is 443.9 meters long and 127.01 meters wide.\n
The vertical segment is 171.93 meters long and 439.98 meters wide.\n
The vertical segment is 79.07 meters to the edge of the horizontal segment.\n
The building orientation is 266 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.11 for the north, 0.16 for the south, 0.81 for the west, and 0.28 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 32, zone 33, zone 34, zone 35, zone 36.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_5_5 = f"""
Simulate a 13 story building that is 156.72 meters long, 380.33 meters wide, with a hip roof\n
The height of story 1 is 12.50 meters.\n
The height of story 2 is 2.82 meters.\n
The height of story 3 is 7.64 meters.\n
The height of story 4 is 11.08 meters.\n
The height of story 5 is 14.56 meters.\n
The height of story 6 is 9.66 meters.\n
The height of story 7 is 13.66 meters.\n
The height of story 8 is 9.24 meters.\n
The height of story 9 is 13.26 meters.\n
The height of story 10 is 14.24 meters.\n
The height of story 11 is 4.26 meters.\n
The height of story 12 is 12.82 meters.\n
The height of story 13 is 8.00 meters.\n
The attic height is 10.59 meters.\n
The building orientation is 351 degrees to the north.\n
The window-to-wall ratio is 0.27 for the north, 0.52 for the south, 0.30 for the west, and 0.57 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 7, 8, 9, 10, 11, 12, 13. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 4, 5, 6, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 7, 8, 9, 10, 11, 12, 13 the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 4, zone 5.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 8, zone 9, zone 10, zone 11, zone 12, zone 13.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_5_6 = f"""
Simulate a 19 story building that is 140.15 meters long, 241.14 meters wide, with a gable roof\n
The height of story 1 is 4.61 meters.\n
The height of story 2 is 13.48 meters.\n
The height of story 3 is 13.95 meters.\n
The height of story 4 is 7.19 meters.\n
The height of story 5 is 13.75 meters.\n
The height of story 6 is 13.83 meters.\n
The height of story 7 is 13.54 meters.\n
The height of story 8 is 5.67 meters.\n
The height of story 9 is 13.18 meters.\n
The height of story 10 is 7.55 meters.\n
The height of story 11 is 4.75 meters.\n
The height of story 12 is 12.40 meters.\n
The height of story 13 is 7.61 meters.\n
The height of story 14 is 14.79 meters.\n
The height of story 15 is 6.52 meters.\n
The height of story 16 is 7.68 meters.\n
The height of story 17 is 8.52 meters.\n
The height of story 18 is 8.07 meters.\n
The height of story 19 is 5.22 meters.\n
The attic height is 7.05 meters.\n
The building orientation is 328 degrees to the north.\n
The window-to-wall ratio is 0.79 for the north, 0.69 for the south, 0.60 for the west, and 0.75 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 4, 5, 6, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 4, zone 5.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_5_7 = f"""
Simulate a 18 story building that is 498.27 meters long, 422.27 meters wide.\n
The height of story 1 is 5.15 meters.\n
The height of story 2 is 13.79 meters.\n
The height of story 3 is 6.53 meters.\n
The height of story 4 is 14.72 meters.\n
The height of story 5 is 13.97 meters.\n
The height of story 6 is 7.94 meters.\n
The height of story 7 is 6.49 meters.\n
The height of story 8 is 2.40 meters.\n
The height of story 9 is 12.05 meters.\n
The height of story 10 is 9.18 meters.\n
The height of story 11 is 11.85 meters.\n
The height of story 12 is 11.50 meters.\n
The height of story 13 is 7.18 meters.\n
The height of story 14 is 7.45 meters.\n
The height of story 15 is 6.25 meters.\n
The height of story 16 is 11.13 meters.\n
The height of story 17 is 7.30 meters.\n
The height of story 18 is 2.00 meters.\n
The building orientation is 52 degrees to the north.\n
The window-to-wall ratio is 0.85 for the north, 0.43 for the south, 0.60 for the west, and 0.69 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 4, 5, 6, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 4, zone 5.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_5_8 = f"""
Simulate a 1 story building that is 476.87 meters long, 189.64 meters wide, with a hip roof\n
The height of story 1 is 2.57 meters.\n
The attic height is 137.29 meters.\n
The building orientation is 60 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 75.44 meters.\n
The window-to-wall ratio is 0.19 for the north, 0.89 for the south, 0.68 for the west, and 0.46 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 4, 5, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 3.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 4.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 5.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_5_9 = f"""
Simulate a 1 story building that is 103.83 meters long, 418.04 meters wide, with a gable roof.\n
The height of story 1 is 4.32 meters.\n
The attic height is 16.93 meters.\n
The building orientation is 202 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 15.21 meters.\n
The window-to-wall ratio is 0.49 for the north, 0.56 for the south, 0.54 for the west, and 0.34 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 5. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 3, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 4, 5, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 3.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 4.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 5.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""
detailed_prompt_5_10 = f"""
Simulate a 4 story building that is 483.73 meters long, 283.50 meters wide.\n
The height of story 1 is 1.66 meters.\n
The height of story 2 is 2.26 meters.\n
The height of story 3 is 6.71 meters.\n
The height of story 4 is 13.28 meters.\n
The attic height is 61.35 meters.\n
The building orientation is 214 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 33.80 meters.\n
The window-to-wall ratio is 0.85 for the north, 0.17 for the south, 0.13 for the west, and 0.72 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 4, 5, 6, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 4, zone 5.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_5_11 = f"""
Simulate a 8 story L-shaped building with a gable roof.\n
The height of story 1 is 8.89 meters.\n
The height of story 2 is 14.69 meters.\n
The height of story 3 is 6.55 meters.\n
The height of story 4 is 11.26 meters.\n
The height of story 5 is 10.67 meters.\n
The height of story 6 is 2.41 meters.\n
The height of story 7 is 7.56 meters.\n
The height of story 8 is 6.00 meters.\n\n
The horizontal segment is 107.92 meters long and 145.43 meters wide.\n
The vertical segment is 34.29 meters long and 171.74 meters wide.\n
The attic height is 7.24 meters.\n
The building orientation is 353 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.40 for the north, 0.34 for the south, 0.49 for the west, and 0.35 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 7, 8, 9, 10, 11, 12, 13, 14, 15, 16. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 4, 5, 6, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 4, zone 5.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_5_12 = f"""
Simulate a 5 story L-shaped building.\n
The height of story 1 is 6.68 meters.\n
The height of story 2 is 14.32 meters.\n
The height of story 3 is 2.86 meters.\n
The height of story 4 is 11.59 meters.\n
The height of story 5 is 4.83 meters.\n\n
The horizontal segment is 481.67 meters long and 131.52 meters wide.\n
The vertical segment is 354.58 meters long and 355.75 meters wide.\n
The building orientation is 61 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.17 for the north, 0.38 for the south, 0.11 for the west, and 0.58 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 7, 8, 9, 10. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 4, 5, 6, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 7, 8, 9, 10, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 4, zone 5.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""

detailed_prompt_5_13 = f"""
Simulate a 5 story hollow square, courtyard building with a gable roof.\n
The height of story 1 is 8.35 meters.\n
The height of story 2 is 7.77 meters.\n
The height of story 3 is 13.14 meters.\n
The height of story 4 is 12.01 meters.\n
The height of story 5 is 9.22 meters.\n
The horizontal segments are 264.69 meters long and 6.64 meters wide.\n
The vertical segments are 64.55 meters long and 52.06 meters wide.\n
The attic height is 67.68 meters.\n
The building orientation is 42 degrees to the north.\n
Each story has 4 thermal zones in each orientation.\n
The window-to-wall ratio is 0.19 for the north, 0.31 for the south, 0.87 for the west, and 0.41 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 4, 5, 6, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 4, zone 5.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""
detailed_prompt_5_14 = f"""
Simulate a 2 story hollow square, courtyard building.\n
The height of story 1 is 9.68 meters.\n
The height of story 2 is 5.85 meters.\n
The horizontal segments are 50.69 meters long and 59.94 meters wide.\n
The vertical segments are 12.12 meters long and 397.26 meters wide.\n
The attic height is 11.39 meters.\n
The building orientation is 222 degrees to the north.\n
Each story has 4 thermal zones in each orientation.\n
The window-to-wall ratio is 0.53 for the north, 0.59 for the south, 0.63 for the west, and 0.89 for the east.

The wall is made of concrete, with a thickness of 0.398 meters and the wall insulation is R37. The roof is made of concrete, with a thickness of 0.401 meters and the roof insulation is R25. The floor is made of concrete, covered with carpet. The window U-factor is 1.51 W/m2K and the SHGC is 0.25. 
This building have 3 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 5.53 m2/person, the lighting density is 8.87 W/m2, and the electric equipment density is 7.14 W/m2. The people activity level is 132 W/person. The infiltration rate is 0.08 ACH. The occupancy rate is 0.75 from 6:00 to 14:00 and 0.27 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 8.82 m2/person, the lighting density is 8.29 W/m2, and the electric equipment density is 3.49 W/m2. The people activity level is 114 W/person. The infiltration rate is 0.03 ACH. The occupancy rate is 0.97 from 7:00 to 13:00 and 0.19 in other periods of time. 
Space type 3 is for zone 7, 8. For space type 3, the people density is 4.83 m2/person, the lighting density is 7.36 W/m2, and the electric equipment density is 4.52 W/m2. The people activity level is 121 W/person. The infiltration rate is 0.05 ACH. The occupancy rate is 0.88 from 9:00 to 17:00 and 0.18 in other periods of time. 
For zone 1, 2, 3, the cooling setpoint is 26.2 Celsius during 8:00 to 18:00, and 28.3 Celsius in unoccupied periods. The heating setpoint is 20.3 Celsius during 8:00 to 18:00, and 22.1 Celsius in unoccupied periods. 
For zone 4, 5, 6, the cooling setpoint is 24.2 Celsius during 8:00 to 14:00, and 28.4 Celsius in unoccupied periods. The heating setpoint is 21.9 Celsius during 8:00 to 14:00, and 23.1 Celsius in unoccupied periods. 
For zone 7, 8, the cooling setpoint is 25.7 Celsius during 6:00 to 20:00, and 28.7 Celsius in unoccupied periods. The heating setpoint is 19.0 Celsius during 6:00 to 20:00, and 22.2 Celsius in unoccupied periods. 

The HVAC system in this building is variable refrigerant flow, VRF, system with dedicated outdoor air system, DOAS.
The rated capacity of the HVAC system is Autosize W for cooling and 40269 W for heating.
The rated cooling COP of the HVAC system is 3.61 and the heating COP is 7.08.
The DOAS 1 serves zone 1, zone 2, zone 3.
The supply air temperature for cooling is 18.4 Celsius, and for heating is 41.7 Celsius.
The outdoor ventilation rate is 1.77 ACH.
The fan efficiency is 0.8, the pressure rise is 1896 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 4, zone 5.
The supply air temperature for cooling is 10.2 Celsius, and for heating is 49.7 Celsius.
The outdoor ventilation rate is 1.64 ACH.
The fan efficiency is 0.67, the pressure rise is 1899 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 18.3 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.65 ACH.
The fan efficiency is 0.62, the pressure rise is 1196 Pa, and the maximum flow rate is 109.8 m3/s.
The DOAS 4 serves zone 8.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 12.7 Celsius, and for heating is 41.5 Celsius.
The outdoor ventilation rate is 1.01 ACH.
The fan efficiency is 0.79, the pressure rise is 404 Pa, and the maximum flow rate is Autosize m3/s.
"""


detailed_prompt_6_1 = f"""
Simulate a 3 story U-shaped building with a gable roof.\n
The height of story 1 is 2.94 meters.\n
The height of story 2 is 4.43 meters.\n
The height of story 3 is 2.42 meters.\n
The horizontal segment is 299.64 meters long and 40.61 meters wide.\n
The left vertical segment is 252.29 meters long and 185.91 meters wide.\n
The right vertical segment is 61.13 meters long and 97 meters wide.\n
The attic height is 40.90 meters.\n
The building orientation is 110 degrees to the north.\n
Each story has 3 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.27 for the north, 0.69 for the south, 0.49 for the west, and 0.81 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 6, 7. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 8, 9. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9,  the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 3, zone 4, zone 5.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7, zone 8, zone 9.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_2 = f"""
Simulate a 3 story U-shaped building.\n
The height of story 1 is 13.82 meters.\n
The height of story 2 is 8.50 meters.\n
The height of story 3 is 13.35 meters.\n
The horizontal segment is 362.02 meters long and 121.27 meters wide.\n
The left vertical segment is 88.68 meters long and 257.4 meters wide.\n
The right vertical segment is 37.72 meters long and 272 meters wide.\n
The attic height is 33.94 meters.\n
The building orientation is 250 degrees to the north.\n
Each story has 3 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.41 for the north, 0.51 for the south, 0.25 for the west, and 0.46 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 6, 7. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 8, 9. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9,  the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 3, zone 4, zone 5.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7, zone 8, zone 9.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_3 = f"""
Simulate a 17 story T-shaped building with a gable roof.\n
The height of story 1 is 5.40 meters.\n
The height of story 2 is 1.77 meters.\n
The height of story 3 is 14.20 meters.\n
The height of story 4 is 3.11 meters.\n
The height of story 5 is 4.70 meters.\n
The height of story 6 is 8.49 meters.\n
The height of story 7 is 9.46 meters.\n
The height of story 8 is 5.02 meters.\n
The height of story 9 is 14.49 meters.\n
The height of story 10 is 7.14 meters.\n
The height of story 11 is 9.09 meters.\n
The height of story 12 is 12.96 meters.\n
The height of story 13 is 3.57 meters.\n
The height of story 14 is 4.22 meters.\n
The height of story 15 is 14.53 meters.\n
The height of story 16 is 7.69 meters.\n
The height of story 17 is 11.95 meters.\n
The horizontal segment is 107.2 meters long and 8.32 meters wide.\n
The vertical segment is 51.48 meters long and 9.89 meters wide.\n
The vertical segment is 0.92 meters to the edge of the horizontal segment.\n
The attic height is 16.64 meters.\n
The building orientation is 144 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.57 for the north, 0.17 for the south, 0.36 for the west, and 0.52 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 25, 26, 27, 28, 29, 30, 31. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 32, 33, 34. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 27, 28, 29, 30, 31, 32, 33, 34, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31, zone 32, zone 33, zone 34.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_4 = f"""
Simulate a 15 story T-shaped building.\n
The height of story 1 is 1.77 meters.\n
The height of story 2 is 4.72 meters.\n
The height of story 3 is 5.84 meters.\n
The height of story 4 is 8.96 meters.\n
The height of story 5 is 7.58 meters.\n
The height of story 6 is 13.88 meters.\n
The height of story 7 is 14.16 meters.\n
The height of story 8 is 11.28 meters.\n
The height of story 9 is 5.65 meters.\n
The height of story 10 is 13.89 meters.\n
The height of story 11 is 1.61 meters.\n
The height of story 12 is 3.34 meters.\n
The height of story 13 is 2.41 meters.\n
The height of story 14 is 2.00 meters.\n
The height of story 15 is 13.40 meters.\n
The horizontal segment is 96.77 meters long and 308.75 meters wide.\n
The vertical segment is 33.28 meters long and 481.41 meters wide.\n
The vertical segment is 26.78 meters to the edge of the horizontal segment.\n
The building orientation is 103 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.46 for the north, 0.23 for the south, 0.33 for the west, and 0.51 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 25, 26, 27. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 28, 29, 30. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 27, 28, 29, 30, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_5 = f"""
Simulate a 13 story building that is 156.72 meters long, 380.33 meters wide, with a hip roof\n
The height of story 1 is 12.50 meters.\n
The height of story 2 is 2.82 meters.\n
The height of story 3 is 7.64 meters.\n
The height of story 4 is 11.08 meters.\n
The height of story 5 is 14.56 meters.\n
The height of story 6 is 9.66 meters.\n
The height of story 7 is 13.66 meters.\n
The height of story 8 is 9.24 meters.\n
The height of story 9 is 13.26 meters.\n
The height of story 10 is 14.24 meters.\n
The height of story 11 is 4.26 meters.\n
The height of story 12 is 12.82 meters.\n
The height of story 13 is 8.00 meters.\n
The attic height is 10.59 meters.\n
The building orientation is 351 degrees to the north.\n
The window-to-wall ratio is 0.27 for the north, 0.52 for the south, 0.30 for the west, and 0.57 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 6, 7. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 8, 9, 10, 11, 12, 13. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 3, zone 4, zone 5.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_6 = f"""
Simulate a 20 story building that is 193.58 meters long, 125.08 meters wide, with a gable roof\nThe height of story 1 is 11.80 meters.\n
The height of story 2 is 6.26 meters.\n
The height of story 3 is 8.42 meters.\n
The height of story 4 is 2.67 meters.\n
The height of story 5 is 8.15 meters.\n
The height of story 6 is 10.52 meters.\n
The height of story 7 is 3.98 meters.\n
The height of story 8 is 13.33 meters.\n
The height of story 9 is 14.25 meters.\n
The height of story 10 is 9.24 meters.\n
The height of story 11 is 7.64 meters.\n
The height of story 12 is 11.95 meters.\n
The height of story 13 is 6.17 meters.\n
The height of story 14 is 6.28 meters.\n
The height of story 15 is 2.06 meters.\n
The height of story 16 is 1.79 meters.\n
The height of story 17 is 2.51 meters.\n
The height of story 18 is 4.88 meters.\n
The height of story 19 is 10.73 meters.\n
The height of story 20 is 10.34 meters.\n
The attic height is 31.50 meters.\n
The building orientation is 232 degrees to the north.\n
The window-to-wall ratio is 0.78 for the north, 0.24 for the south, 0.82 for the west, and 0.69 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 6, 7. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 3, zone 4, zone 5.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_7 = f"""
Simulate a 18 story building that is 498.27 meters long, 422.27 meters wide.\n
The height of story 1 is 5.15 meters.\n
The height of story 2 is 13.79 meters.\n
The height of story 3 is 6.53 meters.\n
The height of story 4 is 14.72 meters.\n
The height of story 5 is 13.97 meters.\n
The height of story 6 is 7.94 meters.\n
The height of story 7 is 6.49 meters.\n
The height of story 8 is 2.40 meters.\n
The height of story 9 is 12.05 meters.\n
The height of story 10 is 9.18 meters.\n
The height of story 11 is 11.85 meters.\n
The height of story 12 is 11.50 meters.\n
The height of story 13 is 7.18 meters.\n
The height of story 14 is 7.45 meters.\n
The height of story 15 is 6.25 meters.\n
The height of story 16 is 11.13 meters.\n
The height of story 17 is 7.30 meters.\n
The height of story 18 is 2.00 meters.\n
The building orientation is 52 degrees to the north.\n
The window-to-wall ratio is 0.85 for the north, 0.43 for the south, 0.60 for the west, and 0.69 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 6, 7. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 3, zone 4, zone 5.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_8 = f"""
Simulate a 6 story building that is 136.60 meters long, 153.72 meters wide, with a hip roof\n
The height of story 1 is 5.11 meters.\n
The height of story 2 is 6.39 meters.\n
The height of story 3 is 3.09 meters.\n
The height of story 4 is 14.90 meters.\n
The height of story 5 is 3.34 meters.\n
The height of story 6 is 7.18 meters.\n
The attic height is 40.59 meters.\n
The building orientation is 50 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 53.86 meters.\n
The window-to-wall ratio is 0.58 for the north, 0.87 for the south, 0.24 for the west, and 0.56 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 25, 26, 27. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 28, 29, 30. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 27, 28, 29, 30, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_9 = f"""
Simulate a 3 story building that is 490.31 meters long, 167.97 meters wide, with a gable roof.\n
The height of story 1 is 8.95 meters.\n
The height of story 2 is 8.05 meters.\n
The height of story 3 is 4.25 meters.\n
The attic height is 133.44 meters.\n
The building orientation is 50 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 65.93 meters.\nThe window-to-wall ratio is 0.18 for the north, 0.76 for the south, 0.45 for the west, and 0.36 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 6, 7. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 8, 9, 10, 11, 12, 13, 14, 15. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 3, zone 4, zone 5.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_10 = f"""
Simulate a 5 story building that is 39.00 meters long, 438.97 meters wide.\n
The height of story 1 is 6.30 meters.\n
The height of story 2 is 13.16 meters.\n
The height of story 3 is 2.97 meters.\n
The height of story 4 is 10.54 meters.\n
The height of story 5 is 5.56 meters.\n
The attic height is 9.97 meters.\n
The building orientation is 246 degrees to the north.\n
Each story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\n
The depth of exterior thermal zone is 14.36 meters.\n
The window-to-wall ratio is 0.82 for the north, 0.67 for the south, 0.79 for the west, and 0.82 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 13, 14, 15, 16. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 17, 18, 19, 20, 21. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 22, 23, 24, 25. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 20, 21, 22, 23, 24, 25, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 21, zone 22, zone 23, zone 24, zone 25.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_11 = f"""
Simulate a 6 story L-shaped building with a gable roof.\n
The height of story 1 is 7.64 meters.\n
The height of story 2 is 12.52 meters.\n
The height of story 3 is 10.38 meters.\n
The height of story 4 is 7.19 meters.\n
The height of story 5 is 7.84 meters.\n
The height of story 6 is 10.28 meters.\n\n
The horizontal segment is 292.61 meters long and 143.9 meters wide.\n
The vertical segment is 109.49 meters long and 273.26 meters wide.\n
The attic height is 25.65 meters.\nThe building orientation is 41 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.89 for the north, 0.82 for the south, 0.57 for the west, and 0.86 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 6, 7. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 8, 9, 10, 11, 12. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 3, zone 4, zone 5.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_12 = f"""
Simulate a 12 story L-shaped building.\n
The height of story 1 is 10.97 meters.\n
The height of story 2 is 8.60 meters.\n
The height of story 3 is 9.93 meters.\n
The height of story 4 is 13.99 meters.\n
The height of story 5 is 6.66 meters.\n
The height of story 6 is 11.35 meters.\n
The height of story 7 is 2.08 meters.\n
The height of story 8 is 12.76 meters.\n
The height of story 9 is 13.65 meters.\n
The height of story 10 is 2.96 meters.\n
The height of story 11 is 12.06 meters.\n
The height of story 12 is 5.53 meters.\n\n
The horizontal segment is 201.74 meters long and 10.38 meters wide.\n
The vertical segment is 56.61 meters long and 14.91 meters wide.\n
The building orientation is 199 degrees to the north.\n
Each story has 2 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.85 for the north, 0.17 for the south, 0.59 for the west, and 0.25 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 13, 14, 15, 16. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 17, 18, 19, 20, 21. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 22, 23, 24. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 20, 21, 22, 23, 24, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 21, zone 22, zone 23, zone 24.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_13 = f"""
Simulate a 2 story hollow square, courtyard building with a gable roof.\n
The height of story 1 is 12.99 meters.\n
The height of story 2 is 13.74 meters.\n
The horizontal segments are 156.01 meters long and 85.71 meters wide.\n
The vertical segments are 18.27 meters long and 421.15 meters wide.\n
The attic height is 4.87 meters.\n
The building orientation is 238 degrees to the north.\n
Each story has 4 thermal zones in each orientation.\n
The window-to-wall ratio is 0.39 for the north, 0.45 for the south, 0.82 for the west, and 0.48 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 6, 7. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 8. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8,  the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 3, zone 4, zone 5.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 6, zone 7, zone 8.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_6_14 = f"""
Simulate a 8 story hollow square, courtyard building.\n
The height of story 1 is 8.32 meters.\n
The height of story 2 is 12.96 meters.\n
The height of story 3 is 7.27 meters.\n
The height of story 4 is 1.87 meters.\n
The height of story 5 is 5.96 meters.\n
The height of story 6 is 9.23 meters.\n
The height of story 7 is 5.63 meters.\n
The height of story 8 is 7.07 meters.\n
The horizontal segments are 140.42 meters long and 8.15 meters wide.\n
The vertical segments are 10.43 meters long and 167.47 meters wide.\n
The attic height is 22.04 meters.\n
The building orientation is 223 degrees to the north.\n
Each story has 4 thermal zones in each orientation.\n
The window-to-wall ratio is 0.18 for the north, 0.40 for the south, 0.55 for the west, and 0.67 for the east.
The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 25, 26, 27. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 28, 29, 30, 31, 32. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 27, 28, 29, 30, 31, 32, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system with dedicated outdoor air system, DOAS.
The DOAS 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan .
The supply air temperature for cooling is 16.0 Celsius, and for heating is 40.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.
The DOAS 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31, zone 32.
It includes an economizer, which operates based on differential dry bulb.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 16.0 Celsius, and for heating is 42.0 Celsius.
The outdoor ventilation rate is 1.0 ACH.
The fan efficiency is 0.7, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""


detailed_prompt_7_1 = f"""
Simulate a 11 story U-shaped building with a gable roof.\n
The height of story 1 is 14.65 meters.\n
The height of story 2 is 9.09 meters.\n
The height of story 3 is 9.61 meters.\n
The height of story 4 is 4.68 meters.\n
The height of story 5 is 13.19 meters.\n
The height of story 6 is 3.70 meters.\n
The height of story 7 is 9.35 meters.\n
The height of story 8 is 7.27 meters.\n
The height of story 9 is 12.39 meters.\n
The height of story 10 is 7.20 meters.\n
The height of story 11 is 10.33 meters.\n
The horizontal segment is 459.76 meters long and 70.08 meters wide.\n
The left vertical segment is 358.98 meters long and 167.87 meters wide.\n
The right vertical segment is 101.93 meters long and 292 meters wide.\n
The attic height is 84.96 meters.\nThe building orientation is 213 degrees to the north.\n
Each story has 3 thermal zones with each segment as one thermal zone.\n
The window-to-wall ratio is 0.66 for the north, 0.37 for the south, 0.73 for the west, and 0.60 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 12, 13, 14, 15, 16, 17, 18, 19, 20, 21. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 22, 23, 24, 25, 26, 27. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 28, 29, 30, 31, 32, 33. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31, zone 32, zone 33.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""


detailed_prompt_7_2 = f"""
Simulate a 11 story U-shaped building.\nThe height of story 1 is 7.20 meters.\nThe height of story 2 is 3.67 meters.\nThe height of story 3 is 2.60 meters.\nThe height of story 4 is 13.72 meters.\nThe height of story 5 is 3.09 meters.\nThe height of story 6 is 13.19 meters.\nThe height of story 7 is 5.59 meters.\nThe height of story 8 is 9.07 meters.\nThe height of story 9 is 2.55 meters.\nThe height of story 10 is 12.33 meters.\nThe height of story 11 is 3.97 meters.\nThe horizontal segment is 366.67 meters long and 22.6 meters wide.\nThe left vertical segment is 208.69 meters long and 103.68 meters wide.\nThe right vertical segment is 2.35 meters long and 100 meters wide.\nThe attic height is 66.26 meters.\nThe building orientation is 88 degrees to the north.\nEach story has 3 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.47 for the north, 0.23 for the south, 0.11 for the west, and 0.29 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 12, 13, 14, 15, 16, 17, 18, 19, 20, 21. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 22, 23, 24, 25, 26, 27. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 28, 29, 30, 31, 32, 33. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31, zone 32, zone 33.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_7_3 = f"""
Simulate a 21 story T-shaped building with a gable roof.\nThe height of story 1 is 11.75 meters.\nThe height of story 2 is 9.07 meters.\nThe height of story 3 is 7.78 meters.\nThe height of story 4 is 3.39 meters.\nThe height of story 5 is 2.40 meters.\nThe height of story 6 is 1.52 meters.\nThe height of story 7 is 9.54 meters.\nThe height of story 8 is 1.84 meters.\nThe height of story 9 is 12.48 meters.\nThe height of story 10 is 12.25 meters.\nThe height of story 11 is 12.92 meters.\nThe height of story 12 is 14.13 meters.\nThe height of story 13 is 7.03 meters.\nThe height of story 14 is 8.66 meters.\nThe height of story 15 is 11.04 meters.\nThe height of story 16 is 13.08 meters.\nThe height of story 17 is 14.42 meters.\nThe height of story 18 is 9.34 meters.\nThe height of story 19 is 8.87 meters.\nThe height of story 20 is 9.01 meters.\nThe height of story 21 is 9.34 meters.\nThe horizontal segment is 370.8 meters long and 91.01 meters wide.\nThe vertical segment is 324.24 meters long and 168.55 meters wide.\nThe vertical segment is 128.52 meters to the edge of the horizontal segment.\nThe attic height is 68.64 meters.\nThe building orientation is 350 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.30 for the north, 0.60 for the south, 0.26 for the west, and 0.85 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 12, 13, 14, 15, 16, 17, 18, 19, 20, 21. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 22, 23, 24, 25, 26, 27. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31, zone 32, zone 33, zone 34, zone 35, zone 36, zone 37, zone 38, zone 39, zone 40, zone 41, zone 42.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_7_4 = f"""
Simulate a 8 story T-shaped building.\nThe height of story 1 is 5.60 meters.\nThe height of story 2 is 12.91 meters.\nThe height of story 3 is 13.94 meters.\nThe height of story 4 is 7.28 meters.\nThe height of story 5 is 9.87 meters.\nThe height of story 6 is 8.21 meters.\nThe height of story 7 is 10.31 meters.\nThe height of story 8 is 7.37 meters.\nThe horizontal segment is 98.79 meters long and 67.61 meters wide.\nThe vertical segment is 27.79 meters long and 76.69 meters wide.\nThe vertical segment is 1.71 meters to the edge of the horizontal segment.\nThe building orientation is 254 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.64 for the north, 0.24 for the south, 0.90 for the west, and 0.23 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9, 10, 11, 12. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 13, 14, 15, 16. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 15, 16, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""


detailed_prompt_7_5 = f"""
Simulate a 20 story building that is 182.13 meters long, 403.33 meters wide, with a hip roof\nThe height of story 1 is 7.21 meters.\nThe height of story 2 is 10.74 meters.\nThe height of story 3 is 14.22 meters.\nThe height of story 4 is 8.38 meters.\nThe height of story 5 is 6.84 meters.\nThe height of story 6 is 6.42 meters.\nThe height of story 7 is 14.25 meters.\nThe height of story 8 is 12.27 meters.\nThe height of story 9 is 4.98 meters.\nThe height of story 10 is 10.44 meters.\nThe height of story 11 is 1.57 meters.\nThe height of story 12 is 7.57 meters.\nThe height of story 13 is 13.56 meters.\nThe height of story 14 is 13.62 meters.\nThe height of story 15 is 14.25 meters.\nThe height of story 16 is 6.74 meters.\nThe height of story 17 is 12.88 meters.\nThe height of story 18 is 8.59 meters.\nThe height of story 19 is 5.29 meters.\nThe height of story 20 is 2.16 meters.\nThe attic height is 46.46 meters.\nThe building orientation is 248 degrees to the north.\nThe window-to-wall ratio is 0.62 for the north, 0.67 for the south, 0.82 for the west, and 0.14 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9, 10, 11, 12. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 13, 14, 15, 16, 17, 18, 19, 20. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 9, 10, 11, 12, 13, 14, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 15, 16, 17, 18, 19, 20, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""


detailed_prompt_7_6 = f"""
Simulate a 5 story building that is 111.32 meters long, 394.31 meters wide, with a gable roof\nThe height of story 1 is 10.76 meters.\nThe height of story 2 is 4.71 meters.\nThe height of story 3 is 11.57 meters.\nThe height of story 4 is 6.97 meters.\nThe height of story 5 is 5.80 meters.\nThe attic height is 20.08 meters.\nThe building orientation is 97 degrees to the north.\nThe window-to-wall ratio is 0.28 for the north, 0.13 for the south, 0.53 for the west, and 0.77 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 1. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 4. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 5. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 5, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""



detailed_prompt_7_7 = f"""
Simulate a 12 story building that is 217.03 meters long, 191.34 meters wide.\nThe height of story 1 is 6.55 meters.\nThe height of story 2 is 14.48 meters.\nThe height of story 3 is 10.53 meters.\nThe height of story 4 is 7.75 meters.\nThe height of story 5 is 5.58 meters.\nThe height of story 6 is 9.44 meters.\nThe height of story 7 is 6.69 meters.\nThe height of story 8 is 13.20 meters.\nThe height of story 9 is 2.04 meters.\nThe height of story 10 is 9.88 meters.\nThe height of story 11 is 4.81 meters.\nThe height of story 12 is 12.02 meters.\nThe building orientation is 312 degrees to the north.\nThe window-to-wall ratio is 0.76 for the north, 0.21 for the south, 0.87 for the west, and 0.55 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10, 11, 12. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4,  the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 5, 6, 7, 8, 9, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 10, 11, 12, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""



detailed_prompt_7_8 = f"""
Simulate a 1 story building that is 476.87 meters long, 189.64 meters wide, with a hip roof\nThe height of story 1 is 2.57 meters.\nThe attic height is 137.29 meters.\nThe building orientation is 60 degrees to the north.\nEach story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\nThe depth of exterior thermal zone is 75.44 meters.\nThe window-to-wall ratio is 0.19 for the north, 0.89 for the south, 0.68 for the west, and 0.46 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 1. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 4. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 5. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 5, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_7_9 = f"""
Simulate a 2 story building that is 84.61 meters long, 409.29 meters wide, with a gable roof.\nThe height of story 1 is 14.60 meters.\nThe height of story 2 is 1.65 meters.\nThe attic height is 15.64 meters.\nThe building orientation is 34 degrees to the north.\nEach story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\nThe depth of exterior thermal zone is 19.75 meters.\nThe window-to-wall ratio is 0.14 for the north, 0.31 for the south, 0.83 for the west, and 0.14 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 1. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 4, 5. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 6, 7, 8, 9, 10. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_7_10 = f"""
Simulate a 2 story building that is 199.07 meters long, 200.66 meters wide.\nThe height of story 1 is 12.88 meters.\nThe height of story 2 is 4.73 meters.\nThe attic height is 31.36 meters.\nThe building orientation is 349 degrees to the north.\nEach story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\nThe depth of exterior thermal zone is 93.59 meters.\nThe window-to-wall ratio is 0.15 for the north, 0.87 for the south, 0.82 for the west, and 0.42 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 1. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 4, 5. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 6, 7, 8, 9, 10. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_7_11 = f"""
Simulate a 3 story L-shaped building with a gable roof.\nThe height of story 1 is 8.48 meters.\nThe height of story 2 is 7.13 meters.\nThe height of story 3 is 13.59 meters.\n\nThe horizontal segment is 352.95 meters long and 110.13 meters wide.\nThe vertical segment is 102.98 meters long and 167.18 meters wide.\nThe attic height is 57.04 meters.\nThe building orientation is 6 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.64 for the north, 0.90 for the south, 0.67 for the west, and 0.70 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 1. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 4, 5. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 6. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6 the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_7_12 = f"""
Simulate a 2 story L-shaped building.\nThe height of story 1 is 4.35 meters.\nThe height of story 2 is 11.46 meters.\n\nThe horizontal segment is 12.33 meters long and 29.1 meters wide.\nThe vertical segment is 5.89 meters long and 32.61 meters wide.\nThe building orientation is 61 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.52 for the north, 0.49 for the south, 0.62 for the west, and 0.65 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 2. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 3. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 4. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 4, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_7_13 = f"""
Simulate a 2 story hollow square, courtyard building with a gable roof.\nThe height of story 1 is 12.99 meters.\nThe height of story 2 is 13.74 meters.\nThe horizontal segments are 156.01 meters long and 85.71 meters wide.\nThe vertical segments are 18.27 meters long and 421.15 meters wide.\nThe attic height is 4.87 meters.\nThe building orientation is 238 degrees to the north.\nEach story has 4 thermal zones in each orientation.\nThe window-to-wall ratio is 0.39 for the north, 0.45 for the south, 0.82 for the west, and 0.48 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 2. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 3. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 4, 5, 6, 7, 8. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 4, 5, 6, 7, 8, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""


detailed_prompt_7_14 = f"""
Simulate a 8 story hollow square, courtyard building.\nThe height of story 1 is 8.32 meters.\nThe height of story 2 is 12.96 meters.\nThe height of story 3 is 7.27 meters.\nThe height of story 4 is 1.87 meters.\nThe height of story 5 is 5.96 meters.\nThe height of story 6 is 9.23 meters.\nThe height of story 7 is 5.63 meters.\nThe height of story 8 is 7.07 meters.\nThe horizontal segments are 140.42 meters long and 8.15 meters wide.\nThe vertical segments are 10.43 meters long and 167.47 meters wide.\nThe attic height is 22.04 meters.\nThe building orientation is 223 degrees to the north.\nEach story has 4 thermal zones in each orientation.\nThe window-to-wall ratio is 0.18 for the north, 0.40 for the south, 0.55 for the west, and 0.67 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 12, 13, 14, 15, 16, 17, 18, 19, 20, 21. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 22, 23, 24, 25, 26, 27. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 28, 29, 30, 31, 32. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is fan coil unit, FCU, system, which serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31, zone 32.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 14.8 Celsius, and for heating is 42.9 Celsius.
The outdoor ventilation rate is 1.6 ACH.
The fan efficiency of fan coil units, FCUs, is 0.82, the pressure rise is 500 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""


detailed_prompt_8_1 = f"""
Simulate a 10 story U-shaped building with a gable roof.\nThe height of story 1 is 6.55 meters.\nThe height of story 2 is 7.72 meters.\nThe height of story 3 is 12.35 meters.\nThe height of story 4 is 14.54 meters.\nThe height of story 5 is 5.98 meters.\nThe height of story 6 is 3.38 meters.\nThe height of story 7 is 12.08 meters.\nThe height of story 8 is 14.61 meters.\nThe height of story 9 is 13.85 meters.\nThe height of story 10 is 2.18 meters.\nThe horizontal segment is 377.85 meters long and 89.82 meters wide.\nThe left vertical segment is 220.19 meters long and 205.35 meters wide.\nThe right vertical segment is 158.0 meters long and 226 meters wide.\nThe attic height is 63.88 meters.\nThe building orientation is 201 degrees to the north.\nEach story has 3 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.22 for the north, 0.64 for the south, 0.75 for the west, and 0.20 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 21, 22, 23, 24, 25. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 26, 27, 28, 29, 30. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.,zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26.,zone 27, zone 28, zone 29, zone 30.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_2 = f"""
Simulate a 5 story U-shaped building.\nThe height of story 1 is 8.33 meters.\nThe height of story 2 is 4.94 meters.\nThe height of story 3 is 14.68 meters.\nThe height of story 4 is 8.25 meters.\nThe height of story 5 is 13.21 meters.\nThe horizontal segment is 330.04 meters long and 40.15 meters wide.\nThe left vertical segment is 58.45 meters long and 398.49 meters wide.\nThe right vertical segment is 6.85 meters long and 195 meters wide.\nThe attic height is 19.42 meters.\nThe building orientation is 22 degrees to the north.\nEach story has 3 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.37 for the north, 0.54 for the south, 0.90 for the west, and 0.58 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 6, 7, 8, 9, 10. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 11, 12, 13. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 14, 15. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, 13, 14, 15, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 11, zone 12, zone 13, zone 14, zone 15.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_3 = f"""
Simulate a 12 story T-shaped building with a gable roof.\nThe height of story 1 is 11.19 meters.\nThe height of story 2 is 12.22 meters.\nThe height of story 3 is 9.54 meters.\nThe height of story 4 is 12.71 meters.\nThe height of story 5 is 1.89 meters.\nThe height of story 6 is 12.74 meters.\nThe height of story 7 is 8.54 meters.\nThe height of story 8 is 8.37 meters.\nThe height of story 9 is 13.79 meters.\nThe height of story 10 is 8.91 meters.\nThe height of story 11 is 7.85 meters.\nThe height of story 12 is 7.81 meters.\nThe horizontal segment is 169.15 meters long and 10.71 meters wide.\nThe vertical segment is 92.24 meters long and 18.91 meters wide.\nThe vertical segment is 103.35 meters to the edge of the horizontal segment.\nThe attic height is 27.57 meters.\nThe building orientation is 11 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.39 for the north, 0.80 for the south, 0.41 for the west, and 0.86 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 11, 12, 13, 14, 15, 16. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 17, 18, 19, 20. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 21, 22, 23, 24. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 21, 22, 23, 24, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.,zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 21, zone 22, zone 23, zone 24.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_4 = f"""
Simulate a 20 story T-shaped building.\nThe height of story 1 is 8.60 meters.\nThe height of story 2 is 9.33 meters.\nThe height of story 3 is 7.32 meters.\nThe height of story 4 is 2.61 meters.\nThe height of story 5 is 2.36 meters.\nThe height of story 6 is 1.73 meters.\nThe height of story 7 is 8.84 meters.\nThe height of story 8 is 4.72 meters.\nThe height of story 9 is 5.94 meters.\nThe height of story 10 is 1.73 meters.\nThe height of story 11 is 11.69 meters.\nThe height of story 12 is 5.56 meters.\nThe height of story 13 is 14.35 meters.\nThe height of story 14 is 2.13 meters.\nThe height of story 15 is 6.71 meters.\nThe height of story 16 is 11.48 meters.\nThe height of story 17 is 14.50 meters.\nThe height of story 18 is 3.36 meters.\nThe height of story 19 is 10.24 meters.\nThe height of story 20 is 14.31 meters.\nThe horizontal segment is 164.83 meters long and 12.34 meters wide.\nThe vertical segment is 140.44 meters long and 41.21 meters wide.\nThe vertical segment is 40.01 meters to the edge of the horizontal segment.\nThe building orientation is 318 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.63 for the north, 0.70 for the south, 0.51 for the west, and 0.18 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 21, 22, 23, 24, 25. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.,zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26.,zone 27, zone 28, zone 29, zone 30, zone 31, zone 32, zone 33, zone 34, zone 35, zone 36.,zone 37, zone 38, zone 39, zone 40.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_5 = f"""
Simulate a 5 story building that is 178.26 meters long, 286.63 meters wide, with a hip roof\nThe height of story 1 is 11.77 meters.\nThe height of story 2 is 9.21 meters.\nThe height of story 3 is 9.32 meters.\nThe height of story 4 is 14.43 meters.\nThe height of story 5 is 5.98 meters.\nThe attic height is 19.70 meters.\nThe building orientation is 235 degrees to the north.\nThe window-to-wall ratio is 0.79 for the north, 0.25 for the south, 0.50 for the west, and 0.55 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 2. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 3. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 4, 5. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 5 the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 3, zone 4.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 5.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_6 = f"""
Simulate a 19 story building that is 207.09 meters long, 391.96 meters wide, with a gable roof\nThe height of story 1 is 3.32 meters.\nThe height of story 2 is 2.92 meters.\nThe height of story 3 is 2.27 meters.\nThe height of story 4 is 9.40 meters.\nThe height of story 5 is 1.88 meters.\nThe height of story 6 is 2.80 meters.\nThe height of story 7 is 2.18 meters.\nThe height of story 8 is 10.24 meters.\nThe height of story 9 is 6.86 meters.\nThe height of story 10 is 10.27 meters.\nThe height of story 11 is 12.41 meters.\nThe height of story 12 is 3.50 meters.\nThe height of story 13 is 10.97 meters.\nThe height of story 14 is 3.92 meters.\nThe height of story 15 is 7.01 meters.\nThe height of story 16 is 6.06 meters.\nThe height of story 17 is 11.29 meters.\nThe height of story 18 is 14.28 meters.\nThe height of story 19 is 2.45 meters.\nThe attic height is 61.15 meters.\nThe building orientation is 345 degrees to the north.\nThe window-to-wall ratio is 0.31 for the north, 0.13 for the south, 0.80 for the west, and 0.66 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 7, 8, 9, 10. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 11, 12, 13, 14, 15. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 16, 17, 18, 19. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, 13, 14, 15, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 16, 17, 18, 19, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 11, zone 12, zone 13, zone 14.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 15, zone 16, zone 17, zone 18, zone 19.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_7 = f"""
Simulate a 12 story building that is 280.56 meters long, 190.32 meters wide.\nThe height of story 1 is 10.59 meters.\nThe height of story 2 is 2.01 meters.\nThe height of story 3 is 10.42 meters.\nThe height of story 4 is 8.61 meters.\nThe height of story 5 is 4.56 meters.\nThe height of story 6 is 13.41 meters.\nThe height of story 7 is 13.85 meters.\nThe height of story 8 is 14.55 meters.\nThe height of story 9 is 9.87 meters.\nThe height of story 10 is 2.23 meters.\nThe height of story 11 is 11.37 meters.\nThe height of story 12 is 4.11 meters.\nThe building orientation is 192 degrees to the north.\nThe window-to-wall ratio is 0.51 for the north, 0.86 for the south, 0.66 for the west, and 0.57 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 6, 7. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 11, 12. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 8, 9, 10. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 11, zone 12.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_8 = f"""
Simulate a 6 story building that is 136.60 meters long, 153.72 meters wide, with a hip roof\nThe height of story 1 is 5.11 meters.\nThe height of story 2 is 6.39 meters.\nThe height of story 3 is 3.09 meters.\nThe height of story 4 is 14.90 meters.\nThe height of story 5 is 3.34 meters.\nThe height of story 6 is 7.18 meters.\nThe attic height is 40.59 meters.\nThe building orientation is 50 degrees to the north.\nEach story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\nThe depth of exterior thermal zone is 53.86 meters.\nThe window-to-wall ratio is 0.58 for the north, 0.87 for the south, 0.24 for the west, and 0.56 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 21, 22, 23, 24, 25. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 26, 27, 28, 29, 30. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.,zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26.,zone 27, zone 28, zone 29, zone 30.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_9 = f"""
Simulate a 7 story building that is 234.18 meters long, 151.94 meters wide, with a gable roof.\nThe height of story 1 is 3.40 meters.\nThe height of story 2 is 13.21 meters.\nThe height of story 3 is 12.94 meters.\nThe height of story 4 is 7.21 meters.\nThe height of story 5 is 8.68 meters.\nThe height of story 6 is 10.85 meters.\nThe height of story 7 is 2.28 meters.\nThe attic height is 0.93 meters.\nThe building orientation is 331 degrees to the north.\nEach story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\nThe depth of exterior thermal zone is 29.58 meters.\nThe window-to-wall ratio is 0.47 for the north, 0.52 for the south, 0.29 for the west, and 0.72 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 21, 22, 23, 24, 25. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 26, 27, 28, 29, 30, 31, 32, 33, 34, 35. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.,zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26.,zone 27, zone 28, zone 29, zone 30, zone 31, zone 32, zone 33, zone 34, zone 35.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_10 = f"""
Simulate a 2 story building that is 356.85 meters long, 82.00 meters wide.\nThe height of story 1 is 6.24 meters.\nThe height of story 2 is 10.70 meters.\nThe attic height is 103.84 meters.\nThe building orientation is 314 degrees to the north.\nEach story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\nThe depth of exterior thermal zone is 37.46 meters.\nThe window-to-wall ratio is 0.51 for the north, 0.65 for the south, 0.48 for the west, and 0.65 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 6, 7. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 9, 10, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 5, zone 6, zone 7.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_11 = f"""
Simulate a 15 story L-shaped building with a gable roof.\nThe height of story 1 is 2.76 meters.\nThe height of story 2 is 11.47 meters.\nThe height of story 3 is 7.04 meters.\nThe height of story 4 is 5.13 meters.\nThe height of story 5 is 1.78 meters.\nThe height of story 6 is 6.14 meters.\nThe height of story 7 is 10.58 meters.\nThe height of story 8 is 8.89 meters.\nThe height of story 9 is 1.88 meters.\nThe height of story 10 is 1.60 meters.\nThe height of story 11 is 13.03 meters.\nThe height of story 12 is 4.56 meters.\nThe height of story 13 is 2.95 meters.\nThe height of story 14 is 2.63 meters.\nThe height of story 15 is 5.80 meters.\n\nThe horizontal segment is 33.24 meters long and 72.1 meters wide.\nThe vertical segment is 8.65 meters long and 95.71 meters wide.\nThe attic height is 4.48 meters.\nThe building orientation is 197 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.61 for the north, 0.32 for the south, 0.59 for the west, and 0.80 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 21, 22, 23, 24, 25. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 26, 27, 28, 29, 30. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.,zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26.,zone 27, zone 28, zone 29, zone 30.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_12 = f"""
Simulate a 14 story L-shaped building.\nThe height of story 1 is 3.32 meters.\nThe height of story 2 is 4.59 meters.\nThe height of story 3 is 9.13 meters.\nThe height of story 4 is 3.77 meters.\nThe height of story 5 is 5.21 meters.\nThe height of story 6 is 10.49 meters.\nThe height of story 7 is 11.55 meters.\nThe height of story 8 is 8.72 meters.\nThe height of story 9 is 8.28 meters.\nThe height of story 10 is 2.28 meters.\nThe height of story 11 is 4.15 meters.\nThe height of story 12 is 11.97 meters.\nThe height of story 13 is 10.53 meters.\nThe height of story 14 is 3.50 meters.\n\nThe horizontal segment is 131.56 meters long and 134.26 meters wide.\nThe vertical segment is 116.6 meters long and 199.08 meters wide.\nThe building orientation is 48 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.55 for the north, 0.49 for the south, 0.47 for the west, and 0.70 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 21, 22, 23, 24, 25. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 26, 27, 28. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 21, 22, 23, 24, 25, 26, 27, 28, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.,zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26.,zone 27, zone 28.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_8_13 = f"""
Simulate a 11 story hollow square, courtyard building with a gable roof.\nThe height of story 1 is 14.37 meters.\nThe height of story 2 is 13.73 meters.\nThe height of story 3 is 1.96 meters.\nThe height of story 4 is 12.46 meters.\nThe height of story 5 is 6.14 meters.\nThe height of story 6 is 5.09 meters.\nThe height of story 7 is 3.69 meters.\nThe height of story 8 is 14.80 meters.\nThe height of story 9 is 7.72 meters.\nThe height of story 10 is 7.80 meters.\nThe height of story 11 is 11.13 meters.\nThe horizontal segments are 443.67 meters long and 62.52 meters wide.\nThe vertical segments are 82.80 meters long and 430.97 meters wide.\nThe attic height is 111.09 meters.\nThe building orientation is 324 degrees to the north.\nEach story has 4 thermal zones in each orientation.\nThe window-to-wall ratio is 0.87 for the north, 0.46 for the south, 0.73 for the west, and 0.82 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 21, 22, 23, 24, 25. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.,zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26.,zone 27, zone 28, zone 29, zone 30, zone 31, zone 32, zone 33, zone 34, zone 35, zone 36.,zone 37, zone 38, zone 39, zone 40, zone 41, zone 42, zone 43, zone 44.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""


detailed_prompt_8_14 = f"""
Simulate a 7 story hollow square, courtyard building.\nThe height of story 1 is 14.62 meters.\nThe height of story 2 is 11.42 meters.\nThe height of story 3 is 7.80 meters.\nThe height of story 4 is 11.16 meters.\nThe height of story 5 is 5.27 meters.\nThe height of story 6 is 8.43 meters.\nThe height of story 7 is 14.78 meters.\nThe horizontal segments are 45.75 meters long and 37.63 meters wide.\nThe vertical segments are 9.78 meters long and 161.37 meters wide.\nThe attic height is 0.70 meters.\nThe building orientation is 45 degrees to the north.\nEach story has 4 thermal zones in each orientation.\nThe window-to-wall ratio is 0.53 for the north, 0.17 for the south, 0.63 for the west, and 0.28 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 21, 22, 23, 24, 25. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 26, 27, 28. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 21, 22, 23, 24, 25, 26, 27, 28, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, system incorporating air handling units, AHUs.
The AHU 1 serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 17.8 Celsius, and for heating is 41.8 Celsius.
The outdoor ventilation rate is 3.11 ACH.
The fan efficiency is 0.76, the pressure rise is 819 Pa, and the maximum flow rate is 78.12 m3/s.
The AHU 2 serves zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.,zone 17, zone 18, zone 19, zone 20.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 10.3 Celsius, and for heating is 51.1 Celsius.
The outdoor ventilation rate is 1.9 ACH.
The fan efficiency is 0.65, the pressure rise is 664 Pa, and the maximum flow rate is 102.04 m3/s.
The AHU 3 serves zone 21, zone 22, zone 23, zone 24, zone 25, zone 26.,zone 27, zone 28.
It includes an economizer, which operates based on differential enthalpy.
The supply air temperature for cooling is 11.5 Celsius, and for heating is 37.6 Celsius.
The outdoor ventilation rate is 0.57 ACH.
The fan efficiency is 0.64, the pressure rise is 470 Pa, and the maximum flow rate is Autosize m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""


detailed_prompt_9_1 = f"""
Simulate a 5 story U-shaped building with a gable roof.\nThe height of story 1 is 3.02 meters.\nThe height of story 2 is 7.59 meters.\nThe height of story 3 is 11.61 meters.\nThe height of story 4 is 13.34 meters.\nThe height of story 5 is 2.75 meters.\nThe horizontal segment is 326.39 meters long and 31.38 meters wide.\nThe left vertical segment is 93.74 meters long and 209.89 meters wide.\nThe right vertical segment is 23.38 meters long and 97 meters wide.\nThe attic height is 34.65 meters.\nThe building orientation is 144 degrees to the north.\nEach story has 3 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.77 for the north, 0.19 for the south, 0.21 for the west, and 0.54 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10, 11, 12, 13, 14, 15. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_9_2 = f"""
Simulate a 4 story U-shaped building.\nThe height of story 1 is 7.31 meters.\nThe height of story 2 is 4.32 meters.\nThe height of story 3 is 6.56 meters.\nThe height of story 4 is 6.59 meters.\nThe horizontal segment is 270.02 meters long and 25.49 meters wide.\nThe left vertical segment is 72.69 meters long and 219.47 meters wide.\nThe right vertical segment is 27.11 meters long and 124 meters wide.\nThe attic height is 36.62 meters.\nThe building orientation is 12 degrees to the north.\nEach story has 3 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.74 for the north, 0.86 for the south, 0.66 for the west, and 0.21 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10, 11, 12. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""


detailed_prompt_9_3 = f"""
Simulate a 11 story T-shaped building with a gable roof.\nThe height of story 1 is 3.45 meters.\nThe height of story 2 is 4.11 meters.\nThe height of story 3 is 9.67 meters.\nThe height of story 4 is 9.26 meters.\nThe height of story 5 is 11.24 meters.\nThe height of story 6 is 8.56 meters.\nThe height of story 7 is 4.94 meters.\nThe height of story 8 is 12.44 meters.\nThe height of story 9 is 9.74 meters.\nThe height of story 10 is 11.83 meters.\nThe height of story 11 is 4.98 meters.\nThe horizontal segment is 183.38 meters long and 94.51 meters wide.\nThe vertical segment is 100.72 meters long and 203.56 meters wide.\nThe vertical segment is 4.53 meters to the edge of the horizontal segment.\nThe attic height is 5.73 meters.\nThe building orientation is 197 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.82 for the north, 0.62 for the south, 0.17 for the west, and 0.64 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_9_4 = f"""
Simulate a 7 story T-shaped building.\nThe height of story 1 is 6.81 meters.\nThe height of story 2 is 10.84 meters.\nThe height of story 3 is 7.79 meters.\nThe height of story 4 is 14.01 meters.\nThe height of story 5 is 2.90 meters.\nThe height of story 6 is 10.05 meters.\nThe height of story 7 is 7.32 meters.\nThe horizontal segment is 175.58 meters long and 169.32 meters wide.\nThe vertical segment is 64.89 meters long and 436.49 meters wide.\nThe vertical segment is 9.51 meters to the edge of the horizontal segment.\nThe building orientation is 59 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.80 for the north, 0.89 for the south, 0.88 for the west, and 0.50 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10, 11, 12, 13, 14. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_9_5 = f"""
Simulate a 14 story building that is 123.65 meters long, 317.02 meters wide, with a hip roof\nThe height of story 1 is 9.64 meters.\nThe height of story 2 is 2.75 meters.\nThe height of story 3 is 6.79 meters.\nThe height of story 4 is 5.14 meters.\nThe height of story 5 is 13.01 meters.\nThe height of story 6 is 13.39 meters.\nThe height of story 7 is 8.57 meters.\nThe height of story 8 is 6.44 meters.\nThe height of story 9 is 1.60 meters.\nThe height of story 10 is 4.45 meters.\nThe height of story 11 is 1.73 meters.\nThe height of story 12 is 11.45 meters.\nThe height of story 13 is 11.57 meters.\nThe height of story 14 is 13.33 meters.\nThe attic height is 3.41 meters.\nThe building orientation is 295 degrees to the north.\nThe window-to-wall ratio is 0.39 for the north, 0.76 for the south, 0.81 for the west, and 0.89 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10, 11, 12, 13, 14. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_9_6 = f"""
Simulate a 9 story building that is 43.84 meters long, 412.01 meters wide, with a gable roof\nThe height of story 1 is 2.28 meters.\nThe height of story 2 is 4.37 meters.\nThe height of story 3 is 1.86 meters.\nThe height of story 4 is 5.35 meters.\nThe height of story 5 is 7.59 meters.\nThe height of story 6 is 12.83 meters.\nThe height of story 7 is 7.27 meters.\nThe height of story 8 is 4.71 meters.\nThe height of story 9 is 12.59 meters.\nThe attic height is 9.26 meters.\nThe building orientation is 249 degrees to the north.\nThe window-to-wall ratio is 0.57 for the north, 0.35 for the south, 0.16 for the west, and 0.35 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 9. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4, zone 5, zone 6, zone 7, zone 8, zone 9.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""


detailed_prompt_9_7 = f"""
Simulate a 19 story building that is 355.71 meters long, 482.97 meters wide.\nThe height of story 1 is 1.54 meters.\nThe height of story 2 is 11.15 meters.\nThe height of story 3 is 8.53 meters.\nThe height of story 4 is 8.63 meters.\nThe height of story 5 is 4.30 meters.\nThe height of story 6 is 13.67 meters.\nThe height of story 7 is 9.06 meters.\nThe height of story 8 is 7.05 meters.\nThe height of story 9 is 10.85 meters.\nThe height of story 10 is 14.21 meters.\nThe height of story 11 is 2.78 meters.\nThe height of story 12 is 5.42 meters.\nThe height of story 13 is 14.01 meters.\nThe height of story 14 is 8.48 meters.\nThe height of story 15 is 1.99 meters.\nThe height of story 16 is 8.82 meters.\nThe height of story 17 is 3.60 meters.\nThe height of story 18 is 4.99 meters.\nThe height of story 19 is 3.98 meters.\nThe building orientation is 43 degrees to the north.\nThe window-to-wall ratio is 0.27 for the north, 0.38 for the south, 0.74 for the west, and 0.67 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10, 11, 12, 13, 14, 15, 16, 17, 18, 19. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_9_8 = f"""
Simulate a 6 story building that is 433.15 meters long, 436.07 meters wide, with a hip roof\nThe height of story 1 is 5.55 meters.\nThe height of story 2 is 13.97 meters.\nThe height of story 3 is 1.83 meters.\nThe height of story 4 is 12.50 meters.\nThe height of story 5 is 7.44 meters.\nThe height of story 6 is 2.97 meters.\nThe attic height is 9.96 meters.\nThe building orientation is 242 degrees to the north.\nEach story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\nThe depth of exterior thermal zone is 159.66 meters.\nThe window-to-wall ratio is 0.28 for the north, 0.45 for the south, 0.63 for the west, and 0.50 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6, 7, 8, 9. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 10, 11, 12, 13, 14, 15, 16, 17, 18, 19. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 20, 21, 22, 23, 24. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 25, 26, 27, 28, 29, 30. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 23, 24, 25, 26, 27, 28, 29, 30, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, .
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_9_9 = f"""
Simulate a 7 story building that is 234.18 meters long, 151.94 meters wide, with a gable roof.\nThe height of story 1 is 3.40 meters.\nThe height of story 2 is 13.21 meters.\nThe height of story 3 is 12.94 meters.\nThe height of story 4 is 7.21 meters.\nThe height of story 5 is 8.68 meters.\nThe height of story 6 is 10.85 meters.\nThe height of story 7 is 2.28 meters.\nThe attic height is 0.93 meters.\nThe building orientation is 331 degrees to the north.\nEach story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\nThe depth of exterior thermal zone is 29.58 meters.\nThe window-to-wall ratio is 0.47 for the north, 0.52 for the south, 0.29 for the west, and 0.72 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3, zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25, zone 26, zone 27, zone 28, zone 29, zone 30, zone 31, zone 32, zone 33, zone 34, zone 35.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""


detailed_prompt_9_10 = f"""
Simulate a 5 story building that is 332.91 meters long, 472.63 meters wide.\nThe height of story 1 is 5.51 meters.\nThe height of story 2 is 3.93 meters.\nThe height of story 3 is 13.79 meters.\nThe height of story 4 is 13.92 meters.\nThe height of story 5 is 14.88 meters.\nThe attic height is 30.04 meters.\nThe building orientation is 183 degrees to the north.\nEach story has 5 thermal zones with 1 core thermal zone and 4 exterior thermal zones in each orientation.\nThe depth of exterior thermal zone is 102.18 meters.\nThe window-to-wall ratio is 0.58 for the north, 0.21 for the south, 0.50 for the west, and 0.72 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3, 4, 5, 6. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 7, 8, 9. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 10, 11, 12. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16, zone 17, zone 18, zone 19, zone 20, zone 21, zone 22, zone 23, zone 24, zone 25.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_9_11 = f"""
Simulate a 8 story L-shaped building with a gable roof.\nThe height of story 1 is 2.40 meters.\nThe height of story 2 is 10.39 meters.\nThe height of story 3 is 9.10 meters.\nThe height of story 4 is 8.85 meters.\nThe height of story 5 is 7.29 meters.\nThe height of story 6 is 2.16 meters.\nThe height of story 7 is 13.31 meters.\nThe height of story 8 is 4.15 meters.\n\nThe horizontal segment is 44.8 meters long and 56.56 meters wide.\nThe vertical segment is 7.4 meters long and 91.94 meters wide.\nThe attic height is 4.93 meters.\nThe building orientation is 218 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.35 for the north, 0.90 for the south, 0.11 for the west, and 0.57 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10, 11, 12, 13, 14, 15, 16. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14, zone 15, zone 16.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_9_12 = f"""
Simulate a 7 story L-shaped building.\nThe height of story 1 is 10.74 meters.\nThe height of story 2 is 2.72 meters.\nThe height of story 3 is 13.37 meters.\nThe height of story 4 is 12.83 meters.\nThe height of story 5 is 6.63 meters.\nThe height of story 6 is 7.36 meters.\nThe height of story 7 is 8.60 meters.\n\nThe horizontal segment is 159.96 meters long and 265.77 meters wide.\nThe vertical segment is 21.94 meters long and 429.09 meters wide.\nThe building orientation is 288 degrees to the north.\nEach story has 2 thermal zones with each segment as one thermal zone.\nThe window-to-wall ratio is 0.60 for the north, 0.56 for the south, 0.11 for the west, and 0.23 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10, 11, 12, 13, 14. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, 13, 14, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12, zone 13, zone 14.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_9_13 = f"""
Simulate a 3 story hollow square, courtyard building with a gable roof.\nThe height of story 1 is 8.80 meters.\nThe height of story 2 is 9.73 meters.\nThe height of story 3 is 12.93 meters.\nThe horizontal segments are 282.58 meters long and 118.14 meters wide.\nThe vertical segments are 35.58 meters long and 456.82 meters wide.\nThe attic height is 21.01 meters.\nThe building orientation is 250 degrees to the north.\nEach story has 4 thermal zones in each orientation.\nThe window-to-wall ratio is 0.76 for the north, 0.90 for the south, 0.83 for the west, and 0.84 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 1, 2, 3. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 4, 5, 6. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 7, 8, 9. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 10, 11, 12. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, 4, 5, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 6, 7, 8, 9, 10, 11, 12, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4, zone 5, zone 6, zone 7, zone 8, zone 9, zone 10, zone 11, zone 12.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

detailed_prompt_9_14 = f"""
Simulate a 1 story hollow square, courtyard building.\nThe height of story 1 is 11.42 meters.\nThe horizontal segments are 144.24 meters long and 19.33 meters wide.\nThe vertical segments are 29.80 meters long and 390.88 meters wide.\nThe attic height is 26.60 meters.\nThe building orientation is 352 degrees to the north.\nEach story has 4 thermal zones in each orientation.\nThe window-to-wall ratio is 0.80 for the north, 0.58 for the south, 0.17 for the west, and 0.78 for the east.

The wall is made of concrete, with a thickness of 0.03 meters and the wall insulation is R18. The roof is made of concrete, with a thickness of 0.05 meters and the roof insulation is R18. The floor is made of concrete, covered with carpet. The window U-factor is 1.8 W/m2K and the SHGC is 0.3. 
This building have 4 space types.
Space type 1 is for zone 2. For space type 1, the people density is 10 m2/person, the lighting density is 4 W/m2, and the electric equipment density is 8 W/m2. The people activity level is 130 W/person. The infiltration rate is 0.11 ACH. The occupancy rate is 0.9 from 8:00 to 16:00 and 0.2 in other periods of time. 
Space type 2 is for zone 1. For space type 2, the people density is 15 m2/person, the lighting density is 8 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 120 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.9 from 6:00 to 18:00 and 0.1 in other periods of time. 
Space type 3 is for zone 3. For space type 3, the people density is 8 m2/person, the lighting density is 6 W/m2, and the electric equipment density is 12 W/m2. The people activity level is 140 W/person. The infiltration rate is 0.12 ACH. The occupancy rate is 0.5 from 9:00 to 14:00 and 0.3 in other periods of time. 
Space type 4 is for zone 4. For space type 4, the people density is 18 m2/person, the lighting density is 12 W/m2, and the electric equipment density is 6 W/m2. The people activity level is 150 W/person. The infiltration rate is 0.13 ACH. The occupancy rate is 0.7 from 10:00 to 18:00 and 0.5 in other periods of time. 
For zone 1, 2, the cooling setpoint is 24.0 Celsius during 6:00 to 18:00, and 26.0 Celsius in unoccupied periods. The heating setpoint is 20.0 Celsius during 6:00 to 18:00, and 18.0 Celsius in unoccupied periods. 
For zone 3, the cooling setpoint is 25.0 Celsius during 8:00 to 20:00, and 27.0 Celsius in unoccupied periods. The heating setpoint is 21.0 Celsius during 8:00 to 20:00, and 18.0 Celsius in unoccupied periods. 
For zone 4, the cooling setpoint is 26.0 Celsius during 10:00 to 22:00, and 28.0 Celsius in unoccupied periods. The heating setpoint is 22.0 Celsius during 10:00 to 22:00, and 16.0 Celsius in unoccupied periods. 

The HVAC system in this building is variable air volume, VAV, + fan coil unit, FCU, system.
The variable air volume, VAV, system serves zone 1, zone 2, zone 3.
It includes an economizer, which operates based on differential dry bulb.
The supply air temperature for cooling is 11.1 Celsius, and for heating is 46.7 Celsius.
The outdoor ventilation rate is 0.9 ACH.
The fan efficiency is 0.71, the pressure rise is 792 Pa, and the maximum flow rate is 119.26 m3/s.
The fan coil unit, FCU, system serves zone 4.
The capacity control method of fan coil units, FCUs, is cycling fan.
The supply air temperature for cooling is 18.1 Celsius, and for heating is 54.7 Celsius.
The outdoor ventilation rate is 1.7 ACH.
The fan efficiency of fan coil units, FCUs, is 0.75, the pressure rise is 1395 Pa, and the maximum flow rate is 99.64 m3/s.

For the chilled water loop in the system, the chilled water is supplied by electric chillers.
Chiller 1 has a rated capacity of Autosize W and a rated COP of 3.5.
Chiller 2 has a rated capacity of Autosize W and a rated COP of 4.5.
Chiller 3 has a rated capacity of Autosize W and a rated COP of 5.5.
The chilled water supply temperature is 6.7 Celsius. The design temperature difference (DeltaT) for chilled water is 6.7 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.

For the hot water loop in the system, the hot water is supplied by Coal boilers.
Boiler 1 has a rated capacity of Autosize W and a rated efficiency of 0.7.
Boiler 2 has a rated capacity of Autosize W and a rated efficiency of 0.85.
The hot water supply temperature is 67 Celsius. The design temperature difference (DeltaT) for hot water is 11 Celsius.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 180000 Pa, and a rated power of Autosize W.

For the condenser water loop in the system, the condenser water is supplied by cooling towers.
Cooling tower 1 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 2 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 3 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
Cooling tower 4 has a rated capacity of Autosize W. The rated air flow rate is Autosize m3/s, and the rated water flow rate is Autosize m3/s. The fan's rated power is Autosize W.
The rated efficiency of the pump is 0.8, with a rated flow rate of Autosize m3/s, a rated pump head of 179352 Pa, and a rated power of Autosize W.
"""

ROBUST_PROMPTS = {
    k: v for k, v in globals().items()
    if k.startswith("detailed_prompt_")
}