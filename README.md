# ChannelTalk → Notion 운영 자동화 프로젝트

ChannelTalk 상담 데이터를 수집·가공하여 Notion 데이터베이스에 자동 등록하는 운영 자동화 프로젝트입니다.

---

## 프로젝트 개요

상담 이력, 재발 방지 액션, 주요 이슈 등을 수기로 정리하는 과정은 누락과 중복이 발생하기 쉽습니다.
이 프로젝트는 ChannelTalk 상담 데이터를 자동 수집하고 Notion DB에 등록하여 운영 기록을 체계적으로 관리하는 것을 목표로 합니다.

### 주요 목적

* 상담 이력 누락 방지
* 운영 기록 일원화
* 재발 방지 액션 추적
* 수기 입력 시간 절감
* Notion 기반 상담 관리 자동화

---

## 지원 기능

* ChannelTalk 상담 데이터 API 조회
* 상담 단위 데이터 가공
* 주요 메시지 요약
* 상담 상태 / 태그 정리
* Notion DB 신규 생성
* 중복 등록 방지 확장 가능
* 주간 / 월간 리포트 확장 가능

---

## 자동화 흐름

1. ChannelTalk API에서 상담 데이터 조회
2. 상담 / 메시지 데이터 정리
3. 주요 필드 추출

   * 상담 ID
   * 이용자 ID
   * 담당자 ID
   * 상담 상태
   * 태그
   * 생성일시
   * 수정일시
   * 상담 요약
4. Notion DB 속성 매핑
5. 중복 여부 확인 후 생성 또는 업데이트

---

## 프로젝트 구조

```bash
.
├─ README.md
├─ requirements.txt
├─ .env.example
├─ .gitignore
├─ LICENSE
├─ main.py
├─ config.py
├─ services/
│  ├─ notion_service.py
│  └─ channeltalk_service.py
├─ processors/
│  └─ channeltalk_processor.py
└─ utils/
   ├─ logger.py
   ├─ helpers.py
   └─ date_utils.py
```

---

## 환경 변수 설정

`.env.example` 파일을 참고하여 `.env` 파일을 생성한 뒤 실제 값을 입력합니다.

```env
# Notion
NOTION_TOKEN=your_notion_token
NOTION_DATABASE_ID=your_notion_database_id

# ChannelTalk
CHANNELTALK_ACCESS_KEY=your_channeltalk_access_key
CHANNELTALK_ACCESS_SECRET=your_channeltalk_access_secret
CHANNELTALK_BASE_URL=https://api.channel.io

# Mode
SYNC_MODE=channeltalk
```

---

## 설치 방법

```bash
pip install -r requirements.txt
```

---

## 실행 방법

`.env` 파일에서 `SYNC_MODE=channeltalk` 로 설정 후 실행합니다.

```bash
python main.py
```

---

## Notion 데이터베이스 예시 속성

* 상담ID
* 이용자ID
* 담당자ID
* 상태
* 태그
* 생성일시
* 수정일시
* 요약

---

## 참고 사항

* 실제 ChannelTalk API 응답 구조 및 Notion DB 속성명에 따라 코드 수정이 필요합니다.
* 공개 저장소에는 실제 토큰, 데이터베이스 ID, 상담 원문 등 민감 정보를 절대 포함하면 안 됩니다.
* 상담 데이터에는 개인정보가 포함될 수 있으므로 샘플 업로드 시 반드시 비식별화가 필요합니다.

---

## 한계 및 보완 필요 사항

현재 저장소는 자동화 구조와 연동 방식 중심으로 정리되어 있습니다.
실서비스 적용 시 아래 보완이 필요합니다.

* 실제 API 엔드포인트 검증
* 응답 필드 구조 확정
* 상담 중복 등록 방지 로직 강화
* 에러 재시도 처리
* 속도 제한(rate limit) 대응
* 상담 요약 품질 개선
* 운영 목적에 맞는 분류 태그 자동화

---

## TODO

* [ ] ChannelTalk API 실제 응답 기준 필드 매핑 확정
* [ ] 상담 ID 기준 upsert 처리
* [ ] 상담 내용 요약 로직 개선
* [ ] 기간별 배치 실행 옵션 추가
* [ ] 로그 파일 저장 기능 추가
* [ ] 주간 / 월간 리포트 자동화 확장

---

## 사용 기술

* Python
* Notion API
* ChannelTalk API
* dotenv
* requests

---

## 라이선스

MIT License
