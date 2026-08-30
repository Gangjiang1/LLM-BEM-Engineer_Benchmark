robust_prompt_1 = f"""Model a 7-story residential building.
WWR 55% south, 35% other façades. Residential occupancy pattern."""

robust_prompt_2 = f"""I want to simulate a 3 story medium-size rectangular office building.
Only one spa type: office room
It should use a VAV system.
The building has moderate window-to-wall radio is 0.4 and standard insulation.
Typical weekday office schedules, with cooling at 24°C and heating at 20°C."""

robust_prompt_3 = f"""Model a 3-story U-shaped office building with a VAV HVAC system.
The window-to-wall ratio is 45% on the south façade and 25% on other orientations.
The building contains 2 space types: office, conference.
Exterior walls are brick with good insulation."""

robust_prompt_4 = f"""Model a two-story laboratory building with a rectangular footprint.
The building uses a fan coil unit (FCU) system with 100% outdoor air.
Exterior walls are precast concrete, and the window-to-wall ratio is limited to 20%."""

robust_prompt_5 = f"""Simulate a five-story U-shaped office building.
The east and west façades have a window-to-wall ratio of 30%, 
while the north and south façades have 50%.
Exterior walls are steel-framed with mineral wool insulation.
Office spaces have equipment loads of 10 W/m² and lighting power density of 9 W/m²."""

robust_prompt_6 = f"""Model a 3-story academic building consisting of classrooms, offices, and corridors.
It is a rectangular building, and each floor has 5 zones.
Classrooms operate from 9:00 to 17:00 with an occupancy density of 0.15 people/m².
Offices follow a standard weekday schedule from 8:00 to 18:00.
The HVAC system is a VAV system with economizers enabled.
The average window-to-wall ratio is 38%."""

robust_prompt_7 = f"""Simulate a seven-story residential building with a linear bar shape.
Each story has 5 zones.
The building uses a heat pump system.
The window-to-wall ratio is 50% on the south façade and 30% elsewhere.
Exterior walls are EIFS with high thermal resistance."""

robust_prompt_8 = f"""Simulate a six-story L-shaped office building with a VAV HVAC system and a window-to-wall ratio of 40%."""

robust_prompt_9 = f"""Simulate a four-story rectangular building. 
The building uses a packaged rooftop VAV system with gas reheat. 
Overall window-to-wall ratio is 30%, and the façade is insulated concrete panels."""

robust_prompt_10 = f"""Simulate a four-story hollow square building. 
The building uses a packaged rooftop VAV system with gas reheat. 
Overall window-to-wall ratio is 30%, and the façade is insulated concrete panels."""

robust_prompt_11 = f"""Simulate a six-story T-shaped mixed-use building with office and retail spaces.
The HVAC system consists of fan coil units served by a dedicated outdoor air system (DOAS).
Office spaces have an occupant density of 0.1 people/m², plug loads of 12 W/m²,
and LED lighting with a lighting power density of 8 W/m².
The average window-to-wall ratio is 35%."""

robust_prompt_12 = f"""Model a ten-story rectengular office building with a central core.
The building uses a variable refrigerant flow (VRF) system with heat recovery.
Cooling and heating setpoints are 24°C and 21°C during occupied hours,
and setback to 28°C and 16°C during unoccupied periods.
Office occupancy follows a weekday schedule from 8:00 to 18:00."""

robust_prompt_13 = f"""Simulate a three-story L-shaped municipal building.
The HVAC system is a VAV system with hot water reheat supplied by gas boilers.
Chilled water is provided by electric chillers with a supply temperature of 6°C.
The window-to-wall ratio is 40% overall, with double-pane low-e glazing."""

robust_prompt_14 = f"""Model a six-story L-shaped office building with perimeter and core zones.
The HVAC system is a VAV system with electric reheat.
Cooling setpoint is 24°C and heating setpoint is 20°C during occupied hours.
Occupant density is 0.09 people/m², lighting power density is 8.5 W/m²,
and equipment power density is 11 W/m².
The overall window-to-wall ratio is 42%, using triple-pane glazing."""

robust_prompt_15 = f"""I want to simulate a medium-size rectangular office building.
It should use a VAV system.
The building has moderate window-to-wall ratio and standard insulation.
Typical weekday office schedules, with cooling at 24°C and heating at 20°C."""

robust_prompt_16 = f"""Please model a 5-story rectengular mixed-use building.
First floor is retail, upper floors are offices. Each floor has 5 zones.
Use a VRF system.
South façade has higher glazing (WWR 55%), north side is more opaque (WWR 30%).
Concrete walls with medium insulation.
Retail operates 9am–9pm, office 8am–6pm."""

robust_prompt_17 = f"""Simulate a 12-story rectangular mixed-use office building in a cold climate, using a central chilled water plant with VAV reheat.
Use a window-to-wall ratio of 35%, with high performance glazing. 
Suitable construction and insulation
Standard office occupancy, efficient lighting, and weekday schedules."""

robust_prompt_18 = f"""Simulate a four-story rectangular hospital outpatient building.
The building has a total of 20 thermal zones.
Space types: exam rooms, offices, waiting areas.
Exam rooms: people 3 m²/person, equipment 15 W/m², lighting 10 W/m².
Offices: people 5 m²/person, equipment 8 W/m², lighting 7 W/m².
Waiting areas: people 2 m²/person, equipment 3 W/m², lighting 6 W/m².
WWR is 40% south, 30% east/west, 20% north.
Exterior walls are insulated precast concrete (U=0.38 W/m²K).
Cooling setpoint 23°C, heating 21°C.
Occupied 7am–7pm weekdays.
HVAC system is VAV with hot water reheat and air-cooled chiller."""

robust_prompt_19 = f"""Model a six-story L-shaped university dormitory.
Space types: dorm rooms, common rooms.
Dorm rooms: people 10 m²/person, equipment 6 W/m², lighting 5 W/m².
Common rooms: people 3 m²/person, equipment 8 W/m², lighting 8 W/m².
The HVAC system is a heat pump system.
WWR is 30% overall.
Exterior walls are EIFS with high insulation.
Cooling 25°C, heating 20°C.
Residential schedule with nighttime occupancy."""

robust_prompt_20 = f"""Simulate a 10-story office tower, hollow square with a central core.
HVAC system is a VRF system with heat recovery.
WWR is 50% on south, 35% elsewhere.
Glass curtain wall with low-e double glazing.
Cooling 24°C, heating 21°C.
Office hours 8am–6pm weekdays."""

robust_prompt_21 = f"""Simulate a five-story U-shaped hotel.
People 20 m²/person, equipment 4 W/m², lighting 6 W/m².
PTAC units with electric heating.
WWR 45% south, 30% other façades.
Occupied 24 hours."""

robust_prompt_22 = f"""Model a two-story retail strip mall with a linear bar shape.
HVAC system is packaged rooftop units with DX cooling and gas heating.
WWR 60% front façade, 15% back.
Glass storefronts with metal framing.
Occupied 10am–10pm daily."""

robust_prompt_23 = f"""Model a three-story elementary school with an L-shaped footprint.
HVAC is heat pump.
WWR 35% south, 25% north, 30% east/west.
Brick walls with interior insulation.
Occupied 8am–3pm weekdays."""

robust_prompt_24 = f"""Simulate a seven-story government office building.
HVAC: DOAS + fan coil units.
WWR 30% overall.
Exterior walls are stone cladding with rigid insulation.
Office schedule 8am–5pm."""

robust_prompt_25 = f"""Model a four-story medical research laboratory.
Each floor has 5 zones.
HVAC system is 100% outdoor air VAV with heat recovery.
WWR 20% overall.
Precast concrete façade.
Cooling 22°C, heating 20°C.
Occupied 24 hours."""

robust_prompt_26 = f"""Model a three-story community center with a courtyard (hollow square).
HVAC is packaged rooftop heat pump units.
WWR 40% south, 20% north.
Occupied 9am–9pm."""

robust_prompt_27 = f"""Model a five-story courthouse.
HVAC: VAV with hot water reheat.
WWR 25% overall.
Concreate façade with insulation.
Occupied 8am–5pm."""

