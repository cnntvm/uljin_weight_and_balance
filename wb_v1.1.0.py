import math
import matplotlib.pyplot as plt
print("")
print("")
print("[ULJIN KOREA AERO SPACE UNIV]")
print("")
print("[WEIGHT AND BALANCE / PERFORMANCE] [ver 1.1.0]")
print("")
print("")

REG = input("항공기 등록기호? (숫자만 입력)   : ")
if int(REG) == 1081 or int(REG) == 1082:
    BEW_WEI = 1686.54 
    BEW_ARM = 39.197
    BEW_MOMENT = 66108
    
elif int(REG) == 1086 or int(REG) == 1087:
    BEW_WEI = 1679.7
    BEW_ARM = 39.678
    BEW_MOMENT = 66647

elif int(REG) == 1131 or int(REG) == 1132 or int(REG) == 1134 or int(REG) == 1135:
    BEW_WEI = 1716.3
    BEW_ARM = 41.080
    BEW_MOMENT = 70506
    
elif int(REG) == 1136:
    BEW_WEI = 1715.5
    BEW_ARM = 40.945
    BEW_MOMENT = 70240

elif int(REG) == 1171:
    BEW_WEI = 1685.7
    BEW_ARM = 40.873
    BEW_MOMENT = 68899

elif int(REG) == 1172:
    BEW_WEI = 1688.1
    BEW_ARM = 40.876
    BEW_MOMENT = 69002

elif int(REG) == 1173 or int(REG) == 1175:
    BEW_WEI = 1700.5
    BEW_ARM = 41.486
    BEW_MOMENT = 70548

elif int(REG) == 1174:
    BEW_WEI = 1697.3
    BEW_ARM = 41.287
    BEW_MOMENT = 70078

elif int(REG) == 1221:
    BEW_WEI = 1695.8
    BEW_ARM = 41.287
    BEW_MOMENT = 70013

elif int(REG) == 1222:
    BEW_WEI = 1669.1
    BEW_ARM = 40.488
    BEW_MOMENT = 67579

elif int(REG) == 1223:
    BEW_WEI = 1706.5
    BEW_ARM = 42.094
    BEW_MOMENT = 71834

elif int(REG) == 2035:
    print("해당 항공기는 아직 지원하지 않습니다. 프로그램을 종료해주세요.")

else:
    BEW_WEI = 0
    BEW_ARM = 0
    BEW_MOMENT = 0
    print("입력오류, 프로그램 종료 후 다시 실행하세요.")
    print("")

if int(REG) == 1081 or int(REG) == 1082 or int(REG) == 1086 or int(REG) == 1087:
    print("C172R")
elif int(REG) == 1131 or int(REG) == 1132 or int(REG) == 1134 or int(REG) == 1135 or int(REG) == 1136 or int(REG) == 1171 or int(REG) == 1172 or int(REG) == 1173 or int(REG) == 1174 or int(REG) == 1175 or int(REG) == 1221 or int(REG) == 1222 or int(REG) == 1223:
    print("C172S")

FRONT_WEI = input("앞좌석 무게?(숫자만 입력/파운드)   : ")
FRONT_MOMENT = float(FRONT_WEI) * 37
REAR_WEI = input("뒷자석 무게?(숫자만 입력/파운드)   : ")
REAR_MOMENT = float(REAR_WEI) * 73
GAL1 = input("연료는 몇 갤런?(숫자만 입력/갤런)   : ")
FUEL1_WEI = 6*float(GAL1)
FUEL1_MOMENT = float(FUEL1_WEI) * 48
BAG1 = input("BAGGAGE AREA 1에 '추가로' 적재할 무게? (숫자만 입력/0입력시 5 적용/파운드)   : ")
BAG1_WEI = float(BAG1) + 5
BAG1_MOMENT = float(BAG1_WEI) * 95
BAG2 = input("BAGGAGE AREA 2에 '추가로' 적재할 무게? (숫자만 입력/0입력시 7 적용/파운드)   : ")
BAG2_WEI = float(BAG2) + 7
BAG2_MOMENT = float(BAG2_WEI) * 123
RAM_WEI = float(BEW_WEI)+float(FRONT_WEI)+float(REAR_WEI)+float(FUEL1_WEI)+float(BAG1_WEI)+float(BAG2_WEI)
RAM_MOMENT = float(BEW_MOMENT)+float(FRONT_MOMENT)+float(REAR_MOMENT)+float(FUEL1_MOMENT)+float(BAG1_MOMENT)+float(BAG2_MOMENT)
RAM_ARM = float(RAM_MOMENT) / float(RAM_WEI)
if int(REG) == 1081 or int(REG) == 1082 or int(REG) == 1086 or int(REG) == 1087:
    TAXI_WEI = 7.0
else:
    TAXI_WEI = 8.4

TAXI_MOMENT = float(TAXI_WEI) * 48
TOW_WEI = float(RAM_WEI) - float(TAXI_WEI)
TOW_MOMENT = float(RAM_MOMENT) - float(TAXI_MOMENT)
TOW_ARM = float(TOW_MOMENT)/float(TOW_WEI)
    
GAL2 = input("비행 소모 연료량은 몇 갤런? (숫자만 입력/갤런)   : ")
FUEL2_WEI = float(GAL2) * 6
FUEL2_MOMENT = float(FUEL2_WEI) * 48

LDW_WEI = float(TOW_WEI) - float(FUEL2_WEI)
LDW_MOMENT = float(TOW_MOMENT) - float(FUEL2_MOMENT)
LDW_ARM = float(LDW_MOMENT) / float(LDW_WEI)

for i in range(74):
    print("-",end='')
print("")
print("{0: <25}".format("[ITEM]"),end='')
print("{0: <20}".format("[WEIGHT]"),end='')
print("{0: <20}".format("[ARM]"),end='')
print("{0: <20}".format("[MOMENT]"))

print("{0: <25}".format("BASIC EMPTY WEIGHT"),end='')
print("{0: <20,}".format(BEW_WEI),end='')
print("{0: <20,}".format(BEW_ARM),end='')
print("{0: <20,}".format(BEW_MOMENT))

print("{0: <25}".format("PILOT-CO- PILOT SEAT"),end='')
print("{0: <20,}".format(float(FRONT_WEI)),end='')
print("{0: <20}".format(37),end='')
print("{0: <20,}".format(FRONT_MOMENT))

print("{0: <25}".format("REAR PASSENGER"),end='')
print("{0: <20,}".format(float(REAR_WEI)),end='')
print("{0: <20}".format(73),end='')
print("{0: <20,}".format(REAR_MOMENT))

