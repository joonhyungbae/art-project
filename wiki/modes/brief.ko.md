# Brief 모드

> 슬래시 명령: `/art-brief` — 명제 문서를 위한 충분한 재료가 있을 때.

## 무엇을 하는가

아티스트가 그랜트 신청서·레지던시 제안서·doctoral exposition·collaborator briefing에 가져갈 수 있는 **10-필드 Concept Brief**를 산출합니다. 모드는 **stay-rough default**로 작동합니다: 아티스트의 목소리가 보존되고 (AI register로 다듬어지지 않음), 빈 필드는 그럴듯한 텍스트로 채워지지 않고 gap으로 보고됩니다.

전체 필드별 명세는 [Concept Brief 스키마](../reference/concept-brief.md) 참조.

## 사용 시점

- `socratic` / `provoke` / `lineage`를 거치며 실질적 재료가 모였을 때.
- 제출 마감이 명제 문서 산출을 강제할 때.
- 인식론적 약속(Frayling type, lineage anchor, disconfirmation condition)을 prose에 밀반입되기 전에 가시화하고 싶을 때.
- 트리거 표현: "draft a concept brief", "write up what I have so far", "one-pager for [grant / collaborator / self]".

## 10개 필드

1. **Working title** — placeholder 수용.
2. **Provocation** (Borgdorff 의미) — 작업이 추구하는 not-yet-knowing.
3. **Proposition** — 작업이 하는 주장.
4. **Anti-proposition** (Sullivan dialectical 의미) — 작업이 반대하는 것.
5. **Disconfirmation condition** — 스튜디오 용어로 작업을 falsify하는 것.
6. **Intended encounter** (Viewpoints 의미) — 작업이 어떻게 만나지길 의도하는지.
7. **Lineage anchor** — 작업이 position하는 선례 (`lineage` 모드에서).
8. **Materials and scale** — 재료적 약속 (크기·지속시간 포함).
9. **Risk and refusal** — 작업이 risk하는 것; 거부하는 것.
10. **Frayling-type declaration** — research *into* / *through* / *for* art.

## IRON rules

- **Stay-rough default** — 이전 모드에서 온 필드의 아티스트 목소리는 그대로 보존됩니다. 플러그인이 단편을 prose로 다듬지 않습니다.
- **gap은 gap으로 보고** — 필드에 재료가 없으면 플러그인은 `[gap, not in input]`으로 표시하고 content를 fabricate하지 않습니다. 이것이 **no-fabrication** 규율입니다.
- **`--polish`는 opt-in만** — 제출용으로 brief를 smooth하고 싶다면 명시적으로 요청해야 합니다. default는 rough입니다.

## Frayling-type declaration

대부분 아티스트가 건너뛰는 필드. 플러그인은 선언을 명시적으로 만들 것을 요구합니다: 당신의 프로젝트는 research *into* art (대상이 art인 역사·이론적 inquiry)인가, research *through* art (지식 생성의 수단으로서의 예술 실천)인가, research *for* art (만듦을 지원하고 작품 자체가 지식의 locus인 inquiry)인가?

Frayling 본인이 세 번째 카테고리를 가장 articulate하기 어렵다고 flag했습니다. 이 필드는 그 어려움을 paper over하지 않고 surface하기 위해 존재합니다. [Frayling 분류](../philosophy/frayling-typology.md) 참조.

## 하지 말 것

- **불충분한 재료로 `brief`를 실행하지 마세요.** 대부분 필드가 `[gap]`이 될 것 같으면 `socratic`이나 `provoke`로 먼저 돌아가세요.
- **플러그인에게 "gap을 채워달라"고 요청하지 마세요.** Gap-acknowledgement가 규칙입니다. Polish(`--polish`로)는 gap을 채우지 않고 기존 재료를 smooth합니다.
- **brief를 최종으로 다루지 마세요.** 사유의 한 순간 스냅숏입니다; 다음 세션은 다른 brief를 산출할 수 있습니다.

## 출력 예시 (요약)

```text
CONCEPT BRIEF — [working title]

1. Working title: "Inscription / counter-inscription"

2. Provocation:
   What the artist wrote and what was written on the artist —
   the back of a photograph; the family record that was not
   the family's. [Borgdorff: not-yet-knowing.]

3. Proposition:
   [stay-rough from session 4 socratic]
   the work is about marks that don't claim authorship

4. Anti-proposition:
   [gap, not in input]

5. Disconfirmation condition:
   the work fails if the viewer reads it as a memorial.

6. Intended encounter:
   [gap, not in input]

7. Lineage anchor:
   From Lineage Map: opposition to On Kawara's date paintings
   (Kawara claims authorship through ritual; this work refuses
   the claim). Kin: [the artist's lineage candidate, name held
   for review].

8. Materials and scale:
   [stay-rough from session 2 socratic]
   photographs, the size of a hand. number unknown yet.

9. Risk and refusal:
   Risk: the work reads as nostalgia.
   Refusal: not a memorial; not a family history piece.

10. Frayling-type declaration:
    Research-FOR art (만듦을 지원하는 작업, 작품이 지식의
    locus). [Artist must confirm.]
```

## 다음 행보

- 제출 전에 하루 이상 brief와 함께 머무세요.
- 제출 전 부담 테스트를 위해 [`rehearsal`](rehearsal.md)로 전환.
- gap을 채워야 하면 해당 필드를 위해 `socratic` / `provoke` / `lineage`로 돌아가기.

## 참고

- [Concept Brief 스키마](../reference/concept-brief.md) — 전체 필드별 명세.
- [Frayling 분류](../philosophy/frayling-typology.md) — 선언 필드가 아티스트에게 약속시키는 것.
