#Auto Metar V1.0.6 selenium v4

# 1. Selenium 4
from http.server import executable
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# 2. os
import os
import urllib.request as req

# 3. 날짜
import datetime
days = ['월','화','수','목','금','토','일']
day = datetime.datetime.today().weekday()
file_time = str(datetime.datetime.now().strftime('%Y%m%d%H%M'))

# 4. Pillow
from PIL import Image

#크롬 드라이버 자동 업데이트
from webdriver_manager.chrome import ChromeDriverManager

# 브라우저 꺼짐 방지
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)

# 불필요한 에러 메시지 없애기
chrome_options.add_experimental_option("excludeSwitches",["enable-logging"])
chrome_options.add_argument("headless")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10)

#웹페이지 해당 주소 이동
driver.implicitly_wait(1)   # 초 대기
driver.maximize_window()  # 화면 최대화

def metar(): #모든 METAR 받아오기(총 38개 공항)
    driver.get("https://global.amo.go.kr/obsMetar/ObsMetar.do")
    Class_metars = driver.find_element(By.CLASS_NAME,"dataT").text
    return Class_metars
    
def taf(): #모든 TAF 받아오기(총 23개 공항)
    driver.get("https://global.amo.go.kr/airfcst/AirFcstBeforeList.do")
    ID_tafs = driver.find_element(By.ID,"contentsTb1").text
    return ID_tafs

def sigmet():
    driver.get("https://global.amo.go.kr/amis/awx/GisSigmetImage.do")
    driver.set_window_size(800, 900)
    driver.implicitly_wait(1)
    image_sigmet = driver.find_element(By.TAG_NAME, 'body')
    # image_sigmet_png = image_sigmet.screenshot('./sigmet.png')
    image_sigmet_png = image_sigmet.screenshot('./3_sigmet_'+file_time+'.png')
    Class_sigmet = driver.find_element(By.CLASS_NAME,"con_all2").text
    return Class_sigmet

def airmet():
    driver.get("https://global.amo.go.kr/amis/awx/GisAirmetImage.do")
    driver.set_window_size(826, 862)
    driver.implicitly_wait(1)
    image_airmet = driver.find_element(By.TAG_NAME, 'body')
    image_airmet_png = image_airmet.screenshot('./4_airmet_'+file_time+'.png')
    Class_airmet = driver.find_element(By.CLASS_NAME,"con_all2").text
    return Class_airmet

def sigwx():
    img_url_sigwx = []
    driver.get("https://global.amo.go.kr/sigwx/Sigwx250.do")
    # sfc = driver.find_element(By.XPATH,'/html/body/form[2]/div/div/div[2]/ul/li[2]/a').click()
    sfc = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/form[2]/div/div/div[2]/ul/li[2]/a'))).click()
    driver.switch_to.frame("ifrm")
    image_sigwx = driver.find_element(By.CSS_SELECTOR,"#img17 > img")
    sigwx_url = image_sigwx.get_attribute('src')
    img_url_sigwx.append(sigwx_url)
    sigwx_url_index = sigwx_url.rfind('/')
    sigwx_url_filename = "2_" + sigwx_url[int(sigwx_url_index)+1:]
    save_path_sigwx = os.getcwd()+ '\\'+ sigwx_url_filename
    download_sigwx = req.urlretrieve(''.join(img_url_sigwx),save_path_sigwx)

def radar():
    driver.get("https://global.amo.go.kr/kama/raid/radar.do")
    width = driver.execute_script("return document.body.scrollWidth")
    height = driver.execute_script("return document.body.scrollHeight")
    driver.set_window_size(width, height) #스크롤 할 수 있는 모든 부분을 지정
    # driver.set_window_size(800, 900)
    #1080해상도
    driver.find_element(By.ID,'kmaRadar').click()
    driver.find_element(By.ID,'kmaRadar').send_keys(Keys.TAB)
    #1080해상도
    driver.implicitly_wait(3)
    image_radar = driver.find_element(By.TAG_NAME, 'body')
    image_radar_png = image_radar.screenshot('./5_radar_'+file_time+'.png')

def naver():
    driver.get("https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EA%B8%B0%EC%84%B1%EB%A9%B4+%EB%82%A0%EC%94%A8")
    driver.implicitly_wait(2)
    naver_wind = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main_pack"]/section[1]/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/ul/li[3]/a'))).click()
    driver.set_window_size(800, 1000)
    image_naver = driver.find_element(By.CLASS_NAME, 'content_area')
    image_naver = driver.find_element(By.ID,"main_pack")
    image_naver_png = image_naver.screenshot('./1_naver_'+file_time+'.png')

#---------------------------------------------------------------------#
def list_metar(): # 모든 METAR 리스트화 (불필요 정보 제거)
    list_metars = metars.split('\n')
    del list_metars[0]
    return list_metars
#---------------------------------------------------------------------#
def rktl(): #RKTL 인덱싱하고 문자열 반환
    find_rktl = 'RKTL'
    for i in range(len(list_metars)):
        if find_rktl in list_metars[i]:
            rktl_metar = list_metars[i]
    return rktl_metar

def rknn(): #RKNN 인덱싱하고 문자열 반환        
    find_rknn = 'RKNN'
    for i in range(len(list_metars)):
        if find_rknn in list_metars[i]:
            rknn_metar = list_metars[i]
    return rknn_metar

def rkny(): #RKNY 인덱싱하고 문자열 반환          
    find_rkny = 'RKNY'
    for i in range(len(list_metars)):
        if find_rkny in list_metars[i]:
            rkny_metar = list_metars[i]
    return rkny_metar
    
def rkty(): #RKTY 인덱싱하고 문자열 반환      
    find_rkty = 'RKTY'
    for i in range(len(list_metars)):
        if find_rkty in list_metars[i]:
            rkty_metar = list_metars[i]
    return rkty_metar

