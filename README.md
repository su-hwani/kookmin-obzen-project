# Kookmin unversity & Obzen collaboration project
<p align="center">
  <img width="200" height="80" alt="스크린샷 2024-01-11 오후 2 35 43" src="https://github.com/su-hwani/kookmin-obzen-project/assets/54920289/8a049608-0ed8-447b-a63a-57cc1bbcdfb5">
</p>

## 국민대학교 & (주)오브젠 산학 협력 프로젝트
> **기간: 2023.06 ~ 2023.12** <br/>
> **인원: 국민대학교 소프트웨어학부 재학생 4명** <br/>
> **목표: 오브젠 회사와 협력하여 자연어 타겟팅으로 고객 데이터를 분석하고 비교하여 효과적인 타겟 마케팅을 수행하는 부분 구현을 목표로 했습니다.**<br/>

## 프로젝트 소개 

> #### ⭐️ 최적의 고객 타겟팅 & AI 기반 자동화 <br/>
> **오브젠의 Digital Marketing은 캠페인 아이디어의 자유로운 설계와 실시간 마케팅, 개인화 마케팅의 통합 실행을 지원하는 자동화 솔루션으로,<br/>
> 고객 경험을 향상시키는 데 핵심적인 역할을 합니다.<br/>
> 특히 Obzect Flow Designer를 활용하여 고객의 속성과 반응에 따라 개인화된 마케팅 경로를 설계하고 실행합니다.<br/>
> 이를 통해 다음과 같은 핵심 목표를 달성하고자 합니다.<br/>**
<br/>
<img width="400"  alt="스크린샷 2024-01-11 오후 4 02 33" src="https://github.com/su-hwani/kookmin-obzen-project/assets/54920289/f1d4d824-cac2-4569-9219-c7f297a2ef5d">



## Stacks 🐈
### Environment
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-007ACC?style=for-the-badge&logo=Visual%20Studio%20Code&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white)
![Github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)             

### Client
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=Typescript&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
### Server
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![MariaDB](https://img.shields.io/badge/MariaDB-003545?style=for-the-badge&logo=MariaDB&logoColor=white)
![AWSEC2](https://img.shields.io/badge/AmazonEC2-FF9900?style=for-the-badge&logo=AmazonEc2&logoColor=white)
![AWSRDS](https://img.shields.io/badge/AmazonRDS-527FFF?style=for-the-badge&logo=AmazonRDS&logoColor=white)
![NGINX](https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=NGINX&logoColor=white)
### Communication
![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=Slack&logoColor=white)
![Notion](https://img.shields.io/badge/Notion-000000?style=for-the-badge&logo=Notion&logoColor=white)
![Zoom](https://img.shields.io/badge/Zoom-0B5CFF?style=for-the-badge&logo=Zoom&logoColor=white)

## 화면 구성 📺
| 메인 페이지 | 대화 페이지|
| :-------------------------------------------: | :------------: |
| <img width="329" alt="스크린샷 2024-01-11 오후 3 47 13" src="https://github.com/su-hwani/kookmin-obzen-project/assets/54920289/c7151c9c-f279-4378-a149-a018b5f7a0f2">| <img width="329" alt="스크린샷 2024-01-11 오후 3 47 26" src="https://github.com/su-hwani/kookmin-obzen-project/assets/54920289/8466d918-8e2d-4ab9-b787-6055f5c03390">|
| sql 페이지 | 그래프 페이지|
|<img width="329" alt="스크린샷 2024-01-11 오후 3 46 45" src="https://github.com/su-hwani/kookmin-obzen-project/assets/54920289/db0df956-01fc-45ff-926d-d5d931436840">|<img width="329" alt="스크린샷 2024-01-11 오후 3 46 55" src="https://github.com/su-hwani/kookmin-obzen-project/assets/54920289/71b84e3c-784d-4cfe-a363-501ac2590fc4">|
| 실사용 예시1 | 실사용 예시2 |
|<img width="329" alt="스크린샷 2024-01-11 오후 3 48 08" src="https://github.com/su-hwani/kookmin-obzen-project/assets/54920289/4e6339be-38d1-43db-bc97-4421efa1b881">|<img width="329" alt="스크린샷 2024-01-11 오후 3 48 23" src="https://github.com/su-hwani/kookmin-obzen-project/assets/54920289/8e9acdf8-319e-48df-8b63-83cfe721cd3d">|


## 동작 시나리오

> **1.  사용자는 웹페이지를 통해 자연어로 질문을 입력합니다.<br/>
> 2.  입력된 자연어 질의 내용은 웹 서버로 전달됩니다.<br/>
> 3.  웹 서버는 받은 질의를 Chat GPT API로 전송하여 처리를 요청합니다.<br/>
> 4.  Chat GPT는 미리 학습된 서비스 데이터베이스를 기반으로 사용자의 자연어 질의를 처리하고, 이를 토대로 관련된 쿼리를 생성합니다.<br/>
> 5.  Chat GPT는 생성된 쿼리를 웹 서버로 반환합니다.<br/>
> 6.  웹 서버는 받은 쿼리를 데이터베이스에 전달하여 해당 쿼리를 실행하고 결과를 가져옵니다.<br/>
> 7.  데이터베이스는 Chat GPT의 응답에 필요한 데이터를 제공하고, 이 데이터를 웹 서버로 반환합니다.<br/>
> 8.  웹 서버는 받은 데이터를 그래프로 시각화하고 숫자로 변환하여 사용자에게 제공합니다.<br/>
> 9.  사용자는 질의 응답 결과를 시각적으로 확인하고 데이터를 분석할 수 있습니다.**<br/>

## 디렉토리 구조
```
./
├── README.md
├── package-lock.json
├── package.json
├── public/
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   └── robots.txt
├── server/
│   ├── README.md
│   ├── __pycache__/
│   │   └── main.cpython-310.pyc
│   ├── db/
│   │   ├── __pycache__/
│   │   ├── db.py
│   │   ├── model_chat.py
│   │   ├── model_chatAnswer.py
│   │   ├── model_chatQuestion.py
│   │   ├── model_chatRoom.py
│   │   ├── model_session.py
│   │   ├── obzen_fakedata.sql
│   │   └── scheduler.py
│   ├── main.py
│   ├── requirements.txt
│   └── routes/
│       ├── JSON_format.py
│       ├── __pycache__/
│       ├── chatAnswer.py
│       ├── chatQuestion.py
│       ├── chatRoom.py
│       ├── chats.py
│       ├── search.py
│       └── session.py
├── src/
│   ├── App.css
│   ├── App.test.tsx
│   ├── App.tsx
│   ├── components/
│   │   ├── Chat.tsx
│   │   ├── DashBoard.tsx
│   │   ├── Header.tsx
│   │   ├── NewChatForm.tsx
│   │   ├── chat_list/
│   │   └── graph/
│   ├── index.css
│   ├── index.tsx
│   ├── logo.svg
│   ├── network/
│   │   └── http.js
│   ├── react-app-env.d.ts
│   ├── reportWebVitals.ts
│   ├── service/
│   │   └── chat.ts
│   └── setupTests.ts
├── tailwind.config.js
├── tsconfig.json
└── yarn.lock
```
