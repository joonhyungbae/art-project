# Lineage 모드

> 슬래시 명령: `/art-project:lineage` — 후보 선례가 있고 확장하고 싶을 때.

## 무엇을 하는가

5–15명/점의 선례 아티스트·작품·텍스트로 구성된 **Lineage Map**을 산출합니다. 각각 당신의 작업에 대해 4개 위치 중 하나로 태그됩니다: **kin** (가까운 친연), **opposition** (생산적 대조), **blind-spot** (kin 전통이 보지 못하는 것), 또는 **unexpected-neighbor** (아티스트가 스스로 떠올리지 못했을 선례).

map은 LLM substrate가 어떤 sub-domain을 over-represent하고 어떤 것을 under-represent하는지 공시하는 **필수 training-data bias header**와 함께 송출됩니다.

## 사용 시점

- 후보 선례 2–3개를 명명할 수 있고 map 확장을 원할 때.
- brief 작성 전에 전통 내에서 작업을 position하고 싶을 때.
- 트리거 표현: "who else has done this", "where am I in the field", "position my work".

## 강제 요구사항: artist-supplied 초기 후보

`lineage` 모드는 **충동만으로 lineage를 산출하지 않습니다**. 플러그인이 확장하기 전에 최소 2개의 후보 선례(아티스트·작품·텍스트)를 supply해야 합니다. 이유: long-tail sub-domain에서의 lineage hallucination은 LLM lineage 도구의 가장 흔한 실패 모드이고, artist-supplied anchor는 실패 공간을 실질적으로 제약합니다.

후보가 아직 없다면 [`socratic`](socratic.md) 또는 [`provoke`](provoke.md)부터 시작하세요.

## Training-data bias header (필수)

모든 Lineage Map과 함께 송출되는 공시:

```text
TRAINING-DATA BIAS DISCLOSURE
─────────────────────────────────────────────────────
LLM substrate over-represents: anglophone 미디어아트
venue (Rhizome, e-flux, Frieze, Artforum); 1990s-2010s
US/UK/DE generative-art 씬; 정전화된 conceptual art
(LeWitt, Weiner, On Kawara).

Under-represented: 비-anglophone PaR doctoral exposition;
한국·동아시아 미디어아트 씬 (특히 2010년대 이후);
구술·의례·즉흥 전통; collective·anonymous 실천.

이 map은 이 편향을 염두에 두고 읽어야 합니다. 작업이
그러한 전통에 기반한다면 비-anglophone 후보를 명시적으로
추가하세요; 플러그인이 그에 따라 라우팅합니다.
─────────────────────────────────────────────────────
```

## 위치 태그

- **Kin** — 선례가 방법·재료·이해관계를 공유. lineage 연속성을 position하는 데 사용.
- **Opposition** — 선례가 당신의 이해관계와 반대로 작동; 대조가 당신의 작업이 *무엇인지* 명료화함.
- **Blind-spot** — 선례의 전통이 당신의 작업이 보는 것을 보지 못함. 당신의 작업이 가져오는 것을 명명함.
- **Unexpected-neighbor** — 아티스트가 스스로 떠올리지 못했을 선례; 관련성이 단언되지 않고 아티스트가 평가하도록 flag됨.

## 한국·동아시아 default 라우팅

세션 신호(입력 언어, 명명된 후보, 명시적 선언)가 한국·동아시아 맥락을 시사하면, 플러그인은 Lineage Map에서 비-anglophone 소스에 우선순위를 둡니다. bias header는 여전히 송출되지만 코퍼스 가중치가 이동합니다.

## Opt-out

training-data bias header 없는 Lineage Map을 원하면(예: 편향이 무관한 sub-domain) 요청에 `--no-lineage` 플래그를 사용하세요. 플래그는 항상 사용 가능합니다.

## 하지 말 것

- **초기 후보 supply 없이 lineage 확장을 요청하지 마세요.** 플러그인이 먼저 후보를 요구합니다.
- **Lineage Map을 랭킹으로 다루지 마세요.** 4개 위치 태그는 범주적이지 순서적이지 않습니다.
- **unexpected-neighbor 항목을 추천으로 다루지 마세요.** 당신의 평가를 위해 flag된 것입니다.

## 다음 행보

- Lineage Map이 강한 위치 감각을 산출하면 [`brief`](brief.md)로 전환하고 lineage를 lineage-anchor 필드로 사용.
- kin 항목이 심문하고 싶은 방법론을 시사하면 그 전통 태그로 [`provoke`](provoke.md)로 전환.

## 참고

- [전통 태그](../reference/tradition-tags.md) — 플러그인이 draw하는 방법론 코퍼스.
- [측정 가능한 위해](../philosophy/measured-harms.md) — bias header가 필수인 이유.