def rkth(): #RKTH 인덱싱하고 문자열 반환        
    find_rkth = 'RKTH'
    for i in range(len(list_metars)):
        if find_rkth in list_metars[i]:
            rkth_metar = list_metars[i]
    return rkth_metar

def rkpu(): #RKPU 인덱싱하고 문자열 반환       
    find_rkpu = 'RKPU'
    for i in range(len(list_metars)):
        if find_rkpu in list_metars[i]:
            rkpu_metar = list_metars[i]
    return rkpu_metar

#-----------------------------------------------------------------#

def wind_rktl(): # "KT" 인덱싱, RKTL 바람 방향, 속도 반환
    index_rktl = rktl_metar.rfind('KT')
    if rktl_metar[int(index_rktl)-4] == "G":
        rktl_winddir = rktl_metar[int(index_rktl)-9:int(index_rktl)-6]
        rktl_windspd = rktl_metar[int(index_rktl)-6:int(index_rktl)]
    else:
        rktl_winddir = rktl_metar[int(index_rktl)-5:int(index_rktl)-2]
        rktl_windspd = rktl_metar[int(index_rktl)-2:int(index_rktl)]
    return index_rktl, rktl_winddir,rktl_windspd

def wind_rknn():
    index_rknn = rknn_metar.rfind('KT')
    if rknn_metar[int(index_rknn)-4] == "G":
        rknn_winddir = rknn_metar[int(index_rknn)-9:int(index_rknn)-6]
        rknn_windspd = rknn_metar[int(index_rknn)-6:int(index_rknn)]
    else:
        rknn_winddir = rknn_metar[int(index_rknn)-5:int(index_rknn)-2]
        rknn_windspd = rknn_metar[int(index_rknn)-2:int(index_rknn)]
    return index_rknn, rknn_winddir,rknn_windspd 

def wind_rkny():
    index_rkny = rkny_metar.rfind('KT')
    if rkny_metar[int(index_rkny)-4] == "G":
        rkny_winddir = rkny_metar[int(index_rkny)-9:int(index_rkny)-6]
        rkny_windspd = rkny_metar[int(index_rkny)-6:int(index_rkny)]
    else:
        rkny_winddir = rkny_metar[int(index_rkny)-5:int(index_rkny)-2]
        rkny_windspd = rkny_metar[int(index_rkny)-2:int(index_rkny)]
    return index_rkny, rkny_winddir,rkny_windspd

def wind_rkty():
    index_rkty = rkty_metar.rfind('KT')
    if rkty_metar[int(index_rkty)-4] == "G":
        rkty_winddir = rkty_metar[int(index_rkty)-9:int(index_rkty)-6]
        rkty_windspd = rkty_metar[int(index_rkty)-6:int(index_rkty)]
    else:
        rkty_winddir = rkty_metar[int(index_rkty)-5:int(index_rkty)-2]
        rkty_windspd = rkty_metar[int(index_rkty)-2:int(index_rkty)]
    return index_rkty, rkty_winddir,rkty_windspd

def wind_rkth():
    index_rkth = rkth_metar.rfind('KT')
    if rkth_metar[int(index_rkth)-4] == "G":
        rkth_winddir = rkth_metar[int(index_rkth)-9:int(index_rkth)-6]
        rkth_windspd = rkth_metar[int(index_rkth)-6:int(index_rkth)]
    else:
        rkth_winddir = rkth_metar[int(index_rkth)-5:int(index_rkth)-2]
        rkth_windspd = rkth_metar[int(index_rkth)-2:int(index_rkth)]
    return index_rkth, rkth_winddir,rkth_windspd

def wind_rkpu():
    index_rkpu = rkpu_metar.rfind('KT')
    if rkpu_metar[int(index_rkpu)-4] == "G":
        rkpu_winddir = rkpu_metar[int(index_rkpu)-9:int(index_rkpu)-6]
        rkpu_windspd = rkpu_metar[int(index_rkpu)-6:int(index_rkpu)]
    else:
        rkpu_winddir = rkpu_metar[int(index_rkpu)-5:int(index_rkpu)-2]
        rkpu_windspd = rkpu_metar[int(index_rkpu)-2:int(index_rkpu)]
    return index_rkpu, rkpu_winddir,rkpu_windspd

#-------------------------------------------------------------------#

def vis_rktl():
    if "CAVOK" in rktl_metar:
        rktl_vis = "CAVOK"
    elif rktl_metar[int(index_rktl)+6] == "V":
        rktl_vis = rktl_metar[int(index_rktl)+11:int(index_rktl)+16]
    else:
        rktl_vis = rktl_metar[int(index_rktl)+3:int(index_rktl)+8]
    return rktl_vis

def vis_rknn():
    if "CAVOK" in rknn_metar:
        rknn_vis = "CAVOK"
    elif rknn_metar[int(index_rknn)+6] == "V":
        rknn_vis = rknn_metar[int(index_rknn)+11:int(index_rknn)+16]
    else:
        rknn_vis = rknn_metar[int(index_rknn)+3:int(index_rknn)+8]
    return rknn_vis

def vis_rkny():
    if "CAVOK" in rkny_metar:
        rkny_vis = "CAVOK"
    elif rkny_metar[int(index_rkny)+6] == "V":
        rkny_vis = rkny_metar[int(index_rkny)+11:int(index_rkny)+16]
    else:
        rkny_vis = rkny_metar[int(index_rkny)+3:int(index_rkny)+8]
    return rkny_vis

def vis_rkty():
    if "CAVOK" in rkty_metar:
        rkty_vis = "CAVOK"
    elif rkty_metar[int(index_rkty)+6] == "V":
        rkty_vis = rkty_metar[int(index_rkty)+11:int(index_rkty)+16]
    else:
        rkty_vis = rkty_metar[int(index_rkty)+3:int(index_rkty)+8]
    return rkty_vis

def vis_rkth():
    if "CAVOK" in rkth_metar:
        rkth_vis = "CAVOK"
    elif rkth_metar[int(index_rkth)+6] == "V":
        rkth_vis = rkth_metar[int(index_rkth)+11:int(index_rkth)+16]
    else:
        rkth_vis = rkth_metar[int(index_rkth)+3:int(index_rkth)+8]
    return rkth_vis

