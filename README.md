# graalpython-test
graalpython 테스트용 python 프로젝트

## 목적
- native로 생성된 것과 jvm으로 생성된 것을 비교할 수 있다.
  - native로 생성된 것은 단일 실행파일으로 동일 명령어 set을 지원하는 환경에서 사용 가능한지 확인
  - jvm으로 생성된 것은 jar 파일로 추출할 수 있는지 확인

## 예제
- 특정 URL에 http 응답이 정상인지 확인하는 예제
- 만약 4회 실패할 경우 종료 이벤트 발생 (SIGABRT)

## 결과
- graalpy에서 테스트 되지 않은 패키지는 안될 가능성이 높음
  - 실제 테스트에 포함된 `apscheulder`는 애초에 목록에 포함되지도 않았다.
- 오히려 nuitka를 사용하면 python3.11로 포함 가능하고 더 적은 standalone 크기를 가질 수 있다.
  - graalpy는 native로 생성할 경우 201M 크기를 가진다.
  - nuitka로 AOT 컴파일할 경우 약 11M 크기를 가진다. 
  - pyinstaller로 번들링할 경우 약 11M 크기를 가진다.

## 결론
- graalpy는 Java에서 python의 데이터 분석 관련해 연동하려할 때 사용하는 것이 최적이다.
- 단순 파이썬 번들링의 경우 nuitka나 pyinstaller를 적극적으로 고려해보는 것이 좋다.