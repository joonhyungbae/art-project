# Frayling 분류

[Christopher Frayling 1993](https://researchonline.rca.ac.uk/384/9/frayling_research_in_art_and_design_1993_OCR.pdf)은 practitioner와 art / design 분야 사이의 세 가지 종류의 연구 관계를 구분했습니다:

- **Research *into* art** — 대상이 art인 역사·이론적 inquiry. 미술사학자의 작업.
- **Research *through* art** — 예술 실천이 지식 생성의 수단인 inquiry. 연구자로서의 아티스트; 실천이 findings를 산출.
- **Research *for* art** — 만듦을 지원하고 작품 자체가 지식이 embodied되는 locus인 inquiry. articulate하기 가장 어려운 카테고리.

Frayling 본인이 세 번째를 가장 어렵다고 flag했습니다: 출력이 paper가 아니라 종종 비-명제적으로 지식을 *embed*하는 작품인 연구.

## 플러그인이 이 분류를 사용하는 이유

세 가지 이유:

1. **영어권 PaR 문헌에서 가장 널리 engaged된 practice-based research 분류**이고, 플러그인 대상 인구(언어를 가로질러 글을 쓰는 아티스트, doctoral exposition 후보)가 마주칠 가능성이 높음.
2. **인식론적 commitment를 강제**하는데, 영어 artist statement는 종종 이를 paper over함. 프로젝트가 어떤 종류의 연구인지를 stating하고 — held to that — 그 자체가 practice-based research 규율의 일부.
3. **세 번째 카테고리의 articulation 어려움이 플러그인의 design space**. 프레임워크는 Frayling 본인이 어려움을 flag한 research-for-art *주변의* 명제적 articulation 작업을 scaffolding함.

## 플러그인이 이 분류로 하지 *않는* 것

이전 프레임워크 초안은 플러그인을 Frayling "layered hybrid"로 다뤘습니다 — 프로젝트의 다른 sub-artefact(작동 중인 플러그인 / reference layer / design-choice layer)에 research-for, research-into, research-through를 assign. 이것은 Frayling이 인식하지 않을 Frayling 행보입니다: 그는 *지식 주장*의 종류를 구분했지 단일 프로젝트의 sub-artefact에 대한 라벨을 구분하지 않았습니다.

현재 프레임워크는 layered-hybrid framing을 폐기합니다. paper는 research *for* art(아티스트 자신의 pre-studio articulation 도구화)이고 research-*into*-art 컴포넌트(전통 태그 reference layer와 그 코퍼스 조사)를 포함합니다. design-choice rationale은 free-standing research-through-art claim이 아니라 [design-research-through-design](https://dl.acm.org/doi/10.1145/1240624.1240704) (Zimmerman 외 2007)으로 다룹니다 — design-choice layer가 research-through-art 카테고리가 요구하는 embodied-knowledge locus를 갖지 않기 때문입니다.

## Sullivan의 세 stance (더 세밀한 어휘)

[Sullivan 2010](https://us.sagepub.com/en-us/nam/art-practice-as-research/book230864)은 같은 영토를 세 종류의 연구가 아닌 세 *stance*로 구조화합니다:

- **Conceptual** — 아티스트가 주장을 하고 만들기를 통해 테스트.
- **Dialectical** — 아티스트가 입장을 그 반대 위치에 두고 긴장을 작업.
- **Contextual** — 아티스트가 작업을 lineage에 position.

플러그인은 Sullivan의 어휘를 특정 장소에서 사용합니다:

- [`lineage`](../modes/lineage.md)의 **lineage-positioning 행보**는 contextual.
- **tension-over-ranking commitment** ([`provoke`](../modes/provoke.md)의 provocation + counter-formulation)은 dialectical.
- 프레임워크의 **네 가지 명명된 contribution** ([README](https://github.com/joonhyungbae/art-project) 참조)은 conceptual.

## Frayling-type declaration 필드

[`brief`](../modes/brief.md) 모드에서 Concept Brief의 field 10은 Frayling-type declaration입니다. 아티스트는 프로젝트가 research *into*, *through*, 또는 *for* art 중 무엇인지 명시해야 합니다. 플러그인은 아티스트를 대신해 고르지 않습니다.

brief 모드 동반 system prompt는 declaration에 따라 downstream 필드를 다르게 weighting하도록 지시받습니다:

- Research-*through*-art → 방법론-as-medium 긴장(provocation, anti-proposition) 강조.
- Research-*for*-art → proposition-disconfirmation 짝짓기 강조.
- Research-*into*-art → lineage anchor와 intended encounter 강조.

conditioning이 downstream cell content를 *바꾸는지*(versus 아티스트에게만 reflexive prompt로 봉사하는지)는 **unablated**입니다. 필드 주변 플러그인 행동은 인식론적 commitment를 surface하기 위해 존재하고; 필드가 downstream cell에 *작동하는지*는 미래 user study를 위한 empirical 질문입니다.

## Frayling을 honestly 읽기

Frayling의 분류는 [Borgdorff](https://lup.nl/publications/art/the-conflict-of-the-faculties/), [Sullivan](https://us.sagepub.com/en-us/nam/art-practice-as-research/book230864), [Smith & Dean](https://edinburghuniversitypress.com/book-practice-led-research-research-led-practice-in-the-creative-arts.html), [Barrett & Bolt](https://www.bloomsbury.com/us/practice-as-research-9781845115593/)에 의해 정제·이의 제기되었습니다. 이 비판들은 플러그인 설계 선택에 surface합니다:

- Borgdorff의 *not-yet-knowing* / dual-discourse → [Concept Brief](../reference/concept-brief.md) Provocation 필드; Smith & Dean의 *iterative cyclic web* → [`full` 모드](../modes/full.md) cross-session 구조; Barrett & Bolt의 *materiality* → [진정성 실천 경계](../reference/authentic-practice-boundaries.md).

프레임워크는 이것들을 Frayling으로 collapse하지 않습니다. distinct로 honored되고, Frayling은 Frayling의 특정 contribution이 작동하는 곳에서만 named됩니다.

## 참고

- [인지적 스캐폴드](cognitive-scaffold.md) — 분류 내 플러그인의 위치.
- [Brief 모드](../modes/brief.md) — declaration 필드가 있는 곳.
- [Concept Brief 스키마](../reference/concept-brief.md) — 전체 필드 명세.