print("{0: <25}".format("FUEL"),end='')
print("{0: <20,}".format(round(FUEL1_WEI,1)),end='')
print("{0: <20}".format(48),end='')
print("{0: <20,}".format(round(FUEL1_MOMENT,1)))

print("{0: <25}".format("BAGGAGE AREA1"),end='')
print("{0: <20,}".format(BAG1_WEI),end='')
print("{0: <20}".format(95),end='')
print("{0: <20,}".format(BAG1_MOMENT))

print("{0: <25}".format("BAGGAGE AREA2"),end='')
print("{0: <20,}".format(BAG2_WEI),end='')
print("{0: <20}".format(123),end='')
print("{0: <20,}".format(BAG2_MOMENT))

print("{0: <25}".format("RAMP WEIGHT & CG"),end='')
print("{0: <20,}".format(round(RAM_WEI,1)),end='')
print("{0: <20,}".format(round(RAM_ARM,1)),end='')
print("{0: <20,}".format(round(RAM_MOMENT,1)))

for i in range(74):
    print("-",end='')
print("")

print("{0: <25}".format("TAXI & RUN-UP"),end='')
print("{0}".format("-"),end='')
print("{0: <19,}".format(TAXI_WEI),end='')
print("{0: <20}".format(48),end='')
print("{0}".format("-"),end='')
print("{0: <19,}".format(round(TAXI_MOMENT,1)))

for i in range(74):
    print("-",end='')
print("")

print("{0: <25}".format("T/O WEIGHT & CG"),end='')
print("{0: <20,}".format(round(TOW_WEI,1)),end='')
print("{0: <20,}".format(round(TOW_ARM,1)),end='')
print("{0: <20,}".format(round(TOW_MOMENT,1)))

for i in range(74):
    print("-",end='')
print("")

print("{0: <25}".format("FUEL BURN"),end='')
print("{0}".format("-"),end='')
print("{0: <19,}".format(round(FUEL2_WEI,1)),end='')
print("{0: <20}".format(48),end='')
print("{0}".format("-"),end='')
print("{0: <19,}".format(round(FUEL2_MOMENT,1)))

for i in range(74):
    print("-",end='')
print("")

print("{0: <25}".format("L/D WEIGHT & CG"),end='')
print("{0: <20,}".format(round(LDW_WEI,1)),end='')
print("{0: <20,}".format(round(LDW_ARM,1)),end='')
print("{0: <20,}".format(round(LDW_MOMENT,1)))

for i in range(74):
    print("-",end='')
print("")
#
if int(REG) == 1081 or int(REG) == 1082 or int(REG) == 1086 or int(REG) == 1087:
    R_NORMAL_CG = [34.99,35,40,47.4,47.41]
    R_NORMAL_WEIGHT = [0,1950,2450,2450,0]
    R_UTILITY_CG = [34.99,35,36.5,40.5,40.51]
    R_UTILITY_WEIGHT = [0,1950,2100,2100,0]

    TAKEOFF_CG = []
    TAKEOFF_WEIGHT = []
    LANDING_CG = []
    LANDING_WEIGHT = []

    TAKEOFF_CG.append(float(TOW_ARM))
    TAKEOFF_WEIGHT.append(float(TOW_WEI))
    LANDING_CG.append(float(LDW_ARM))
    LANDING_WEIGHT.append(float(LDW_WEI))

    TAKEOFF_CG_P1 = float(TOW_ARM)+0.01
    TAKEOFF_CG.append(TAKEOFF_CG_P1)
    LANDING_CG_P1 = float(LDW_ARM)+0.01
    LANDING_CG.append(LANDING_CG_P1)

    TAKEOFF_WEIGHT_P1 = float(TOW_WEI)+0.01
    TAKEOFF_WEIGHT.append(TAKEOFF_WEIGHT_P1)
    LANDING_WEIGHT_P1 = float(LDW_WEI)+0.01
    LANDING_WEIGHT.append(LANDING_WEIGHT_P1)

    plt.plot(R_NORMAL_CG, R_NORMAL_WEIGHT)
    plt.plot(R_UTILITY_CG, R_UTILITY_WEIGHT)
    plt.plot(TAKEOFF_CG, TAKEOFF_WEIGHT,'ro', label='TAKEOFF C.G.')
    plt.plot(LANDING_CG, LANDING_WEIGHT,'bo', label='LANDING C.G.')

    plt.axis([32, 50, 1500, 2500])
    plt.title('AIRPLANE C.G. LOCATION')
    plt.xlabel('C.G. LOCATION')
    plt.ylabel('AIRPLANE WEIGHT')
    plt.grid(True)
    plt.legend(loc=(0.01, 0.86))

    plt.show()

elif int(REG) == 1131 or int(REG) == 1132 or int(REG) == 1134 or int(REG) == 1135 or int(REG) == 1136 or int(REG) == 1171 or int(REG) == 1172 or int(REG) == 1173 or int(REG) == 1174 or int(REG) == 1175 or int(REG) == 1221 or int(REG) == 1222 or int(REG) == 1223:
    S_NORMAL_CG = [34.99,35,41,47.3,47.31]
    S_NORMAL_WEIGHT = [0,1950,2550,2550,0]
    S_UTILITY_CG = [34.99,35,37.5,40.5,40.51]
    S_UTILITY_WEIGHT = [0,1950,2200,2200,0]

    TAKEOFF_CG = []
    TAKEOFF_WEIGHT = []
    LANDING_CG = []
    LANDING_WEIGHT = []

    TAKEOFF_CG.append(float(TOW_ARM))
    TAKEOFF_WEIGHT.append(float(TOW_WEI))
    LANDING_CG.append(float(LDW_ARM))
    LANDING_WEIGHT.append(float(LDW_WEI))

    TAKEOFF_CG_P1 = float(TOW_ARM)+0.01
    TAKEOFF_CG.append(TAKEOFF_CG_P1)
    LANDING_CG_P1 = float(LDW_ARM)+0.01
    LANDING_CG.append(LANDING_CG_P1)

    TAKEOFF_WEIGHT_P1 = float(TOW_WEI)+0.01
    TAKEOFF_WEIGHT.append(TAKEOFF_WEIGHT_P1)
    LANDING_WEIGHT_P1 = float(LDW_WEI)+0.01
    LANDING_WEIGHT.append(LANDING_WEIGHT_P1)

    plt.plot(S_NORMAL_CG, S_NORMAL_WEIGHT)
    plt.plot(S_UTILITY_CG, S_UTILITY_WEIGHT)
    plt.plot(TAKEOFF_CG, TAKEOFF_WEIGHT,'ro', label='TAKEOFF C.G.')
    plt.plot(LANDING_CG, LANDING_WEIGHT,'bo', label='LANDING C.G.')

    plt.axis([32, 50, 1500, 2600])
    plt.title('AIRPLANE C.G. LOCATION')
    plt.xlabel('C.G. LOCATION')
    plt.ylabel('AIRPLANE WEIGHT')
    plt.grid(True)
    plt.legend(loc=(0.01, 0.86))

    plt.show()

