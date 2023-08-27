# Beep--
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


### 실행방법(제일 최신)
1. git clone https://github.com/hyeyeoung/Beeeep--
2. pip install -r requriements.txt
3. mkdir data
4. python get_data.py --get_links

### 위방법대로 실행 안되면, 원본 레파지토리 clone 후 아래 명령어 실행

1. pip install --upgrade numpy Cython
2. pip install pandas
3. pip install pytube
4. pip install moviepy
5. pip install librosa
6. pip install matplotlib
7. mkdir data
8. run 명령어
- python get_data.py --get_links

### 08.27 수정사항
1. requirements.txt 변경
2. pysrt 추가 해야함(추가하면 추가한 사람이 이 문장 삭제 ㄱㄱ)