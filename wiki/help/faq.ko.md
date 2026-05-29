# 자주 묻는 질문 (FAQ)

자주 반복되는 질문에 대한 빠른 답변. 각 항목의 아키텍처 근거가 궁금하시면 링크된 Philosophy 또는 Reference 페이지를 보세요.

## 범위와 위치

### AI 미술 생성기인가?

아니요. 플러그인은 **언어** — 질문, brief, lineage map, rehearsal transcript — 를 산출하고, 아티스트가 이것을 스튜디오로 가져갑니다. 작품 자체를 만들지 않습니다. [인지적 스캐폴드](../philosophy/cognitive-scaffold.md) 참조.

### 그냥 ChatGPT로 같은 걸 하면 안 되나?

가능하지만, 플러그인은 일반 어시스턴트가 강제하지 않는 특정 규율을 강제합니다: lineage fabrication 거부, 필수 training-data bias header, 인용된 전통별 진정성 실천 경계, 탐색 의도에서 auto-convergence 금지, 반복 rehearsal의 simulation-pedagogy harm에 대한 아키텍처 마찰. 이것들이 프레임워크의 IRON rules입니다. [모드 개요](../modes/overview.md) 참조.

### 모든 사람을 위한 도구인가?

아니요. 명제적 언어화가 병목인 아티스트(신진, 모국어 외 언어로 글쓰는, doctoral candidate, 마감 압박, collective)를 위해 scoping되었습니다. 언어화가 이미 유창한 아티스트, 그리고 언어화가 본질적으로 unwanted인 전통(즉흥, 의례, 구술)에는 **unsuitable**(suboptimal 아닌)입니다. [측정 가능한 위해](../philosophy/measured-harms.md) §6 참조.

### 왜 "ideation" 대신 "pre-studio articulation"인가?

플러그인은 예술의 ideation이 비언어적이고 물질적이며 만듦과 분리될 수 없다는 강한 비판(Penny, Ingold, Borgdorff)을 받아들입니다. ideation을 *둘러싼* 명제적 작업 — 그랜트 신청서, doctoral exposition, 레지던시 제안서, collaborator briefing — 은 분리 가능한 다른 단계이고 플러그인은 그 자리에 scoping합니다. [Frayling 분류](../philosophy/frayling-typology.md) 참조.

## 모드와 라우팅

### 어떤 모드를 언제 쓰나?

| 상황 | 모드 |
|---|---|
| 막연한 끌림, 아직 컨셉 없음 | [`socratic`](../modes/socratic.md) |
| 부분 컨셉, 막힘 | [`provoke`](../modes/provoke.md) |
| 후보 선례 있음, 확장 원함 | [`lineage`](../modes/lineage.md) |
| 재료 있음, 명제 문서 필요 | [`brief`](../modes/brief.md) |
| brief 있음, 제출 전 부담 테스트 | [`rehearsal`](../modes/rehearsal.md) |
| 주·월 단위 프로젝트 | [`full`](../modes/full.md) |

전체 표는 [모드 개요](../modes/overview.md).

### 한 세션에 여러 모드를 돌릴 수 있나?

단일-모드 명령(`/art-project:brief`, `/art-project:provoke` 등)에서는 가능합니다 — 단 플러그인이 *auto-pipeline*은 거부합니다(예: 명시적 재트리거 없이 `socratic → brief`를 연속 실행 안 함). `/art-project:ideate`(full 프로젝트 파일)에서는 **세션당 1개 모드** 규칙이 아키텍처적으로 강제됩니다: 세션 내 전환 시도 시 플러그인이 경고하고 명시적 override를 요구합니다.

### `lineage`는 왜 선례를 명명하기 전까지 시작을 거부하나?

long-tail sub-domain에서의 lineage hallucination이 LLM lineage 도구의 가장 흔한 실패 모드이고, artist-supplied 초기 후보가 실패 공간을 실질적으로 제약하기 때문입니다. [`lineage`](../modes/lineage.md) 참조. 선례가 없으면 [`socratic`](../modes/socratic.md) 또는 [`provoke`](../modes/provoke.md)부터.

### `brief`와 `rehearsal`의 차이는?