def vis_rkpu():
    if "CAVOK" in rkpu_metar:
        rkpu_vis = "CAVOK"
    elif rkpu_metar[int(index_rkpu)+6] == "V":
        rkpu_vis = rkpu_metar[int(index_rkpu)+11:int(index_rkpu)+16]
    else:
        rkpu_vis = rkpu_metar[int(index_rkpu)+3:int(index_rkpu)+8]
    return rkpu_vis

#--------------------------------------------------------------------#

def cld_rktl():
    list_cld_rktl = []
    if "CAVOK" in rktl_metar:
        list_cld_rktl.append("CAVOK")
    elif "NCD" in rktl_metar:
        list_cld_rktl.append("NCD")
    elif "SKC" in rktl_metar:
        list_cld_rktl.append("SKC")
    elif "FEW" in rktl_metar:
        index_few_rktl = rktl_metar.rfind('FEW')
        list_cld_rktl.append(rktl_metar[int(index_few_rktl):int(index_few_rktl)+6])
    
    if rktl_metar.count("SCT") == 1:
        index_sct_rktl = rktl_metar.rfind('SCT')
        list_cld_rktl.append(rktl_metar[int(index_sct_rktl):int(index_sct_rktl)+6])
    elif rktl_metar.count("SCT") == 2:
        index_sct_rktl = rktl_metar.find('SCT')
        list_cld_rktl.append(rktl_metar[int(index_sct_rktl):int(index_sct_rktl)+6])
        index_sct2_rktl = rktl_metar.rfind('SCT')
        list_cld_rktl.append(rktl_metar[int(index_sct2_rktl):int(index_sct2_rktl)+6])
    elif rktl_metar.count("SCT") == 3:
        index_sct_rktl = rktl_metar.find('SCT')
        list_cld_rktl.append(rktl_metar[int(index_sct_rktl):int(index_sct_rktl)+6])
        removed_rktl_metar = rktl_metar[int(index_sct_rktl)+7:]
        index_sct2_rktl = removed_rktl_metar.find('SCT')
        list_cld_rktl.append(removed_rktl_metar[int(index_sct2_rktl):int(index_sct2_rktl)+6])
        index_sct3_rktl = removed_rktl_metar.rfind('SCT')
        list_cld_rktl.append(removed_rktl_metar[int(index_sct3_rktl):int(index_sct3_rktl)+6])
        
    if rktl_metar.count("BKN") == 1:
        index_bkn_rktl = rktl_metar.rfind('BKN')
        list_cld_rktl.append(rktl_metar[int(index_bkn_rktl):int(index_bkn_rktl)+6])
    elif rktl_metar.count("BKN") == 2:
        index_bkn_rktl = rktl_metar.find('BKN')
        list_cld_rktl.append(rktl_metar[int(index_bkn_rktl):int(index_bkn_rktl)+6])
        index_bkn2_rktl = rktl_metar.rfind('BKN')
        list_cld_rktl.append(rktl_metar[int(index_bkn2_rktl):int(index_bkn2_rktl)+6])
    elif rktl_metar.count("BKN") == 3:
        index_bkn_rktl = rktl_metar.find('BKN')
        list_cld_rktl.append(rktl_metar[int(index_bkn_rktl):int(index_bkn_rktl)+6])
        removed_rktl_metar = rktl_metar[int(index_bkn_rktl)+7:]
        index_bkn2_rktl = removed_rktl_metar.find('BKN')
        list_cld_rktl.append(removed_rktl_metar[int(index_bkn2_rktl):int(index_bkn2_rktl)+6])
        index_bkn3_rktl = removed_rktl_metar.rfind('BKN')
        list_cld_rktl.append(removed_rktl_metar[int(index_bkn3_rktl):int(index_bkn3_rktl)+6])
        
    if rktl_metar.count("OVC") == 1:
        index_ovc_rktl = rktl_metar.rfind('OVC')
        list_cld_rktl.append(rktl_metar[int(index_ovc_rktl):int(index_ovc_rktl)+6])
    elif rktl_metar.count("OVC") == 2:
        index_ovc_rktl = rktl_metar.find('OVC')
        list_cld_rktl.append(rktl_metar[int(index_ovc_rktl):int(index_ovc_rktl)+6])
        index_ovc2_rktl = rktl_metar.rfind('OVC')
        list_cld_rktl.append(rktl_metar[int(index_ovc2_rktl):int(index_ovc2_rktl)+6])
    elif rktl_metar.count("OVC") == 3:
        index_ovc_rktl = rktl_metar.find('OVC')
        list_cld_rktl.append(rktl_metar[int(index_ovc_rktl):int(index_ovc_rktl)+6])
        removed_rktl_metar = rktl_metar[int(index_ovc_rktl)+7:]
        index_ovc2_rktl = removed_rktl_metar.find('OVC')
        list_cld_rktl.append(removed_rktl_metar[int(index_ovc2_rktl):int(index_ovc2_rktl)+6])
        index_ovc3_rktl = removed_rktl_metar.rfind('OVC')
        list_cld_rktl.append(removed_rktl_metar[int(index_ovc3_rktl):int(index_ovc3_rktl)+6])
    cld_rktl = ' '.join(list_cld_rktl)
    return cld_rktl

