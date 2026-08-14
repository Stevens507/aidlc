# AI-DLC 기반 웅진씽크빅 북큐레이터 AI 에이전트 구축 | AWS 기술 블로그

# AI-DLC 기반 웅진씽크빅 북큐레이터 AI 에이전트 구축

by Jaeyoung Ha, Daeun Lee, Sewoong Kim, and Yongduck Hong on 12 2월 2026 in [Amazon Bedrock](https://aws.amazon.com/ko/blogs/tech/category/artificial-intelligence/amazon-machine-learning/amazon-bedrock/ "View all posts in Amazon Bedrock"), [Amazon Q Developer](https://aws.amazon.com/ko/blogs/tech/category/amazon-q/amazon-q-developer/ "View all posts in Amazon Q Developer"), [Customer Solutions](https://aws.amazon.com/ko/blogs/tech/category/post-types/customer-solutions/ "View all posts in Customer Solutions"), [Intermediate (200)](https://aws.amazon.com/ko/blogs/tech/category/learning-levels/intermediate-200/ "View all posts in Intermediate \(200\)"), [Kiro](https://aws.amazon.com/ko/blogs/tech/category/artificial-intelligence/kiro/ "View all posts in Kiro") [Permalink](https://aws.amazon.com/ko/blogs/tech/aws-aidlc-woongjinthinkbig-tech-blog/) Share

  * [](https://www.facebook.com/sharer/sharer.php?u=https://aws.amazon.com/ko/blogs/tech/aws-aidlc-woongjinthinkbig-tech-blog/)
  * [](https://twitter.com/intent/tweet/?text=AI-DLC%20%EA%B8%B0%EB%B0%98%20%EC%9B%85%EC%A7%84%EC%94%BD%ED%81%AC%EB%B9%85%20%EB%B6%81%ED%81%90%EB%A0%88%EC%9D%B4%ED%84%B0%20AI%20%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8%20%EA%B5%AC%EC%B6%95&via=awscloud&url=https://aws.amazon.com/ko/blogs/tech/aws-aidlc-woongjinthinkbig-tech-blog/)
  * [](https://www.linkedin.com/shareArticle?mini=true&title=AI-DLC%20%EA%B8%B0%EB%B0%98%20%EC%9B%85%EC%A7%84%EC%94%BD%ED%81%AC%EB%B9%85%20%EB%B6%81%ED%81%90%EB%A0%88%EC%9D%B4%ED%84%B0%20AI%20%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8%20%EA%B5%AC%EC%B6%95&source=Amazon%20Web%20Services&url=https://aws.amazon.com/ko/blogs/tech/aws-aidlc-woongjinthinkbig-tech-blog/)
  * [](mailto:?subject=AI-DLC%20%EA%B8%B0%EB%B0%98%20%EC%9B%85%EC%A7%84%EC%94%BD%ED%81%AC%EB%B9%85%20%EB%B6%81%ED%81%90%EB%A0%88%EC%9D%B4%ED%84%B0%20AI%20%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8%20%EA%B5%AC%EC%B6%95&body=AI-DLC%20%EA%B8%B0%EB%B0%98%20%EC%9B%85%EC%A7%84%EC%94%BD%ED%81%AC%EB%B9%85%20%EB%B6%81%ED%81%90%EB%A0%88%EC%9D%B4%ED%84%B0%20AI%20%EC%97%90%EC%9D%B4%EC%A0%84%ED%8A%B8%20%EA%B5%AC%EC%B6%95%0A%0Ahttps://aws.amazon.com/ko/blogs/tech/aws-aidlc-woongjinthinkbig-tech-blog/)
  * 


## “2일 만에 AI 에이전트의 MVP를 만들 수 있을까요?”

2025년 12월, 웅진씽크빅과 함께 AWS AI-DLC 워크숍(Unicorn Gym)을 진행하면서 이 질문에 대한 답을 찾았습니다. 결론부터 말하면, 가능했습니다. [AI-DLC(AI-Driven Development Life Cycle)](https://aws.amazon.com/ko/blogs/tech/ai-driven-development-life-cycle/) 방법론을 적용하여 북큐레이터를 위한 AI 에이전트의 MVP를 단 2일 만에 완성했고, 약 한 달간의 고도화를 거쳐 2026년 1월 베타 서비스를 오픈했습니다.

이 글에서는 AI와 개발자가 협업하는 새로운 개발 방법론인 AI-DLC를 실제 프로젝트에 어떻게 적용했는지, 그 과정에서 어떤 도전과 성과가 있었는지를 공유합니다.

## 웅진씽크빅 소개

## ![](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2026/02/12/Screenshot-2026-02-12-at-1.21.07 PM.png)

웅진씽크빅은 교육 산업 분야에서 혁신적인 디지털 교육 솔루션을 제공하는 선도 기업입니다. 웅진씽크빅은 최신 기술을 활용하여 학생들에게 개인화된 학습 경험을 제공하고 있으며, 이를 통해 교육의 질을 향상시키고 학습 효과를 극대화하는 데 주력하고 있습니다.

웅진씽크빅은 2019년 AWS 클라우드 인프라를 기반으로 맞춤형 학습 서비스를 출시했습니다. 이 서비스는 인공지능 기술과 통합 데이터 분석 플랫폼을 활용하여 각 학생의 학습 패턴과 수준에 맞는 최적화된 교육 콘텐츠를 제공합니다. AWS의 확장 가능하고 안정적인 클라우드 환경을 통해 웅진씽크빅은 대규모 사용자에게 끊김 없는 서비스를 제공하면서도 운영 효율성을 크게 향상시킬 수 있었습니다. 이러한 디지털 전환을 통해 웅진씽크빅은 전통적인 교육 방식을 혁신하고, 학생들에게 더욱 효과적이고 접근성 높은 학습 환경을 제공하는 데 성공했습니다.

## 웅진씽크빅이 풀고 싶었던 문제

웅진씽크빅의 북큐레이터를 아시나요? 웅진 북큐레이터는 웅진북클럽의 회원제 독서·학습 맞춤 큐레이션 서비스를 제공하는 전문 컨설턴트입니다. 북큐레이터는 고객의 자녀 연령과 독서 수준을 진단하고, 개인별 맞춤 독서 플랜을 설계하여 체계적인 독서 습관 형성을 지원합니다. 지국장은 이러한 북큐레이터들을 관리하고 코칭하는 역할을 맡고 있습니다.

현장에서 만난 북큐레이터들과 지국장들은 몇 가지 공통된 어려움을 토로했습니다.

역할 | 문제 | 현장의 목소리  
---|---|---  
북큐레이터 | 고객 데이터 분산 | “고객 정보가 여기저기 흩어져 있어서 상담 전에 정리하는 데만 시간이 많이 걸려요.”  
| 상담 기록 부재 | “상담하고 나면 내용을 정리해야 하는데, 다음 고객 만나러 이동하느라 바빠서 제대로 못 해요.”  
지국장 | 코칭 근거 부족 | “북큐레이터들 개별 코칭을 해주고 싶은데, 상담 이력이 없으니 뭘 어떻게 도와줘야 할지 모르겠어요.”  
  
가망(예상)고객 데이터가 지인 소개, 박람회, 온라인 행사 등 다양한 경로로 들어오지만 체계적으로 관리되지 않았습니다. 상담 기록도 마찬가지였습니다. 특히 차량으로 이동하면서 통화하는 경우가 많아, 상담 내용을 따로 정리하기가 현실적으로 어려웠습니다.

이러한 문제들을 해결하기 위해 웅진씽크빅은 북큐레이터와 지국장들의 업무 효율 및 생산성 증대에 도움을 주기 위하여 AI 에이전트 도입을 결정했습니다. 그리고 빠른 검증이 필요했기에, AI-DLC 방법론을 적용해보기로 했습니다.

## AI-DLC, 왜 주목했나

AI-DLC는 AI와 개발자가 각자의 강점을 살려 함께 설계하고 개발하는 방법론입니다. 요즘 많이 이야기되는 바이브 코딩(Vibe Coding)과는 조금 다릅니다.

바이브 코딩이 개발자의 직관과 간단한 프롬프트에 의존한다면, AI-DLC는 체계적이고 구조화된 명세서를 기반으로 AI와 협업합니다. “대충 이런 거 만들어줘”가 아니라, “이런 요구사항이 있고, 이렇게 설계했으니, 이 부분을 구현해줘”라고 요청하는 방식입니다.

### 역할 분담이 핵심

AI-DLC에서 AI와 개발자는 명확히 역할을 나눕니다.

| 개발 단계 | AI | 개발자  
---|---|---|---  
1 | 계획 | 요구사항 분석, 개발 계획 제안 | 검증 및 최종 승인  
2 | 분해 | 복잡한 기능을 작은 단위로 분해 | 우선순위 결정  
3 | 설계 | 시스템 구조와 컴포넌트 관계 설계 | 기술적 판단, 위험 요소 식별  
4 | 구현 | 코드와 테스트 코드 생성 | 코드 리뷰, 품질 책임  
  
AI가 생성하고, 개발자는 오케스트레이터 역할을 합니다. AI가 빠르게 생성한 결과물을 검토하고, 전체 방향을 조율하며 최종 판단을 내립니다.

### 세 단계로 진행

AI-DLC는 Inception, Construction, Operation 세 단계로 구성됩니다.

**1) Inception****단계**

**무엇을****만들고****왜****만드는지** 를 정의하는 단계입니다.

  * 요구사항 분석: 이해관계자의 요구를 수집하고, 명확화 질문을 통해 요구사항을 구체화합니다
  * 유저 스토리 작성: “북큐레이터는 상담 전 고객 정보를 빠르게 확인하고 싶다”와 같이 사용자 관점에서 기능을 정의합니다
  * 애플리케이션 설계: 전체 시스템의 논리적 아키텍처와 도메인 모델을 설계합니다
  * 유닛 생성: 독립적으로 개발할 수 있는 작업 단위로 분리하여 병렬 개발을 가능하게 합니다



**2) Construction****단계**

**어떻게****만들****것인지** 를 결정하고 실제로 구현하는 단계입니다.

  * 기능 설계: 각 유닛의 상세 컴포넌트를 설계합니다. API 엔드포인트, 데이터베이스 스키마, 서비스 간 인터페이스 등이 포함됩니다
  * 비기능 요구사항 정의: 성능, 보안, 확장성 등 비기능 요구사항을 정의하고 이를 충족하는 설계를 수립합니다
  * 인프라 설계: 클라우드 인프라 구성을 설계합니다
  * 코드 생성: 설계 문서를 기반으로 AI가 코드를 생성하고, 개발자가 리뷰합니다
  * 빌드 및 테스트: 빌드 구성과 테스트를 수행하여 품질을 검증합니다



**3) Operation****단계**  – _향후_ _지원_ _예정_

실제 환경에 배포하고 운영하는 단계입니다. 현재 AI-DLC 워크플로우에서는 Inception과 Construction 단계를 중점적으로 지원하며, Operation 단계는 향후 확장될 예정입니다.

## Kiro Steering으로 AI-DLC 워크플로우 적용하기

이번 프로젝트에서는 [Kiro](https://kiro.dev/)의 Steering 기능을 활용했습니다.

### Steering이란?

Steering은 Kiro가 프로젝트 컨텍스트를 이해하고 일관된 방식으로 개발을 안내하도록 하는 기능입니다. .kiro/steering 폴더에 규칙 파일을 넣어두면, Kiro가 해당 규칙을 자동으로 인식하여 코드 생성, 설계 문서 작성, 리뷰 등 모든 작업에 반영합니다.

예를 들어, “모든 API는 RESTful 규칙을 따른다”, “테스트 코드는 Given-When-Then 패턴으로 작성한다” 같은 팀 컨벤션을 정의해두면, Kiro가 생성하는 모든 산출물에 일관되게 적용됩니다. 개발자가 매번 지시하지 않아도 프로젝트 표준을 유지할 수 있는 것입니다.

### AI-DLC 워크플로우 적용

AWS에서 제공하는 [aidlc-workflows](https://github.com/awslabs/aidlc-workflows) 저장소에는 AI-DLC 방법론을 Kiro와 Amazon Q Developer에서 사용할 수 있도록 사전 정의된 규칙과 프롬프트가 포함되어 있습니다.

사용 방법은 간단합니다. 프로젝트 워크스페이스의 .kiro/steering 폴더에 규칙 파일들을 복사해 넣으면 됩니다. 이후 Kiro는 AI-DLC의 Inception → Construction → Operation 단계를 인식하고, 각 단계에 맞는 산출물을 생성합니다.
    
    
    mkdir -p .kiro/steering
    cp -R aidlc-workflows/aidlc-rules/aws-aidlc-rules .kiro/steering/

이렇게 설정하고 나면, “Using AI-DLC, 북큐레이터를 위한 AI 상담 어시스턴트를 만들고 싶습니다”라고 요청하는 것만으로 AI-DLC 워크플로우가 자동으로 시작됩니다. 어떤 질문을 해야 하는지, 어떤 산출물을 만들어야 하는지를 AI가 단계별로 안내해줍니다.

덕분에 워크숍 참여자들이 AI-DLC 방법론을 처음 접하더라도 자연스럽게 따라갈 수 있었습니다.

## 2일간의 워크숍 과정

워크숍에는 사업 기획, IT 기획, 개발자 총 8명이 참여했습니다. 다양한 배경의 참여자들이 모여 각자의 관점에서 요구사항을 정의하고 검증했습니다.

### 첫날 오전: 문제 정의, 요구사항 도출 및 유닛 생성

먼저 북큐레이터와 지국장이 겪는 문제를 구체화했습니다. 현장의 목소리를 바탕으로 AI 에이전트가 해결해야 할 핵심 기능을 정의했습니다.

  1. 상담 회의록 자동 저장 및 분석
  2. 가망고객 데이터 기반 상담 준비 지원
  3. 지국장의 북큐레이터 관리 및 코칭 지원
  4. 웅진씽크빅의 성격유형 검사, 패턴별 검사 데이터를 활용한 맞춤형 학습 방법 제안



AI-DLC의 Inception 단계에서는 이 요구사항들을 유저 스토리로 변환하고, 독립적으로 개발할 수 있는 유닛으로 분리했습니다. 유닛 단위로 나누면 여러 개발자가 동시에 작업할 수 있어 개발 속도가 빨라집니다.

**AI-DLC****산출물****예시**

AI-DLC의 각 단계에서는 구체적인 산출물이 생성됩니다. 아래는 AI-DLC 워크플로우에서 생성되는 산출물 구조의 예시입니다.

![](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2026/02/12/Screenshot-2026-02-12-at-1.24.54 PM.png)

<Pic. Inception 단계의 산출물 요약>

### 첫날 오후 ~ 둘째 날: 설계, 구현 및 통합

Construction 단계에서는 Inception에서 정의한 유닛별로 설계와 구현을 진행했습니다.

**설계**

Kiro에게 유닛별 설계를 요청하면 도메인 설계 문서와 컴포넌트 설계 문서가 생성됩니다. 개발팀은 생성된 문서를 리뷰하고 피드백을 반영했습니다. 예를 들어, 상담 데이터 모델에서 웅진씽크빅 고유의 성격유형 검사 필드가 누락된 경우 피드백을 주면, Kiro가 수정안을 제안하고 다시 검토하는 과정을 거쳤습니다. 이 과정을 2~3회 반복하여 설계를 확정했습니다.

**구현**

설계가 확정되면 코드 생성으로 넘어갔습니다. Kiro는 설계 문서를 기반으로 프론트엔드와 백엔드 코드를 생성합니다. 개발자는 생성된 코드를 리뷰하고, 필요시 수정 요청을 통해 코드 품질을 확보했습니다.

**검증****및****통합**

둘째 날 오후에는 유닛별 검증과 통합을 진행했습니다. 프론트엔드는 UI 컴포넌트가 요구사항 명세대로 구현되었는지 기능 검증을 수행하고, 백엔드는 API 엔드포인트의 요청-응답 처리가 정상 동작하는지 확인했습니다. 각 유닛의 검증이 완료된 후, 프론트엔드와 백엔드를 연동하고 End-to-End 테스트를 거쳐 MVP를 완성했습니다.

![](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2026/02/12/Screenshot-2026-02-12-at-1.25.25 PM.png)

<Pic. Construction 단계의 산출물 요약>

## 북큐레이터 AI 에이전트 기능

  1. **상담****회의록****자동****저장****및****분석**   
북큐레이터가 상담을 마친 후 내용을 입력하면, AI가 자동으로 구조화된 회의록을 생성합니다. 설문지 등 상담 문서의 경우 OCR 모델을 이용하여 손쉽게 정형 데이터로 변환합니다. 회의록 생성이 완료되면 고객의 관심사, 추천한 도서, 후속 조치 사항 등이 깔끔하게 정리됩니다.
  2. **가망고객****기반****상담****준비**   
“오늘 오후에 김XX 고객 방문 예정인데, 어떻게 준비하면 좋을까요?” 이런 질문을 하면 AI가 과거 상담 이력, 구매 패턴, 자녀 연령과 학습 성향을 종합해서 상담 포인트를 제안합니다. 이동 중에도 빠르게 상담을 준비할 수 있게 됐습니다.
  3. **RAG****기반****맞춤형****학습****제안**   
웅진씽크빅의 성격유형 검사, 패턴별 검사 결과를 활용합니다. 고객이 자녀의 학습 고민을 이야기하면, AI가 검사 결과와 교육 자료를 바탕으로 맞춤형 학습 방법을 제안합니다. 북큐레이터는보다 고도화된 분석을 통해 아이에게 맞는 학습 솔루션을 제안하는 전문가로 거듭날 수 있습니다.
  4. **지국장****관리****기능**   
지국장은 소속 북큐레이터들의 상담 현황을 한눈에 파악합니다. AI가 분석한 상담 패턴을 바탕으로 “이 북큐레이터는 클로징 단계에서 어려움을 겪고 있어요. 이런 점을 코칭해보세요”라는 식의 제안도 받을 수 있습니다.



![](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2026/02/12/Screenshot-2026-02-12-at-1.25.50 PM.png)

<pic. 북큐레이터 AI 에이전트 화면>

## 아키텍처 살펴보기

북큐레이터 AI 에이전트는 다음과 같은 AWS 서비스들로 구성됐습니다.

![](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2026/02/12/Screenshot-2026-02-12-at-1.26.20 PM.png)

<pic. 북큐레이터 AI 에이전트 구성도>

### Amazon Bedrock (Amazon Nova 2 Lite)

자연어 처리의 핵심입니다. 2025년 12월에 출시된 [Amazon Nova 2 Lite](https://aws.amazon.com/ko/blogs/aws/introducing-amazon-nova-2-lite-a-fast-cost-effective-reasoning-model/) 모델을 활용하여 상담 내용을 분석하고, 고객에게 맞는 학습 방법을 제안합니다. Nova 2 Lite는 AWS에서 개발한 차세대 추론 모델로, 단계별 사고(extended thinking)와 작업 분해 기능을 지원합니다. 비용 효율성과 성능의 균형이 뛰어나 일상적인 업무 워크로드에 적합하며, 텍스트, 이미지, 비디오 입력을 처리할 수 있습니다.

### Amazon S3 Vectors

RAG 구현을 위한 벡터 저장소로 [Amazon S3 Vectors](https://aws.amazon.com/ko/s3/features/vectors/)를 선택했습니다. 2025년 12월에 GA된 이 서비스는 기존 OpenSearch 대비 벡터 저장 비용을 최대 90%까지 절감할 수 있습니다. 웅진씽크빅이 보유한 교육 자료, 상담 가이드, 성격유형 검사 데이터 등을 임베딩하여 저장하고, 상담 상황에 맞는 정보를 빠르게 검색합니다. 서버리스 방식이라 인프라 관리 부담도 없습니다.

### Amazon Transcribe

고객상담 전에 북큐레이터가 실제 음성을 기반으로 AI상담코칭 챗봇을 통해 모의 상담을 진행할 수 있도록 [Amazon Transcribe](https://aws.amazon.com/ko/pm/transcribe/?trk=b2c21416-1904-4611-b3bf-586ba98d0b94&sc_channel=ps&trk=b2c21416-1904-4611-b3bf-586ba98d0b94&sc_channel=ps&ef_id=Cj0KCQiAhOfLBhCCARIsAJPiopMeznGdf4QdNt26vWEBdsN_uqI4topeaG3Pihunt5jZnXiKwdAtMyUaAr3aEALw_wcB:G:s&s_kwcid=AL!4422!3!785574083495!e!!g!!amazon%20transcription!23296341551!193013719110&gad_campaignid=23296341551&gbraid=0AAAAADjHtp-02aoFqf5oFyU9c-tYquZyT&gclid=Cj0KCQiAhOfLBhCCARIsAJPiopMeznGdf4QdNt26vWEBdsN_uqI4topeaG3Pihunt5jZnXiKwdAtMyUaAr3aEALw_wcB)를 활용하여 음성을 텍스트로 바꿔주는 기능을 지원합니다.

### Amazon EKS

AI 에이전트의 실행 환경으로 [Amazon EKS](https://aws.amazon.com/ko/eks/)를 사용했습니다. 컨테이너 기반으로 에이전트를 배포하여 확장성과 운영 안정성을 확보했습니다. 웅진씽크빅의 기존 인프라와의 통합도 용이했습니다.

### Amazon DynamoDB

상담 이력, 가망고객 정보, 북큐레이터 활동 데이터를 저장하는 NoSQL 데이터베이스입니다. [Amazon DynamoDB](https://aws.amazon.com/ko/dynamodb/?trk=55da752f-45a7-4b2f-b07c-d90d7c2eb6d5&sc_channel=ps&trk=55da752f-45a7-4b2f-b07c-d90d7c2eb6d5&sc_channel=ps&ef_id=Cj0KCQiAhOfLBhCCARIsAJPiopPusZeTIVuEJj2wvUJBfKpOHmQbUOpyC3tCli5IiT3wsEIzSYYMHHIaAg4HEALw_wcB:G:s&s_kwcid=AL!4422!3!785574063590!e!!g!!amazon%20dynamodb!23300619517!195951875264&gad_campaignid=23300619517&gbraid=0AAAAADjHtp9ofZRv0bypsvW127R9uQx1e&gclid=Cj0KCQiAhOfLBhCCARIsAJPiopPusZeTIVuEJj2wvUJBfKpOHmQbUOpyC3tCli5IiT3wsEIzSYYMHHIaAg4HEALw_wcB)는 어떤 규모에서도 10밀리초 미만의 일관된 응답 시간을 제공하며, 서버리스 방식으로 용량 관리가 필요 없습니다. 북큐레이터가 이동 중에도 빠르게 고객 정보를 조회하고 상담 내용을 저장할 수 있어야 했기에, 낮은 지연 시간과 높은 가용성을 제공하는 DynamoDB가 적합했습니다.

## 프로젝트 성과

이번 프로젝트의 성과는 두 가지 관점에서 볼 수 있습니다. AI-DLC 방법론 적용을 통한 개발 생산성 향상, 그리고 북큐레이터 AI 에이전트 도입을 통한 현장 업무 효율화입니다.

### AI-DLC 적용 효과: 개발 생산성의 혁신

| 지표 | 성과 | 설명  
---|---|---|---  
1 | 개발 속도 | 4배 이상 향상 | 요구사항 정의부터 MVP 화면 구성까지 2일 완료. 기존 방식 대비 3~4주 단축  
2 | 개발 비용 | 70% 이상 절감 | AI가 설계 문서와 코드를 생성하고, 개발자가 검토하는 협업 방식으로투입 인력 최소화  
3 | 품질 관리 | 체계적 검증 | 단계별 리뷰 프로세스와 테스트 코드 자동 생성으로 설계-구현 품질확보  
  
AI-DLC는 단순히 “AI로 코드를 빨리 만든다”는 것이 아닙니다. 요구사항 분석부터 설계, 구현, 테스트까지 전 과정에서 AI와 개발자가 역할을 분담하고, 각 단계의 산출물을 체계적으로 검증하는 프로세스입니다. 이번 프로젝트를 통해 AI-DLC가 실제 엔터프라이즈 환경에서 개발 생산성과 품질을 동시에 높일 수 있음을 확인했습니다.

### 북큐레이터 AI 에이전트 효과: 현장 업무의 변화

2026년 1월 베타 오픈 후, 현장에서 체감하는 변화는 명확합니다.

**북큐레이터의****변화**

가장 큰 변화는 상담 준비 시간입니다. 예전에는 여러 시스템에 흩어진 고객 정보를 찾고 정리하는 데만 30분 가까이 걸렸습니다. 이제는 AI에게 고객 이름만 말하면 과거 상담 이력, 자녀 학습 현황, 성격유형 검사 결과까지 정리된 형태로 바로 확인할 수 있습니다.

상담 기록도 달라졌습니다. 이동 중 통화로 상담하는 경우가 많아 내용 정리가 어려웠는데, 이제는 상담 후 북큐레이터가 음성으로 내용을 입력하면 자동으로 회의록이 생성됩니다. 상담이 끝나면 핵심 내용이 이미 정리되어 있어, 다음 고객 미팅 준비에 바로 들어갈 수 있습니다.

_**“****예전에는****상담****가기****전에****고객****정보****찾느라 30****분은****썼는데,****지금은 AI****한테****물어보면****바로****정리해줘요.**_

_**상담****준비가****훨씬****편해졌어요.”**_

**지국장의****변화**

20명이 넘는 북큐레이터를 관리하는 지국장에게도 변화가 생겼습니다. 이전에는 개별 상담 현황을 파악하기 어려워 코칭 근거가 부족했습니다. 이제는 AI가 분석한 상담 패턴과 성과 데이터를 바탕으로 각 북큐레이터에게 맞는 코칭 포인트를 잡을 수 있게 됐습니다.

_**“****북큐레이터가 20****명****넘는데,****일일이****상담****내용을****파악하기****어려웠거든요.**_

_**이제는 AI****가****분석해준****내용****보면서****코칭****포인트를****잡을****수****있어서****좋아요.”**_

### 앞으로의 비전

웅진씽크빅은 이번 베타 서비스를 시작으로, AI 에이전트의 기능을 지속적으로 확장할 계획입니다. 상담 데이터가 축적될수록 AI의 제안 정확도는 높아지고, 북큐레이터는 보다 고도화된 분석을 통해 “학습 컨설턴트”로서의 역할을 강화할 수 있습니다.

AI-DLC 관점에서도 이번 프로젝트는 시작점입니다. 2일 만에 MVP를 만들 수 있다는 것은, 아이디어를 빠르게 검증하고 시장 피드백을 반영하여 개선하는 애자일한 개발 문화를 가능하게 합니다. 웅진씽크빅은 AI-DLC 방법론을 다른 프로젝트에도 확대 적용하여, AI와 개발자의 협업을 조직 전체로 확산할 예정입니다.

## 마치며

이번 프로젝트를 통해 AI-DLC 방법론이 실제 엔터프라이즈 환경에서 효과적으로 적용될 수 있음을 확인했습니다. AI가 생성한 산출물을 개발자가 검토하고 피드백하는 협업 방식은, 개발 속도와 품질을 동시에 높일 수 있는 가능성을 보여줬습니다.

특히 Kiro Steering을 통해 AI-DLC 워크플로우를 일관되게 적용할 수 있었고, Amazon S3 Vectors는 비용 효율적인 RAG 구현을, Amazon EKS 및 Strands SDK는 안정적인 에이전트 실행 환경을 제공했습니다. AI 네이티브 개발 시대가 본격화되면서, AI와 개발자의 협업 방식은 계속 진화할 것입니다. AI-DLC는 이러한 변화 속에서 체계적인 협업 프레임워크를 제공합니다.

빠르게 변화하는 비즈니스 환경에서 새로운 시스템을 구축해야 하는데, 일정과 리소스가 부족하다면 AI-DLC를 고려해보세요. AI 에이전트뿐 아니라 고객 관리, 콘텐츠 관리, 물류·재고 관리 등 현장 업무를 지원하는 시스템에도 적용할 수 있습니다. 아이디어를 빠르게 검증하고 현장 피드백을 반영하는 애자일한 개발, AI-DLC로 시작해보세요.

### 참고 자료

  * [AI와 SDLC의 만남: GenAI로 혁신하는 소프트웨어 개발](https://aws.amazon.com/ko/blogs/tech/ai-sdlc-with-genai-software-development/)
  * [AI-Driven Development Life Cycle: Reimagining Software Engineering](https://aws.amazon.com/ko/blogs/devops/ai-driven-development-life-cycle/)
  * [Open-Sourcing Adaptive Workflows for AI-Driven Development Life Cycle (AI-DLC)](https://aws.amazon.com/ko/blogs/devops/open-sourcing-adaptive-workflows-for-ai-driven-development-life-cycle-ai-dlc/)
  * [AI-DLC Workflows GitHub Repository](https://github.com/awslabs/aidlc-workflows)



![곽태호 ](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2026/02/12/Screenshot-2026-02-12-at-1.29.18 PM.png)

### 곽태호 기술총괄부문장

웅진씽크빅에서 기술총괄부문장으로서, AI와 개발자가 협업하는 새로운 개발 방법론인 AI-DLC의 도입과 실행을 이끌었습니다. 도전적인 목표였던 ‘2일 만의 MVP 개발’을 성공적으로 이끌며 애자일한 개발 문화를 조직에 정착시켰습니다. AI 기반 개발 문화를 확산하고, 기술과 업무 전반의 일하는 방식을 재설계해, AI를 ‘도입’이 아닌 ‘실행되는 AX’로 조직에 정착시키고 있습니다.

![이훈희](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2026/02/12/Screenshot-2026-02-12-at-1.29.46 PM.png)

### 이훈희 AX연구소 플랫폼개발팀장

웅진씽크빅에서 Software Engineer로 근무하며, 북큐레이터 AI 에이전트의 개발 전반을 총괄했습니다. AI-DLC 기반 설계 산출물을 실제 서비스 구조로 구체화하고, Amazon Bedrock, S3 Vectors, EKS 등 AWS 환경에서 AI 에이전트를 안정적으로 구현하도록 개발을 이끌었습니다. AI가 생성한 코드와 설계를 기술적으로 검증하고 방향성을 조율하며, 기능 구현부터 통합, 품질 확보까지 전 과정을 리드했습니다. 안정적이고 확장 가능한 AI 서비스 환경을 구현하고 기술적 의사결정을 주도하는 데 깊은 전문성을 보유하고 있습니다.

![손윤정](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2026/02/12/Screenshot-2026-02-12-at-1.30.09 PM.png)

### 손윤정 AX연구소 플랫폼개발팀 책임연구원

웅진씽크빅의 Service Planner로서 북큐레이터 AI 에이전트를 기획했습니다. 북큐레이터와 지국장의 현장 문제를 정의하고, 이를 AI 서비스 요구사항과 유저 스토리로 구체화했습니다. 가망고객 기반 상담 준비, RAG 기반 맞춤 제안 등 핵심 기능을 기획하며 AI-DLC Inception 단계를 주도했습니다. 현장 업무 효율을 높이는 실질적인 AI 서비스 기획을 담당하며, 기술을 통해 사용자에게 실질적인 가치를 주는 서비스 경험을 만드는 것을 목표로 하고 있습니다.

![이주영](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2026/02/12/Screenshot-2026-02-12-at-1.30.33 PM.png)

### 이주영 AX연구소 플랫폼개발팀 선임연구원

웅진씽크빅에서 Software Engineer로 근무하며, 북큐레이터 AI 에이전트의 핵심 기능 구현을 담당했습니다. AI-DLC 기반 설계 문서를 토대로 API, 데이터 모델, UI를 개발하고, AI가 생성한 코드의 리뷰와 개선을 통해 서비스 완성도를 높였습니다. 생성형 AI와 클라우드 환경을 실제 서비스로 연결하는 개발을 수행하며, 빠른 구현과 안정성을 동시에 확보했습니다. 이를 바탕으로 생성형 AI 기술을 실제 비즈니스 환경에 안정적으로 적용하고, 확장 가능한 AI 서비스 아키텍처를 구현하는 것을 목표로 하고 있습니다.

* * *

![Jaeyoung Ha](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2023/02/01/JaeyoungHa.jpg)

### Jaeyoung Ha

하재영 솔루션즈 아키텍트는 소프트웨어 개발자 및 소프트웨어 아키텍트의 경험을 바탕으로 엔터프라이즈 고객을 대상으로 클라우드 마이그레이션과 모더나이제이션을 담당하고 있으며 최적의 아키텍처 설계를 구성하는 역할을 수행하고 있습니다.

![Daeun Lee](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2025/11/12/프로필-crop.jpg)

### Daeun Lee

이다은 솔루션즈 아키텍트는 엔터프라이즈 서비스 설계 및 운영 경험을 바탕으로 유통/소비재 고객분들의 AWS 기반 최적화된 아키텍처 설계와 기술 전략 수립을 지원하고 있습니다.

![Sewoong Kim](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2025/05/23/Screenshot-2025-05-23-at-4.16.17 PM.png)

### Sewoong Kim

김세웅 Analytics Specialist SA는 분석 서비스와 컨테이너, 서버리스 중심으로 AWS 기반 서비스를 구성하는 고객들에게 최적화된 아키텍처를 제공하고, AI를 위한 데이터 분석 플랫폼을 보다 고도화 하기 위한 여러 기술적인 도움을 드리고 있습니다.

![Yongduck Hong](https://d2908q01vomqb2.cloudfront.net/2a459380709e2fe4ac2dae5733c73225ff6cfee1/2025/11/12/홍용덕.jpeg)

### Yongduck Hong

홍용덕 Sr. Account Manager는 다양한 인더스트리의 고객과 협업하며 여러 프로젝트를 성공적으로 수행해왔습니다. 그간의 경험을 바탕으로 엔터프라이즈 고객들이 클라우드를 통해 제품·서비스 혁신에 집중할 수 있도록, 고객들이 직면한 과제들을 해결하고 디지털 트랜스포메이션 여정을 함께합니다.
