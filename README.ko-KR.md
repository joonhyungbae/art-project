# art-project for Claude Code (한국어)

[![Version](https://img.shields.io/badge/version-v0.1.0--ideation-blue)](https://github.com/joonhyungbae/art-project/releases)
[![License: CC BY-NC 4.0](https://img.shields.io/badge/license-CC%20BY--NC%204.0-lightgrey)](https://creativecommons.org/licenses/by-nc/4.0/)

> 영어판(권위 있는 정본): [README.md](README.md). 이 문서는 한국어 요약이며 세부 변경 이력은 영어판을 따릅니다.

**실천 기반 예술 연구(practice-based artistic research)**를 위한 **스튜디오 진입 전 단계의 *언어화* 스캐폴드(pre-studio articulation scaffold)** Claude Code 플러그인입니다. **아이데이션 엔진이 아닙니다.** Penny / Ingold / Borgdorff의 비판 — 예술의 ideation은 비언어적이고 물질적이며 만듦과 분리되지 않는다 — 을 *받아들이고*, 플러그인의 범위를 ideation을 *둘러싼* 명제적 언어화 작업으로 한정했습니다. 실제 ideation은 작업실에서, 재료와 함께 일어납니다.

> **포크 계보:** [academic-research-skills (ARS)](https://github.com/Imbad0202/academic-research-skills) v3.9.4.2 → **art-paper** v0.1.0 (논문 작성 특화, SIGGRAPH Asia Art Papers 트랙) → **art-project** v0.1.0-ideation (2026-05-24 피봇, 논문 작성 범위 폐기 + 스튜디오 진입 전 언어화 범위로 재특화). 네 명의 에이전트 비평(예술-연구 방법론자 + HCI/AI-창의성 연구자 + 현역 작가 스튜디오-측 리뷰 + Devil's Advocate)을 통합한 v0.2 합성 설계: [`docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md`](docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md).

## 30초 설치

```text
/plugin marketplace add joonhyungbae/art-project
/plugin install art-project
```

설치 후 `/art-socratic`로 막연한 충동을 끌어내거나, `/art-provoke`로 갇힌 지점을 자극하거나, 자연어로 그냥 "새 프로젝트 같이 생각해줘"라고 시작하면 됩니다.

## 자기 위치 (Frayling 3층 하이브리드)

- **도구 층 — research FOR art:** 실천 기반 작가가 사용하는 도구.
- **참조 층 — research INTO art:** [`shared/references/art_ideation_methodology.md`](shared/references/art_ideation_methodology.md) — 선행 ideation 방법론 문헌의 2차 종합.
- **설계-선택 층 — research THROUGH art/design:** 생성-평가 분리 / 긴장-유지(랭킹 거부) / 계보-반대-포함 / 형성적-비결정적 자기비평 리허설 / Authentic Practice Boundary 동반 tradition-tag — 이 다섯 가지 아키텍처 선택 자체가 PaR 명제 기여.

## 인식론적 입장 — *cognitive scaffold*

Clark & Chalmers (1998), Malafouris (2013), Penny (2017). 도구도 아니고 공저자도 아닌 중간 위치. 작가의 사유가 plugin이라는 외부 발판으로 *확장*되되, 작품의 저자성은 작가에게 명확히 머무릅니다.

## 사용자 비대칭 (이건 모두를 위한 도구가 아닙니다)

명제적 언어화가 **병목**인 작가를 위한 도구:
- 초기 경력 작가 (artist statement / grant proposal 장르 관례 미숙)
- 제2언어 작가 (영문 grant 신청, 그 반대)
- PaR 박사 후보 (exposition 작성)
- 마감 직전 작가 (grant cycle, 레지던시 신청, 비엔날레 콜)
- 외부 스캐폴드가 도움 되는 작가

**아닌 경우:** 명제적 언어화가 이미 유창한 작가에게는 구조적으로 부적합. 즉흥/의례/구술 전통처럼 *언어화 자체를 거부하는* 전통에도 부적합.

## 6개 모드 (단일 스킬 `art-ideation`)

| 슬래시 커맨드 | 모드 | 산출물 |
|---|---|---|
| `/art-socratic` | 소크라테스 대화 | Concept Pull Map (impulses / fragments / constraints / refusals / **residue**) |
| `/art-provoke` | 도발 카드 | tradition-tagged 도발 8–20개, 자동 해석 금지(unhelpfulness 보존) |
| `/art-lineage` | 계보 지도 | **작가가 후보를 먼저 제시**해야 활성화. 학습-데이터 편향 헤더 의무. 한국어 세션은 한국/동아시아 자료 우선 |
| `/art-brief` | Concept Brief | proposition / **anti-proposition** / **disconfirmation 조건** / Frayling-type 선언 + stay-rough 기본값 |
| `/art-rehearsal` | 자기비평 리허설 | 4 페르소나 (큐레이터·실기 동료·이론가·Devil's Advocate). *형성적, 결정적 아님.* 매번 의무 disclaimer + persona-collapse 감지 |
| `/art-ideate` | 장기 프로젝트 파일 | 며칠/몇 주 간격 세션 across 누적 (Smith & Dean iterative cyclic web). 한 세션 = 한 모드 |

## IRON RULES

1. 탐색적 의도에서 자동 수렴 금지 (socratic)
2. Oblique-style 도발 후 침묵 (provoke) — 자동 해석 금지
3. 작가 후보 제시 없는 계보 제안 금지 (lineage)
4. 모든 Lineage Map에 학습-데이터 편향 헤더 의무 부착
5. Brief는 stay-rough 기본 — 작가 목소리 보존, 자동 윤문 금지
6. Brief 빈 필드는 *결손으로 보고*, 그럴듯한 채움 금지
7. Rehearsal 출력은 매번 disclaimer 헤더 의무
8. 랭킹 거부 — provocations / lineage / brief / rehearsal critiques 모두
9. Tradition tag는 *style affinity*, 인과적 attribution 아님
10. Full 모드는 세션 사이 영속성 — 단일 세션 파이프라인 금지

## Tradition tags + Authentic Practice Boundary

각 모드의 출력에는 *tradition tag* (어떤 선행 방법론에 grounding 됐는지)가 붙되, **각 방법론마다 Authentic Practice Boundary**가 함께 — plugin이 *시뮬레이션하지 않고 작가에게 위임하는 부분*을 명시.

- **Eno & Schmidt Oblique Strategies (1975).** 경계: 물리적·유한·맹목추출 카드 덱은 대체 불가. 진지한 사용은 실물 덱을 권장; plugin 출력은 *Oblique-affine* 수준.
- **Cage chance operations.** 경계: plugin은 procedure를 *기술*만 함. **주사위는 작가가 던집니다.** 작가가 procedure를 수행하는 *시간*이 작품의 일부이며, LLM이 "chance result"를 생성하면 그 인식론적 핵심이 무너집니다.
- **LeWitt instruction-based work.** 경계: plugin은 작가에게 instruction을 *쓰도록 prompt*만 함. **Instruction은 작가가 씁니다.** LeWitt의 "the idea is the machine that makes the art"는 작가가 rule-setter라는 조건이 핵심.
- **Bogart Viewpoints (1995).** 경계: Viewpoints는 *몸·앙상블·시간성*의 스튜디오 실천. plugin은 Viewpoints에서 *유도된 질문*만 가능; Viewpoints 작업 자체는 못 함.

전체 목록: [`art_ideation_methodology.md`](shared/references/art_ideation_methodology.md).

## Measured-harm 공개 (Model Cards 형식, Mitchell et al. 2019 + Bender et al. 2021 양식)

6개 harm class를 공개합니다 — [POSITIONING.md](POSITIONING.md) 참고:

1. **Lineage hallucination** — 서브도메인별 측정 (영어권 미디어아트 / 한국 미디어아트 / 퍼포먼스아트). 한국 미디어아트 같은 long-tail 도메인에서 작가/작품/전시 환각 위험.
2. **학습-데이터 canon 편향** — 영어권 well-funded 기관(Ars Electronica, ZKM, SIGGRAPH, Whitney, MIT) 과대표현. lineage 모드의 의무 헤더가 운영 형태.
3. **Simulation-pedagogy risk (rehearsal)** — Schön (1983) 인용. simulacrum critique으로 훈련하는 것이 실제 critique 수용 시 방어성 또는 과도순응을 키울 위험. v0.1의 mitigations: 의무 disclaimer + 아키텍처 마찰 + persona-collapse detector.
4. **저자성 인식 이동** — Wordcraft (Yuan 2022), Sparks (Gero 2022), ghostwriter 효과 (Draxler 2024 — verify). v0.1 mitigations: tradition tag footnote-level 가시성 기본값, brief stay-rough 기본값.
5. **Conviviality / normalization risk** (Illich 1973, Turkle 2015, Hui 2016) — plugin의 존재 자체가 LLM-매개의 *normalization*에 기여. 작가 자율성 commitment (랭킹 거부, IRON RULE 인간 결정, lineage opt-out)가 plugin을 conviviality 쪽에 놓는다는 입장은 *주장*이지 사실 아님.
6. **제한된 사용자 모집단** — 위 "사용자 비대칭" 섹션 참고.

## 학술 기여 (committed)

v0.2 synthesis spec §4.1의 네 가지 claim:

- **Claim A** (방법론): executable tradition-tag 참조 layer schema
- **Claim B** (Design-research): 5개 아키텍처 선택이 PaR commitment를 인코딩
- **Claim C** (인식론): cognitive scaffold position
- **Claim D** (Negative / 경계): pre-studio articulation phase의 구조적 분리

## 출판 venue 경로 (2026-05-25 개정 — Conceptual paper 우선, 실증 트랙은 그 다음)

1. ***Aslib JIM* (Aslib Journal of Information Management, Emerald)** — **v0.1 1차 출판**. **Conceptual paper** 분류 (4,000–10,000 단어, structured abstract, 사용자 평가 불필요). 작업 중 LaTeX 골조: [`art-project_paper/`](art-project_paper/).
2. ***Digital Creativity*** (Routledge) 자매 — methods paper, ~7,000 단어. Aslib JIM 심사 진입 후 제출.
3. **ACM C&C 2027 / 2028** — 실증 트랙. Study 1 (N=12 CSI / NASA-TLX 파일럿) + longitudinal 필요; Conceptual paper 제출 후 활성화.
4. **Journal for Artistic Research (JAR)** — exposition (전통적 논문 아님). Phase 5 출판으로 framework가 확립된 뒤.
5. **Leonardo / ISEA / SIGGRAPH Art Papers** — practitioner-facing. Longitudinal 데이터 확보 후.

## AI는 부조종사이지 조종사가 아닙니다 (그리고 작가의 사유를 *대체*하지 않습니다)

이 plugin은 작가를 위해 작품을 만들지 않습니다. 작품의 컨셉을 정하지도 않습니다. *언어화*만 도와줍니다 — 작가가 머릿속에 가진 충동을 grant 마감 직전에 종이 위로 옮기는 작업, 모호한 계보 감각을 명시적 후보 목록으로 정리하는 작업, 작가가 자기 자신에게 던질 어색한 질문을 미리 들이대는 작업.

작품은 작가가 만듭니다. 그 작품에 대한 권위 있는 결정은 작가가 합니다. plugin은 그 결정의 *준비 도구*입니다.

## 라이선스 & 인용

CC BY-NC 4.0. 비상업 사용. 상위 academic-research-skills(저자: Cheng-I Wu)에서 art-paper(Joon-Hyung Bae)를 거쳐 art-project로 pivot.

```
art-project (Version 0.1.0-ideation) [Computer software].
Pivoted from art-paper v0.1.0 (Joon-Hyung Bae),
itself forked from Academic Research Skills (Cheng-I Wu).
https://github.com/joonhyungbae/art-project
Companion paper: see docs/design/2026-05-24-art-project-v0.2-synthesis-spec.md.
```

상속된 ARS 전체 변경 이력(v1.0 → v3.9.4.2)은 [`ref/academic-research-skills/CHANGELOG.md`](ref/academic-research-skills/CHANGELOG.md).