else:
    print("항공기 등록기호 오류, 프로그램을 다시 실행해주세요.")

#
if int(REG) == 1081 or int(REG) == 1082 or int(REG) == 1086 or int(REG) == 1087:
    if 35<=int(TOW_ARM)<=36.5 and int(TOW_WEI)<=100*int(TOW_ARM)-1550:
        print("Utility Category, Within CG")
    elif 36.5<int(TOW_ARM)<=40.5 and int(TOW_WEI)<=2100:
        print("Utility Category, Within CG")
    elif 35<=int(TOW_ARM)<=40 and int(TOW_WEI)<=100*int(TOW_ARM)-1550:
        print("Normal Category, Within CG")
    elif 40<int(TOW_ARM)<=47.4 and int(TOW_WEI)<=2450:
        print("Normal Category, Within CG")
    else:
        print("Out of CG")
elif int(REG) == 1131 or int(REG) == 1132 or int(REG) == 1134 or int(REG) == 1135 or int(REG) == 1136 or int(REG) == 1171 or int(REG) == 1172 or int(REG) == 1173 or int(REG) == 1174 or int(REG) == 1175 or int(REG) == 1221 or int(REG) == 1222 or int(REG) == 1223:
    if 35<=int(TOW_ARM)<=37.5 and int(TOW_WEI)<=100*int(TOW_ARM)-1550:
        print("Utility Category, Within CG")
    elif 37.5<int(TOW_ARM)<=40.5 and int(TOW_WEI)<=2200:
        print("Utility Category, Within CG")
    elif 35<=int(TOW_ARM)<=41 and int(TOW_WEI)<=100*int(TOW_ARM)-1550:
        print("Normal Category, Within CG")
    elif 41<int(TOW_ARM)<=47.2 and int(TOW_WEI)<=2550:
        print("Normal Category, Within CG")
    else:
        print("Out of CG")
else:
    print("항공기 등록기호 오류, 프로그램을 다시 실행해주세요.")
    
if int(REG) == 1081 or int(REG) == 1082 or int(REG) == 1086 or int(REG) == 1087:
    Va = (int(LDW_WEI)/2450) ** (1/2) *99
    print("Va = ",math.floor(Va))
elif int(REG) == 1131 or int(REG) == 1132 or int(REG) == 1134 or int(REG) == 1135 or int(REG) == 1136 or int(REG) == 1171 or int(REG) == 1172 or int(REG) == 1173 or int(REG) == 1174 or int(REG) == 1175 or int(REG) == 1221 or int(REG) == 1222 or int(REG) == 1223:
    Va = (int(LDW_WEI)/2550) ** (1/2) *105
    print("Va = ",math.floor(Va))
else:
    print("항공기 등록기호 오류, 프로그램을 다시 실행해주세요.")

print(" ")
TEMP = input("온도는 몇인가요?   : ")
QNH = input("알티미터 세팅 값 입력하세요 ex) 29.92   : ")
FE = input("공항 표고 입력하세요 ex) 175   : ")
PA = (29.92-float(QNH))*1000 + int(FE)
DA = (int(TEMP)-15)*120 + PA

if int(PA) < 0:
    NUM1="N"
elif 0<= int(PA) < 1000:
    NUM1=0
elif 1000<= int(PA) < 2000:
    NUM1=1
elif 2000<= int(PA) < 3000:
    NUM1=2
elif 3000<= int(PA) < 4000:
    NUM1=3
elif 4000<= int(PA) < 5000:
    NUM1=4
elif 5000<= int(PA) < 6000:
    NUM1=5
elif 6000<= int(PA) < 7000:
    NUM1=6
elif 7000<= int(PA) < 8000:
    NUM1=7
else:
    print("PA가 너무 큽니다. 계산불가")


if int(TEMP) < 0:
    NUM2="N"
elif 0<= int(TEMP) < 10:
    NUM2=0
elif 10<= int(TEMP) <20:
    NUM2=1
elif 20<= int(TEMP) <30:
    NUM2=2
elif 30<= int(TEMP) <40:
    NUM2=3
else:
    print("온도가 너무 덥습니다. 계산불가")

#T/O Ground Roll
if int(REG) == 1081 or int(REG) == 1082 or int(REG) == 1086 or int(REG) == 1087:
    TOG = {"TOG00" : 845 , "TOG01" : 910 , "TOG02" : 980 , "TOG03" : 1055 , "TOG04" : 1135, 
    "TOG10": 925 , "TOG11" : 1000 , "TOG12" : 1075, "TOG13" : 1160 , "TOG14" : 1245,
    "TOG20": 1015 , "TOG21" : 1095 , "TOG22" : 1185, "TOG23" : 1275 , "TOG24" : 1365,
    "TOG30": 1115 , "TOG31" : 1205 , "TOG32" : 1305, "TOG33" : 1400 , "TOG34" : 1505,
    "TOG40": 1230 , "TOG41" : 1330 , "TOG42" : 1435, "TOG43" : 1545 , "TOG44" : 1655,
    "TOG50": 1355 , "TOG51" : 1470 , "TOG52" : 1585, "TOG53" : 1705 , "TOG54" : 1830,
    "TOG60": 1500 , "TOG61" : 1625 , "TOG62" : 1750, "TOG63" : 1880 , "TOG64" : 2020,
    "TOG70": 1660 , "TOG71" : 1795 , "TOG72" : 1935, "TOG73" : 2085 , "TOG74" : 2240,
    "TOG80": 1840 , "TOG81" : 1995 , "TOG82" : 2150, "TOG83" : 2315 , "TOG84" : 0}