robust_prompt_28 = f"""Simulate a two-story industrial office + warehouse building.
Office zones: people 6 m²/person, lighting 7 W/m².
Warehouse zones: lighting 4 W/m², equipment 5 W/m².
HVAC: rooftop units for office, unit heaters for warehouse.
WWR 15%."""

robust_prompt_29 = f"""Simulate a four-story research office with a courtyard.
HVAC: VAV with economizer and heat recovery.
WWR 35%.
Brick façade with high insulation.
Office hours 8am–6pm."""

robust_prompt_30 = f"""Simulate a four-story T-shaped office building.
HVAC system is a dual-duct VAV system with hot water reheat.
Office spaces: people 8 m²/person, equipment 12 W/m², lighting 9 W/m².
WWR is 45% south, 30% east/west, 20% north.
Exterior walls are insulated metal panels.
Cooling 24°C, heating 20°C.
Occupied 8am–6pm weekdays."""

robust_prompt_31 = f"""Model a four-story food court and commercial center.
HVAC is packaged rooftop units with gas heating.
Kitchen zones: equipment 25 W/m², lighting 12 W/m².
Dining zones: people 1.5 m²/person, lighting 10 W/m².
WWR 60% front façade, 20% others."""

robust_prompt_32 = f"""Simulate an eight-story student center with a courtyard.
HVAC system is VRF with heat recovery.
WWR 40% south, 25% north, 30% east/west.
Exterior walls are precast concrete.
Cooling 24°C, heating 20°C."""

robust_prompt_33 = f"""Model a three-story suburban medical clinic.
HVAC: packaged VAV rooftop system.
WWR 30%.
Exam rooms operate 7am–6pm.
Cooling 23°C, heating 21°C."""

robust_prompt_34 = f"""Simulate a four-story cultural center with a circular courtyard. Overall WWR is 30%."""

robust_prompt_35 = f"""Model a six-story logistics headquarters.
HVAC: VAV.
WWR 35%.
Cooling 24°C, heating 20°C."""

robust_prompt_36 = f"""Simulate a two-story airport terminal support building.
WWR 45% front, 20% rear.
Occupied 24 hours."""

robust_prompt_37 = f"""Model a nine-story residential courtyard tower.
HVAC: packaged heat pump units.
WWR 40% south, 25% others.
EIFS façade."""

robust_prompt_38 = f"""Model a three-story training center.
HVAC: rooftop VAV system.
WWR 35%.
Occupied 9am–5pm weekdays."""

robust_prompt_39 = f"""Simulate a seven-story research office with a hollow-square footprint.
HVAC: VAV with heat recovery and economizer.
WWR 38%.
Brick façade with rigid insulation."""

robust_prompt_40 = f"""Simulate a five-story rectangular office building.
HVAC system is a VAV system with hot water reheat.
WWR is 35% south, 30% east/west, 20% north.
Exterior walls are insulated concrete panels.
Cooling 24°C, heating 20°C.
Occupied 8am–6pm weekdays."""

robust_prompt_41 = f"""Model a three-story U-shaped school building.
Space types: classroom, office.
Classrooms: people 0.18 people/m², lighting 9 W/m².
Offices: people 0.1 people/m², lighting 7 W/m².
HVAC: packaged rooftop heat pump.
WWR 40% south, 25% others.
Occupied 8am–4pm weekdays."""

robust_prompt_42 = f"""Simulate a seven-story L-shaped residential building.
HVAC system is a VRF system.
WWR 45% south, 30% others.
EIFS façade with high insulation.
Cooling 25°C, heating 20°C.
Residential schedule."""

robust_prompt_43 = f"""Model a four-story hollow square office building.
HVAC is dual-duct VAV with reheat.
WWR 38% overall.
Brick walls with interior insulation.
Cooling 24°C, heating 20°C.
Office hours 8am–6pm."""

robust_prompt_44 = f"""Simulate a six-story rectangular mixed-use building.
First floor retail, upper floors offices.
Each floor has 5 zones.
HVAC: VRF system with heat recovery.
WWR 50% south, 30% north, 35% east/west.
Concrete walls with medium insulation."""

robust_prompt_45 = f"""Simulate a five-story hotel building.
HVAC: fan coil units with DOAS.
People 18 m²/person, lighting 6 W/m².
WWR 40% south, 25% others.
Occupied 24 hours."""

robust_prompt_46 = f"""Model a four-story medical outpatient clinic.
Space types: exam rooms, offices.
HVAC: VAV with hot water reheat.
WWR 35%.
Precast concrete façade.
Occupied 7am–7pm weekdays."""

robust_prompt_47 = f"""Simulate a ten-story office tower with central core.
HVAC: VRF with heat recovery.
WWR 45% south, 35% others.
Glass curtain wall, low-e glazing.
Office hours 8am–6pm."""

robust_prompt_48 = f"""Model a two-story retail strip mall.
HVAC: packaged rooftop units.
WWR 55% front, 20% back.
Metal framed storefront glazing.
Occupied 10am–10pm."""

robust_prompt_49 = f"""Simulate a six-story research office.
HVAC: VAV with heat recovery.
WWR 35%.
Brick façade with rigid insulation.
Cooling 24°C, heating 20°C."""

robust_prompt_50 = f"""Model a three-story community center.
HVAC: packaged heat pump units.
WWR 40% south, 25% others.
Occupied 9am–9pm."""

robust_prompt_51 = f"""Simulate an eight-story government office.
HVAC: DOAS + fan coil.
WWR 30%.
Stone cladding with insulation.
Occupied 8am–5pm."""

robust_prompt_52 = f"""Model a five-story courthouse.
HVAC: VAV with hot water reheat.
WWR 28%.
Concrete façade with insulation.
Occupied 8am–5pm."""

robust_prompt_53 = f"""Simulate a four-story medical research laboratory.
HVAC: 100% outdoor air VAV with heat recovery.
WWR 20%.
Precast concrete façade.
Occupied 24 hours."""

robust_prompt_54 = f"""Model a six-story data center support building.
Space types: server halls, offices.
Server halls: equipment 900 W/m².
WWR 10%.
Metal panel façade."""

robust_prompt_55 = f"""Simulate a five-story U-shaped office building.
HVAC: VAV.
WWR 32% east/west, 45% south, 25% north.
Insulated metal panel façade."""

robust_prompt_56 = f"""Model a three-story elementary school.
HVAC: heat pump.
WWR 30% south, 25% north, 28% east/west.
Brick façade.
Occupied 8am–3pm weekdays."""

robust_prompt_57 = f"""Simulate a seven-story student dormitory.
HVAC: packaged heat pump.
WWR 38%.
EIFS façade.
Residential schedule."""

robust_prompt_58 = f"""Model a four-story cultural center.
HVAC: VAV.
WWR 30%.
Concrete façade with insulation.
Occupied 10am–8pm."""

robust_prompt_59 = f"""Simulate a five-story research office with courtyard.
HVAC: VAV with economizer.
WWR 36%.
Brick façade with insulation."""

robust_prompt_60 = f"""Model a two-story industrial office + warehouse.
HVAC: rooftop for office, unit heaters for warehouse.
WWR 15%."""

robust_prompt_61 = f"""Simulate a six-story logistics headquarters.
HVAC: VAV.
WWR 34%.
Cooling 24°C, heating 20°C."""

robust_prompt_62 = f"""Model a nine-story residential courtyard tower.
HVAC: VRF.
WWR 42%.
EIFS façade."""

robust_prompt_63 = f"""Simulate a three-story training center.
HVAC: rooftop VAV.
WWR 33%.
Occupied 9am–5pm."""

robust_prompt_64 = f"""Model a seven-story research office.
HVAC: VAV with heat recovery.
WWR 37%.
Brick façade."""

robust_prompt_65 = f"""Simulate a four-story hospital outpatient building.
HVAC: VAV with hot water reheat.
WWR 34%.
Cooling 23°C, heating 21°C."""

robust_prompt_66 = f"""Model a three-story office building.
HVAC: VAV.
WWR 35%.
Insulated concrete façade."""

robust_prompt_67 = f"""Simulate an eight-story student center.
HVAC: VRF with heat recovery.
WWR 39%.
Precast concrete façade."""

