# 설치

## 사전 요구사항

- **Claude Code** 설치 (CLI, 데스크톱 앱, 또는 웹 [claude.ai/code](https://claude.ai/code))
- Anthropic 계정 (Sonnet 4.6 이상 권장; `rehearsal` 모드에는 Opus 티어 선호)

## 30초 설치 (플러그인 마켓플레이스)

```text
/plugin marketplace add joonhyungbae/art-project
/plugin install art-project
```

끝입니다. 다음 Claude Code 세션부터 6개 슬래시 명령(`/art-project:socratic`, `/art-project:provoke`, `/art-project:lineage`, `/art-project:brief`, `/art-project:rehearsal`, `/art-project:ideate`)이 활성화됩니다.

## 대안: 소스에서 설치

플러그인을 설치 전에 검토하거나 수정하고 싶다면:

```bash
git clone https://github.com/joonhyungbae/art-project ~/.claude/plugins/art-project
```

이후 Claude Code 설정에서 활성화하거나 세션을 재시작하세요.

## 설치 확인

새 Claude Code 세션에서:

```text
/art-project:socratic
```

Socratic 모드 인트로가 나오면 설치 성공입니다. "command not found"가 나오면 Claude Code를 재시작하거나 플러그인이 설정에서 활성화되었는지 확인하세요.

## 언어 설정

플러그인은 입력 언어에 맞춰 응답합니다. 한국어로 쓰면 한국어로, 영어로 쓰면 영어로 답합니다.

세션 도중 언어를 바꾸고 싶다면 [첫 세션](first-session.md)을 참고하세요.

## 업데이트

새 버전이 릴리스되면:

```text
/plugin update art-project
```

변경사항은 [CHANGELOG](https://github.com/joonhyungbae/art-project/blob/main/CHANGELOG.md)에서 확인하세요.

## 제거

```text
/plugin uninstall art-project
```

플러그인은 제거되지만 `/art-project:ideate full` 모드로 만든 프로젝트 파일은 보존됩니다.