elif  int(REG) == 1131 or int(REG) == 1132 or int(REG) == 1134 or int(REG) == 1135 or int(REG) == 1136 or int(REG) == 1171 or int(REG) == 1172 or int(REG) == 1173 or int(REG) == 1174 or int(REG) == 1175 or int(REG) == 1221 or int(REG) == 1222 or int(REG) == 1223:
    TOG = {"TOG00" : 860 , "TOG01" : 925 , "TOG02" : 995 , "TOG03" : 1070 , "TOG04" : 1150, 
    "TOG10": 940 , "TOG11" : 1010 , "TOG12" : 1090, "TOG13" : 1170 , "TOG14" : 1260,
    "TOG20": 1025 , "TOG21" : 1110 , "TOG22" : 1195, "TOG23" : 1285 , "TOG24" : 1380,
    "TOG30": 1125 , "TOG31" : 1215 , "TOG32" : 1310, "TOG33" : 1410 , "TOG34" : 1515,
    "TOG40": 1235 , "TOG41" : 1335 , "TOG42" : 1440, "TOG43" : 1550 , "TOG44" : 1660,
    "TOG50": 1355 , "TOG51" : 1465 , "TOG52" : 1585, "TOG53" : 1705 , "TOG54" : 1825,
    "TOG60": 1495 , "TOG61" : 1615 , "TOG62" : 1745, "TOG63" : 1875 , "TOG64" : 2010,
    "TOG70": 1645 , "TOG71" : 1785 , "TOG72" : 1920, "TOG73" : 2065 , "TOG74" : 2215,
    "TOG80": 1820 , "TOG81" : 1970 , "TOG82" : 2120, "TOG83" : 2280 , "TOG84" : 2450}
else:
    print("등록된 항공기가 아닙니다. 프로그램을 다시 실행하세요")

# T/O Obst
if int(REG) == 1081 or int(REG) == 1082 or int(REG) == 1086 or int(REG) == 1087:
    TOO = {"TOO00" : 1510 , "TOO01" : 1625 , "TOO02" : 1745 , "TOO03" : 1875 , "TOO04" : 2015, 
    "TOO10": 1660 , "TOO11" : 1790 , "TOO12" : 1925, "TOO13" : 2070 , "TOO14" : 2220,
    "TOO20": 1830 , "TOO21" : 1970 , "TOO22" : 2125, "TOO23" : 2290 , "TOO24" : 2455,
    "TOO30": 2020 , "TOO31" : 2185 , "TOO32" : 2360, "TOO33" : 2540 , "TOO34" : 2730,
    "TOO40": 2245 , "TOO41" : 2430 , "TOO42" : 2630, "TOO43" : 2830 , "TOO44" : 3045,
    "TOO50": 2500 , "TOO51" : 2715 , "TOO52" : 2945, "TOO53" : 3175 , "TOO54" : 3430,
    "TOO60": 2805 , "TOO61" : 3060 , "TOO62" : 3315, "TOO63" : 3590 , "TOO64" : 3895,
    "TOO70": 3170 , "TOO71" : 3470 , "TOO72" : 3770, "TOO73" : 4105 , "TOO74" : 4485,
    "TOO80": 3620 , "TOO81" : 3975 , "TOO82" : 4345, "TOO83" : 4775 , "TOO84" : 0}
elif  int(REG) == 1131 or int(REG) == 1132 or int(REG) == 1134 or int(REG) == 1135 or int(REG) == 1136 or int(REG) == 1171 or int(REG) == 1172 or int(REG) == 1173 or int(REG) == 1174 or int(REG) == 1175 or int(REG) == 1221 or int(REG) == 1222 or int(REG) == 1223:
    TOO = {"TOO00" : 1465 , "TOO01" : 1575 , "TOO02" : 1690 , "TOO03" : 1810 , "TOO04" : 1945, 
    "TOO10": 1600 , "TOO11" : 1720 , "TOO12" : 1850, "TOO13" : 1990 , "TOO14" : 2135,
    "TOO20": 1755 , "TOO21" : 1890 , "TOO22" : 2035, "TOO23" : 2190 , "TOO24" : 2355,
    "TOO30": 1925 , "TOO31" : 2080 , "TOO32" : 2240, "TOO33" : 2420 , "TOO34" : 2605,
    "TOO40": 2120 , "TOO41" : 2295 , "TOO42" : 2480, "TOO43" : 2685 , "TOO44" : 2880,
    "TOO50": 2345 , "TOO51" : 2545 , "TOO52" : 2755, "TOO53" : 2975 , "TOO54" : 3205,
    "TOO60": 2605 , "TOO61" : 2830 , "TOO62" : 3075, "TOO63" : 3320 , "TOO64" : 3585,
    "TOO70": 2910 , "TOO71" : 3170 , "TOO72" : 3440, "TOO73" : 3730 , "TOO74" : 4045,
    "TOO80": 3265 , "TOO81" : 3575 , "TOO82" : 3880, "TOO83" : 4225 , "TOO84" : 4615}
else:
    print("등록된 항공기가 아닙니다. 프로그램을 다시 실행하세요")

if NUM1 == "N" and NUM2 == "N":
    TO_GR = TOG.get("TOG"+"00")
    TO_TOTAL = TOO.get("TOO"+"00")

elif NUM1 != "N" and NUM2 != "N":
    TO_GR_PA1 = TOG.get("TOG"+str(NUM1)+str(NUM2))
    TO_GR_PA2 = TOG.get("TOG"+str(int(NUM1)+1)+str(NUM2))
    TO_GR_TEMP1 = TOG.get("TOG"+str(NUM1)+str(NUM2))
    TO_GR_TEMP2 = TOG.get("TOG"+str(NUM1)+str(int(NUM2)+1))
    TO_GR_PA = int(TO_GR_PA1)+(((PA%1000)/1000)*(int(TO_GR_PA2)-int(TO_GR_PA1)))
    TO_GR_TEMP = int(TO_GR_TEMP1)+(((int(TEMP)%10)/10)*(int(TO_GR_TEMP2)-int(TO_GR_TEMP1)))

    TO_TOTAL_PA1 = TOO.get("TOO"+str(NUM1)+str(NUM2))
    TO_TOTAL_PA2 = TOO.get("TOO"+str(int(NUM1)+1)+str(NUM2))
    TO_TOTAL_TEMP1 = TOO.get("TOO"+str(NUM1)+str(NUM2))
    TO_TOTAL_TEMP2 = TOO.get("TOO"+str(NUM1)+str(int(NUM2)+1))
    TO_TOTAL_PA = int(TO_TOTAL_PA1)+(((PA%1000)/1000)*(int(TO_TOTAL_PA2)-int(TO_TOTAL_PA1)))
    TO_TOTAL_TEMP = int(TO_TOTAL_TEMP1)+(((int(TEMP)%10)/10)*(int(TO_TOTAL_TEMP2)-int(TO_TOTAL_TEMP1)))
   
    TO_GR = (int(TO_GR_PA) + int(TO_GR_TEMP))/2
    TO_TOTAL = (int(TO_TOTAL_PA) + int(TO_TOTAL_TEMP))/2
    