robust_prompt_68 = f"""Model a four-story medical clinic.
HVAC: packaged VAV.
WWR 30%.
Occupied 7am–6pm."""

robust_prompt_69 = f"""Model a five-story courthouse.
HVAC: VAV.
WWR 26%.
Concrete façade."""

robust_prompt_70 = f"""Simulate a six-story research lab.
HVAC: 100% OA VAV.
WWR 18%."""

robust_prompt_71 = f"""Model a ten-story office tower.
HVAC: VRF.
WWR 40%.
Glass curtain wall."""

robust_prompt_72 = f"""Model a three-story school.
HVAC: heat pump.
WWR 33%.
Occupied 8am–4pm."""

robust_prompt_73 = f"""Simulate a seven-story dormitory.
HVAC: packaged heat pump.
WWR 36%."""

robust_prompt_74 = f"""Model a four-story research office.
HVAC: VAV.
WWR 34%.
Brick façade."""

robust_prompt_75 = f"""Simulate a five-story rectangular office building.
Each floor has 5 zones.
HVAC: VAV with electric reheat.
WWR 36% south, 28% east/west, 22% north.
Insulated concrete façade.
Cooling 24°C, heating 20°C.
Office hours 8am–6pm."""

robust_prompt_76 = f"""Model a three-story U-shaped school building.
Space types: classroom, office.
Classrooms: people 0.16 people/m², lighting 8.5 W/m².
Offices: people 0.09 people/m², lighting 7 W/m².
HVAC: packaged rooftop heat pump.
WWR 42% south, 27% others.
Occupied 8am–4pm weekdays."""

robust_prompt_77 = f"""Simulate a seven-story L-shaped residential building.
HVAC system is a VRF system.
WWR 47% south, 32% others.
EIFS façade with high insulation.
Cooling 25°C, heating 20°C.
Residential schedule."""

robust_prompt_78 = f"""Model a four-story hollow square office building.
HVAC is dual-duct VAV with hot water reheat.
WWR 40% overall.
Brick walls with interior insulation.
Cooling 24°C, heating 20°C.
Office hours 8am–6pm."""

robust_prompt_79 = f"""Simulate a five-story hotel building.
HVAC: fan coil units with DOAS.
People 17 m²/person, lighting 6.5 W/m².
WWR 42% south, 28% others.
Occupied 24 hours."""

robust_prompt_80 = f"""Model a four-story medical outpatient clinic.
Space types: exam rooms, offices.
HVAC: VAV with hot water reheat.
WWR 37%.
Precast concrete façade.
Occupied 7am–7pm weekdays."""

robust_prompt_81 = f"""Simulate a ten-story office tower with central core.
HVAC: VRF with heat recovery.
WWR 47% south, 37% others.
Glass curtain wall, low-e glazing.
Office hours 8am–6pm."""

robust_prompt_82 = f"""Model a two-story retail strip mall.
HVAC: packaged rooftop units.
WWR 57% front, 18% back.
Metal framed storefront glazing.
Occupied 10am–10pm."""

robust_prompt_83 = f"""Simulate a six-story research office.
HVAC: VAV with heat recovery.
WWR 37%.
Brick façade with rigid insulation.
Cooling 24°C, heating 20°C."""

robust_prompt_84 = f"""Model a three-story community center.
HVAC: packaged heat pump units.
WWR 42% south, 27% others.
Occupied 9am–9pm."""

robust_prompt_85 = f"""Model a five-story courthouse.
HVAC: VAV with hot water reheat.
WWR 30%.
Concrete façade with insulation.
Occupied 8am–5pm."""

robust_prompt_86 = f"""Simulate a four-story medical research laboratory.
HVAC: 100% outdoor air VAV with heat recovery.
WWR 22%.
Precast concrete façade.
Occupied 24 hours."""

robust_prompt_87 = f"""Model a six-story data center support building.
Space types: server halls, offices.
Server halls: equipment 950 W/m².
WWR 12%.
Metal panel façade."""

robust_prompt_88 = f"""Simulate a five-story U-shaped office building.
HVAC: VAV.
WWR 34% east/west, 47% south, 27% north.
Insulated metal panel façade."""

robust_prompt_89 = f"""Model a three-story elementary school.
HVAC: heat pump.
WWR 32% south, 27% north, 30% east/west.
Brick façade.
Occupied 8am–3pm weekdays."""

robust_prompt_90 = f"""Simulate a seven-story student dormitory.
HVAC: packaged heat pump.
WWR 40%.
EIFS façade.
Residential schedule."""

robust_prompt_91 = f"""Model a four-story cultural center.
HVAC: VAV.
WWR 32%.
Concrete façade with insulation.
Occupied 10am–8pm."""

robust_prompt_92 = f"""Simulate a five-story research office with courtyard.
HVAC: VAV with economizer.
WWR 38%.
Brick façade with insulation."""

robust_prompt_93 = f"""Model a two-story industrial office + warehouse.
HVAC: rooftop for office, unit heaters for warehouse.
WWR 17%."""

robust_prompt_94 = f"""Simulate a six-story logistics headquarters.
HVAC: VAV.
WWR 36%.
Cooling 24°C, heating 20°C."""

robust_prompt_95 = f"""Model a nine-story residential courtyard tower.
HVAC: VRF.
WWR 44%.
EIFS façade."""

robust_prompt_96 = f"""Simulate a three-story training center.
HVAC: rooftop VAV.
WWR 35%.
Occupied 9am–5pm."""

robust_prompt_97 = f"""Model a seven-story research office.
HVAC: VAV with heat recovery.
WWR 39%.
Brick façade."""

robust_prompt_98 = f"""Simulate a four-story hospital outpatient building.
HVAC: VAV with reheat.
WWR 36%.
Cooling 23°C, heating 21°C."""

robust_prompt_99 = f"""Model a five-story hotel.
HVAC: PTAC units.
WWR 45% south, 32% others.
Occupied 24 hours."""

robust_prompt_100 = f"""Model a three-story office building.
HVAC: VAV.
WWR 37%.
Insulated concrete façade."""

robust_prompt_101 = f"""Simulate an eight-story student center.
HVAC: VRF with heat recovery.
WWR 41%.
Precast concrete façade."""

robust_prompt_102 = f"""Model a four-story medical clinic.
HVAC: packaged VAV.
WWR 32%.
Occupied 7am–6pm."""

robust_prompt_103 = f"""Model a five-story courthouse.
HVAC: VAV.
WWR 28%.
Concrete façade."""

robust_prompt_104 = f"""Simulate a six-story research lab.
HVAC: 100% OA VAV.
WWR 20%."""

robust_prompt_105 = f"""Model a ten-story office tower.
HVAC: VRF.
WWR 42%.
Glass curtain wall."""

robust_prompt_106 = f"""Simulate a two-story retail strip.
HVAC: rooftop DX.
WWR 60% front, 20% back."""

robust_prompt_107 = f"""Model a three-story school.
HVAC: heat pump.
WWR 35%.
Occupied 8am–4pm."""

robust_prompt_108 = f"""Simulate a seven-story dormitory.
HVAC: packaged heat pump.
WWR 38%."""

robust_prompt_109 = f"""Model a four-story research office.
HVAC: VAV.
WWR 36%.
Brick façade."""

robust_prompt_110 = f"""Simulate a five-story rectangular office building.
The HVAC system is a VAV system with economizers enabled.
The window-to-wall ratio is 35% overall.
Exterior walls are brick with interior insulation.
Cooling setpoint is 24°C and heating setpoint is 20°C.
Office operates 8am–6pm on weekdays."""

robust_prompt_111 = f"""Model a four-story U-shaped office building.
The HVAC system is a packaged rooftop VAV system with gas reheat.
Overall window-to-wall ratio is 28%.
Exterior walls are insulated concrete panels.
Cooling 24°C, heating 21°C."""

robust_prompt_112 = f"""Simulate a six-story T-shaped office building.
The HVAC system is a VAV system with hot water reheat.
Chilled water is provided by electric chillers.
WWR is 40% overall with low-e glazing.
Cooling 24°C, heating 20°C."""