def cld_rknn():
    list_cld_rknn = []
    if "CAVOK" in rknn_metar:
        list_cld_rknn.append("CAVOK")
    elif "NCD" in rknn_metar:
        list_cld_rknn.append("NCD")
    elif "SKC" in rknn_metar:
        list_cld_rknn.append("SKC")
    elif "FEW" in rknn_metar:
        index_few_rknn = rknn_metar.rfind('FEW')
        list_cld_rknn.append(rknn_metar[int(index_few_rknn):int(index_few_rknn)+6])
    
    if rknn_metar.count("SCT") == 1:
        index_sct_rknn = rknn_metar.rfind('SCT')
        list_cld_rknn.append(rknn_metar[int(index_sct_rknn):int(index_sct_rknn)+6])
    elif rknn_metar.count("SCT") == 2:
        index_sct_rknn = rknn_metar.find('SCT')
        list_cld_rknn.append(rknn_metar[int(index_sct_rknn):int(index_sct_rknn)+6])
        index_sct2_rknn = rknn_metar.rfind('SCT')
        list_cld_rknn.append(rknn_metar[int(index_sct2_rknn):int(index_sct2_rknn)+6])
    elif rknn_metar.count("SCT") == 3:
        index_sct_rknn = rknn_metar.find('SCT')
        list_cld_rknn.append(rknn_metar[int(index_sct_rknn):int(index_sct_rknn)+6])
        removed_rknn_metar = rknn_metar[int(index_sct_rknn)+7:]
        index_sct2_rknn = removed_rknn_metar.find('SCT')
        list_cld_rknn.append(removed_rknn_metar[int(index_sct2_rknn):int(index_sct2_rknn)+6])
        index_sct3_rknn = removed_rknn_metar.rfind('SCT')
        list_cld_rknn.append(removed_rknn_metar[int(index_sct3_rknn):int(index_sct3_rknn)+6])
        
    if rknn_metar.count("BKN") == 1:
        index_bkn_rknn = rknn_metar.rfind('BKN')
        list_cld_rknn.append(rknn_metar[int(index_bkn_rknn):int(index_bkn_rknn)+6])
    elif rknn_metar.count("BKN") == 2:
        index_bkn_rknn = rknn_metar.find('BKN')
        list_cld_rknn.append(rknn_metar[int(index_bkn_rknn):int(index_bkn_rknn)+6])
        index_bkn2_rknn = rknn_metar.rfind('BKN')
        list_cld_rknn.append(rknn_metar[int(index_bkn2_rknn):int(index_bkn2_rknn)+6])
    elif rknn_metar.count("BKN") == 3:
        index_bkn_rknn = rknn_metar.find('BKN')
        list_cld_rknn.append(rknn_metar[int(index_bkn_rknn):int(index_bkn_rknn)+6])
        removed_rknn_metar = rknn_metar[int(index_bkn_rknn)+7:]
        index_bkn2_rknn = removed_rknn_metar.find('BKN')
        list_cld_rknn.append(removed_rknn_metar[int(index_bkn2_rknn):int(index_bkn2_rknn)+6])
        index_bkn3_rknn = removed_rknn_metar.rfind('BKN')
        list_cld_rknn.append(removed_rknn_metar[int(index_bkn3_rknn):int(index_bkn3_rknn)+6])
        
    if rknn_metar.count("OVC") == 1:
        index_ovc_rknn = rknn_metar.rfind('OVC')
        list_cld_rknn.append(rknn_metar[int(index_ovc_rknn):int(index_ovc_rknn)+6])
    elif rknn_metar.count("OVC") == 2:
        index_ovc_rknn = rknn_metar.find('OVC')
        list_cld_rknn.append(rknn_metar[int(index_ovc_rknn):int(index_ovc_rknn)+6])
        index_ovc2_rknn = rknn_metar.rfind('OVC')
        list_cld_rknn.append(rknn_metar[int(index_ovc2_rknn):int(index_ovc2_rknn)+6])
    elif rknn_metar.count("OVC") == 3:
        index_ovc_rknn = rknn_metar.find('OVC')
        list_cld_rknn.append(rknn_metar[int(index_ovc_rknn):int(index_ovc_rknn)+6])
        removed_rknn_metar = rknn_metar[int(index_ovc_rknn)+7:]
        index_ovc2_rknn = removed_rknn_metar.find('OVC')
        list_cld_rknn.append(removed_rknn_metar[int(index_ovc2_rknn):int(index_ovc2_rknn)+6])
        index_ovc3_rknn = removed_rknn_metar.rfind('OVC')
        list_cld_rknn.append(removed_rknn_metar[int(index_ovc3_rknn):int(index_ovc3_rknn)+6])
    cld_rknn = ' '.join(list_cld_rknn)
    return cld_rknn

