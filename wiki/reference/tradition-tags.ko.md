# 전통 태그

플러그인은 provocation, lineage 확장, authentic-practice boundary를 이전 ideation 방법론 코퍼스에 grounding합니다. 각 항목은 고정된 6-필드 스키마로 구조화된 **전통 태그(tradition tag)**입니다.

## 항목당 6개 필드

1. **Author + year** — 아티스트가 primary source를 읽을 수 있는 bibliographic anchor.
2. **Core gesture** — 한 문장으로 표현된 방법론의 중심 행보.
3. **Ideation mechanism** — 방법론이 활성화하는 것 (chance, constraint, instruction, embodied protocol, …).
4. **Authentic Practice Boundary** — 방법론이 요구하지만 AI가 시뮬레이션하지 않는 것. [진정성 실천 경계](authentic-practice-boundaries.md) 참조.
5. **Contested in** — 방법론이 받은 counter-position 또는 비판.
6. **Skill-hook** — 어느 플러그인 모드(socratic, provoke, lineage, brief, rehearsal, full)가 항목을 소비하는지.

## 코퍼스 (약 25개 항목)

다섯 카테고리에 걸쳐:

- **General creativity and cognition theory** — Geneplore (Finke / Ward / Smith 1992), combinational / exploratory / transformational creativity (Boden 2004), SCAMPER (Eberle 1971).
- **Design and planning methodology** — Shneiderman creativity-support principles (2007), reflective practice (Schön 1983), studio-as-laboratory (Edmonds 외 2005).
- **Art-specific methodologies** — Oblique Strategies (Eno & Schmidt 1975), instruction art (LeWitt 1967), chance operations (Cage 1961), Viewpoints (Bogart & Landau 2005).
- **Media-art and technology** — embodied epistemology (Penny 2017), speculative design (Dunne & Raby 2013).
- **비-anglophone context** — Paik *Exposition of music* (1963), cosmotechnics (Hui 2016), 한국 맥락 PaR (Lee & Lee 2024).

비-anglophone 카테고리는 **의도적으로 불완전**합니다 — 현재 under-developed인 [`measured harms`](../philosophy/measured-harms.md) 클래스입니다. 한국-맥락 후보들은 v0.1에서 ship되지만 더 넓은 동아시아·Global South 커버리지는 v0.3+ 목표입니다.

## 전통 태그가 무엇이고 무엇이 아닌가

- 전통 태그는 **prompt-grounding 및 style-affinity claim**입니다: "이 항목이 prompt에 로드되었다; 출력은 이 전통의 style affinity 내에서 작동하도록 의도한다."
- 전통 태그는 **causal-attribution claim이 아닙니다**. 플러그인은 LLM의 생성 메커니즘이 named 전통에 causally traceable하다고 주장하지 않습니다; 메커니즘은 opaque합니다.

이 구분은 load-bearing입니다. `전통 태그`라는 라벨은 의도적입니다: 플러그인은 overclaim을 거부하고, 실제로 수행된 grounding 작업(prompt conditioning, boundary 선언, bibliographic anchoring)에 contribution을 둡니다.

## 태그가 플러그인 출력에 나타나는 방식

- **`provoke`에서**: 모든 provocation 카드가 하나 이상의 태그를 carry. 아티스트는 provocation이 어느 전통에 conditioning되었는지 정확히 볼 수 있음.
- **`lineage`에서**: lineage map 항목은 관련 있는 경우 방법론적 전통으로 태그됨.
- **`brief`에서**: brief의 Provocation, Proposition, Anti-proposition, Lineage anchor, Frayling-type-declaration 필드가 각 cell을 grounding하는 전통을 보여주는 태그를 carry.

## 새 태그 추가

코퍼스는 open입니다. 새 전통 태그를 제안하려면 6-필드 구조가 populated된 채로 [`shared/references/art_ideation_methodology.md`](https://github.com/joonhyungbae/art-project/blob/main/shared/references/art_ideation_methodology.md) 파일에 PR을 제출하세요. [기여](../contributing.md) 참조.

## 참고

- [진정성 실천 경계](authentic-practice-boundaries.md) — per-method 선언.
- [Provoke 모드](../modes/provoke.md) — 전통 태그가 가장 무겁게 사용됨.
- [Lineage 모드](../modes/lineage.md) — 전통 태그가 위치 attribution을 shape함.
