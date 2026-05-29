# Provoke 모드

> 슬래시 명령: `/art-project:provoke` — 부분적 컨셉이 있고 막혔을 때.

## 무엇을 하는가

8–20장의 **전통-태그된 provocation set**을 산출합니다. 각 카드는 방법론(Eno/Schmidt Oblique Strategies, Cage chance operations, LeWitt instruction-art, Viewpoints 등)으로 태그되고, 그 방법론이 요구하지만 AI가 시뮬레이션할 수 없는 것을 명시하는 **진정성 실천 경계(Authentic Practice Boundary)**를 동반하며, **반대 정식화(counter-formulation)**와 함께 송출되어 provocation이 단일 독해로 무너지지 않습니다.

카드 송출 후, 시스템은 침묵합니다. 플러그인은 아티스트를 대신해 카드를 해석하지 않습니다. 이것이 **보존된 불-유용성(preserved unhelpfulness)** 규칙입니다.

## 사용 시점

- 부분적 컨셉이 있고 막혔을 때.
- 익숙한 패턴 내에서 정제되기보다 *displaced* 되고 싶을 때.
- 트리거 표현: "give me provocations", "what if", "throw constraints at me" / 막혔어.

## 산출 구조

각 카드:

1. **The provocation** (짧고, 단정적이며, 종종 명령형)
2. **Tradition tag** (provocation을 grounding하는 방법론)
3. **Authentic Practice Boundary** (인용된 방법론이 요구하지만 AI가 수행할 수 없는 것)
4. **Counter-formulation** (반대 또는 인접 행보; provocation이 지시로 읽히지 않도록 의도적으로 함께 표시)

## IRON rules

- **랭킹보다 긴장(Tension-over-ranking)** — 모든 provocation은 counter-formulation과 함께; 세트는 랭킹되지 않음.
- **보존된 불-유용성(Preserved unhelpfulness)** — 카드 송출 후 플러그인은 침묵. 어느 카드를 따를지, 작업에 어떤 의미인지, 어떻게 조합할지 해석하지 않음.
- **방법론 시뮬라크럼 없음** — 인용된 모든 방법론에 대해 Authentic Practice Boundary가 대체할 수 *없는* 것을 명시함 (예: Oblique Strategies 덱의 물리적 blind-drawn 특성; Cage chance operation을 수행하는 아티스트의 시간).

## 하지 말 것

- **플러그인에게 카드를 골라달라고 요청하지 마세요.** 거부합니다. 고르는 것은 당신의 일입니다.
- **"내 프로젝트에 이게 무슨 뜻인지 설명해줘"라고 요청하지 마세요.** 거부합니다. provocation은 *displace*하는 것이지 지시하는 것이 아닙니다.
- **`socratic` 영역에 있을 때(즉 아직 컨셉이 없을 때) `provoke`를 실행하지 마세요.** 빈 공간에 대한 provocation은 displace하지 않고 invent 합니다.

## 출력 예시 (요약)

```text
Card 3 of 12
─────────────────────────────────────────────────────
PROVOCATION:    What if the documentation IS the work?

TRADITION TAG:  LeWitt instruction-based art (Paragraphs
                on Conceptual Art, 1967)

AUTHENTIC PRACTICE BOUNDARY:
                LeWitt은 아티스트가 instruction을 쓸 것을
                요구합니다. 플러그인은 provocation을 제안하지만
                instruction을 당신을 위해 저자화하지 않습니다.

COUNTER-FORMULATION:
                또는: documentation이 없고, 흔적만
                있다면 어떻게 될까?
─────────────────────────────────────────────────────

[12 카드 전달. 시스템 침묵. 함께 머무세요.]
```

## 다음 행보

provocation 이후:

- 카드들과 몇 시간 또는 며칠 함께 머물기; 즉시 다음 모드로 점프하지 마세요.
- 카드가 후보 lineage를 표면화하면 [`lineage`](lineage.md)로 전환.
- 카드가 brief에 충분한 재료를 산출하면 [`brief`](brief.md)로 전환.
- 특정 태그에 대한 추가 provocation이 필요하면 그 태그를 명시하고 `provoke` 재진입.

## 참고

- [진정성 실천 경계](../reference/authentic-practice-boundaries.md) — per-method 선언.
- [전통 태그](../reference/tradition-tags.md) — provocation이 draw하는 코퍼스.
