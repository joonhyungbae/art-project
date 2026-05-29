# Full 프로젝트 파일 모드

> 슬래시 명령: `/art-project:ideate` — 여러 세션에 걸쳐 주(週)·월(月) 단위로 이어지는 프로젝트.

## 무엇을 하는가

여러 Claude Code 세션(며칠 또는 몇 주 간격)에 걸쳐 상태를 누적하는 **장기 프로젝트 파일**을 유지합니다. 각 세션은 최대 1개 모드(socratic, provoke, lineage, brief, rehearsal)를 실행하고; 파일은 어느 모드가 실행되었는지, 어떤 재료를 산출했는지, 아티스트의 주석을 기록합니다.

이 모드는 Smith & Dean의 iterative cyclic web framing에 대한 운영적 응답입니다 — ideation은 단일 up-front 단계가 아니라 프로젝트 lifecycle에 걸쳐 recur합니다.

## 사용 시점

- 프로젝트가 1회 이상의 Claude Code 세션이 걸릴 것으로 예상될 때.
- 이전 세션의 재료(Concept Pull Map, Lineage Map, brief 초안)가 지속되고 참조 가능하길 원할 때.
- 다주 그랜트·레지던시 타임라인 아래에서 작업할 때.
- 트리거 표현: "start a new project", "open my project file", "continue where I left off".

## 프로젝트 파일은 어떻게 작동하는가 (v0.1: 아티스트 관리)

**v0.1 정직 노트.** 플러그인은 당신 파일시스템에 프로젝트 파일 디렉터리를 *자동 생성·읽기 하지 않습니다*. 지속성은 **아티스트가 관리**합니다: 파일명을 선택하고(권장 기본: 현재 Claude Code 작업 디렉터리의 `art-project-{slug}.md`), 그 파일을 버전 관리·백업하는 책임도 당신에게 있습니다. 플러그인은 세션 로그를 당신이 append할 텍스트로 emit하고; 나중 세션에서 파일을 paste/upload하면 플러그인이 이전 상태를 읽습니다. 실제 cross-session 파일시스템 지속성은 v0.2 작업입니다.

매 세션, 어느 모드를 실행할지 선택합니다. 프로젝트 파일을 context로 paste/참조하면; 플러그인이 읽고 모드를 실행하고 세션 출력을 당신이 append할 형태로 emit합니다. 다음 세션에서는 이전 세션을 이름으로 참조할 수 있습니다 (예: "session 4 socratic에서 X라고 했는데, 여전히 holds하는가?").

## 세션당 1개 모드 규칙

full 프로젝트 파일의 각 세션은 **최대 1개 모드**를 실행합니다. 이유: 세션 내 cross-mode pipelining은 `provoke → brief → rehearsal` rapid-fire 도구들이 최적화하는 패턴이고, 그 패턴은 cyclic web을 적극적으로 undermine합니다. full 모드는 아티스트가 1개 모드 후 세션을 닫고, 스튜디오 시간에, 산출된 재료와 함께 나중에 돌아오도록 강제합니다.

세션 도중 모드를 전환하고 싶다면 세션을 닫고 다음 모드를 위해 새 세션을 시작하세요.

## IRON rules (full 특수)

- **세션당 1개 모드** — 아키텍처적으로 강제됨; 세션 내 모드 전환을 시도하면 플러그인이 경고하고 명시적 override를 요구함.
- **단일-세션 pipelining 금지** — 한 자리에서 `socratic → brief`는 cyclic web에 구조적으로 적대적; 플러그인이 pipeline을 거부함.
- **프로젝트 파일 지속** — 모든 세션 출력이 append됨; 어떤 것도 overwrite되지 않음. 파일은 플러그인이 아닌 아티스트의 것임.

## 프로젝트 파일 모습

```text
# art-project: inscription-counter-inscription
created: 2026-04-12
sessions: 7

─────────────────────────────────────────────────────
SESSION 1 — socratic — 2026-04-12 16:30
─────────────────────────────────────────────────────
[Concept Pull Map produced. Stored below.]

[map content...]

ARTIST NOTES (added 2026-04-14):
- the residue feels like the most live thing
- the constraint about "not a memorial" is now stronger

─────────────────────────────────────────────────────
SESSION 2 — provoke — 2026-04-18 10:15
─────────────────────────────────────────────────────
[12 provocation cards. Stored below.]

[cards content...]

ARTIST NOTES (added 2026-04-21):
- card 3 (LeWitt) and card 9 (Cage) keep returning
- sat with them for 4 days; decided card 9 is the one

─────────────────────────────────────────────────────
SESSION 3 — lineage — 2026-04-25 09:00
[etc.]
```

## 하지 말 것

- **단일-세션 작업에 `full`을 실행하지 마세요.** 이미 가진 재료에서 brief 하나만 작성하면 되는 경우 `/art-project:brief`를 직접 사용하세요.
- **세션 내에서 모드를 pipeline하지 마세요.** 플러그인이 세션당 1개 모드 규칙을 강제합니다.
- **플러그인이 프로젝트를 "관리"해줄 것이라 기대하지 마세요.** 프로젝트 파일은 당신의 것입니다; 플러그인은 append할 뿐 direct하지 않습니다.

## Cross-session resume

프로젝트 파일에 재진입하면 플러그인이 짧은 요약(마지막 세션의 모드, 산출물, 다음에 실행할 만한 모드)을 보여주고 무엇을 할지 묻습니다. 옵션:

- 새 모드 세션 실행.
- 이전 세션 출력 주석 달기.
- 파일 전체 읽기.
- 수정 없이 닫기.

## 다음 행보

- full 모드 자체가 다음 모드입니다. `full` 내에서 매 세션 어느 sub-mode를 실행할지 선택합니다.
- 어느 sub-mode가 어느 순간에 맞는지는 [모드 개요](overview.md) 참조.

## 참고

- [첫 세션](../getting-started/first-session.ko.md) — 단일 모드 대신 `full`로 시작하고 싶다면.
- [인지적 스캐폴드](../philosophy/cognitive-scaffold.md) — ideation-across-time이 중요한 이유.