elif NUM1 == "N" and NUM2 != "N":
    TO_GR_TEMP1 = TOG.get("TOG0"+str(NUM2))
    TO_GR_TEMP2 = TOG.get("TOG0"+str(int(NUM2)+1))
    TO_GR = (int(TO_GR_TEMP1)+int(TO_GR_TEMP2))/2

    TO_TOTAL_TEMP1 = TOO.get("TOO0"+str(NUM2))
    TO_TOTAL_TEMP2 = TOO.get("TOO0"+str(int(NUM2)+1))
    TO_TOTAL = (int(TO_TOTAL_TEMP1)+int(TO_TOTAL_TEMP2))/2

elif NUM1 != "N" and NUM2 == "N":
    TO_GR_PA1 = TOG.get("TOG"+str(NUM1)+"0")
    TO_GR_PA2 = TOG.get("TOG"+str(int(NUM1)+1)+"0")
    TO_GR = (TO_GR_PA1+TO_GR_PA2)/2

    TO_TOTAL_PA1 = TOO.get("TOO"+str(NUM1)+"0")
    TO_TOTAL_PA2 = TOO.get("TOO"+str(int(NUM1)+1)+"0")
    TO_TOTAL = (TO_TOTAL_PA1+TO_TOTAL_PA2)/2
else:
    print("프로그램 오류")

#L/D Ground Roll
if int(REG) == 1081 or int(REG) == 1082 or int(REG) == 1086 or int(REG) == 1087:
    LDG = {"LDG00" : 525 , "LDG01" : 540 , "LDG02" : 560 , "LDG03" : 580 , "LDG04" : 600, 
    "LDG10": 545 , "LDG11" : 560 , "LDG12" : 580, "LDG13" : 600 , "LDG14" : 620,
    "LDG20": 565 , "LDG21" : 585 , "LDG22" : 605, "LDG23" : 625 , "LDG24" : 645,
    "LDG30": 585 , "LDG31" : 605 , "LDG32" : 625, "LDG33" : 650 , "LDG34" : 670,
    "LDG40": 605 , "LDG41" : 630 , "LDG42" : 650, "LDG43" : 670 , "LDG44" : 695,
    "LDG50": 630 , "LDG51" : 650 , "LDG52" : 675, "LDG53" : 700 , "LDG54" : 720,
    "LDG60": 655 , "LDG61" : 675 , "LDG62" : 700, "LDG63" : 725 , "LDG64" : 750,
    "LDG70": 680 , "LDG71" : 705 , "LDG72" : 730, "LDG73" : 755 , "LDG74" : 775,
    "LDG80": 705 , "LDG81" : 730 , "LDG82" : 755, "LDG83" : 780 , "LDG84" : 810}
elif  int(REG) == 1131 or int(REG) == 1132 or int(REG) == 1134 or int(REG) == 1135 or int(REG) == 1136 or int(REG) == 1171 or int(REG) == 1172 or int(REG) == 1173 or int(REG) == 1174 or int(REG) == 1175 or int(REG) == 1221 or int(REG) == 1222 or int(REG) == 1223:
    LDG = {"LDG00" : 545 , "LDG01" : 565 , "LDG02" : 585 , "LDG03" : 605 , "LDG04" : 625, 
    "LDG10": 565 , "LDG11" : 585 , "LDG12" : 605, "LDG13" : 625 , "LDG14" : 650,
    "LDG20": 585 , "LDG21" : 610 , "LDG22" : 630, "LDG23" : 650 , "LDG24" : 670,
    "LDG30": 610 , "LDG31" : 630 , "LDG32" : 655, "LDG33" : 675 , "LDG34" : 695,
    "LDG40": 630 , "LDG41" : 655 , "LDG42" : 675, "LDG43" : 700 , "LDG44" : 725,
    "LDG50": 655 , "LDG51" : 680 , "LDG52" : 705, "LDG53" : 725 , "LDG54" : 750,
    "LDG60": 680 , "LDG61" : 705 , "LDG62" : 730, "LDG63" : 755 , "LDG64" : 780,
    "LDG70": 705 , "LDG71" : 730 , "LDG72" : 760, "LDG73" : 785 , "LDG74" : 810,
    "LDG80": 735 , "LDG81" : 760 , "LDG82" : 790, "LDG83" : 815 , "LDG84" : 840}
else:
    print("등록된 항공기가 아닙니다. 프로그램을 다시 실행하세요")

# L/D Obst
if int(REG) == 1081 or int(REG) == 1082 or int(REG) == 1086 or int(REG) == 1087:
    LDO = {"LDO00" : 1250 , "LDO01" : 1280 , "LDO02" : 1310 , "LDO03" : 1340 , "LDO04" : 1370, 
    "LDO10": 1280 , "LDO11" : 1310 , "LDO12" : 1345, "LDO13" : 1375 , "LDO14" : 1405,
    "LDO20": 1310 , "LDO21" : 1345 , "LDO22" : 1375, "LDO23" : 1410 , "LDO24" : 1440,
    "LDO30": 1345 , "LDO31" : 1380 , "LDO32" : 1415, "LDO33" : 1445 , "LDO34" : 1480,
    "LDO40": 1380 , "LDO41" : 1415 , "LDO42" : 1450, "LDO43" : 1485 , "LDO44" : 1520,
    "LDO50": 1415 , "LDO51" : 1455 , "LDO52" : 1490, "LDO53" : 1525 , "LDO54" : 1560,
    "LDO60": 1455 , "LDO61" : 1490 , "LDO62" : 1530, "LDO63" : 1565 , "LDO64" : 1605,
    "LDO70": 1495 , "LDO71" : 1535 , "LDO72" : 1570, "LDO73" : 1610 , "LDO74" : 1650,
    "LDO80": 1535 , "LDO81" : 1575 , "LDO82" : 1615, "LDO83" : 1655 , "LDO84" : 1695}
