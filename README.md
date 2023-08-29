# 실시간 음성 비속어 필터링 프로젝트
### 공개SW 개발자 대회에서 진행된 프로젝트입니다.


# 0. 환경세팅

1. 파이썬 버전 3.7.x 준비.(Conda 사용 추천)
2. 자기 크롬에 맞는 크롬드라이버 준비. (크롬 업데이트하면 116.0.xxxx.xxx니까 레파지토리에 있는거 그대로 사용해도 됨)
3. 크롬드라이버는 get_data와 동일한 경로에 위치

# 1. 실행

0. 터미널에 `pip install --upgrade pip` 실행 -> pip 최신버전으로 업그레이드
1. 터미널에 `pip install -r requirements.txt` 명령어 실행
2. 터미널에 `mkdir data` 명령어 실행
3. data 폴더에 각자 전달받은 csv파일 넣기
4. 터미널에 `python get_data.py --get_videos` 실행 -> video가 제대로 다운되는지 확인
5. 터미널에 `python get_data.py --get_texts` 실행 -> **크롤링이 제대로 확인되고 있는지 확인**, text폴더 확인
6. 터미널에 `python get_data.py --get_audios` 실행 -> 오디오가 클립대로 잘 분리되고 있는지 확인
7. 터미널에 `python get_data.py --labeling` 실행
9. 터미널에 `python get_data.py --save_label`
9. 터미널에서 자막 라벨링
10. 터미널에 `python get_data.py --get_images` 실행 -> mel spectrom이 잘 다운됐는지 확인

# 3. 주의사항
* 만약 라이브러리 설치 중 라이브러리 업데이트 해라는 문구가 뜨면 그냥 업데이트하면됨.

---
# Beep-- ref
### 제 9회 투빅스 컨퍼런스의 일환으로 진행된 프로젝트 입니다.
[발표자료](http://www.datamarket.kr/xe/board_pdzw77/63632)  
  
[발표동영상](https://www.youtube.com/watch?v=n1BqCii2yVU)

#### 1) 목표
    - 한국어 욕설 음성 필터링

#### 2) 데이터 준비
  1) 유튜브에서 음성 얻기  
    - `get_data.py`  
  2) 음성 클래스 별로 분해하기  
    - `audio_label_cliping.ipynb`   
  3) Overlay을 통해 데이터 Generations  
    - `make_train_by_overlay.ipynb`  
    
#### 3) 학습    
   1) Colab을 통해 학습  
    - `Trigger word detection.ipynb`  
    
#### 4) 구현
   1) 유튜브 url을 넣으면, 필터링 된 동영상 Return  
    - `demo.py`

  
## 세부사항

### 폴더 경로

`./data`  

`./data/video`  
- blahblah.mp4  
  
`./data/audio`  
- blahblah.wav  
- blahblah_0.wav  

`./data/text`  
- blahblah.txt  

`./data/label`  
- blahblah_0.txt  
- blahblah_0.wav  

`./data/audio_label_clip`  
- background_0.wav  
- negative_0.wav  
- positive_0.wav  

`./data/train_audios`  
- mix_0.wav  

`./data/XY_train`  
- x_0.npy
- y_0.npy



### ref
https://github.com/Tony607/Keras-Trigger-Word