robust_prompt_113 = f"""Model a three-story rectangular school building.
Classrooms operate from 8am to 4pm.
Occupancy density is 0.18 people/m².
The HVAC system is a heat pump packaged rooftop unit.
WWR is 35% overall."""

robust_prompt_114 = f"""Simulate a ten-story rectangular office building.
The HVAC system is a VRF system with heat recovery.
Cooling 24°C, heating 21°C.
Office hours 8am–6pm weekdays.
Window-to-wall ratio is 38%.
Exterior walls are steel-framed with mineral wool."""

robust_prompt_115 = f"""Model a five-story hollow square office building.
The HVAC system is a VAV system with electric reheat.
WWR is 45% on south, 30% elsewhere.
Triple-pane glazing.
Lighting power density is 8 W/m²."""

robust_prompt_116 = f"""Simulate a six-story linear residential building.
The HVAC system is a heat pump system.
WWR is 50% on south, 30% elsewhere.
Exterior walls are EIFS with high thermal resistance.
Cooling 25°C, heating 20°C."""

robust_prompt_117 = f"""Model a four-story rectangular hospital outpatient building.
The HVAC system is VAV with hot water reheat.
Cooling setpoint 23°C, heating 21°C.
WWR is 35% overall.
Exterior walls are insulated precast concrete."""

robust_prompt_118 = f"""Simulate an eight-story L-shaped office building.
The HVAC system is a VAV system.
WWR is 42% overall.
Exterior walls are brick with interior insulation.
Cooling 24°C, heating 20°C."""

robust_prompt_119 = f"""Model a three-story U-shaped municipal building.
The HVAC system is a VAV system with electric reheat.
Overall window-to-wall ratio is 33%.
Double-pane low-e glazing."""

robust_prompt_120 = f"""Model a seven-story T-shaped office building.
The HVAC system is a packaged rooftop VAV system with gas reheat.
Overall window-to-wall ratio is 30%.
Exterior walls are steel-framed with mineral wool."""

robust_prompt_121 = f"""Model a six-story L-shaped office building.
The HVAC system is a VAV system with economizers.
WWR is 38% overall.
Cooling 24°C, heating 20°C."""

robust_prompt_122 = f"""Simulate a ten-story rectangular office building.
The HVAC system is a central chilled water VAV system with reheat.
WWR is 35% overall.
Cooling 24°C, heating 21°C."""

robust_prompt_123 = f"""Model a four-story hollow square academic building.
Space types: classrooms and offices.
The HVAC system is a VAV system.
Overall window-to-wall ratio is 40%."""

robust_prompt_124 = f"""Simulate a six-story rectangular dormitory building.
The HVAC system is a heat pump system.
WWR is 30% overall.
Cooling 25°C, heating 20°C.
Residential schedule with nighttime occupancy."""

robust_prompt_125 = f"""Model a twelve-story rectangular office tower.
The HVAC system is a VRF system with heat recovery.
WWR is 50% on south, 35% elsewhere.
Cooling 24°C, heating 21°C.
Office operates 8am–6pm weekdays."""

robust_prompt_126 = f"""Model a 4-story rectangular office building with a VAV HVAC system.
The window-to-wall ratio is 30% on east and west façades, 50% on south, and 25% on north.
Exterior walls are steel-framed with mineral wool insulation.
Office spaces have equipment loads of 8 W/m² and lighting power density of 7 W/m².
Cooling setpoint 24°C, heating 20°C.
Occupied 8am-6pm on weekdays."""

robust_prompt_127 = f"""Simulate a 5-story L-shaped office building.
Each story has 2 zones.
Space type: office with people 5 m²/person, equipment 11 W/m², lighting 8.5 W/m².
WWR is 42% overall with triple-pane glazing.
HVAC system is VAV with electric reheat.
Exterior walls are insulated concrete panels."""

robust_prompt_128 = f"""Model a 3-story hollow square academic building.
First floor classrooms: people 2 m²/person, equipment 10 W/m², lighting 9 W/m².
Upper floors offices: people 4 m²/person, equipment 5 W/m², lighting 7 W/m².
WWR 35% east/west, 25% north, 45% south.
Exterior walls brick with interior insulation (U-value = 0.45 W/m²K).
HVAC: heat pump packaged rooftop units with gas heating.
Occupied 9am-5pm weekdays."""

robust_prompt_129 = f"""Model a 2-story rectangular laboratory building.
HVAC system: fan coil units with 100% outdoor air.
WWR limited to 20% on all façades.
Exterior walls precast concrete (U=0.38 W/m²K).
Cooling setpoint 23°C, heating 21°C.
Occupied 7am-7pm weekdays."""

robust_prompt_130 = f"""Simulate a seven-story linear bar shaped residential building.
Each story has 5 zones with dorm rooms and common rooms.
Dorm rooms: people 10 m²/person, equipment 6 W/m², lighting 5 W/m².
Common rooms: people 3 m²/person, equipment 8 W/m², lighting 8 W/m².
HVAC: heat pump system.
WWR 30% overall, EIFS with high insulation.
Cooling 25°C, heating 20°C, residential nighttime occupancy schedule."""

robust_prompt_131 = f"""Model a 10-story hollow square office building with central core.
HVAC system is VRF with heat recovery.
WWR 50% south façade, 35% on other orientations.
Glass curtain wall with low-e double glazing.
Cooling 24°C, heating 21°C during 8am-6pm weekdays."""

robust_prompt_132 = f"""Simulate a four-story U-shaped office building.
HVAC: packaged rooftop VAV system with gas reheat.
Overall WWR 30%.
Exterior walls insulated concrete panels.
Office spaces: equipment 10 W/m², lighting 9 W/m².
Cooling 24°C, heating 20°C on weekday schedule."""

robust_prompt_133 = f"""Model a 12-story rectangular office building in cold climate.
HVAC: central chilled water plant with VAV reheat.
WWR 35% with high performance glazing.
Standard office occupancy density 0.09 people/m².
Equipment 11 W/m², lighting 8.5 W/m².
Cooling 24°C occupied / 28°C unoccupied, heating 21°C occupied / 16°C unoccupied."""

robust_prompt_134 = f"""Simulate a three-story L-shaped municipal building.
HVAC: VAV system with hot water reheat from gas boilers, chilled water from electric chillers (6°C supply).
WWR 40% overall with double-pane low-e glazing.
Cooling setpoint 24°C, heating 20°C.
Weekday occupancy 8am-6pm."""

robust_prompt_135 = f"""Model a six-story T-shaped mixed-use building.
HVAC: fan coil units served by dedicated outdoor air system (DOAS).
Office zones: 0.1 people/m², 12 W/m² equipment, 8 W/m² LED lighting.
Retail zones: 9am-9pm operation.
Average WWR 35%.
Exterior walls steel-framed with mineral wool insulation."""

robust_prompt_136 = f"""Simulate a 5-story rectangular office building.
HVAC: VAV system with economizers enabled.
Average WWR 38%.
Office spaces operate 8am-6pm weekdays.
Equipment loads 10 W/m², lighting power density 9 W/m².
Exterior walls brick with good insulation.
Cooling 24°C, heating 21°C."""

robust_prompt_137 = f"""Model a four-story rectangular hospital outpatient building.
Total 20 thermal zones with exam rooms, offices, waiting areas.
Exam rooms: 3 m²/person, 15 W/m² equipment, 10 W/m² lighting.
Offices: 5 m²/person, 8 W/m² equipment, 7 W/m² lighting.
Waiting areas: 2 m²/person, 3 W/m² equipment, 6 W/m² lighting.
WWR 40% south, 30% east/west, 20% north.
Insulated precast concrete walls (U=0.38 W/m²K).
VAV with hot water reheat and air-cooled chiller.
Occupied 7am-7pm weekdays, cooling 23°C, heating 21°C."""

robust_prompt_138 = f"""Simulate a 3-story U-shaped office building.
HVAC: VAV system.
WWR 45% south façade, 25% on other orientations.
Exterior walls brick with good insulation.
Office equipment 10 W/m², lighting 9 W/m².
Cooling 24°C, heating 20°C on typical weekday schedule."""