def cld_rkny():
    list_cld_rkny = []
    if "CAVOK" in rkny_metar:
        list_cld_rkny.append("CAVOK")
    elif "NCD" in rkny_metar:
        list_cld_rkny.append("NCD")
    elif "SKC" in rkny_metar:
        list_cld_rkny.append("SKC")
    elif "FEW" in rkny_metar:
        index_few_rkny = rkny_metar.rfind('FEW')
        list_cld_rkny.append(rkny_metar[int(index_few_rkny):int(index_few_rkny)+6])
    
    if rkny_metar.count("SCT") == 1:
        index_sct_rkny = rkny_metar.rfind('SCT')
        list_cld_rkny.append(rkny_metar[int(index_sct_rkny):int(index_sct_rkny)+6])
    elif rkny_metar.count("SCT") == 2:
        index_sct_rkny = rkny_metar.find('SCT')
        list_cld_rkny.append(rkny_metar[int(index_sct_rkny):int(index_sct_rkny)+6])
        index_sct2_rkny = rkny_metar.rfind('SCT')
        list_cld_rkny.append(rkny_metar[int(index_sct2_rkny):int(index_sct2_rkny)+6])
    elif rkny_metar.count("SCT") == 3:
        index_sct_rkny = rkny_metar.find('SCT')
        list_cld_rkny.append(rkny_metar[int(index_sct_rkny):int(index_sct_rkny)+6])
        removed_rkny_metar = rkny_metar[int(index_sct_rkny)+7:]
        index_sct2_rkny = removed_rkny_metar.find('SCT')
        list_cld_rkny.append(removed_rkny_metar[int(index_sct2_rkny):int(index_sct2_rkny)+6])
        index_sct3_rkny = removed_rkny_metar.rfind('SCT')
        list_cld_rkny.append(removed_rkny_metar[int(index_sct3_rkny):int(index_sct3_rkny)+6])
        
    if rkny_metar.count("BKN") == 1:
        index_bkn_rkny = rkny_metar.rfind('BKN')
        list_cld_rkny.append(rkny_metar[int(index_bkn_rkny):int(index_bkn_rkny)+6])
    elif rkny_metar.count("BKN") == 2:
        index_bkn_rkny = rkny_metar.find('BKN')
        list_cld_rkny.append(rkny_metar[int(index_bkn_rkny):int(index_bkn_rkny)+6])
        index_bkn2_rkny = rkny_metar.rfind('BKN')
        list_cld_rkny.append(rkny_metar[int(index_bkn2_rkny):int(index_bkn2_rkny)+6])
    elif rkny_metar.count("BKN") == 3:
        index_bkn_rkny = rkny_metar.find('BKN')
        list_cld_rkny.append(rkny_metar[int(index_bkn_rkny):int(index_bkn_rkny)+6])
        removed_rkny_metar = rkny_metar[int(index_bkn_rkny)+7:]
        index_bkn2_rkny = removed_rkny_metar.find('BKN')
        list_cld_rkny.append(removed_rkny_metar[int(index_bkn2_rkny):int(index_bkn2_rkny)+6])
        index_bkn3_rkny = removed_rkny_metar.rfind('BKN')
        list_cld_rkny.append(removed_rkny_metar[int(index_bkn3_rkny):int(index_bkn3_rkny)+6])
        
    if rkny_metar.count("OVC") == 1:
        index_ovc_rkny = rkny_metar.rfind('OVC')
        list_cld_rkny.append(rkny_metar[int(index_ovc_rkny):int(index_ovc_rkny)+6])
    elif rkny_metar.count("OVC") == 2:
        index_ovc_rkny = rkny_metar.find('OVC')
        list_cld_rkny.append(rkny_metar[int(index_ovc_rkny):int(index_ovc_rkny)+6])
        index_ovc2_rkny = rkny_metar.rfind('OVC')
        list_cld_rkny.append(rkny_metar[int(index_ovc2_rkny):int(index_ovc2_rkny)+6])
    elif rkny_metar.count("OVC") == 3:
        index_ovc_rkny = rkny_metar.find('OVC')
        list_cld_rkny.append(rkny_metar[int(index_ovc_rkny):int(index_ovc_rkny)+6])
        removed_rkny_metar = rkny_metar[int(index_ovc_rkny)+7:]
        index_ovc2_rkny = removed_rkny_metar.find('OVC')
        list_cld_rkny.append(removed_rkny_metar[int(index_ovc2_rkny):int(index_ovc2_rkny)+6])
        index_ovc3_rkny = removed_rkny_metar.rfind('OVC')
        list_cld_rkny.append(removed_rkny_metar[int(index_ovc3_rkny):int(index_ovc3_rkny)+6])
    cld_rkny = ' '.join(list_cld_rkny)
    return cld_rkny

def cld_rkty():
    list_cld_rkty = []
    if "CAVOK" in rkty_metar:
        list_cld_rkty.append("CAVOK")
    elif "NCD" in rkty_metar:
        list_cld_rkty.append("NCD")
    elif "SKC" in rkty_metar:
        list_cld_rkty.append("SKC")
    elif "FEW" in rkty_metar:
        index_few_rkty = rkty_metar.rfind('FEW')
        list_cld_rkty.append(rkty_metar[int(index_few_rkty):int(index_few_rkty)+6])
    
    if rkty_metar.count("SCT") == 1:
        index_sct_rkty = rkty_metar.rfind('SCT')
        list_cld_rkty.append(rkty_metar[int(index_sct_rkty):int(index_sct_rkty)+6])
    elif rkty_metar.count("SCT") == 2:
        index_sct_rkty = rkty_metar.find('SCT')
        list_cld_rkty.append(rkty_metar[int(index_sct_rkty):int(index_sct_rkty)+6])
        index_sct2_rkty = rkty_metar.rfind('SCT')
        list_cld_rkty.append(rkty_metar[int(index_sct2_rkty):int(index_sct2_rkty)+6])
    elif rkty_metar.count("SCT") == 3:
        index_sct_rkty = rkty_metar.find('SCT')
        list_cld_rkty.append(rkty_metar[int(index_sct_rkty):int(index_sct_rkty)+6])
        removed_rkty_metar = rkty_metar[int(index_sct_rkty)+7:]
        index_sct2_rkty = removed_rkty_metar.find('SCT')
        list_cld_rkty.append(removed_rkty_metar[int(index_sct2_rkty):int(index_sct2_rkty)+6])
        index_sct3_rkty = removed_rkty_metar.rfind('SCT')
        list_cld_rkty.append(removed_rkty_metar[int(index_sct3_rkty):int(index_sct3_rkty)+6])
        
    if rkty_metar.count("BKN") == 1:
        index_bkn_rkty = rkty_metar.rfind('BKN')
        list_cld_rkty.append(rkty_metar[int(index_bkn_rkty):int(index_bkn_rkty)+6])
    elif rkty_metar.count("BKN") == 2:
        index_bkn_rkty = rkty_metar.find('BKN')
        list_cld_rkty.append(rkty_metar[int(index_bkn_rkty):int(index_bkn_rkty)+6])
        index_bkn2_rkty = rkty_metar.rfind('BKN')
        list_cld_rkty.append(rkty_metar[int(index_bkn2_rkty):int(index_bkn2_rkty)+6])
    elif rkty_metar.count("BKN") == 3:
        index_bkn_rkty = rkty_metar.find('BKN')
        list_cld_rkty.append(rkty_metar[int(index_bkn_rkty):int(index_bkn_rkty)+6])
        removed_rkty_metar = rkty_metar[int(index_bkn_rkty)+7:]
        index_bkn2_rkty = removed_rkty_metar.find('BKN')
        list_cld_rkty.append(removed_rkty_metar[int(index_bkn2_rkty):int(index_bkn2_rkty)+6])
        index_bkn3_rkty = removed_rkty_metar.rfind('BKN')
        list_cld_rkty.append(removed_rkty_metar[int(index_bkn3_rkty):int(index_bkn3_rkty)+6])
        
    if rkty_metar.count("OVC") == 1:
        index_ovc_rkty = rkty_metar.rfind('OVC')
        list_cld_rkty.append(rkty_metar[int(index_ovc_rkty):int(index_ovc_rkty)+6])
    elif rkty_metar.count("OVC") == 2:
        index_ovc_rkty = rkty_metar.find('OVC')
        list_cld_rkty.append(rkty_metar[int(index_ovc_rkty):int(index_ovc_rkty)+6])
        index_ovc2_rkty = rkty_metar.rfind('OVC')
        list_cld_rkty.append(rkty_metar[int(index_ovc2_rkty):int(index_ovc2_rkty)+6])
    elif rkty_metar.count("OVC") == 3:
        index_ovc_rkty = rkty_metar.find('OVC')
        list_cld_rkty.append(rkty_metar[int(index_ovc_rkty):int(index_ovc_rkty)+6])
        removed_rkty_metar = rkty_metar[int(index_ovc_rkty)+7:]
        index_ovc2_rkty = removed_rkty_metar.find('OVC')
        list_cld_rkty.append(removed_rkty_metar[int(index_ovc2_rkty):int(index_ovc2_rkty)+6])
        index_ovc3_rkty = removed_rkty_metar.rfind('OVC')
        list_cld_rkty.append(removed_rkty_metar[int(index_ovc3_rkty):int(index_ovc3_rkty)+6])
    cld_rkty = ' '.join(list_cld_rkty)
    return cld_rkty

