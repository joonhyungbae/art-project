# 기여

art-project 플러그인은 CC-BY-NC 4.0으로 오픈되어 있습니다. 기여는 네 가지 카테고리로 환영합니다.

## 1. 전통 태그 추가

[`shared/references/art_ideation_methodology.md`](https://github.com/joonhyungbae/art-project/blob/main/shared/references/art_ideation_methodology.md)의 코퍼스는 open입니다. 새 전통 태그를 제안하려면 6-필드 스키마가 populated된 PR을 제출하세요:

1. **Author + year** (DOI 또는 stable URL과 함께)
2. **Core gesture** (한 문장)
3. **Ideation mechanism**
4. **Authentic Practice Boundary** (필수 — 방법론이 요구하지만 AI가 시뮬레이션하지 않는 것)
5. **Contested in** (counter-position 또는 비판)
6. **Skill-hook** (어느 모드가 항목을 소비하는지)

Authentic Practice Boundary 필드가 누락된 PR은 받아들여지지 않습니다. 근거는 [전통 태그](reference/tradition-tags.md)와 [진정성 실천 경계](reference/authentic-practice-boundaries.md) 참조.

**특히 환영**: 비-anglophone 전통 태그. 현재 코퍼스는 한국·동아시아 항목(Paik, Hui, Lee & Lee 2024)을 갖지만 다른 곳은 anglophone-heavy입니다. 구술 전통, Indigenous 실천, Global South 방법론, 텍스트적 fixation에 저항하지만 적절한 경계로 인용할 수 있는 전통에서의 태그 모두 환영합니다.

## 2. 측정 가능한 위해 클래스 보고

[6개 명명된 harm 클래스](philosophy/measured-harms.md)는 exhaustive하지 않습니다. 플러그인 문서가 명명하지 않는 harm 클래스를 식별하면 다음과 함께 issue를 file하세요:

- **Class name** (제안)
- **Description** (어떤 종류의 harm, 어떤 맥락에서)
- **Mitigation candidate** (있다면 — "none yet" 수용)
- **Where it surfaces** (어느 모드, 어느 출력 유형)

Harm-class issue는 기능 요청 전에 triage됩니다.

## 3. 문서 기여 (이 위키)

위키는 저장소 root의 `wiki/`에 있습니다. 기여하려면:

- 관련 `.md` 파일 (영어)과 `.ko.md` 파일 (한국어)을 **함께** 편집하세요. 플러그인의 번역 규율은 두 언어가 lockstep으로 업데이트되도록 요구합니다; 한국어 버전은 secondary 번역이 아닌 parallel canonical 버전입니다.
- 새 페이지의 경우 `mkdocs.yml`의 `nav:` 섹션 + `en`과 `ko` 로케일 둘 다의 `nav_translations:` 키도 업데이트하세요.
- `mkdocs serve`로 로컬 빌드(`pip install mkdocs-material mkdocs-static-i18n` 필요)하고 두 언어 경로가 올바르게 렌더되는지 검증하세요.

### 번역 규율

한 언어 파일을 편집할 때 다른 언어 파일도 같은 PR에서 업데이트되어야 합니다. 언어 버전 간 drift는 문서 버그로 다뤄집니다. 한국어와 영어 버전이 같은 것을 말할 수 없다면 (개념이 번역하기 어려워서), 차이는 파일에서 명시적으로 명명되어야 합니다 — paper over되지 않고.

## 4. 코드 기여 (플러그인 자체)

플러그인 코드 변경(`art-ideation/`, `commands/`, `agents/`)은 표준 PR 흐름을 따릅니다:

1. 먼저 변경을 describing하는 issue를 open. 아키텍처 변경(IRON rule 수정, 새 모드, 스키마 확장)의 경우, issue는 변경이 respect하는 [POSITIONING.md](https://github.com/joonhyungbae/art-project/blob/main/POSITIONING.md) 제약을 참조해야 합니다.
2. `main`에서 branch; commit message는 conventional-commits 스타일 따름.
3. 테스트 스위트 실행 (저장소 root에서 `pytest`).
4. description, rationale, 관련 docs 링크와 함께 PR 제출.

**먼저 논의 없이는 받아들여지지 않음**:

- 어떤 IRON rule 제거 또는 약화.
- Authentic Practice Boundary 규율 제거.
- `lineage` 모드의 필수 bias header 제거.
- `rehearsal` 모드의 disclaimer header 또는 아키텍처 마찰 제거.
- 단일 세션 내 모드-pipelining 추가.

이것들은 프레임워크가 rest하는 아키텍처 commitment입니다. 변경은 synthesis-spec-level 논의를 먼저 요구합니다; [`docs/design/`](https://github.com/joonhyungbae/art-project/blob/main/docs/design/) 참조.

## 행동 강령

이 플러그인이 *위한* 아티스트를 존중하세요. 프레임워크 비판은 환영합니다; practice-based research, 비-anglophone 예술-연구 전통, 또는 AI를 인지적 파트너로 사용하는 아티스트에 대한 dismissal은 환영하지 않습니다.

## 라이선스

CC-BY-NC 4.0 (Creative Commons Attribution-NonCommercial 4.0 International). 기여는 같은 라이선스로 수용됩니다. 프레임워크 또는 파생물의 상업적 사용은 별도 licensing을 요구합니다 — 메인테이너 contact.

## 메인테이너

Joonhyung Bae — [GitHub](https://github.com/joonhyungbae)

## 참고

- [POSITIONING.md](https://github.com/joonhyungbae/art-project/blob/main/POSITIONING.md) — 프레임워크의 public positioning 및 제약.
- [MODE_REGISTRY.md](https://github.com/joonhyungbae/art-project/blob/main/MODE_REGISTRY.md) — 모드의 single source of truth.
- [CHANGELOG.md](https://github.com/joonhyungbae/art-project/blob/main/CHANGELOG.md) — 버전 history.