robust_prompt_139 = f"""Model a six-story L-shaped office building with perimeter and core zones.
HVAC: VAV system with electric reheat.
Occupant density 0.09 people/m², lighting 8.5 W/m², equipment 11 W/m².
Overall WWR 42% with triple-pane glazing.
Cooling setpoint 24°C, heating 20°C during occupied hours."""

robust_prompt_140 = f"""Simulate a medium-size 3-story rectangular office building.
HVAC: VAV system.
Moderate WWR 40%, standard insulation (brick with interior insulation U=0.45 W/m²K).
Typical weekday office schedule 8am-6pm.
Cooling 24°C, heating 20°C.
Office loads: 5 W/m² equipment, 7 W/m² lighting, 4 m²/person occupancy."""

robust_prompt_141 = f"""Simulate a 4-story hollow square building.
HVAC: packaged rooftop VAV system with gas reheat.
Overall WWR 30%.
Façade: insulated concrete panels.
Cooling setpoint 24°C, heating 21°C.
Weekday occupancy 8am-6pm.
Office equipment 10 W/m², lighting 9 W/m²."""

robust_prompt_142 = f"""Simulate a 10-story rectangular office tower with central core.
HVAC: VRF system with heat recovery.
WWR 50% south façade, 35% elsewhere.
Glass curtain wall with low-e double glazing.
Cooling 24°C, heating 21°C during 8am-6pm weekdays.
Office occupancy density 0.15 people/m², equipment 10 W/m², lighting 9 W/m²."""

robust_prompt_143 = f"""Simulate a five-story rectangular office building.
The HVAC system is a VAV system with hot water reheat.
Cooling setpoint is 24°C and heating setpoint is 20°C.
Office hours are 8am–6pm on weekdays.
WWR is 40% overall.
Exterior walls are brick with interior insulation."""

robust_prompt_144 = f"""Model a four-story U-shaped office building.
The HVAC system is a packaged rooftop VAV system with gas reheat.
Overall window-to-wall ratio is 32%.
Exterior walls are insulated concrete panels.
Cooling 24°C, heating 21°C."""

robust_prompt_145 = f"""Simulate a six-story T-shaped office building.
The HVAC system is a VAV system with electric reheat.
WWR is 42% overall.
Triple-pane glazing.
Cooling 24°C, heating 20°C."""

robust_prompt_146 = f"""Model a three-story rectangular school building.
Each story has 5 zones.
Classrooms operate from 8am to 4pm.
Occupancy density is 0.16 people/m².
The HVAC system is a heat pump packaged rooftop unit.
WWR is 38% overall."""

robust_prompt_147 = f"""Simulate a nine-story rectangular office building.
The HVAC system is a VRF system with heat recovery.
Cooling 24°C, heating 21°C.
Office hours 8am–6pm weekdays.
Window-to-wall ratio is 36%.
Exterior walls are steel-framed with mineral wool."""

robust_prompt_148 = f"""Model a five-story hollow square office building.
The HVAC system is a VAV system with electric reheat.
WWR is 45% on south, 30% elsewhere.
Lighting power density is 8.5 W/m²."""

robust_prompt_149 = f"""Simulate a seven-story linear residential building.
The HVAC system is a heat pump system.
WWR is 48% on south, 32% elsewhere.
Exterior walls are EIFS with high thermal resistance.
Cooling 25°C, heating 20°C."""

robust_prompt_150 = f"""Model a four-story rectangular hospital outpatient building.
The HVAC system is VAV with hot water reheat.
Cooling setpoint 23°C, heating 21°C.
WWR is 33% overall.
Exterior walls are insulated precast concrete."""

robust_prompt_151 = f"""Simulate a six-story L-shaped office building.
The HVAC system is a VAV system.
WWR is 41% overall.
Exterior walls are brick with interior insulation.
Cooling 24°C, heating 20°C."""

robust_prompt_152 = f"""Model a three-story U-shaped municipal building.
The HVAC system is a VAV system with electric reheat.
Overall window-to-wall ratio is 34%.
Double-pane low-e glazing."""

robust_prompt_153 = f"""Model a seven-story T-shaped office building.
The HVAC system is a packaged rooftop VAV system with gas reheat.
Overall window-to-wall ratio is 29%.
Exterior walls are steel-framed with mineral wool."""

robust_prompt_154 = f"""Simulate a two-story laboratory building.
The HVAC system is fan coil units with 100% outdoor air.
WWR is limited to 22%.
Exterior walls are precast concrete."""

robust_prompt_155 = f"""Model an eight-story L-shaped office building.
The HVAC system is a VAV system with economizers.
WWR is 39% overall.
Cooling 24°C, heating 20°C."""

robust_prompt_156 = f"""Simulate a ten-story rectangular office building.
The HVAC system is a central chilled water VAV system with reheat.
WWR is 36% overall.
Cooling 24°C, heating 21°C."""

robust_prompt_157 = f"""Model a four-story hollow square academic building.
Space types: classrooms and offices.
The HVAC system is a VAV system.
Overall window-to-wall ratio is 43%."""

robust_prompt_158 = f"""Simulate a six-story rectangular dormitory building.
The HVAC system is a heat pump system.
WWR is 32% overall.
Cooling 25°C, heating 20°C.
Residential schedule with nighttime occupancy."""

robust_prompt_159 = f"""Model a 5-story rectangular office building with a VAV HVAC system.
WWR is 35% on east and west façades, 25% on north, and 50% on south.
Exterior walls are brick with good insulation.
Office spaces: people 4 m²/person, equipment 10 W/m², lighting 9 W/m².
Cooling setpoint 24°C, heating 21°C during 8am-6pm weekdays."""

robust_prompt_160 = f"""Simulate a 3-story L-shaped academic building.
First floor classrooms: people 2 m²/person, equipment 10 W/m², lighting 9 W/m².
Second and third floors offices: people 4 m²/person, equipment 5 W/m², lighting 7 W/m².
HVAC: heat pump packaged rooftop units with gas heating.
WWR 40% south, 30% east/west, 25% north.
Exterior walls brick with interior insulation (U-value = 0.45 W/m²K).
Occupied 9am-5pm weekdays."""

robust_prompt_161 = f"""Model a 6-story hollow square office building with central core.
HVAC system is VAV with hot water reheat supplied by gas boilers.
WWR 45% south façade, 30% on other orientations.
Exterior walls insulated concrete panels.
Office occupancy 0.1 people/m², equipment 11 W/m², lighting 8.5 W/m².
Cooling 24°C, heating 20°C on 8am-6pm weekday schedule."""

robust_prompt_162 = f"""Model a 2-story rectangular laboratory building.
HVAC: fan coil units with 100% outdoor air.
WWR 20% on all façades.
Exterior walls precast concrete (U=0.38 W/m²K).
Cooling setpoint 23°C, heating 21°C.
Occupied 8am-6pm weekdays."""

robust_prompt_163 = f"""Simulate a 7-story linear bar shaped residential building.
Each story has 5 zones with dorm rooms and common rooms.
Dorm rooms: people 10 m²/person, equipment 6 W/m², lighting 5 W/m².
Common rooms: people 3 m²/person, equipment 8 W/m², lighting 8 W/m².
HVAC: heat pump system.
WWR 35% overall, EIFS with high insulation.
Cooling 25°C, heating 20°C with residential nighttime occupancy schedule."""

robust_prompt_164 = f"""Model a 10-story rectangular office tower with central core.
HVAC: VRF system with heat recovery.
WWR 45% south façade, 30% elsewhere.
Glass curtain wall with low-e double glazing.
Cooling 24°C, heating 21°C during 8am-6pm weekdays.
Office occupancy density 0.15 people/m²."""

robust_prompt_165 = f"""Simulate a 5-story L-shaped office building.
HVAC: packaged rooftop VAV system with gas reheat.
Overall WWR 35%.
Exterior walls insulated concrete panels.
Office spaces: equipment 10 W/m², lighting 9 W/m².
Cooling 24°C, heating 20°C on weekday schedule 8am-6pm."""

robust_prompt_166 = f"""Model a 12-story rectangular office building in cold climate.
HVAC: central chilled water plant with VAV reheat.
WWR 40% with high performance glazing.
Office occupancy 0.09 people/m².
Equipment 11 W/m², lighting 8.5 W/m².
Cooling 24°C occupied / 28°C unoccupied, heating 21°C occupied / 16°C unoccupied.
Weekday schedule 8am-6pm."""