def cld_rkth():
    list_cld_rkth = []
    if "CAVOK" in rkth_metar:
        list_cld_rkth.append("CAVOK")
    elif "NCD" in rkth_metar:
        list_cld_rkth.append("NCD")
    elif "SKC" in rkth_metar:
        list_cld_rkth.append("SKC")
    elif "FEW" in rkth_metar:
        index_few_rkth = rkth_metar.rfind('FEW')
        list_cld_rkth.append(rkth_metar[int(index_few_rkth):int(index_few_rkth)+6])
    
    if rkth_metar.count("SCT") == 1:
        index_sct_rkth = rkth_metar.rfind('SCT')
        list_cld_rkth.append(rkth_metar[int(index_sct_rkth):int(index_sct_rkth)+6])
    elif rkth_metar.count("SCT") == 2:
        index_sct_rkth = rkth_metar.find('SCT')
        list_cld_rkth.append(rkth_metar[int(index_sct_rkth):int(index_sct_rkth)+6])
        index_sct2_rkth = rkth_metar.rfind('SCT')
        list_cld_rkth.append(rkth_metar[int(index_sct2_rkth):int(index_sct2_rkth)+6])
    elif rkth_metar.count("SCT") == 3:
        index_sct_rkth = rkth_metar.find('SCT')
        list_cld_rkth.append(rkth_metar[int(index_sct_rkth):int(index_sct_rkth)+6])
        removed_rkth_metar = rkth_metar[int(index_sct_rkth)+7:]
        index_sct2_rkth = removed_rkth_metar.find('SCT')
        list_cld_rkth.append(removed_rkth_metar[int(index_sct2_rkth):int(index_sct2_rkth)+6])
        index_sct3_rkth = removed_rkth_metar.rfind('SCT')
        list_cld_rkth.append(removed_rkth_metar[int(index_sct3_rkth):int(index_sct3_rkth)+6])
        
    if rkth_metar.count("BKN") == 1:
        index_bkn_rkth = rkth_metar.rfind('BKN')
        list_cld_rkth.append(rkth_metar[int(index_bkn_rkth):int(index_bkn_rkth)+6])
    elif rkth_metar.count("BKN") == 2:
        index_bkn_rkth = rkth_metar.find('BKN')
        list_cld_rkth.append(rkth_metar[int(index_bkn_rkth):int(index_bkn_rkth)+6])
        index_bkn2_rkth = rkth_metar.rfind('BKN')
        list_cld_rkth.append(rkth_metar[int(index_bkn2_rkth):int(index_bkn2_rkth)+6])
    elif rkth_metar.count("BKN") == 3:
        index_bkn_rkth = rkth_metar.find('BKN')
        list_cld_rkth.append(rkth_metar[int(index_bkn_rkth):int(index_bkn_rkth)+6])
        removed_rkth_metar = rkth_metar[int(index_bkn_rkth)+7:]
        index_bkn2_rkth = removed_rkth_metar.find('BKN')
        list_cld_rkth.append(removed_rkth_metar[int(index_bkn2_rkth):int(index_bkn2_rkth)+6])
        index_bkn3_rkth = removed_rkth_metar.rfind('BKN')
        list_cld_rkth.append(removed_rkth_metar[int(index_bkn3_rkth):int(index_bkn3_rkth)+6])
        
    if rkth_metar.count("OVC") == 1:
        index_ovc_rkth = rkth_metar.rfind('OVC')
        list_cld_rkth.append(rkth_metar[int(index_ovc_rkth):int(index_ovc_rkth)+6])
    elif rkth_metar.count("OVC") == 2:
        index_ovc_rkth = rkth_metar.find('OVC')
        list_cld_rkth.append(rkth_metar[int(index_ovc_rkth):int(index_ovc_rkth)+6])
        index_ovc2_rkth = rkth_metar.rfind('OVC')
        list_cld_rkth.append(rkth_metar[int(index_ovc2_rkth):int(index_ovc2_rkth)+6])
    elif rkth_metar.count("OVC") == 3:
        index_ovc_rkth = rkth_metar.find('OVC')
        list_cld_rkth.append(rkth_metar[int(index_ovc_rkth):int(index_ovc_rkth)+6])
        removed_rkth_metar = rkth_metar[int(index_ovc_rkth)+7:]
        index_ovc2_rkth = removed_rkth_metar.find('OVC')
        list_cld_rkth.append(removed_rkth_metar[int(index_ovc2_rkth):int(index_ovc2_rkth)+6])
        index_ovc3_rkth = removed_rkth_metar.rfind('OVC')
        list_cld_rkth.append(removed_rkth_metar[int(index_ovc3_rkth):int(index_ovc3_rkth)+6])
    cld_rkth = ' '.join(list_cld_rkth)
    return cld_rkth

