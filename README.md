# "퍼스널 컬러 스마트 미러"
> OpenCV, RaspberryPI3, Python2 이용하여 개발


 
## 1. 퍼스널 컬러 스마트 미러

## a. 프로젝트 설명


#### 1)	퍼스널 컬러란?

퍼스널 컬러란 타고난 개인의 신체 컬러를 말하며, 퍼스널 컬러 진단으로 개인에게 어울리는 계열의 컬러를 알 수 있다. 퍼스널 컬러의 계열 종류로는 봄 웜톤, 여름 쿨톤, 가을 웜톤, 겨울 쿨톤이 있다.

#### 2) 기존 퍼스널 컬러 진단은 어떻게 이루어지나?

  퍼스널 컬러 진단은 수십, 수백개의 천을 상체에 둘러보며 진행되며, 본인의 얼굴 색이 밝아지는 컬러가 본인에게 맞는 컬러이다. 기존의 퍼스널 컬러는 한번 진단에 8만원 정도로, 매우 비싸다.
  따라서, 퍼스널 컬러와 스마트 미러가 합쳐진 퍼스널 컬러 스마트 미러는 비용 절감 효과와 편리상을 갖추게 될 것 이다.

#### 3)	준비

#### SW :
OpenCV, Python2, Raspbarian OS

#### HW :
Raspberry PI 3, 2way Mirror(2 way mirror film+glass), Camera(Raspberry camera module v2), LED Monitor


#### 매핑시킬 색상 천 제작 :

<img width="600" alt="image" src="https://user-images.githubusercontent.com/41661879/55071159-2b817b80-50cb-11e9-8ad8-4a3e329a9cc0.png">

<img width="682" alt="매핑천제작" src="https://user-images.githubusercontent.com/41661879/55075310-fa5a7880-50d5-11e9-8380-dc5d2fdf9ed8.png">


## b. 시연

흰 목폴라 위로 매칭 천이 덧대어지며 퍼스널 컬러 확인.

<img width="249" alt="시연" src="https://user-images.githubusercontent.com/41661879/55073812-0fcda380-50d2-11e9-942f-11c2fea1d1c5.png">


## c. 문제 해결

#### 1) Raspbarian OS 설치 문제 (부팅 미시행-모니터 아무 화면도 안 들어옴) :
SD카드 리더기를 사용하지 말고, 라즈베리파이 본체에 있는 SD카드 슬롯에 직접 넣을 것.


#### 2) OpenCV 다운로드 문제 : 
인터넷이 끊겼는지 확인할 것. 계속 서버를 이용해서 패키지 다운로드 중이었더라도 인터넷이 갑자기 끊길 수 있음.

#### 3) OpenCV 빌드 문제 : 
make clean하고 빌드 포맷하고 다시 빌드 환경설정 및 빌드할 것.
(빌드 한 번 소요시간 1시간 반 이상. 인내심 필요)

#### 4) 라즈베리파이 카메라 인식 문제 : 
라즈베리파이 펌웨어 업그레이드 + config.txt에 추가 문장들 필요.

#### 참고 : http://cafe.naver.com/studyonarduino/3100


####	- 라즈베리파이 펌웨어 업데이트 하기 위한 다운로드 명령 입력
```$ sudo wget http://goo.gl/1BOfJ -O /usr/bin/rpi-update```

####	- 다운로드 받은 파일을 /usr/bin 폴더에 저장. 따라서 해당 디렉토리로 이동

```$ cd /usr/bin```

####	 - 다운로드 받은 파일(rpi-update)의 특성을 보기 위해 아래와 같이 명령

```
$ ls -l rpi* 
-rwxr-xr-x 1 root root 10666 Feb 11 04:13 rpi-update 
```

위와 같이 나오면 실행 가능

####	- 다음 명령어를 실행
```$ sudo rpi-update```

####	- 재부팅
```$ sudo reboot```

####	 - /boot/config.txt 파일을 열어서 

```vi $ sudo vi /boot/config.txt```

####	- 파일의 맨 마직막에 아래 세 줄을 추가
```
gpu_mem=128
start_file=start_x.elf
fixup_file=fixup_x.dat
```

####	- 위 파일을 저장하고 나온 다음(:wq) 재부팅  
```$ sudo reboot```



## 2. 개발자 정보

홍정수
  
## 3. 최종 업데이트 날짜

2016.12