robust_prompt_167 = f"""Simulate a 3-story rectangular municipal building.
HVAC: VAV system with hot water reheat from gas boilers.
Chilled water supplied by electric chillers at 6°C.
WWR 38% overall with double-pane low-e glazing.
Cooling setpoint 24°C, heating 20°C.
Occupied 8am-6pm weekdays."""

robust_prompt_168 = f"""Model a 6-story T-shaped mixed-use building with office and retail spaces.
HVAC: fan coil units served by dedicated outdoor air system (DOAS).
Office spaces: 0.1 people/m² occupancy, 12 W/m² plug loads, 8 W/m² LED lighting.
Retail operates 9am-9pm, office 8am-6pm.
Average WWR 40%.
Exterior walls steel-framed with mineral wool insulation."""

robust_prompt_169 = f"""Simulate a 4-story rectangular academic building.
Each floor has 5 zones with classrooms, offices, and corridors.
Classrooms: 9am-5pm operation, occupancy 0.15 people/m².
Offices: standard weekday schedule 8am-6pm.
HVAC: VAV system with economizers enabled.
Average WWR 35%.
Exterior walls brick with good insulation."""

robust_prompt_170 = f"""Model a 4-story rectangular hospital outpatient building.
Total 20 thermal zones including exam rooms, offices, waiting areas.
Exam rooms: 3 m²/person, 15 W/m² equipment, 10 W/m² lighting.
Offices: 5 m²/person, 8 W/m² equipment, 7 W/m² lighting.
Waiting areas: 2 m²/person, 3 W/m² equipment, 6 W/m² lighting.
WWR 35% south, 30% east/west, 25% north.
Insulated precast concrete walls (U=0.38 W/m²K).
VAV with hot water reheat and air-cooled chiller.
Occupied 7am-7pm weekdays."""

robust_prompt_171 = f"""Simulate a 3-story U-shaped office building.
HVAC: VAV system.
WWR 50% south façade, 30% on other orientations.
Exterior walls brick with good insulation.
Office equipment 10 W/m², lighting 9 W/m².
Cooling 24°C, heating 21°C on typical weekday schedule 8am-6pm."""

robust_prompt_172 = f"""Model a 6-story L-shaped office building with perimeter and core zones.
HVAC: VAV system with electric reheat.
Occupant density 0.1 people/m², lighting 8 W/m², equipment 12 W/m².
Overall WWR 40% with triple-pane glazing.
Cooling setpoint 24°C, heating 20°C during occupied hours.
Weekday schedule 8am-6pm."""

robust_prompt_173 = f"""Simulate a medium-size 4-story rectangular office building.
HVAC: VAV system.
Moderate WWR 38%, standard insulation (brick with interior insulation U=0.45 W/m²K).
Typical weekday office schedule 8am-6pm.
Cooling 24°C, heating 20°C.
Office loads: 5 W/m² equipment, 7 W/m² lighting, 4 m²/person occupancy."""

robust_prompt_174 = f"""Simulate a 4-story hollow square building.
HVAC: packaged rooftop VAV system with gas reheat.
Overall WWR 35%.
Façade: insulated concrete panels.
Cooling setpoint 24°C, heating 21°C.
Weekday occupancy 8am-6pm.
Office equipment 11 W/m², lighting 8.5 W/m²."""

robust_prompt_175 = f"""Simulate a five-story rectangular office building.
The building uses a VAV system with economizer.
WWR is around 38% overall, slightly higher on south façade.
Exterior walls are brick with moderate insulation.
Cooling setpoint is 24C, heating is about 20C.
Weekday ocupancy from 8am to 6pm."""

robust_prompt_176 = f"""Model a 3-story U-shaped municipal building.
It uses a VRF system with heat recovery.
South WWR 45%, north maybe 25%, east/west 30%.
Double pane glazing, good insulation.
Office hours are standard weekdays."""

robust_prompt_177 = f"""Model a five story T-shaped office building.
HVAC is VAV with electric reheat.
Occupancy is typical office, lighting about 8 W/m2.
WWR is 35% overall with low-e glazing.
Cooling setpoint 24, heating 20."""

robust_prompt_178 = f"""Simulate a 7-story L-shape residential building.
Each floor has around 2 zones.
HVAC system is heat pump.
WWR 50% south, 30% other sides.
EIFS walls with high insulation."""

robust_prompt_179 = f"""Model a four-story rectangular laboratory building.
It uses FCU with 100% outside air.
WWR is limited to about 22%.
Exterior walls are precast concrete.
Schedules are mostly daytime."""

robust_prompt_180 = f"""Simulate a ten story rectangular office building with central core.
HVAC system is VRF.
Cooling setpoint 24°C, heating 21°C.
Office operates 8am–6pm weekdays.
WWR is around 42%."""

robust_prompt_181 = f"""Model a 6-story U-shaped office building.
The HVAC is VAV with hot water reheat.
WWR: 30% north, 45% south, 35% east/west.
Brick wall with interior insulation."""

robust_prompt_182 = f"""Simulate a 3-story rectangular school building.
Each floor has 5 zones.
Space types are classroom and office.
HVAC system is packaged heat pump.
Occupied 8am–4pm on weekdays."""

robust_prompt_183 = f"""Model a four story hollow-square office building.
HVAC is rooftop VAV with gas reheat.
WWR is 30%.
Insulated concrete panels.
Office schedule on weekdays."""

robust_prompt_184 = f"""Model a 10-story office tower.
Rectangular shape, central core.
HVAC is VRF with heat recovery.
WWR 50% south, 35% other.
Office hours weekdays."""

robust_prompt_185 = f"""Model a six story U-shaped office building.
HVAC is VAV with economizer.
Lighting is around 9 W/m2, equipment 10 W/m2.
WWR is approx 38%."""

robust_prompt_186 = f"""Simulate a 12-story rectangular mixed-use office building.
HVAC is central chilled water with VAV reheat.
WWR is about 35%.
Efficient lighting, weekday schedule."""

robust_prompt_187 = f"""Model a 5-story rectangular office building.
HVAC system is VAV.
Moderate glazing, standard insulation.
Cooling 24, heating 20.
Office schedule on weekdays."""

robust_prompt_188 = f"""Simulate a four-story rectangluar office building.
HVAC is a VAV system, probably with reheat.
WWR is about 35%, maybe a bit higher on south.
Exterior walls have standard insulation.
Typical weekday scheduel."""

robust_prompt_189 = f"""Model a six story L-shaped academic building.
Space types: classroom and ofice.
HVAC is VAV with economzier.
WWR is roughly 40%.
Occupied during normal school hours."""

robust_prompt_190 = f"""Simulate a 5-story hollow sqaure office building.
The HVAC system is rooftop VAV.
Overall WWR is around 32%.
Facade has moderate insulation.
Cooling about 24C, heating maybe 20C."""

robust_prompt_191 = f"""Model a three-story U-shape municipal building.
It uses VRF with heat recovry.
WWR maybe 45% south, 30% elsewhere.
Office hours are kind of standard."""

robust_prompt_192 = f"""Simulate a seven-story residential bulding.
HVAC is heat pumpp system.
WWR is approx 30% overall.
High insulation, or something similar."""

robust_prompt_193 = f"""Model a 4-story rectangluar laboratory building.
It uses FCU with 100% outdoor air.
WWR is limitted to about 20%.
Walls are precast concrte.
Mostly daytime opertaion."""

robust_prompt_194 = f"""Simulate a ten story central-core ofice building.
HVAC is VRF.
Cooling setpoint is 24C, heating about 21.
WWR is roughly 42%.
Typical weekday use."""

robust_prompt_195 = f"""Model a five story T-shape office building.
HVAC is VAV with electric rehete.
WWR around 35%.
Lighting and equipment are standard.
Office hours are normal."""

robust_prompt_196 = f"""Simulate a 3-story school bulding.
Space types are classroom and office.
HVAC is packaged heat pump.
Occupied around 8am–4pm weekdays."""

