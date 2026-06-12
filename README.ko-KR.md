# Art-Project for Claude Code (한국어)

[![Claude Code Plugin](https://img.shields.io/badge/Claude%20Code-plugin-D77757)](https://docs.claude.com/claude-code)
[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](https://github.com/joonhyungbae/art-project/releases)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)
[![위키](https://img.shields.io/badge/wiki-KO%20%2F%20EN-blue)](https://apesuite.org/plugins/#/art-project/ko/index)
[![Sponsor](https://img.shields.io/badge/sponsor-Buy%20Me%20a%20Coffee-orange?logo=buy-me-a-coffee)](https://buymeacoffee.com/crucify020v)

> 영어판(권위 있는 정본): [README.md](README.md) · 📖 위키: [한국어](https://apesuite.org/plugins/#/art-project/ko/index) / [English](https://apesuite.org/plugins/#/art-project/en/index)

**실천 기반 예술 연구(practice-based artistic research)**를 위한 **스튜디오 진입 전 단계의 *언어화* 스캐폴드(pre-studio articulation scaffold)** Claude Code 플러그인입니다. **아이데이션 엔진이 아닙니다.** Penny / Ingold / Borgdorff의 비판 — 예술의 아이데이션은 비언어적·물질적이며 만듦과 분리되지 않는다 — 을 *받아들이고*, 플러그인의 범위를 아이데이션을 *둘러싼* 명제적 언어화 작업(그랜트 신청서, 박사 exposition, 레지던시 제안서, 협업자 브리핑)으로 한정했습니다. 실제 아이데이션은 작업실에서, 재료와 함께 일어납니다.

---

## 동반 플러그인

**art-project**와 **art-paper**는 같은 메인테이너가 만든, 실천 기반 예술 연구를 위한 두 자매 Claude Code 플러그인으로, 프로젝트 생애의 양 끝을 담당합니다:

| | 플러그인 | 단계 | 스캐폴딩하는 것 |
|---|---|---|---|
| **← 현재 위치** | **[art-project](https://github.com/joonhyungbae/art-project)** | *작품 이전* | 스튜디오 진입 전 언어화 — 충동 surfacing, 전통-태그 도발, 계보 위치잡기, Concept Brief, 자기비평 리허설 |
| | **[art-paper](https://github.com/joonhyungbae/art-paper)** | *작품 이후* | 실천 기반 아트페이퍼 집필 — 탐구, 초안, ACM 인용, SIGGRAPH Asia 심사단, acmart LaTeX → PDF |

흐름: **art-project** 개념 언어화 → *스튜디오에서 작품 제작* → **art-paper** 심사용 논문 집필. 각각 독립적으로 쓸 수 있고, 함께 쓰면 개념-투-출판 전 구간을 잇습니다.

> 계보: 둘 다 [academic-research-skills](https://github.com/Imbad0202/academic-research-skills)(Cheng-I Wu)에서 내려옵니다. art-paper가 이 스위트를 아트페이퍼 장르로 포크했고, art-project가 다시 art-paper에서 스튜디오 진입 전 단계로 피봇했습니다.

---

## 30초 설치

```text
/plugin marketplace add joonhyungbae/art-project
/plugin install art-project
```

스킬 하나(`art-ideation`), 모드 6개. 슬래시 명령 `/art-project:*`로 호출. 출력은 Markdown이라 별도 빌드 도구 불필요.

> **플랜 안내.** 6개 명령 중 3개(`socratic`, `rehearsal`, `ideate`)는 load-bearing IRON RULE(의도 분류, 페르소나 안정성, 다중 세션 통합)을 다루므로 **Claude Opus**를 요청합니다. 나머지 3개(`provoke`, `lineage`, `brief`)는 Sonnet 기본. Claude 플랜에 Opus 접근이 없다면 `socratic` / `rehearsal` / `ideate`는 플랜 기본 모델로 fall through — 대부분의 규칙은 작동하지만 페르소나·의도 분류 discipline은 약해집니다. 위키에 모델 tier note 있음.

**예시로 하나 실행:**

- `/art-project:socratic` — *"뭔가에 끌리는데 아직 작품이 뭔지는 모르겠어."*
- `/art-project:provoke` — *"막혔어. 제약을 던져줘."*
- 자연어: *"새 프로젝트 같이 생각해줘."* — 의도 감지로 자동 라우팅, 라우팅 결정은 투명하게 announce.

**👉 [위키 — apesuite.org/plugins/#/art-project](https://apesuite.org/plugins/#/art-project/ko/index)** 와 [QUICKSTART.md](QUICKSTART.md) — 전체 walkthrough.

---

## 무엇을 하나

스킬 하나(`art-ideation`), 모드 6개.

| 슬래시 명령 | 산출물 | 핵심 규칙 |
|---|---|---|
| `/art-project:socratic` | Concept Pull Map (impulse / fragments / constraints / refusals / **residue**) | 탐색적 의도에서 자동 수렴 금지 — 3턴마다 의도 분류로 HARD-bound |
| `/art-project:provoke` | 전통 태그된 도발 8–20개, 각각 [Authentic Practice Boundary](https://apesuite.org/plugins/#/art-project/ko/reference/authentic-practice-boundaries) 동반 | **Unhelpfulness 보존** — 발행 후 침묵, 자동 해석 금지, 랭킹 금지 |
| `/art-project:lineage` | **작가가 후보를 먼저 제시**해야 활성화. kin / opposition / blind-spot / unexpected-neighbor 태그 | 학습-데이터 편향 헤더 의무; 한국어 세션은 한국/동아시아 자료 우선 라우팅; *retrieval, ideation 아님* |
| `/art-project:brief` | 10필드 Concept Brief (proposition / **anti-proposition** / **disconfirmation 조건** / **Frayling-type 선언** / …) | Stay-rough 기본값 — 작가 목소리 보존; 빈 필드 **자동 채움 금지** |
| `/art-project:rehearsal` | 4 페르소나 자기비평 (큐레이터 + 실기 동료 + 이론가 + Devil's Advocate) | *형성적, 결정적 아님*; 매번 disclaimer 헤더; consultative friction은 `~/.art-project/rehearsal-log.jsonl`에 기반 |
| `/art-project:ideate` | 며칠/몇 주 간격 세션을 누적하는 장기 프로젝트 파일 `~/.art-project/projects/<codename>/project.md` (Smith & Dean iterative cyclic web) | 세션당 한 모드; 단일 세션 파이프라이닝 금지 |

각 모드는 25개 이상 항목의 방법론 참조 layer에 wiring (Frayling, Borgdorff, Sullivan, Smith & Dean, Eno & Schmidt, LeWitt, Cage, Bogart, Bauhaus, Manovich, Penny, Dunne & Raby + 한국·동아시아 + HCI 선행). 전체 참조는 [위키](https://apesuite.org/plugins/#/art-project/ko/reference/tradition-tags).

---

## 설계 근거

**인지적 스캐폴드(cognitive scaffold) 입장** (Clark & Chalmers 1998; Malafouris 2013; Penny 2017). 도구도 공저자도 아닌 중간 위치. 다섯 가지 아키텍처 commitment(생성–평가 분리; 랭킹보다 긴장; 대립을 포함한 계보; 형성적-비결정적 리허설; Authentic Practice Boundary와 짝지은 전통 태그)이 특정 PaR 입장을 operational하게 인코딩; 전통 태그는 **Authentic Practice Boundary**(각 인용 방법이 요구하지만 플러그인이 *시뮬레이션하지 않는* 것)와 짝지어집니다.

> *예.* Cage chance operations: 플러그인이 procedure (어떤 I Ching, 어떤 dice protocol)를 *제안*만 함. **주사위는 작가가 던집니다.** 작가가 procedure를 수행하는 *시간*이 작품의 일부이고, LLM이 chance result를 생성하면 그 방법의 구성적 특징이 무너집니다.

자세히: [인지적 스캐폴드](https://apesuite.org/plugins/#/art-project/ko/philosophy/cognitive-scaffold), [Frayling 분류](https://apesuite.org/plugins/#/art-project/ko/philosophy/frayling-typology), [진정성 실천 경계](https://apesuite.org/plugins/#/art-project/ko/reference/authentic-practice-boundaries), [측정된 위해](https://apesuite.org/plugins/#/art-project/ko/philosophy/measured-harms), 그리고 [v0.2 합성 spec](docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md).

---

## 누구를 위한 것인가

**명제적 언어화가 병목인 작가**를 위한 도구:

- 초기 경력 작가 (artist statement / grant proposal 장르 관례 미숙)
- 제2언어 작가 (예: 한국어 모국어 작가가 영문 그랜트 신청서를 쓰는 경우)
- PaR 박사 과정생 (*Journal for Artistic Research* 등 exposition 작성)
- 그랜트·레지던시 마감 직전 작가
- 공유 언어화 문서가 필요한 collective

**아닌 경우.** 명제적 언어화가 이미 유창한 작가에게는 구조적으로 부적합 (Claude를 직접 사용하면 됩니다). 즉흥·의례·구술처럼 *언어화 자체를 거부하는* 전통에도 부적합. 경계를 명시하는 것 자체가 설계의 일부 — [philosophy / measured harms §6](https://apesuite.org/plugins/#/art-project/ko/philosophy/measured-harms) 참고.

이중 언어: 영어 기본, 한국어 세션에서 한국·동아시아 라우팅 자동 활성. **정직한 disclosure:** 참조 layer의 동아시아 섹션은 가장 미숙(v0.1.0 기준 3 entries; 확장은 자료조사 진행 중). 한국어 세션에서 `lineage`는 학습-데이터 편향 헤더를 띄우지만 여전히 한국어 1차 사료보다 영어권 한국학 자료로 fallback될 수 있음. 한국어 경험은 v0.2 참조 확장 전까지 *씨앗 수준*이지 영어와 *완전히 병렬*은 아니라고 다뤄 주세요.

---

## 라이선스 & 인용

[CC-BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). 공유·수정·표기 가능, 비상업 사용 한정.

```text
art-project (Version 0.1.0).
Pivoted from art-paper v0.1.0; ultimately forked from
Academic Research Skills (Cheng-I Wu) v3.9.4.2.
https://github.com/joonhyungbae/art-project
```

---

## 출처

**메인테이너.** 배준형 (`joonhyungbae` GitHub; `jh.bae@kaist.ac.kr`). v0.2 설계 종합(Frayling 3층 하이브리드 자기위치, 인지적 스캐폴드 framing, 진정성 실천 경계 아키텍처, 6모드 reshape, 측정된 위해 공개)은 메인테이너의 작업입니다.

**계보.** [academic-research-skills](https://github.com/Imbad0202/academic-research-skills) v3.9.4.2 ([Cheng-I Wu](https://github.com/Imbad0202)) → art-paper v0.1.0 → art-project v0.1.0. 장르 중립 안전 기계장치(L3 인용 신뢰성 게이트, Concession Threshold Protocol, intent detection, 라우팅 규율)는 ARS에서 변경 없이 상속됨. 메인테이너는 diff용 pristine ARS 클론을 `ref/academic-research-skills/`에 로컬로 보관; 이 디렉토리는 gitignore되며 공개 플러그인 배포에는 포함되지 않습니다.

**4-에이전트 설계 비평** (2026-05-24) — v0.2 설계는 네 명의 전문 에이전트 비평에서 종합되었습니다: 예술 연구 방법론자(PaR / Frayling / Borgdorff / Sullivan), HCI / AI-creativity 연구자(Shneiderman / Cherry-Latulipe / Davis / Wordcraft-Sparks), 현역 작가 스튜디오측 리뷰, Devil's Advocate(Penny / Ingold / Borgdorff / Wittgenstein / Illich의 전제 공격).

---

## 저장소 구조

```text
art-project/
├── art-ideation/
│   ├── SKILL.md                       # 단일 스킬 spec
│   ├── agents/                        # v0.2 정렬 4개 + deprecated/ 아래 archive 4개
│   ├── references/ + templates/       # in-skill 참조와 (deprecated) 템플릿
│   └── examples/                      # in-skill 예시 (v0.1-deprecated; 위키 참고)
├── commands/                          # 6개 슬래시 커맨드 파일 (bare name: brief, ideate, …)
├── shared/references/                 # 방법론 참조 + 용어집 + 라우팅
├── docs/                              # 설계 spec / 감사 / 검증 / 운영
├── ref/academic-research-skills/      # pristine ARS 참조 (gitignore; 로컬 전용)
├── hooks/ + scripts/                  # SessionStart hook + announce 스크립트
├── .claude-plugin/{plugin,marketplace}.json
└── README{,.ko-KR}.md, LICENSE, NOTICE, SECURITY, CHANGELOG, MODE_REGISTRY,
    POSITIONING, QUICKSTART
```

---

## 변경 이력 (최근)

전체 이력은 [CHANGELOG.md](CHANGELOG.md) 참고.

- **v0.1.0** (2026-05-24, art-paper에서 피봇) — 논문 작성 범위 폐기; `art-inquiry` → `art-ideation`으로 6모드 reshape; 참조 layer 재구축 (positionality + Tensions + Authentic Practice Boundary + Penny/Borgdorff 비판적 edge 복원); HCI 선행 섹션 추가; 측정된 위해 공개 ship.
- **v0.2 내부 마일스톤** (2026-05-30) — 런타임 준비성 정직성 sweep; intent detection을 `socratic`에 HARD-bound; Dialogue Health Indicator를 `rehearsal`의 Devil's-Advocate 하위 휴리스틱으로 demote; rehearsal friction이 실제 `~/.art-project/rehearsal-log.jsonl` 로그에 기반 (honour-system에서 업그레이드); `ideate` full-mode 영속성이 `~/.art-project/projects/<codename>/project.md` 기반 (artist-managed에서 업그레이드); v0.1-drift 에이전트들 `art-ideation/agents/deprecated/`로 archive. 자세히: [`docs/V0.2-DESIGN-DECISIONS.md`](docs/V0.2-DESIGN-DECISIONS.md) + [`docs/V0.2-VERIFICATION.md`](docs/V0.2-VERIFICATION.md).
- **위키 canonical → apesuite** (2026-06-12) — 사용자 위키는 이제 [apesuite.org/plugins/](https://apesuite.org/plugins/)에 거주; GitHub Pages에 배포되던 MkDocs mirror는 제거됨.
