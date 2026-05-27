# 모드 개요

플러그인은 단일 스킬(`art-ideation`)에 6개 모드를 노출합니다. 각 모드는 3개의 핵심 아키텍처 약속(IRON rules)과 2개의 하위 규율 아래에서 작동합니다. 자세한 모드 설계는 저장소의 [MODE_REGISTRY.md](https://github.com/joonhyungbae/art-project/blob/main/MODE_REGISTRY.md)에 정리되어 있습니다.

## 6개 모드

| 모드 | 슬래시 명령 | 산출물 | 감독 강도 |
|---|---|---|---|
| [Socratic](socratic.md) | `/art-socratic` | 대화 + Concept Pull Map | Very High |
| [Provoke](provoke.md) | `/art-provoke` | 전통-태그된 provocation set (8–20 카드) | High |
| [Lineage](lineage.md) | `/art-lineage` | Lineage Map (5–15 선례, kin / opposition / blind-spot 태그) | Medium |
| [Brief](brief.md) | `/art-brief` | 10-필드 Concept Brief | High |
| [Rehearsal](rehearsal.md) | `/art-rehearsal` | 자기-비평 rehearsal transcript (4 페르소나) | High |
| [Full](full.md) | `/art-ideate` | 여러 세션에 걸친 장기 프로젝트 파일 | Very High |

## 기본 라우팅 규칙

| 상황 | 추천 모드 |
|---|---|
| 아직 컨셉이 없고 막연한 끌림 | `socratic` |
| 부분적 컨셉, 막힌 느낌 | `provoke` |
| 후보 lineage가 있고 확장하고 싶음 | `lineage` |
| 충분한 재료가 있고 명제 문서가 필요 | `brief` |
| 초안 brief가 있고 제출 전 부담 테스트 필요 | `rehearsal` |
| 주 단위로 이어지는 전체 호 | `full` |
| 모호함, 재료 없음 | `socratic` (default — 안내부터) |

## IRON rules (모드 공통)

1. **생성-평가 분리(Generation–evaluation separation)** — 탐색 의도에서 자동 수렴 금지. 플러그인은 후보를 산출하지만 아티스트가 아직 탐색 중일 때는 랭킹하거나 단일 추천으로 수렴하지 않습니다.
2. **랭킹보다 긴장(Tension-over-ranking)** — provocation은 반대 정식화와 함께 송출; Oblique 스타일 카드 발행 후 시스템은 침묵. 플러그인은 자신의 provocation을 아티스트 대신 해석하기를 거부합니다.
3. **전통-태그 + 진정성 실천 경계(Tradition-tag with authentic-practice boundary)** — 인용된 각 방법론은 AI가 시뮬레이션하지 *않는* 것에 대한 명시적 선언과 짝지어집니다. [진정성 실천 경계](../reference/authentic-practice-boundaries.md) 참조.

## 2개의 하위 규율

- **반대를 동반한 lineage(Lineage-with-opposition)** — `lineage` 모드는 artist-supplied 초기 후보를 요구하고, 필수 training-data bias header와 함께 송출하며, `--no-lineage` opt-out을 제공합니다.
- **decisional이 아닌 formative rehearsal** — `rehearsal` 모드는 disclaimer header와 함께 송출되고, 아키텍처 마찰(같은 컨셉에 대해 2회 / 14일 후 경고)과 persona-collapse 디텍터를 갖습니다.

## 어떤 모드도 하지 않는 것

- 작품을 만들지 않습니다.
- 아티스트·아이디어·방법론을 랭킹하지 않습니다.
- 명시적 사용자 트리거 없이 진행하지 않습니다 (turn-taking IRON rule).
- 탐색 의도에서 자동 수렴하지 않습니다.

## 명명 변경: `panel → rehearsal` (v0.2)

v0.1에서는 rehearsal 모드를 `panel`로 명명했습니다. 변경은 *method-not-evaluation* 판정을 명시합니다: `rehearsal`은 아티스트가 실제 큐레이터·동료·비평가를 마주하기 *전에* 자신의 작업을 질문 아래에서 명료화하는 연습을 할 수 있도록 존재합니다. 실제 비평은 관계적 역사(큐레이터의 수년에 걸친 스튜디오 방문, 동료의 씬에 대한 stake) — 어떤 시뮬레이션도 갖지 못한 것 — 로 구성됩니다; rehearsal은 아티스트 자신의 준비를 위한 것이지 대체 리뷰가 아닙니다.

## 모드 전환

모드 전환은 명시적입니다. `socratic`에서 `provoke`로 전환할 때 플러그인은 침묵으로 행동을 바꾸지 않고 전환을 명시합니다. 이것이 **모드 전환 투명성** 규칙입니다.

`/art-ideate`(full 프로젝트 파일)로 시작하면 파일이 각 세션이 어느 모드였는지 추적하므로 cross-session 전환을 감사할 수 있습니다.

## 참고

- [첫 세션](../getting-started/first-session.md) — `socratic`에서 시작하는 walkthrough.
- [Concept Brief 스키마](../reference/concept-brief.md) — `brief` 모드의 산출물.
- [인지적 스캐폴드](../philosophy/cognitive-scaffold.md) — 모드들이 운영화하는 철학적 입장.