robust_prompt_197 = f"""Simulate a 4-story hollow-sqaure office building.
HVAC is rooftop VAV with gas reheaat.
WWR is 30% overall.
Facade is insulated panel.
Standard office schedual."""

robust_prompt_198 = f"""Simulate a ten-story rectangluar hospital outpatient building.
Space types include exam rooms and ofices.
HVAC is VAV with hot water reheta.
WWR is around 35%.
Occupied most of the day."""

robust_prompt_199 = f"""Model a five story U-shape office building.
HVAC is VAV with economizer.
WWR: about 45% south, 30% north, others in between.
Brick wall with decent insulation."""

robust_prompt_200 = f"""Simulate a 12-story rectangular mixed-use ofice building.
HVAC is central chilled water with VAV reheat.
WWR is approx 35%.
Efficient lighting, normal weekday shedule."""

robust_prompt_201 = f"""Model a 3-story rectangluar academic building.
Space types are classroom and office.
HVAC is VAV.
WWR is maybe around 40%.
Standard school opertaion."""

robust_prompt_202 = f"""Simulate a 7-story L-shape residential building.
HVAC is heat pump.
WWR 50% south, 30% other sides.
Good insulation, not very specifc."""

robust_prompt_203 = f"""Model a four-story hollow square ofice building.
HVAC is rooftop VAV.
WWR is 30%.
Insulated concrte panels.
Typical weekday office hours."""

robust_prompt_204 = f"""Simulate a 5-story rectangular office bulding.
HVAC system is VAV.
Moderate glazing, standard insulation.
Cooling 24, heating about 20.
Normal office use."""

robust_prompt_205 = f"""Model a 6-story U-shaped office building.
HVAC is VAV with hot water reheat.
WWR is around 38%.
Lighting is typical, equipment is normal.
Office runs mostly weekdays."""

robust_prompt_206 = f"""Simulate a five-story hollow square academic building.
Each floor has 4 zones with classrooms and offices.
HVAC is VAV with economizer.
Window-to-wall ratio around 35-40%.
Exterior walls are concrete with decent insulation.
Occupancy 8am-5pm weekdays."""

robust_prompt_207 = f"""Model a 2-story laboratory building with rectagular footprint.
FCU system with 100% outdoor air.
WWR limited to low values on all orientations.
Precast concrete walls.
Equipment loads are high due to lab equipment.
Cooling 22°C, heating 20°C."""

robust_prompt_208 = f"""Simulate a six-story L-shaped office building.
Perimeter and core zoning strategy.
VAV system with gas reheat.
WWR is 45% on east/west, 35% on north/south.
Steel-framed walls with mineral wool.
Office density approx 0.1 people/m²."""

robust_prompt_209 = f"""This is a 3-story hollow square shaped school building.
Each story has 4 zones.
There are 2 space types: classroom and office. 
For space 1, classroom: people 2 m²/person, equipment 10 W/m², lighting 9 W/m².
For space 2, office: people 4 m²/person, 5 W/m² equipment, 7 W/m² lighting.
First story is for space type 1, and second and third stories are for space type 2.
WWR is 35% on east and west façades, 25% on north, and 45% on south.
Exterior walls are brick with interior insulation (U-value = 0.45 W/m²K).
Cooling setpoint 24°C, heating 21°C.
Occupied 8am-4pm on weekdays.
Heating and cooling air system is heat pump packaged rooftop units with gas heating."""

robust_prompt_210 = f"""Model a four-story rectengular hospital outpatient facility.
Total 16 thermal zones.
Exam rooms, offices, waiting areas with different loads.
WWR 35% average across façades.
Insulated precast concrete walls.
VAV system with reheat coils.
Occupied 8am-6pm weekdays."""

robust_prompt_211 = f"""Simulate a 5-story mixed-use building, T-shaped.
Ground floor retail, upper floors offices.
DOAS with fan coil units.
Retail: 0.15 people/m², offices: 0.1 people/m².
WWR 50% south, 35% north.
Concrete walls with medium insulation level."""

robust_prompt_212 = f"""Model a 10-story office tower with hollow square plan.
Central core configuration.
VRF system with heat recovery capability.
WWR 48% south façade, 32% elsewhere.
Curtain wall with low-e glazing.
Standard office schedule 8am-6pm."""

robust_prompt_213 = f"""Simulate a 3-story school building, rectagular shape.
Each floor 5 zones: classrooms and corridors.
Classrooms: 2.2 m²/person density.
WWR 30% north, 40% south, 35% east/west.
Brick walls with interior insulation.
Packaged rooftop units with gas heating."""

robust_prompt_214 = f"""Simulate a 4-story laboratory building.
Rectangular footprint with 8 zones per floor.
FCU system with dedicated outdoor air.
WWR kept low at 25% average.
Precast concrete walls with vapor barrier.
High equipment loads for lab equipment."""

robust_prompt_215 = f"""Model a 8-story residential tower, linear configuration.
Each floor contains 5 residential units.
Heat pump system serving all zones.
WWR 45% on south, 30% on other orientations.
EIFS exterior with high R-value.
Nighttime occupancy predominates."""

robust_prompt_216 = f"""Simulate a five-story U-shaped office building.
VAV system with economizer cycle.
WWR 50% on south and north, 30% on east/west.
Steel stud walls with batt insulation.
Office equipment loads about 11 W/m².
Cooling 24°C, heating setback to 16°C unoccupied."""

robust_prompt_217 = f"""Simulate a six-story L-shaped mixed-use building.
Lower floors retail, upper floors offices.
Fan coil units with DOAS.
Retail WWR 40%, office WWR 35%.
Concrete frame with brick veneer.
Retail 10am-8pm, office 8am-6pm schedules."""

robust_prompt_218 = f"""Model a 12-story rectengular office tower in cold climate.
Central plant with VAV reheat terminals.
WWR 38% with high-performance glazing.
Exterior walls have suitable insulation for climate.
Standard office occupancy and efficient lighting.
Setback temperatures during nights and weekends."""

robust_prompt_219 = f"""Simulate a 4-story hollow square municipal building.
VAV system with hot water reheat.
Chilled water plant with 6.5°C supply.
WWR 42% overall with double low-e glazing.
Office occupancy density 0.085 people/m²."""

robust_prompt_220 = f"""Model a 6-story dormitory building, L-shaped plan.
Space types: student rooms and common areas.
Student rooms: 8 m²/person, common areas: 4 m²/person.
Heat pump HVAC system.
WWR around 32% average.
EIFS walls with continous insulation.
Residential schedule with 24-hour occupancy."""

robust_prompt_221 = f"""Simulate a 5-story rectengular office building with central core.
VAV system with hot water reheat.
WWR is moderatly high on south façade.
Exterior walls have decent insullation performance.
Cooling setpoint around 24°C, heating approx 20°C.
Typical weekday schudule 8am-6pm."""

robust_prompt_222 = f"""Simulate a four-story hollow square academic facility.
HVAC is VAV with economizer feature.
Window-to-wall ratio somewhere between 35-40%.
Concrete walls with acceptable insulation level.
Occupancy during daytime hours on weekdays."""

robust_prompt_223 = f"""Model a 2-story laboratory building with rectagular plan.
FCU system with 100% outdoor air supply.
WWR kept relatively low on all orientations.
Precast concrete walls with vapor barrrier.
Equipment loads are quite high for labs.
Cooling setpoint 22°C, heating around 20°C."""

robust_prompt_224 = f"""Simulate a six-story L-shaped office tower.
Perimeter and core zoning approach.
VAV system with electric reheat coils.
WWR approx 42% east/west, 38% north/south.
Steel-framed walls with mineral wool batts.
Occupant density roughly 0.1 people/m²."""

robust_prompt_225 = f"""Model a 8-story residential building with linear bar shape.
Heat pump system for space conditioning.
WWR about 50% on south, 35% elsewhere.
EIFS walls with good thermal resistence.
Residential schudule with evening occupancy peaks."""

robust_prompt_226 = f"""Model a four-story rectengular hospital outpatient center.
Total zones around 20 thermal zones.
Exam rooms, offices, waiting areas with varing loads.
WWR average about 35% across all façades.
Insullated precast concrete exterior walls.
VAV system with reheat capability.
Occupied roughly 7am-7pm weekdays."""

