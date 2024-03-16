# graalpython-test
graalpython 테스트용 python 프로젝트

## 목적
- native로 생성된 것과 jvm으로 생성된 것을 비교할 수 있다.
  - native로 생성된 것은 단일 실행파일으로 동일 명령어 set을 지원하는 환경에서 사용 가능한지 확인
  - jvm으로 생성된 것은 jar 파일로 추출할 수 있는지 확인

## 예제
- 특정 URL에 http 응답이 정상인지 확인하는 예제
- 만약 4회 실패할 경우 종료 이벤트 발생 (SIGABRT)