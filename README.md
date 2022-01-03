# MalPdf-Detection

### 사용된 기술스택
- flask
- docker
- ELK (elastic search, logstash, kibana)
- sklearn

### 원리
1. 준비된 bulk 정상 pdf / 악성 pdf 들을 각각 hidost 라이브러리를 이용해 구조 분석 
2. hidost 분석 결과 저장 후 randomforest 이용해 모델 학습 
3. 새로운 pdf 를 웹에 업로드 
4. 해당 pdf 구조를 hidost 로 다시 분석 
5. 모델에 넣어 결과 출력 
6. elk로 결과 로그 생성