def cld_rkpu():
    list_cld_rkpu = []
    if "CAVOK" in rkpu_metar:
        list_cld_rkpu.append("CAVOK")
    elif "NCD" in rkpu_metar:
        list_cld_rkpu.append("NCD")
    elif "SKC" in rkpu_metar:
        list_cld_rkpu.append("SKC")
    elif "FEW" in rkpu_metar:
        index_few_rkpu = rkpu_metar.rfind('FEW')
        list_cld_rkpu.append(rkpu_metar[int(index_few_rkpu):int(index_few_rkpu)+6])
    
    if rkpu_metar.count("SCT") == 1:
        index_sct_rkpu = rkpu_metar.rfind('SCT')
        list_cld_rkpu.append(rkpu_metar[int(index_sct_rkpu):int(index_sct_rkpu)+6])
    elif rkpu_metar.count("SCT") == 2:
        index_sct_rkpu = rkpu_metar.find('SCT')
        list_cld_rkpu.append(rkpu_metar[int(index_sct_rkpu):int(index_sct_rkpu)+6])
        index_sct2_rkpu = rkpu_metar.rfind('SCT')
        list_cld_rkpu.append(rkpu_metar[int(index_sct2_rkpu):int(index_sct2_rkpu)+6])
    elif rkpu_metar.count("SCT") == 3:
        index_sct_rkpu = rkpu_metar.find('SCT')
        list_cld_rkpu.append(rkpu_metar[int(index_sct_rkpu):int(index_sct_rkpu)+6])
        removed_rkpu_metar = rkpu_metar[int(index_sct_rkpu)+7:]
        index_sct2_rkpu = removed_rkpu_metar.find('SCT')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_sct2_rkpu):int(index_sct2_rkpu)+6])
        index_sct3_rkpu = removed_rkpu_metar.rfind('SCT')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_sct3_rkpu):int(index_sct3_rkpu)+6])
        
    if rkpu_metar.count("BKN") == 1:
        index_bkn_rkpu = rkpu_metar.rfind('BKN')
        list_cld_rkpu.append(rkpu_metar[int(index_bkn_rkpu):int(index_bkn_rkpu)+6])
    elif rkpu_metar.count("BKN") == 2:
        index_bkn_rkpu = rkpu_metar.find('BKN')
        list_cld_rkpu.append(rkpu_metar[int(index_bkn_rkpu):int(index_bkn_rkpu)+6])
        index_bkn2_rkpu = rkpu_metar.rfind('BKN')
        list_cld_rkpu.append(rkpu_metar[int(index_bkn2_rkpu):int(index_bkn2_rkpu)+6])
    elif rkpu_metar.count("BKN") == 3:
        index_bkn_rkpu = rkpu_metar.find('BKN')
        list_cld_rkpu.append(rkpu_metar[int(index_bkn_rkpu):int(index_bkn_rkpu)+6])
        removed_rkpu_metar = rkpu_metar[int(index_bkn_rkpu)+7:]
        index_bkn2_rkpu = removed_rkpu_metar.find('BKN')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_bkn2_rkpu):int(index_bkn2_rkpu)+6])
        index_bkn3_rkpu = removed_rkpu_metar.rfind('BKN')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_bkn3_rkpu):int(index_bkn3_rkpu)+6])
        
    if rkpu_metar.count("OVC") == 1:
        index_ovc_rkpu = rkpu_metar.rfind('OVC')
        list_cld_rkpu.append(rkpu_metar[int(index_ovc_rkpu):int(index_ovc_rkpu)+6])
    elif rkpu_metar.count("OVC") == 2:
        index_ovc_rkpu = rkpu_metar.find('OVC')
        list_cld_rkpu.append(rkpu_metar[int(index_ovc_rkpu):int(index_ovc_rkpu)+6])
        index_ovc2_rkpu = rkpu_metar.rfind('OVC')
        list_cld_rkpu.append(rkpu_metar[int(index_ovc2_rkpu):int(index_ovc2_rkpu)+6])
    elif rkpu_metar.count("OVC") == 3:
        index_ovc_rkpu = rkpu_metar.find('OVC')
        list_cld_rkpu.append(rkpu_metar[int(index_ovc_rkpu):int(index_ovc_rkpu)+6])
        removed_rkpu_metar = rkpu_metar[int(index_ovc_rkpu)+7:]
        index_ovc2_rkpu = removed_rkpu_metar.find('OVC')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_ovc2_rkpu):int(index_ovc2_rkpu)+6])
        index_ovc3_rkpu = removed_rkpu_metar.rfind('OVC')
        list_cld_rkpu.append(removed_rkpu_metar[int(index_ovc3_rkpu):int(index_ovc3_rkpu)+6])
    cld_rkpu = ' '.join(list_cld_rkpu)
    return cld_rkpu


#------------------------------------------------------------------------#
def nosig():
    if rktl_airmet == "번호 현상 발표시각(UTC) 유효시간(UTC) 내용\n- - - - -":
        nosig_airmet_rktl = "NO AIRMET IN EFFECT"
    else:
        rktl_airmet_split = rktl_airmet.split("\n")
        del rktl_airmet_split[0]
        nosig_airmet_rktl = "".join(rktl_airmet_split)
        
    if rktl_sigmet == "번호 현상 발표시각(UTC) 유효시간(UTC) 내용\n- - - - -":
        nosig_sigmet_rktl = "NO SIGMET IN EFFECT"
    else:
        rktl_sigmet_split = rktl_sigmet.split("\n")
        del rktl_sigmet_split[0]
        nosig_sigmet_rktl = "".join(rktl_sigmet_split)
    return nosig_airmet_rktl, nosig_sigmet_rktl