elif  int(REG) == 1131 or int(REG) == 1132 or int(REG) == 1134 or int(REG) == 1135 or int(REG) == 1136 or int(REG) == 1171 or int(REG) == 1172 or int(REG) == 1173 or int(REG) == 1174 or int(REG) == 1175 or int(REG) == 1221 or int(REG) == 1222 or int(REG) == 1223:
    LDO = {"LDO00" : 1290 , "LDO01" : 1320 , "LDO02" : 1350 , "LDO03" : 1380 , "LDO04" : 1415, 
    "LDO10": 1320 , "LDO11" : 1350 , "LDO12" : 1385, "LDO13" : 1420 , "LDO14" : 1450,
    "LDO20": 1355 , "LDO21" : 1385 , "LDO22" : 1420, "LDO23" : 1455 , "LDO24" : 1490,
    "LDO30": 1385 , "LDO31" : 1425 , "LDO32" : 1460, "LDO33" : 1495 , "LDO34" : 1530,
    "LDO40": 1425 , "LDO41" : 1460 , "LDO42" : 1495, "LDO43" : 1535 , "LDO44" : 1570,
    "LDO50": 1460 , "LDO51" : 1500 , "LDO52" : 1535, "LDO53" : 1575 , "LDO54" : 1615,
    "LDO60": 1500 , "LDO61" : 1540 , "LDO62" : 1580, "LDO63" : 1620 , "LDO64" : 1660,
    "LDO70": 1545 , "LDO71" : 1585 , "LDO72" : 1625, "LDO73" : 1665 , "LDO74" : 1705,
    "LDO80": 1585 , "LDO81" : 1630 , "LDO82" : 1670, "LDO83" : 1715 , "LDO84" : 1755}
else:
    print("등록된 항공기가 아닙니다. 프로그램을 다시 실행하세요")

if NUM1 == "N" and NUM2 == "N":
    LD_GR = LDG.get("LDG"+"00")
    LD_TOTAL = LDO.get("LDO"+"00")

elif NUM1 != "N" and NUM2 != "N":
    LD_GR_PA1 = LDG.get("LDG"+str(NUM1)+str(NUM2))
    LD_GR_PA2 = LDG.get("LDG"+str(int(NUM1)+1)+str(NUM2))
    LD_GR_TEMP1 = LDG.get("LDG"+str(NUM1)+str(NUM2))
    LD_GR_TEMP2 = LDG.get("LDG"+str(NUM1)+str(int(NUM2)+1))
    LD_GR_PA = int(LD_GR_PA1)+(((PA%1000)/1000)*(int(LD_GR_PA2)-int(LD_GR_PA1)))
    LD_GR_TEMP = int(LD_GR_TEMP1)+(((int(TEMP)%10)/10)*(int(LD_GR_TEMP2)-int(LD_GR_TEMP1)))

    LD_TOTAL_PA1 = LDO.get("LDO"+str(NUM1)+str(NUM2))
    LD_TOTAL_PA2 = LDO.get("LDO"+str(int(NUM1)+1)+str(NUM2))
    LD_TOTAL_TEMP1 = LDO.get("LDO"+str(NUM1)+str(NUM2))
    LD_TOTAL_TEMP2 = LDO.get("LDO"+str(NUM1)+str(int(NUM2)+1))
    LD_TOTAL_PA = int(LD_TOTAL_PA1)+(((PA%1000)/1000)*(int(LD_TOTAL_PA2)-int(LD_TOTAL_PA1)))
    LD_TOTAL_TEMP = int(LD_TOTAL_TEMP1)+(((int(TEMP)%10)/10)*(int(LD_TOTAL_TEMP2)-int(LD_TOTAL_TEMP1)))

    LD_GR = (int(LD_GR_PA) + int(LD_GR_TEMP))/2
    LD_TOTAL = (int(LD_TOTAL_PA) + int(LD_TOTAL_TEMP))/2
    
elif NUM1 == "N" and NUM2 != "N":

    LD_GR_TEMP1 = LDG.get("LDG0"+str(NUM2))
    LD_GR_TEMP2 = LDG.get("LDG0"+str(int(NUM2)+1))
    LD_GR = (int(LD_GR_TEMP1)+int(LD_GR_TEMP2))/2

    LD_TOTAL_TEMP1 = LDO.get("LDO0"+str(NUM2))
    LD_TOTAL_TEMP2 = LDO.get("LDO0"+str(int(NUM2)+1))
    LD_TOTAL = (int(LD_TOTAL_TEMP1)+int(LD_TOTAL_TEMP2))/2

elif NUM1 != "N" and NUM2 == "N":

    LD_GR_PA1 = LDG.get("LDG"+str(NUM1)+"0")
    LD_GR_PA2 = LDG.get("LDG"+str(int(NUM1)+1)+"0")
    LD_GR = (LD_GR_PA1+LD_GR_PA2)/2

    LD_TOTAL_PA1 = LDO.get("LDO"+str(NUM1)+"0")
    LD_TOTAL_PA2 = LDO.get("LDO"+str(int(NUM1)+1)+"0")
    LD_TOTAL = (LD_TOTAL_PA1+LD_TOTAL_PA2)/2
else:
    print("프로그램 오류")

HW = input("HeadWind 성분은 몇 kt 인가요?   : ")
TW = input("TailWind 성분은 몇 kt 인가요?   : ")
GUST = input("Gust는 몇 kt인가요?   : ")

VREF0 = 75 ; VREF1 = 70 ; VREF2 = 65 ; VREF3 = 60
HW_HALF = int(HW)/2
HW_GUST = int(GUST) -int(HW)
WIND_FACTOR = int(HW_HALF) + int(HW_GUST)

if float(WIND_FACTOR) >= 5:
    VAPP = int(WIND_FACTOR)
elif float(WIND_FACTOR) < 5:
    VAPP = 5
else:
    print("Vapp Calculation Error")

VAPP0 = int(VREF0) + int(VAPP)
VAPP1 = int(VREF1) + int(VAPP)
VAPP2 = int(VREF2) + int(VAPP)
VAPP3 = int(VREF3) + int(VAPP)

if int(HW) != 0 and int(TW) == 0:
    TO_GR = int(TO_GR)-int(TO_GR)*((int(HW)/9*0.1))
    TO_TOTAL = int(TO_TOTAL)-int(TO_TOTAL)*((int(HW)/9*0.1))
    
    LD_GR = int(LD_GR)-int(LD_GR)*((int(HW)/9*0.1))
    LD_TOTAL = int(LD_TOTAL)-int(LD_TOTAL)*((int(HW)/9*0.1))
elif int(HW) == 0 and int(TW) != 0:
    TO_GR = int(TO_GR)+int(TO_GR)*(int(TW)/2*0.1)
    TO_TOTAL = int(TO_TOTAL)+int(TO_TOTAL)*(int(TW)/2*0.1)

    LD_GR = int(LD_GR)+int(LD_GR)*(int(TW)/2*0.1)
    LD_TOTAL = int(LD_TOTAL)+int(LD_TOTAL)*(int(TW)/2*0.1)
elif int(HW) == 0 and int(TW) == 0:
    print("WIND CALM! HAVE A GOOD FLIGHT!!!")