robust_prompt_227 = f"""Simulate a 5-story mixed-use building, T-shaped plan.
Ground floor retail, floors above for offices.
DOAS coupled with fan coil terminal units.
Retail occupancy approx 0.15 people/m².
WWR 52% south façade, 33% north side.
Concrete walls with medium-grade insulation."""

robust_prompt_228 = f"""Model a 10-story office tower with hollow square layout.
Central core serving perimeter zones.
VRF system with heat recovery function.
WWR 47% on south, 33% on other façades.
Glass curtain wall with low-e coating.
Standard office hours 8am-6pm weekdays."""

robust_prompt_229 = f"""Model an 8-story residential building.
WWR 60% south, 40% other façades. Residential occupancy pattern with higher nighttime presence."""

robust_prompt_230 = f"""I want to simulate a 4 story medium-size rectangular office building.
Only one space type: office room
It should use a VRF system with heat recovery.
The building has moderate window-to-wall ratio of 0.45 and good insulation.
Typical weekday office schedules, with cooling at 23°C and heating at 21°C."""

robust_prompt_231 = f"""Model a 4-story U-shaped office building with a VAV HVAC system with economizer.
The window-to-wall ratio is 50% on the south façade and 30% on other orientations.
The building contains 3 space types: office, conference, corridor.
Exterior walls are brick with high insulation."""

robust_prompt_232 = f"""Model a three-story laboratory building with a rectangular footprint.
The building uses a fan coil unit (FCU) system with 80% outdoor air.
Exterior walls are precast concrete with additional insulation, and the window-to-wall ratio is limited to 25%."""

robust_prompt_233 = f"""Simulate a six-story U-shaped office building.
The east and west façades have a window-to-wall ratio of 35%, 
while the north and south façades have 55%.
Exterior walls are steel-framed with high-performance mineral wool insulation.
Office spaces have equipment loads of 12 W/m² and lighting power density of 10 W/m²."""

robust_prompt_234 = f"""Model a 4-story academic building consisting of classrooms, offices, and corridors.
Classrooms operate from 8:30 to 16:30 with an occupancy density of 0.18 people/m².
Offices follow a standard weekday schedule from 8:00 to 19:00.
The HVAC system is a VAV system with hot water reheat.
The average window-to-wall ratio is 40%."""

robust_prompt_235 = f"""Simulate an eight-story residential building with a linear bar shape.
The building uses a heat pump system with heat recovery.
The window-to-wall ratio is 55% on the south façade and 35% elsewhere.
Exterior walls are EIFS with ultra-high thermal resistance."""

robust_prompt_236 = f"""Simulate a seven-story L-shaped office building with a VAV HVAC system and a window-to-wall ratio of 45%."""

robust_prompt_237 = f"""Simulate a five-story rectangular building. 
The building uses a packaged rooftop VAV system with electric reheat. 
Overall window-to-wall ratio is 35%, and the façade is insulated concrete panels with enhanced thermal performance."""

robust_prompt_238 = f"""Simulate a five-story hollow square building. 
The building uses a packaged rooftop VAV system with electric reheat. 
Overall window-to-wall ratio is 35%, and the façade is insulated concrete panels with stone cladding."""

robust_prompt_239 = f"""Simulate a seven-story T-shaped mixed-use building with office and retail spaces.
The HVAC system consists of fan coil units served by a dedicated outdoor air system (DOAS).
Office spaces have an occupant density of 0.12 people/m², plug loads of 14 W/m²,
and LED lighting with a lighting power density of 9 W/m².
The average window-to-wall ratio is 40%."""

robust_prompt_240 = f"""Simulate a four-story L-shaped municipal building.
The HVAC system is a VAV system with hot water reheat supplied by gas boilers.
Chilled water is provided by electric chillers with a supply temperature of 7°C.
The window-to-wall ratio is 45% overall, with triple-pane low-e glazing."""

robust_prompt_241 = f"""Model a seven-story L-shaped office building with perimeter and core zones.
The HVAC system is a VAV system with hot water reheat.
Cooling setpoint is 23.5°C and heating setpoint is 21°C during occupied hours.
Occupant density is 0.11 people/m², lighting power density is 9 W/m²,
and equipment power density is 13 W/m².
The overall window-to-wall ratio is 45%, using triple-pane glazing with argon fill."""

robust_prompt_242 = f"""I want to simulate a medium-size rectangular office building with 5 stories.
It should use a VAV system with economizer.
The building has moderate window-to-wall ratio of 0.42 and enhanced insulation.
Typical weekday office schedules with extended hours 7am–7pm, with cooling at 23.5°C and heating at 21°C."""

robust_prompt_243 = f"""Simulate a 10-story rectangular mixed-use office building in a cold climate, using a central chilled water plant with VAV reheat and heat recovery.
Use a window-to-wall ratio of 40%, with triple-pane high performance glazing. 
Enhanced construction and insulation
Standard office occupancy with extended hours, efficient lighting, and weekday schedules 7am–7pm."""

robust_prompt_244 = f"""Simulate a five-story rectangular hospital outpatient building.
The building has a total of 25 thermal zones.
Space types: exam rooms, offices, waiting areas.
Exam rooms: people 2.5 m²/person, equipment 18 W/m², lighting 12 W/m².
Offices: people 4.5 m²/person, equipment 10 W/m², lighting 8 W/m².
Waiting areas: people 1.8 m²/person, equipment 4 W/m², lighting 7 W/m².
WWR is 45% south, 35% east/west, 25% north.
Exterior walls are insulated precast concrete (U=0.32 W/m²K).
Cooling setpoint 22.5°C, heating 21.5°C.
Occupied 6:30am–8pm weekdays.
HVAC system is VAV with hot water reheat and water-cooled chiller."""

robust_prompt_245 = f"""Simulate a 12-story office tower, hollow square with a central core.
HVAC system is a VRF system with heat recovery.
WWR is 55% on south, 40% elsewhere.
Glass curtain wall with triple-pane low-e glazing.
Cooling 23.5°C, heating 21.5°C.
Office hours 7:30am–7pm weekdays."""

robust_prompt_246 = f"""Simulate a six-story U-shaped hotel.
People 18 m²/person, equipment 5 W/m², lighting 7 W/m².
PTAC units with heat pump heating.
WWR 50% south, 35% other façades.
Occupied 24 hours with varying occupancy patterns."""

robust_prompt_247 = f"""Model a three-story retail strip mall with a linear bar shape.
HVAC system is packaged rooftop units with DX cooling and electric heating.
WWR 65% front façade, 20% back.
Glass storefronts with thermally broken metal framing.
Occupied 9am–11pm daily."""

robust_prompt_248 = f"""Model a four-story elementary school with an L-shaped footprint.
HVAC is heat pump with heat recovery.
WWR 40% south, 30% north, 35% east/west.
Brick walls with enhanced interior insulation.
Occupied 7:30am–3:30pm weekdays."""

robust_prompt_249 = f"""Model a five-story medical research laboratory.
HVAC system is 100% outdoor air VAV with enthalpy wheel heat recovery.
WWR 25% overall.
Precast concrete façade with enhanced insulation.
Cooling 21.5°C, heating 20.5°C.
Occupied 24 hours with high ventilation requirements."""

robust_prompt_250 = f"""Model a four-story community center with a courtyard (hollow square).
HVAC is packaged rooftop heat pump units with economizers.
WWR 45% south, 25% north.
Occupied 8am–10pm with weekend operation."""

robust_prompt_251 = f"""Simulate a three-story industrial office + warehouse building.
Office zones: people 5 m²/person, lighting 8 W/m², equipment 10 W/m².
Warehouse zones: lighting 5 W/m², equipment 8 W/m².
HVAC: VAV rooftop units for office, radiant heaters for warehouse.
WWR 20% with enhanced glazing on office façade."""

robust_prompt_252 = f"""Model a 7-story residential building.
WWR 60% south, 30% other façades. Residential occupancy pattern."""

ROBUST_PROMPTS = {
    k: v for k, v in globals().items()
    if k.startswith("robust_prompt_")
}