def text_create():
    t1 = "안녕하십니까?\n"
    t2 = str(datetime.datetime.now().month) +"월 "+str(datetime.datetime.now().day) +"일 (" + str(days[day]) + ") 울진 주변 공항 기상 예보입니다.\n"
    t3 = "울진 북부 (RKNN, RKNY)\n"
    t4 = "- 바람 : " + rknn_winddir + rknn_windspd + "KT / " + rkny_winddir + rkny_windspd + "KT\n"
    t5 = "- 시정 : " + rknn_vis + " / " + rkny_vis +"\n"
    t6 = "- 구름 : " + rknn_cld + " / " + rkny_cld + "\n\n"
    t7 = "울진 서부 (RKTY)\n"
    t8 = "- 바람 : " + rkty_winddir + rkty_windspd + "KT\n"
    t9 = "- 시정 : " + rkty_vis +"\n"
    t10 = "- 구름 : " + rkty_cld + "\n\n"
    t11 = "울진 남부 (RKTH, RKPU)\n"
    t12 = "- 바람 : " + rkth_winddir + rkth_windspd + "KT / " + rkpu_winddir + rkpu_windspd + "KT\n"
    t13 = "- 시정 : " + rkth_vis + " / " + rkpu_vis +"\n"
    t14 = "- 구름 : " + rkth_cld + " / " + rkpu_cld + "\n\n"
    t15 = rktl_nosig_sigmet + "\n"
    t16 = rktl_nosig_airmet + "\n\n"
    t17 = "오늘도 안전 비행 부탁드립니다.\n"
    t18 = "감사합니다."
    text_final = t1+t2+t3+t4+t5+t6+t7+t8+t9+t10+t11+t12+t13+t14+t15+t16+t17+t18
    return text_final

def text_save():
    with open('아침보고.txt','w',encoding='UTF-8') as f:
        f.write(text_final)

def crop_sigmet():
    sigmet_img_path = os.getcwd() + './3_sigmet_'+ file_time +'.png'
    sigmet_img = Image.open(sigmet_img_path)
    sigmet_crop_img = sigmet_img.crop((30, 150, 800, 900)) # (left,upper,right,lower)
    sigmet_crop_img.save(sigmet_img_path)

def crop_airmet():
    airmet_img_path = os.getcwd() + './4_airmet_'+ file_time +'.png'
    airmet_img = Image.open(airmet_img_path)
    airmet_crop_img = airmet_img.crop((30, 150, 800, 900)) # (left,upper,right,lower)
    airmet_crop_img.save(airmet_img_path)

def crop_radar():
    radar_img_path = os.getcwd() + './5_radar_'+ file_time +'.png'
    radar_img = Image.open(radar_img_path)
    radar_crop_img = radar_img.crop((75, 250, 900, 1100)) # (left,upper,right,lower)
    radar_crop_img.save(radar_img_path)

def crop_naver():
    naver_img_path = os.getcwd() + './1_naver_'+ file_time +'.png'
    naver_img = Image.open(naver_img_path)
    naver_crop_img = naver_img.crop((50, 130, 700, 730)) # (left,upper,right,lower)
    naver_crop_img.save(naver_img_path)

#함수 실행 부분
metars = metar()
list_metars = list_metar()

rktl_metar = rktl()
rknn_metar = rknn()
rkny_metar = rkny()
rkty_metar = rkty()
rkth_metar = rkth()
rkpu_metar = rkpu()

# print(rktl_metar)
# print(rknn_metar)
# print(rkny_metar)
# print(rkty_metar)
# print(rkth_metar)
# print(rkpu_metar)

index_rktl, rktl_winddir, rktl_windspd = wind_rktl()
index_rknn, rknn_winddir, rknn_windspd = wind_rknn()
index_rkny, rkny_winddir, rkny_windspd = wind_rkny()
index_rkty, rkty_winddir, rkty_windspd = wind_rkty()
index_rkth, rkth_winddir, rkth_windspd = wind_rkth()
index_rkpu, rkpu_winddir, rkpu_windspd = wind_rkpu()

# print(rktl_winddir, rktl_windspd)
# print(rknn_winddir, rknn_windspd)
# print(rkny_winddir, rkny_windspd)
# print(rkty_winddir, rkty_windspd)
# print(rkth_winddir, rkth_windspd)
# print(rkpu_winddir, rkpu_windspd)

rktl_vis = vis_rktl()
rknn_vis = vis_rknn()
rkny_vis = vis_rknn()
rkty_vis = vis_rknn()
rkth_vis = vis_rknn()
rkpu_vis = vis_rknn()

# print(rktl_vis)
# print(rknn_vis)
# print(rkny_vis)
# print(rkty_vis)
# print(rkth_vis)
# print(rkpu_vis)

rktl_cld = cld_rktl()
rknn_cld = cld_rknn()
rkny_cld = cld_rkny()
rkty_cld = cld_rkty()
rkth_cld = cld_rkth()
rkpu_cld = cld_rkpu()

# print(rktl_cld)
# print(rknn_cld)
# print(rkny_cld)
# print(rkty_cld)
# print(rkth_cld)
# print(rkpu_cld)

tafs = taf()
# print(tafs)

rktl_airmet = airmet()
# print(rktl_airmet)

rktl_sigmet = sigmet()
# print(rktl_sigmet)

rktl_sigwx = sigwx()
rktl_radar = radar()
rktl_naver = naver()

rktl_nosig_airmet, rktl_nosig_sigmet = nosig()
text_final = text_create()
# print(text_final)
text_save()
crop_sigmet()
crop_airmet()
crop_radar()
crop_naver()