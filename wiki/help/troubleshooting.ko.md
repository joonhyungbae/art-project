# 트러블슈팅

흔한 이슈, 원인, 조치. 각 문제마다 한 줄 진단과 구체적 다음 행보.

## 설치

### `/art-project:socratic`이 "command not found"라고 함

**원인**: 플러그인이 설치되지 않았거나, 활성화되지 않았거나, 설치 완료 전에 세션이 시작됨.

**조치**:
1. 설치 확인: `/plugin list`에 `art-project`가 있어야 함.
2. 없으면 설치: `/plugin marketplace add joonhyungbae/art-project` 후 `/plugin install art-project`.
3. 있지만 비활성화면 Claude Code 설정에서 활성화.
4. Claude Code 세션 재시작 — 슬래시 명령은 세션 시작 시 로드됨.

### 플러그인은 설치된 것 같은데 슬래시 명령이 여전히 없음

**원인**: Claude Code가 이전 세션의 플러그인 목록을 캐싱 중.

**조치**: Claude Code 완전 재시작(새 창만이 아닌). 세션 시작 hook이 플러그인 슬래시 명령을 다시 로드.

### `mkdocs serve`가 "Address already in use" 반환

**원인**: 다른 프로세스가 포트 8000을 잡고 있음(종료 안 한 이전 `mkdocs serve` 또는 무관한 dev server).

**조치**: 다른 포트 사용: `mkdocs serve -a localhost:8001`. 또는 잡고 있는 프로세스 찾아서 정지: `lsof -i :8000` 후 stale이 확인되면 `kill <pid>`.

## 모드가 시작을 거부

### `/art-project:lineage`가 "supply at least two candidate precedents"라고 함

**원인**: 버그가 아닌 [lineage IRON rule](../modes/lineage.md). long-tail sub-domain의 lineage hallucination이 LLM lineage 도구의 가장 흔한 실패 모드라, 플러그인이 artist-supplied anchor를 요구.

**조치**: lineage 호출 전에 선례 아티스트·작품·텍스트를 2개 이상 명명. 없으면 [`socratic`](../modes/socratic.md)(충동 표면화) 또는 [`provoke`](../modes/provoke.md)(제약 생성)부터.

### `/art-project:rehearsal`이 "no brief found"라고 함

**원인**: rehearsal 모드는 기존 Concept Brief를 부담 테스트; brief를 먼저 안 했으면 테스트할 게 없음.

**조치**: [`brief`](../modes/brief.md)를 실행해 10-필드 Concept Brief 산출. 그다음 rehearsal로 복귀.

### `/art-project:rehearsal`이 "friction warning: you have rehearsed this concept N times in the last 14 days"라고 함

**원인**: 버그가 아닌 [rehearsal 아키텍처 마찰](../modes/rehearsal.md). 같은 컨셉에 대해 14일 내 2회 호출 후, 플러그인이 simulation-pedagogy harm(Schön 1983)을 경고.

**조치**: 경고를 끝까지 읽기. 경고가 제안하는 정직한 세 경로: (a) brief를 실제 interlocutor에게 가져가기; (b) rehearsal에서 surface된 질문들과 함께 socratic/provoke로 돌아가기; (c) 추가 rehearsal 없이 brief와 함께 머물기. Override는 가능하지만 deliberate해야 함.

## 출력이 이상함

### Brief 모드가 모든 필드를 `[gap, not in input]`으로 보여줌

**원인**: 불충분한 재료로 brief 실행. 플러그인의 stay-rough default는 빈 필드용 content를 fabricate하기를 거부.

**조치**: 이것이 옳은 행동. 누락 필드가 필요로 하는 재료를 만들기 위해 [`socratic`](../modes/socratic.md), [`provoke`](../modes/provoke.md), [`lineage`](../modes/lineage.md)로 돌아가기. 그다음 brief로 복귀.

### Brief 출력이 AI-statement boilerplate처럼 들림

**원인**: `--polish` 사용으로 smoothing이 아티스트 목소리를 납작하게 만듦. 또는 처음부터 AI-statement register로 재료를 씀.

**조치**: `--polish` 빼고 재실행; stay-rough default는 거친 단편을 verbatim 보존. 기저 재료가 이미 AI-toned면, "stay rough, write fragments not paragraphs" 지시와 함께 [`socratic`](../modes/socratic.md)로 복귀.

### (socratic의) Concept Pull Map이 이상함 / 내가 말한 것과 안 맞음

**원인**: Socratic 대화가 당신 답을 mis-reading으로 따라감. 일반적 실패 모드.

**조치**: 직접 말하기. 플러그인이 어긋남을 낳은 질문들을 다시 던집니다. 다섯 카테고리(Impulses / Fragments / Constraints / Refusals / Residue) 중 아무거나 거부하고 플러그인이 당신의 수정에서 map을 다시 derive하게 할 수 있음.

### Lineage map이 들어본 적 없는 아티스트를 인용

**원인**: training-data canon 편향, 드물게 long-tail sub-domain의 lineage hallucination. 모든 lineage map의 필수 bias header가 over-/under-represented sub-domain을 명명; 당신 작업이 under-represented 영역이면 unexpected-neighbor 항목을 추가 회의로 대하기.

