# Rehearsal 모드

> 슬래시 명령: `/art-project:rehearsal` — 제출 전 초안 brief의 부담 테스트.

## 무엇을 하는가

brief가 4개 명명된 페르소나 — **Curator**, **Practitioner-peer**, **Theorist**, **Devil's Advocate** — 의 질문을 받는 **자기-비평 rehearsal**을 실행합니다. 출력은 transcript: 각 페르소나의 질문, 아티스트의 응답(또는 막힌 지점), brief가 어디에서 견뎠고 어디에서 휘었는지의 요약.

모드는 **decisional이 아닌 formative**입니다: 아티스트가 실제 큐레이터·동료·비평가를 마주하기 *전에* 자신의 작업을 질문 아래에서 명료화하는 연습을 할 수 있도록 존재합니다. 실제 비평을 대체하지 않습니다.

## 사용 시점

- [`brief`](brief.md) 모드에서 초안 Concept Brief가 있을 때.
- 제출·스튜디오 방문·동료 리뷰가 다가올 때.
- 다른 누군가가 발견하기 전에 약한 articulation 지점을 찾고 싶을 때.
- 트리거 표현: "stress-test this", "rehearse for curatorial feedback", "tear it apart in safety".

## 필수 disclaimer header

모든 rehearsal transcript는 다음으로 시작합니다:

```text
REHEARSAL DISCLAIMER
─────────────────────────────────────────────────────
이것은 formative 연습이지 decisional 리뷰가 아닙니다.
아래 페르소나는 시뮬레이션이며; 그들의 질문은 실제
큐레이터·동료·비평 피드백을 대체하지 않습니다.
실제 비평은 시뮬레이션이 갖지 못한 관계적 역사로
구성됩니다.

이 rehearsal을 사용해 질문 아래에서 작업을 articulate
하는 연습을 하세요. brief가 "준비되었다" 또는 "준비되지
않았다"의 증거로 사용하지 마세요 — 그 판단은 실제
interlocutor를 요구합니다.
─────────────────────────────────────────────────────
```

disclaimer는 선택사항이 아닙니다.

## 아키텍처 마찰

같은 컨셉에 대해 **14일 내 2회** `rehearsal` 호출 후, 플러그인은 friction 경고를 발행합니다:

```text
FRICTION WARNING
─────────────────────────────────────────────────────
이 컨셉을 지난 14일 내 2회 rehearse 했습니다. 추가
rehearsal은 simulation-pedagogy harm (Schön 1983)을
risk합니다: 시뮬레이션에서 반복 rehearse하는 아티스트는
실제로 마주할 비평과 구조적으로 다른 안전한 비평에 대해
방어하도록 자신을 훈련시킬 수 있습니다.

고려: (a) brief를 실제 interlocutor에게 가져가기;
(b) rehearsal에서 표면화된 질문들과 함께 socratic /
provoke로 돌아가기; (c) 추가 rehearsal 없이 brief와
함께 머물기.

그래도 진행? [y/N]
─────────────────────────────────────────────────────
```

이 마찰은 아키텍처적이지 advisory가 아닙니다; 임계값 이후 매번 경고가 발생합니다.

## Persona-collapse 디텍터

rehearsal 중 둘 이상의 페르소나가 같은 질문 라인으로 수렴하면 플러그인은 **persona collapse**를 flag합니다: 시뮬레이션이 distinct 관점 유지에 실패하고 있고, rehearsal이 더 이상 informative하지 않습니다. 아티스트에게 세션 종료가 권장됩니다.

## 4개 페르소나

- **Curator** — 작업의 프로그램·venue·public과의 관계를 묻습니다. curatorial 어휘 및 institutional fit과의 일관성을 신경 씁니다.
- **Practitioner-peer** — brief가 함의하는 스튜디오 결정을 묻습니다. 재료, 시간, 작업이 만든이에게 요구하는 것을 신경 씁니다.
- **Theorist** — 작업의 이론적 anchor와 작업이 안다고 주장하는 것을 묻습니다. 인식론적 일관성을 신경 씁니다.
- **Devil's Advocate** — 아티스트가 가장 받기 두려워하는 질문을 묻습니다. 생산적 불편함을 신경 씁니다.

## IRON rules

- **decisional이 아닌 formative** — disclaimer header가 필수; rehearsal 출력은 결코 평가로 framing되지 않음.
- **아키텍처 마찰** — 2/14 friction 경고가 자동 발사됨.
- **Persona-collapse 디텍터** — 플러그인이 페르소나 수렴을 self-monitor하고 flag함.

## 하지 말 것

- **Concept Brief 없이 `rehearsal`을 실행하지 마세요.** 부담 테스트할 대상이 없습니다.
- **rehearsal을 피드백으로 다루지 마세요.** 실제 피드백은 관계적 역사를 가진 실제 interlocutor에서 옵니다.
- **rehearsal을 brief를 그 자리에서 "고치는" 데 사용하지 마세요.** 약한 지점을 찾는 데 사용하고, 해당 모드로 돌아가서 처리하세요.

## 다음 행보

- rehearsal이 약한 필드를 표면화하면 그 필드를 위해 `socratic` / `provoke` / `lineage`로 돌아가기.
- brief가 견뎠다면 다음 단계는 실제 비평 (스튜디오 방문, 동료 독서, 제출).
- 같은 컨셉을 다시 rehearse하고 싶어진다면 friction 경고가 진짜 신호입니다 — 함께 머무세요.

## 참고

- [측정 가능한 위해](../philosophy/measured-harms.md) — simulation-pedagogy harm class.
- [Brief 모드](brief.md) — rehearsal 진입 전 갖춰야 할 것.
