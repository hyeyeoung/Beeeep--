# # Voyagerx 를 통한 자막 추출  
# 
# ###   환경 :
#     1) 윈도우  + python 3.7.x  
#     2) 현재 디렉토리에 Chrome_webdriver 존재
#     3) 현재 디렉토리 중 하위 폴더 (movie)에 동영상 파일만 존재  
#     4) 다운로드는 디폴트로 설정된 곳으로 바로 다운로드 됨  

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from tqdm import tqdm_notebook
import time
import pywinauto
import os
import shutil

# 크롬 드라이버 옵션
options = webdriver.ChromeOptions()
options.add_argument('headless')

def crawling(df, chrome_dir, links_videos_texts_dir):
    save_file = links_videos_texts_dir
    with open(save_file, 'a') as f:
        f.write('links,videos,texts\n')

    browser = webdriver.Chrome(chrome_dir, options=options)
    ## 자막 추출사이트 변경
    browser.get('https://downsub.com/') 
    wait = WebDriverWait(browser, 15)
    # try:
    #     element = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="input-34"]')))
    #     # browser.find_element_by_class_name('close').click()
    #     element.click()
    # except:
    #     print("error! next code")
    # time.sleep(5)
    print('-'*50)

    # 크롤링 루프
    print(df)
    for idx, row in df.iterrows():
        print(idx)
        video = row['videos'][11:]
        print(video,'추출')
        video = video.split(os.sep)[-1].split(".")[0]
        
        # 기본 변수 생성
        # 이 부분부터 수정 ㄱㄱ
        # path = os.path.join(os.getcwd(), video)
        # check = browser.find_elements_by_class_name('word')[:10]
        # new_check = browser.find_elements_by_class_name('word')[:10]
        # # 파일 탭으로 이동
        # browser.find_element_by_tag_name('button').click()
        
        # 다운로드 탭으로 이동 & 자막 생성
        link = row['links']
        browser.get(f'https://downsub.com/?url={link}')
        browser.implicitly_wait(15)
        
        # 자막 다운로드
        wait = WebDriverWait(browser, 10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/main/div/div[2]/div/div[1]/div[1]/div[2]/div[1]/button[1]')))
        try:
            print("다운로드 시작")
            element.click()
            time.sleep(15) # 자막 다운로드 대기
            print("다운로드 완료")
        except:
            print("다운로드 실패")
            return  
        
        # 자막 파일 이름 변경
        download_path = "c:/Users/{}/Downloads".format(os.getlogin())
        new_filename = os.path.join(".", "data", "text", video + ".srt")
        filename = max([download_path + "/" + f for f in os.listdir(download_path)], key=os.path.getctime)
        shutil.move(os.path.join(download_path, filename), new_filename)
        print("폴더 변경 완료")
        
        # 자막 링크 파일 쓰기
        with open(save_file, 'a') as f:
            f.write('{},{},{}\n'.format(row['links'], row['videos'], new_filename))
        print("자막 링크 파일 쓰기 완료")
        print('-'*50) 

        # # 업로드 실행
        # time.sleep(1)
        # app = pywinauto.application.Application().connect(title_re='열기')
        # app.열기.Edit.SetText(path)
        # time.sleep(1)
        # app.열기.Button.click()
        # try :
        #     app.열기.Button.click()
        # except:
        #     pass

        # # 변환 확인
        # wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'blue-button')))
        # browser.find_element_by_class_name('blue-button').click()
        # new_check = browser.find_elements_by_class_name('word')[:10]

        # i=0
        # while check == new_check:
        #     new_check = browser.find_elements_by_class_name('word')[:10]
        #     print(i*30,' 초째아직 추출중')
        #     i += 1
        #     time.sleep(30)

    
        # # 파일 탭에서 추출 누르기, 전체화면 이어야 함
        # browser.find_element_by_tag_name('button').click() # 탭
        # browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/div[7]').click()
        # browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div[2]/div[1]/div[1]/ul/li[2]/div/button').click()   
        # browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/label/span[1]').click()
        # browser.find_element_by_class_name('blue-button').click() 
        # print('추출완료')
        # time.sleep(10)
        # text_file = save_text(video)
        # with open(save_file, 'a') as f:
        #     f.write('{},{},{}\n'.format(row['links'], row['videos'], text_file))
        # print("저장완료")
        # print('-'*50)       