`brief`는 10-필드 Concept Brief(*문서*)를 산출합니다. `rehearsal`은 기존 brief를 4 페르소나 비평가(Curator + Practitioner-peer + Theorist + Devil's Advocate) 시뮬레이션으로 부담 테스트합니다. 보통 `brief` 먼저, 그다음 `rehearsal`. brief 없이 `rehearsal`을 실행하면 쓸 만한 게 안 나옵니다.

## 출력과 데이터

### 내 프로젝트 파일은 어디 있나?

`/art-project:ideate`(full 모드)에서는 프로젝트 파일을 생성할 때 플러그인이 경로를 알려줍니다. 기본 이름: 현재 작업 디렉터리의 `art-project-{slug}.md`. 파일은 당신의 것이고, 플러그인은 append할 뿐 direct하지 않습니다. [`full`](../modes/full.md) 참조.

### Word / PDF로 export 가능한가?

플러그인은 기본적으로 Markdown을 산출합니다. PDF / DOCX export는 향후 버전(v0.2+)으로 미뤄져 있습니다. 그동안은 Pandoc 등으로 변환하세요.

### 플러그인이 내 프로젝트 파일을 어디로 보내나?

다른 Claude Code 세션 입력처럼 Claude API를 통해 처리됩니다. 다른 서비스로 전송되지 않습니다. 플러그인 자체는 phone home하지 않습니다.

### 출력은 어느 언어로 나오나?

입력 언어 그대로입니다. 한국어 입력 → 한국어 출력; 영어 입력 → 영어 출력. 세션 도중 섞을 수 있습니다(거친 재료는 한국어로 쓰고, `brief` 모드에서 "이걸 영어로 정리해줘"로 전환).

## 라이선스와 기여

### 상업적 사용 가능한가?

플러그인은 CC-BY-NC 4.0입니다. 비상업적 사용은 허용; 상업적 사용은 별도 licensing 필요. 메인테이너에게 contact.

### 전통 태그 corpus를 확장할 수 있나?

네. [기여](../contributing.md) §1 참조. 특히 환영: 비-anglophone 전통, 구술 방법론, Global South 실천. 진정성 실천 경계 필드는 모든 새 태그에 필수.

### 새 harm 클래스를 제안할 수 있나?

네. [기여](../contributing.md) §2 참조. 현재 6개 클래스는 exhaustive하지 않습니다.

## 아키텍처 세부

### 진정성 실천 경계가 뭔가?

플러그인이 인용하는 모든 전통(Oblique Strategies, Cage, LeWitt, Viewpoints 등)에 대해, 플러그인은 인용을 — 그 인용된 방법이 요구하지만 AI가 시뮬레이션하지 *않는* 것의 명시적 선언과 — 짝짓습니다. 예시는 [진정성 실천 경계](../reference/authentic-practice-boundaries.md).

### 같은 컨셉에 `rehearsal`을 두 번째 사용할 때 왜 경고가 뜨나?

simulation-pedagogy harm(Schön 1983)에 대한 아키텍처 마찰: 시뮬레이션에서 반복 rehearse하는 아티스트는 시뮬레이션된 종류의 비평에 방어하도록 자신을 훈련시킬 수 있는데, 이것은 실제로 마주할 비평과 구조적으로 다릅니다. 마찰은 advisory가 아니라; 임계값 이후 매번 발생합니다. [`rehearsal`](../modes/rehearsal.md) 및 [측정 가능한 위해](../philosophy/measured-harms.md) §3 참조.

### "stay-rough default"가 뭔가?

`brief` 모드가 이전 모드 재료(예: `socratic` 세션의 단편)를 끌어올 때, 아티스트의 목소리를 verbatim 보존합니다 — 단편을 AI-statement register로 다듬지 않습니다. 빈 필드는 fabricate되지 않고 `[gap, not in input]`으로 보고됩니다. 이것이 no-fabrication 규율입니다. 제출용 smoothing은 `--polish` opt-in 플래그. [Concept Brief 스키마](../reference/concept-brief.md) §Stay-rough default 참조.

## 버전과 업데이트

### 어느 버전을 갖고 있는지 어떻게 아나?

플러그인 슬래시 명령을 아무거나 실행하면 preamble에 버전 라인이 나옵니다. 또는 [CHANGELOG](https://github.com/joonhyungbae/art-project/blob/main/CHANGELOG.md) 확인.

### 어떻게 업데이트하나?

```text
/plugin update art-project
```

### 업데이트가 기존 프로젝트 파일을 깨뜨리나?

프로젝트 파일은 안정적 Markdown 형식을 따르고; 업데이트는 확장하되 깨뜨리지 않습니다. 모드 이름이 바뀐 경우(예: v0.2의 `panel → rehearsal`), 플러그인이 legacy 모드 이름 참조를 우아하게 처리합니다.

## 이 FAQ가 멈추는 지점

이것은 빠른-답변 인덱스이지 매뉴얼이 아닙니다. 위 각 주제에 대해 링크된 Modes / Reference / Philosophy 페이지가 canonical 소스입니다. 여기 없는 반복 질문이 있다면 [기여](../contributing.md) §3에 추가 방법이 있습니다.
