# Art-project

실천 기반 예술 연구(practice-based artistic research)를 위한 **스튜디오 진입 전 단계의 *언어화* 스캐폴드(pre-studio articulation scaffold)** Claude Code 플러그인입니다.

**아이데이션 엔진이 아닙니다.** Penny / Ingold / Borgdorff의 비판 — 예술의 ideation은 비언어적이고 물질적이며 만듦과 분리되지 않는다 — 을 *받아들이고*, 플러그인의 범위를 ideation을 *둘러싼* 명제적 언어화 작업으로 한정했습니다. 실제 ideation은 작업실에서, 재료와 함께 일어납니다.

---

## 이 위키의 목적

`art-ideation` 스킬의 6가지 모드 사용법, 핵심 스키마(Concept Brief, 전통 태그, 진정성 실천 경계), 그리고 프레임워크의 설계 철학을 정리합니다.

- **처음이신가요?** [설치](getting-started/install.md) → [첫 세션](getting-started/first-session.md)부터.
- **특정 모드를 찾고 계신가요?** [모드 개요](modes/overview.md)를 보세요.
- **설계 근거가 궁금하신가요?** [인지적 스캐폴드](philosophy/cognitive-scaffold.md), [Frayling 분류](philosophy/frayling-typology.md)를 보세요.
- **기여하거나 확장하실 건가요?** [기여](contributing.md) 참조.

## 대상 사용자

명제적 언어화가 병목인 다음과 같은 아티스트를 위해 설계되었습니다:

- 아티스트-스테이트먼트 관습이 아직 익숙하지 않은 신진 아티스트
- 모국어와 다른 언어로 글을 써야 하는 아티스트 (예: 영어 그랜트 신청서를 작성하는 한국어 모국어 아티스트)
- *Journal for Artistic Research* 등에 doctoral exposition을 준비하는 박사과정 학생
- 그랜트·레지던시 마감이 임박한 아티스트
- 공유 언어화 문서가 필요한 collective

언어화가 이미 유창한 아티스트, 그리고 언어화 자체가 본질적으로 거부되는 전통(즉흥, 의례, 구술)에는 유용하지 않습니다. **무엇을 위한 도구가 아닌가**를 명시하는 것 자체가 설계의 일부입니다.

## 6가지 모드 한눈에

| 모드 | 슬래시 명령 | 사용 시점 |
|---|---|---|
| `socratic` | `/art-project:socratic` | 아직 컨셉이 없고 막연한 끌림만 있을 때 |
| `provoke` | `/art-project:provoke` | 부분적 컨셉이 있지만 막혔을 때 |
| `lineage` | `/art-project:lineage` | 후보 lineage가 있고 확장하고 싶을 때 |
| `brief` | `/art-project:brief` | 충분한 재료가 모였고 명제 문서가 필요할 때 |
| `rehearsal` | `/art-project:rehearsal` | 초안 brief가 있고 제출 전 부담 테스트가 필요할 때 |
| `full` | `/art-project:ideate` | 주(週) 단위로 이어지는 장기 프로젝트 |

자세한 내용은 [모드 개요](modes/overview.md)를 참고하세요.

## 플러그인이 산출하는 것

**언어** — 질문, brief, lineage map, rehearsal transcript — 이를 아티스트가 스튜디오로 가져갑니다. 플러그인은 작품 자체를 만들지 않습니다.

## Frayling 분류 내 위치

플러그인은 research *for* art(작동 중인 도구)이고, research-*into*-art 구성요소(전통 태그 reference layer)를 포함합니다. 설계 선택 자체는 design-research-through-design ([Zimmerman 외 2007](https://dl.acm.org/doi/10.1145/1240624.1240704))로 다룹니다. [Frayling 분류](philosophy/frayling-typology.md) 참조.

## 라이선스

CC-BY-NC 4.0. 저장소의 `LICENSE` 파일을 보세요.
