

# 데이터 청년 캠퍼스 - 동국대학교
<img width="1456" alt="page01" src="https://user-images.githubusercontent.com/69189272/187603814-30042793-13a7-43cf-806f-783ee24ba147.png">

- ### 팀명 : 다람쥐 오래걷기
- ### 주제명 : 생태통로 효율성 추정 및 주요 요인 분석
  - 야생동물 서식지와 활동영역의 단절화로 인해 로드킬이 빈번히 발생하고 있다. 이를 방지하기 위해서는 효율적인 생태통로 운영이 필요한 실정이다. 따라서 본 프로젝트에서는, 효율성이 일정 수준 이상인 생태통로를 바탕으로 효율성이 낮은 생태통로의 개선을 목표로 데이터 분석을 진행한다.

## 0. 실행 환경 및 의존성
- OS : Windows 11 or macOS 12.3.1
- Python version : 3.8
- Anaconda version : 4.11.0
- Dependencies
  ```shell
  $ conda env create -f requirements.yaml
  
  $ conda activate datacampus_dao
  ```

## 1-1. [Preprocessing](https://github.com/TeamHKL/datacampus_dao/tree/main/preprocessing) 코드 설명
- ### DB.py
  - AWS RDS를 연결하여 데이터를 불러오거나 내보내는 코드
- ### 0. vworld 산책로 Open API.ipynb
  - 브이월드 api로 산책로 데이터를 불러와 '산책로_2013.csv' 파일로 저장하는 코드
- ### 0. 생태통로 네트워크 크롤링.ipynb
  - 국립생태원 생태통로 네트워크에서 전국의 생태통로 이름, 위경도, 모니터링 등의 정보를 크롤링하는 코드
  - Selenium이 실행되지 않는 경우 chrome 브라우저 버전과 [chromedriver.exe](https://chromedriver.chromium.org/downloads) 간 버전이 일치하는지 확인
- ### 1. 생태통로 전처리.ipynb
  - 생태통로 데이터의 결측치 처리, 라벨링 및 규격 데이터를 추가하는 코드
  - maindata_수정.csv, 생태통로_국립생태원PDF.csv, 생태통로_환경부PDF.csv, 생태통로_규격계산.csv 파일이 필요합니다.
- ### 2. 경사도.ipynb
  - QGIS로 추출한 경사도 데이터를 전처리 하는 코드
  - 경사도.csv 파일이 필요합니다.
- ### 2. 교통량, 국토환경성평가, 건물까지거리.ipynb
  - 각 생태통로에서 7.82km 이내에 있는 도로의 교통량(AADT)의 평균 값을 구하는 코드
  - QGIS로 추출한 생태통로 좌표의 국토환경성평가 등급과, 측정된 건물까지 최단 거리 데이터를 추가하는 코드
  - 2021년 도로 종류별 교통량 및 X.Y좌표.xlsx, 국토환경성 평가지도 병합.csv, 건물까지거리_병합.csv 파일이 필요합니다.
- ### 2. 농가까지의 거리(km).ipynb
  - 생태통로와 농가 간의 최단 거리를 구하는 코드
  - 경지계1-3.csv, 경지계4-7.csv 파일이 필요합니다.
- ### 2. 도로 최고제한속도.ipynb
  - 생태통로가 속하는 도로의 제한 속도를 구하는 코드
  - 생태통로현황_2022.csv 파일이 필요합니다. (+ 한국도로공사_고속도로_제한최고속도_220331.pdf 파일 참고)
- ### 2. 등산로.ipynb
  - 생태통로와 등산로 간 최단 거리를 구하는 코드
  - 등산로_join.csv 파일이 필요합니다.
- ### 2. 산책로까지의 최단 거리(km).ipynb
  - 생태통로와 주변 산책로 간 최단 거리를 구하는 코드
  - 산책로_2013.csv 파일이 필요합니다.
- ### 2. 식생 라벨링.ipynb
  - QGIS로 추출한 생태통로 2.3km 내의 식물군락명 라벨링 하는 코드
  - 식생_join.csv 파일이 필요합니다.
- ### 2. 유도울타리.ipynb
  - 각 생태통로에서 2.3km 이내의 모든 유도울타리의 연장과 높이를 구하는 코드 (없는 경우 결측치로 대체)
  - 유도울타리현황_2021.csv, 한국도로공사_도로중심선.csv 파일이 필요합니다.
- ### 2. 주변 로드킬 빈도.ipynb
  - 각 생태통로에서 2.3km 이내의 로드킬 빈도를 구하는 코드
  - 한국도로공사_로드킬데이터_2021.csv 파일이 필요합니다.
- ### 2. 지형경관.ipynb
  - 각 생태통로에서 2.3km 이내의 지형경관 특성을 가져오는 코드 (2.3km 이상 떨어질 경우 결측치로 대체)
  - 지형경관_join.csv 파일이 필요합니다.
- ### 2. 포유류.ipynb
  - 목표종(멧돼지,고라니,노루,너구리,오소리,족제비,멧토끼,청설모,다람쥐) 중 생태통로 주변에 얼마나 많은 종의 동물이 서식하는지, 출현빈도는 어떤지 구하는 코드
  - Markdown 셀들은 Google Colab 환경에서 포유류_join.csv 파일을 생성하기 위한 과정
  - Google Colab으로 생성한 포유류_join.csv 파일이 필요합니다.
- ### 2. 하천거리.ipynb
  - 생태통로와 주변 하천 간 최단 거리를 구하는 코드
  - 하천_join.csv 파일이 필요합니다.
- ### 3. maindata 합.ipynb
  - 생태통로 데이터와 변수들의 데이터를 병합하여 메인 데이터를 완성하는 코드
- ### 4. EDA.ipynb
  - 각 변수들의 분포 특성을 파악하기 위한 EDA 코드
- ### 5. 전처리 및 효율성 추정(Pycaret).ipynb
  - 메인 데이터를 전처리 하고 생태통로 효율성의 '판단불가' 값을 추정하는 코드
  - Google Colab 환경에서 실행해야 합니다.
  - Package install & Import 실행 후, 설치 버전 적용을 위해 런타임 다시 시작 및 코드 재실행 필요

## 1-2. [Analysis](https://github.com/TeamHKL/datacampus_dao/tree/main/analysis) 코드 설명
- ### Analytics_on_colab.ipynb
  - AutoML인 pycaret을 이용해 육교형, 터널형 생태통로별 최적의 모델을 선정하고 분류 분석을 수행하는 코드
  - 변수 중요도 확인 후, Top 10개의 주요 요인을 임의로 개선해 개선율을 예측함으로써 해당 모델의 유효성을 확인
  - Google Colab 환경에서 실행해야 합니다.
  - Package 설치 후, 설치 버전 적용을 위해 런타임 다시 시작 및 코드 재실행 필요

## 2. 실행 순서
1. [requirements.yaml](https://github.com/TeamHKL/datacampus_dao/data/requirements.txt)을 이용해 필요한 패키지 설치
2. preprocessing의 코드들을 파일명 앞 숫자의 순서대로 실행
3. analysis의 코드 실행