else:
    print("HEADWIND와 TAILWIND는 공존할 수 없어요!")

if int(PA) <= 0:
    NUM3="N"
elif 0< int(PA) < 2000:
    NUM3=0
elif 2000<= int(PA) < 4000:
    NUM3=2
elif 4000<= int(PA) < 6000:
    NUM3=4
elif 6000<= int(PA) < 8000:
    NUM3=6
elif 8000<= int(PA) < 10000:
    NUM3=8
elif 10000<= int(PA) < 12000:
    NUM3=10
else:
    print("PA가 너무 큽니다. 계산불가")

if 0 <= int(TEMP) < 40 :
    if 0<= int(TEMP) < 20:
        NUM4=0
    elif 20<= int(TEMP) < 40:
        NUM4=2
    else:
        print("Error")
elif -20 < int(TEMP) < 0:
    NUM4=0
else:
    print("TEMPARATURE IS TOO LOW OR HIGH, CANCLE FLIGHT")

if 0<= int(TEMP) < 40:
    if int(REG) == 1081 or int(REG) == 1082 or int(REG) == 1086 or int(REG) == 1087:
        ROC = {"ROC00" : 770 , "ROC02" : 705 , "ROC04" : 640 , 
        "ROC20": 655 , "ROC22" : 595 , "ROC24" : 535,
        "ROC40": 585 , "ROC42" : 525 , "ROC44" : 465,
        "ROC60": 475 , "ROC62" : 415 , "ROC64" : 360,
        "ROC80": 365 , "ROC82" : 310 , "ROC84" : 250,
        "ROC100": 255 , "ROC102" : 200 , "ROC104" : 145,
        "ROC120": 145 , "ROC122" : 0 , "ROC124" : 0}
    elif  int(REG) == 1131 or int(REG) == 1132 or int(REG) == 1134 or int(REG) == 1135 or int(REG) == 1136 or int(REG) == 1171 or int(REG) == 1172 or int(REG) == 1173 or int(REG) == 1174 or int(REG) == 1175 or int(REG) == 1221 or int(REG) == 1222 or int(REG) == 1223:
        ROC = {"ROC00" : 785 , "ROC02" : 710 , "ROC04" : 645 , 
        "ROC20": 695 , "ROC22" : 625 , "ROC24" : 560,
        "ROC40": 620 , "ROC42" : 555 , "ROC44" : 495,
        "ROC60": 515 , "ROC62" : 450 , "ROC64" : 390,
        "ROC80": 405 , "ROC82" : 345 , "ROC84" : 285,
        "ROC100": 300 , "ROC102" : 240 , "ROC104" : 180,
        "ROC120": 195 , "ROC122" : 135 , "ROC124" : 0}
    else:
        print("등록된 항공기가 아닙니다. 프로그램을 다시 실행하세요")
elif  -20 < int(TEMP) < 0:
    if int(REG) == 1081 or int(REG) == 1082 or int(REG) == 1086 or int(REG) == 1087:
        ROC = {"ROC00" : 770 , "ROC02" : 830 ,
        "ROC20": 655 , "ROC22" : 720 ,
        "ROC40": 585 , "ROC42" : 645 ,
        "ROC60": 475 , "ROC62" : 530 ,
        "ROC80": 365 , "ROC82" : 420 ,
        "ROC100": 255 , "ROC102" : 310 ,
        "ROC120": 145 , "ROC122" : 200 }
    elif int(REG) == 1131 or int(REG) == 1132 or int(REG) == 1134 or int(REG) == 1135 or int(REG) == 1136 or int(REG) == 1171 or int(REG) == 1172 or int(REG) == 1173 or int(REG) == 1174 or int(REG) == 1175 or int(REG) == 1221 or int(REG) == 1222 or int(REG) == 1223:
        ROC = {"ROC00" : 770 , "ROC02" : 855 ,
        "ROC20": 655 , "ROC22" : 760 ,
        "ROC40": 585 , "ROC42" : 685 ,
        "ROC60": 475 , "ROC62" : 575 ,
        "ROC80": 365 , "ROC82" : 465 ,
        "ROC100": 255 , "ROC102" : 360 ,
        "ROC120": 145 , "ROC122" : 255 }
    else:
        print("등록된 항공기가 아닙니다. 프로그램을 다시 실행하세요")
else:
    print("TEMPARATURE IS TOO LOW OR HIGH, CANCLE FLIGHT")

if NUM3 != "N":
    if 0 <= int(TEMP) < 40:
        FPM_PA1 = ROC.get("ROC"+str(NUM3)+str(NUM4))
        FPM_PA2 = ROC.get("ROC"+str(int(NUM3)+2)+str(NUM4))
        FPM_TEMP1 = ROC.get("ROC"+str(NUM3)+str(NUM4))
        FPM_TEMP2 = ROC.get("ROC"+str(NUM3)+str(int(NUM4)+2))
        
        FPM_PA_DIF = float(FPM_PA1)-float(FPM_PA2)
        # print("FPM_PA_DIF = {0}".format(FPM_PA_DIF))
        FPM_PA_RATIO = (1-((int(PA)%2000)/2000))
        # print("FPM_PA_RATIO = {0}".format(FPM_PA_RATIO))
        FPM_PA_VALUE = (FPM_PA_DIF)*(FPM_PA_RATIO)
        # print("FPM_PA_VALUE = {0}".format(FPM_PA_VALUE))
        FPM_PA = float(FPM_PA2) + FPM_PA_VALUE

        FPM_TEMP_DIF = float(FPM_TEMP1)-float(FPM_TEMP2)
        # print("FPM_TEMP_DIF = {0}".format(FPM_TEMP_DIF))
        FPM_TEMP_RATIO = (1-((int(TEMP)%20)/20))
        # print("FPM_TEMP_RATIO = {0}".format(FPM_TEMP_RATIO))
        FPM_TEMP_VALUE = (FPM_TEMP_DIF)*(FPM_TEMP_RATIO)
        # print("FPM_TEMP_VALUE = {0}".format(FPM_TEMP_VALUE))
        FPM_TEMP = float(FPM_TEMP2) + FPM_TEMP_VALUE

        FPM = (FPM_PA+FPM_TEMP)/2
    elif -20 < int(TEMP) < 0:
        FPM_PA1 = ROC.get("ROC"+str(NUM3)+str(NUM4))
        FPM_PA2 = ROC.get("ROC"+str(int(NUM3)+2)+str(NUM4))
        FPM_TEMP1 = ROC.get("ROC"+str(NUM3)+str(NUM4))
        FPM_TEMP2 = ROC.get("ROC"+str(NUM3)+str(int(NUM4)+2))

        FPM_PA_DIF = float(FPM_PA1)-float(FPM_PA2)
        # print("FPM_PA_DIF = {0}".format(FPM_PA_DIF))
        FPM_PA_RATIO = (1-((int(PA)%2000)/2000))
        # print("FPM_PA_RATIO = {0}".format(FPM_PA_RATIO))
        FPM_PA_VALUE = (FPM_PA_DIF)*(FPM_PA_RATIO)
        # print("FPM_PA_VALUE = {0}".format(FPM_PA_VALUE))
        FPM_PA = float(FPM_PA2) + float(FPM_PA_VALUE)
        # print("FPM_PA = {0}".format(FPM_PA))

        FPM_TEMP_DIF = float(FPM_TEMP2)-float(FPM_TEMP1)
        # print("FPM_TEMP_DIF = {0}".format(FPM_TEMP_DIF))
        TEMP_REVERSE = int(TEMP)*-1
        FPM_TEMP_RATIO = ((int(TEMP_REVERSE)%20)/20)
        # print("FPM_TEMP_RATIO = {0}".format(FPM_TEMP_RATIO))
        FPM_TEMP_VALUE = (FPM_TEMP_DIF)*(FPM_TEMP_RATIO)
        # print("FPM_TEMP_VALUE = {0}".format(FPM_TEMP_VALUE))
        FPM_TEMP = float(FPM_TEMP1) + float(FPM_TEMP_VALUE)
        # print("FPM_TEMP = {0}".format(FPM_TEMP))

        FPM = (float(FPM_PA)+float(FPM_TEMP))/2
    else:
        print("TEMPARATURE IS TOO LOW OR HIGH")