**조치**: map에 붙은 bias header 읽기. 항목이 invented 느낌이면 플러그인에게 "verify the citation for [entry]: source, year, primary reference"라고 요청. verification 실패 시 hallucination으로 다루고 제거. [측정 가능한 위해](../philosophy/measured-harms.md) §1 참조.

### Provoke 카드가 generic 느낌 / tradition-tagged가 아닌 듯

**원인**: 플러그인이 provocation을 전통에 grounding 실패. 드물지만 입력이 어떤 전통도 anchoring하기에 너무 추상적일 때 발생.

**조치**: anchoring할 더 구체적 재료(특정 이미지, 구절, 최근 만남)를 플러그인에게 주거나, tagged 부분집합을 명시적으로 요청: `/art-project:provoke --tradition=oblique-strategies` 또는 `--tradition=cage`.

## 프로젝트 파일 (full 모드)

### 내 프로젝트 파일을 못 찾겠음

**원인**: 프로젝트 파일은 *생성 시점*의 Claude Code 작업 디렉터리에 `art-project-{slug}.md`가 기본. 작업 디렉터리가 바뀌었다면 파일은 원래 위치.

**조치**: 검색: `find ~ -name "art-project-*.md" -type f 2>/dev/null` (Unix) / `Get-ChildItem -Path $HOME -Filter "art-project-*.md" -Recurse -ErrorAction SilentlyContinue` (PowerShell).

### 플러그인이 한 세션 내 모드 전환을 거부

**원인**: 버그가 아닌 [full 모드 세션당 1개 모드 IRON rule](../modes/full.md). 세션 내 cross-mode pipelining은 iterative cyclic web(Smith & Dean 2009)을 구조적으로 undermine.

**조치**: 현재 모드 종료 후 세션 닫기. 다음 모드를 위해 새 세션에서 프로젝트 파일로 복귀. "세션 사이의 스튜디오 시간"은 한계가 아닌 설계의 일부.

### Cross-session re-entry가 잘못된 요약을 보여줌

**원인**: 세션 사이에 프로젝트 파일이 플러그인 외부에서(수동으로, 다른 도구로, 또는 sync 충돌로) 편집됨.

**조치**: 파일을 직접 읽어 상태 확인. 손상되었으면 버전 관리에서 복원(프로젝트 파일은 git repo 또는 백업에 있어야 함). 플러그인은 프로젝트 파일을 auto-version하지 않음 — 아티스트의 책임.

## 언어와 라우팅

### 한국어를 원하는데 플러그인이 영어로 답함

**원인**: 플러그인은 입력 언어를 match. 입력이 대부분 영어면(예: 슬래시 명령 + 영어 follow-up), 응답이 영어.

**조치**: 다음 메시지를 한국어로 쓰기. 플러그인이 다음 응답부터 전환. `/art-project:ideate` 내에서 지속적 한국어 선호는 프로젝트 파일 frontmatter에 `language: ko` 라인 추가.

### 한국 맥락 작업인데 Lineage map이 anglophone-heavy

**원인**: training-data canon 편향. 플러그인의 한국·동아시아 default 라우팅은 세션 신호(입력 언어, 명명된 후보, 명시적 선언)에 발사; 신호가 약하면 라우팅이 engage 안 할 수 있음.

**조치**: 한국 선례를 명시적으로 명명(예: "Paik Nam-June과 이불에서 확장")하거나, 라우팅 강제용 `--non-anglophone` 플래그 사용.

## 빌드와 dev

### MkDocs 빌드가 Material 2.0 deprecation 경고

**원인**: Material for MkDocs 팀이 모든 빌드마다 다가올 MkDocs 2.0 비호환 banner를 표시.

**조치**: 무시; informational이고 빌드와 무관. 빌드 상태는 `INFO -- Documentation built in N.NN seconds`가 말함.

### 배포된 사이트에서 위키 한국어 페이지가 404

**원인**: GitHub Pages 미활성화, 또는 잘못된 source로 활성화.

**조치**: repo Settings → Pages, Source를 **"GitHub Actions"**(not "Deploy from a branch")로. push 또는 워크플로우 재실행; 라이브 URL은 `https://<user>.github.io/art-project/` (en) + `/ko/` (ko).

### 로컬 `mkdocs serve`가 `/ko/`에 404 반환

**원인**: dev server는 기본 로케일을 root에 serve할 수 있지만, plugin/버전에 따라 로컬에서 `/ko/` prefix로 routing 안 할 수 있음.

**조치**: `mkdocs build` 실행 후 `site/ko/index.html`이 있는지 확인. 배포 사이트(GitHub Actions를 통해)는 로컬 dev server의 i18n routing이 부분적이어도 두 로케일을 올바르게 serve.

## 이 페이지가 도움 안 될 때

문제가 여기 없으면:

1. [모드](../modes/overview.md)에서 관련 모드 페이지 확인 — 그 모드를 governing하는 IRON rules.
2. [측정 가능한 위해](../philosophy/measured-harms.md) 확인 — 행동이 알려진 실패 모드 + 완화인지.
3. [저장소](https://github.com/joonhyungbae/art-project/issues)에 issue를 열기 — 실행한 슬래시 명령, 정확한 에러 또는 예상 외 출력, 플랫폼(CLI / 데스크톱 앱 / 웹).
