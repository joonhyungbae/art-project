# 측정 가능한 위해 (Measured harms)

프레임워크는 artefact가 야기하거나 기여할 수 있는 6개 클래스 위해의 명시적 disclosure와 함께 ship됩니다. disclosure는 [model-cards 형식](https://dl.acm.org/doi/10.1145/3287560.3287596) (Mitchell 외 2019)과 [stochastic-parrots 성향](https://dl.acm.org/doi/10.1145/3442188.3445922) (Bender 외 2021) — AI 시스템이 설계상 전파하는 harm을 명명하려는 — 을 따릅니다.

프레임워크가 잘못할 수 있는 것을 명명하는 것 자체가 설계의 일부입니다 — 사후 disclaimer가 아닙니다.

## 6개 위해 클래스

### 1. Long-tail sub-domain에서의 lineage hallucination

`lineage` 모드는 training-data 커버리지가 thin한 domain에서 아티스트·전시·작품을 hallucinate할 수 있습니다. 정전적 LLM 실패 모드: 아티스트가 이미 분야를 알지 않으면 실제 선례와 구분하기 어려운 fabrication.

**완화**: 모든 Lineage Map에 필수 bias header; lineage 확장 전 artist-supplied 초기 후보 요구; `--no-lineage` opt-out.

### 2. Training-data canon 편향

LLM substrate는 anglophone 미디어아트 venue (Rhizome, e-flux, Frieze, Artforum), 1990s–2010s US/UK/DE generative-art 씬, 정전화된 conceptual art (LeWitt, Weiner, On Kawara)를 over-represent합니다. 비-anglophone PaR doctoral exposition, 한국·동아시아 미디어아트 (특히 2010년대 이후), 구술·의례·즉흥 전통, collective·anonymous 실천을 under-represent합니다.

**완화**: 세션 신호가 요구하면 runtime 비-anglophone 라우팅; `lineage` 모드의 필수 bias header. 기저 코퍼스 편향은 구조적이고 **숨겨지지 않고 명명됩니다**.

### 3. Rehearsal의 simulation-pedagogy risk

[Schön 1983](https://www.basicbooks.com/titles/donald-a-schon/the-reflective-practitioner/9780465068784/)을 draw하여: 시뮬레이션에서 반복 rehearse하는 아티스트는 안전한 비평에 대해 방어하거나 low-stakes 피드백에 over-comply하도록 자신을 훈련시킬 수 있습니다. 위험은 아티스트가 시뮬레이션된 종류의 비평에 능숙해지면서 실제 종류에는 비례적으로 덜 준비되는 것입니다.

**완화**: 모든 rehearsal transcript에 필수 disclaimer header; 같은 컨셉에 대해 14일 내 2회 호출 후 아키텍처 마찰; persona-collapse 디텍터. 장기 효과는 open question으로 명명; deferred 종단 연구가 proper instrument.

### 4. Brief 모드의 authorship-perception 이동

[AI ghostwriter effect](https://dl.acm.org/doi/10.1145/3637875) (Draxler 외 2024)는 사용자에 의한 AI 기여 under-claiming입니다. 아티스트는 framing이 플러그인에서 왔다는 것을 register하지 않고 brief의 재료를 그랜트 신청서로 가져갈 수 있어, 자신의 사유가 어디에서 끝나고 스캐폴드가 시작되었는지의 self-knowledge가 erode됩니다.

**완화**: stay-rough default가 아티스트의 목소리를 verbatim 보존 (아티스트가 자신의 것이라고 들을 수 있음); footnote-level 전통-태그 attribution이 스캐폴딩이 들어온 곳을 surface. Draxler 본인의 발견은 footnote attribution이 *더 약한* 개입 중 하나임을 시사; 완화는 solved가 아닌 design 가설. between-subjects attribution-UI 테스트는 미래 user study로 sequenced.

### 5. Conviviality 및 normalisation risk

[Illich 1973](https://en.wikipedia.org/wiki/Tools_for_Conviviality): 한 능력을 돕겠다고 약속하는 도구는 그 능력의 매개를 normalise할 수 있어, 매개되지 않은 버전이 더 어려운 경로가 됩니다. [Turkle 2015](https://www.penguinrandomhouse.com/books/315557/reclaiming-conversation-by-sherry-turkle/)는 이것을 주의와 대화로 확장; [Hui 2016](https://www.urbanomic.com/book/the-question-concerning-technology-in-china/)은 비-서구 기술 cosmology로 확장.

프레임워크의 존재는 — 최근까지 매개가 부재했던 — 인지 domain에서 LLM 매개의 normalisation에 기여합니다.

**완화**: 아티스트 자율성에 대한 아키텍처 commitment (랭킹 거부, 작품 참여 거부, 탐색 의도에서 수렴 거부, `rehearsal`의 아키텍처 마찰)가 프레임워크를 Illich의 line의 convivial 측에 둡니다. 입장은 settled가 아닌 contestable.

### 6. 한정된 사용자 인구

user-asymmetry scope statement 자체가 harm disclosure입니다. 프레임워크는 명제적 articulation이 병목인 아티스트를 위해 scoped됩니다. 명명된 인구 밖의 아티스트에게 프레임워크는 **suboptimal이 아닌 unsuitable**입니다.

구체적으로, 프레임워크는 다음에 unsuitable:

- articulation이 이미 유창한 아티스트 (스캐폴드가 방해)
- articulation이 본질적으로 unwanted인 전통 (즉흥, 의례, 구술)
- 명제적 artefact가 실천을 적극적으로 손상시키는 맥락 (일부 performance 맥락; 일부 ceremonial 전통)

프레임워크가 *무엇을 위한* 것이 아닌지 명명하는 것은 약점이 아닌 강화 행보로 다뤄집니다.

## 이 disclosure가 주장하지 *않는* 것

- **exhaustive하지 않음.** 6개 클래스가 명명됨; deployment에서 새 클래스가 surface할 수 있음.
- **solved가 아님.** 각 클래스는 완화를 가짐; 어떤 것도 "fixed"가 아님. 완화는 user-study 확인을 기다리는 design 가설.
- **외부 검증되지 않음.** 이것은 self-disclosure임; 독립 audit은 프레임워크 architect가 보지 못하는 harm을 surface할 것임.

## 왜 disclose하는가?

세 가지 이유:

1. **정직성.** 프레임워크는 명명하지 않은 것을 deliver할 수 없음. harm 클래스 disclosure는 아티스트가 informed consent로 프레임워크를 사용하기 위한 precondition.
2. **Auditability.** 각 harm 클래스는 특정 아키텍처 완화에 연결됨. disclosure가 완화를 checkable하게 함.
3. **Scope 규율.** Disclosure가 프레임워크가 무엇을 *잘못* 하는지 마주하도록 강제하여, *잘* 하는 것을 over-claim하려는 유혹을 제약함.

## 참고

- [인지적 스캐폴드](cognitive-scaffold.md) — harm이 disclosed되는 입장.
- [Frayling 분류](frayling-typology.md) — bounded-user-population 클래스를 ground하는 분류.
- [진정성 실천 경계](../reference/authentic-practice-boundaries.md) — harm 클래스 #1을 완화하는 per-method 규율.