elif NUM3 == "N":
    if 0 <= int(TEMP) < 40:
        FPM_TEMP1 = ROC.get("ROC0"+str(NUM4))
        FPM_TEMP2 = ROC.get("ROC0"+str(int(NUM4)+2))

        FPM_TEMP_DIF = float(FPM_TEMP1)-float(FPM_TEMP2)
        # print("FPM_TEMP_DIF = {0}".format(FPM_TEMP_DIF))
        FPM_TEMP_RATIO = (1-((int(TEMP)%20)/20))
        # print("FPM_TEMP_RATIO = {0}".format(FPM_TEMP_RATIO))
        FPM_TEMP_VALUE = (FPM_TEMP_DIF)*(FPM_TEMP_RATIO)
        # print("FPM_TEMP_VALUE = {0}".format(FPM_TEMP_VALUE))
        FPM_TEMP = float(FPM_TEMP2) + FPM_TEMP_VALUE

        FPM = FPM_TEMP
    elif -20 < int(TEMP) < 0:
        FPM_TEMP1 = ROC.get("ROC0"+str(NUM4))
        FPM_TEMP2 = ROC.get("ROC0"+str(int(NUM4)+2))

        FPM_TEMP_DIF = float(FPM_TEMP2)-float(FPM_TEMP1)
        # print("FPM_TEMP_DIF = {0}".format(FPM_TEMP_DIF))
        TEMP_REVERSE = int(TEMP)*-1
        FPM_TEMP_RATIO = ((int(TEMP_REVERSE)%20)/20)
        # print("FPM_TEMP_RATIO = {0}".format(FPM_TEMP_RATIO))
        FPM_TEMP_VALUE = (FPM_TEMP_DIF)*(FPM_TEMP_RATIO)
        # print("FPM_TEMP_VALUE = {0}".format(FPM_TEMP_VALUE))
        FPM_TEMP = float(FPM_TEMP1) + float(FPM_TEMP_VALUE)

        FPM = FPM_TEMP
    else:
        print("TEMPARATURE IS TOO LOW OR HIGH")
else:
    print("ERROR")

print("")
for i in range(39):
    print("-",end='')
print("")
print("{0: <25}".format("       [TAKEOFF PERFORMANCE]"),end='')
print("")
print("{0: <20}".format("GROUND ROLL"),end='')
print("{0: <20}".format("TAKEOFF DISTANCE"),end='')
print("")
print("{0: <20,}".format(round(TO_GR,1)),end='')
print("{0: <20,}".format(round(TO_TOTAL,1),end=''))
print("")
print("{0: <20}".format("RATE OF CLIMB"))
print("{0: <20,}".format(round(FPM,1)))
print("")
print("{0: <20}".format("PRESSURE ALTITUDE"),end='')
print("{0: <20}".format("DENSITY ALTITUDE"),end='')
print("")
print("{0: <20,}".format(round(PA,1)),end='')
print("{0: <20,}".format(round(DA,1),end=''))
print("")
print("{0: <25}".format("       [LANDING PERFORMANCE]"),end='')
print("")
print("{0: <20}".format("GROUND ROLL"),end='')
print("{0: <20}".format("LANDING DISTANCE"),end='')
print("")
print("{0: <20,}".format(round(LD_GR,1)),end='')
print("{0: <20,}".format(round(LD_TOTAL,1),end=''))
print("")
for i in range(50):
    print("-",end='')

print("")
print("{0: <25}".format("[REFERENCE SPEED]"),end='')
print("{0: <15}".format("[APPROACH SPEED]"),end='')
print("")
print("{0: <17}".format("Vref Flaps 0°"),end='')
print("{0: <3}kt   ".format(round(VREF0,1)),end='')
print("{0: <17}".format("Vapp Flaps 0°"),end='')
print("{0: <3}kt".format(round(VAPP0,1)),end='')
print("")
print("{0: <17}".format("Vref Flaps 10°"),end='')
print("{0: <3}kt   ".format(round(VREF1,1)),end='')
print("{0: <17}".format("Vapp Flaps 10°"),end='')
print("{0: <3}kt".format(round(VAPP1,1)),end='')
print("")
print("{0: <17}".format("Vref Flaps 20°"),end='')
print("{0: <3}kt   ".format(round(VREF2,1)),end='')
print("{0: <17}".format("Vapp Flaps 20°"),end='')
print("{0: <3}kt".format(round(VAPP2,1)),end='')
print("")
print("{0: <17}".format("Vref Flaps 30°"),end='')
print("{0: <3}kt   ".format(round(VREF3,1)),end='')
print("{0: <17}".format("Vapp Flaps 30°"),end='')
print("{0: <3}kt".format(round(VAPP3,1)),end='')
print("")
for i in range(50):
    print("-",end='')
print("")

EXIT = input("종료하려면 ENTER를 눌러주세요")