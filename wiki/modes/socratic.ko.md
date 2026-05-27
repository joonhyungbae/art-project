# Socratic 모드

> 슬래시 명령: `/art-socratic` — 아직 컨셉은 없고 끌림만 있을 때.

## 무엇을 하는가

Socratic 대화를 통한 pre-reflective 표면화. **Concept Pull Map**을 산출합니다: 명명된 충동, 단편, 제약, 거부, 그리고 *잔여(residue)* — 다른 어떤 카테고리에도 맞지 않은 끌림의 부분.

## 사용 시점

- 무언가에 끌리지만 무엇인지 말할 수 없을 때.
- 만남(이미지, 구절, 최근 독서)을 묘사할 수 있지만 왜 자신에게 중요한지 말할 수 없을 때.
- 그랜트 마감이 다가오는데 "이 작업이 무엇에 대한 것인지"에 대한 정직한 답이 "아직 모르겠다"일 때.
- 트리거 표현: "guide me", "I don't know what I'm doing yet", "help me find what the work wants to be" / 도와줘, 잘 모르겠어.

## 대화는 어떻게 진행되는가

플러그인은 stance 질문(보통 "최근에 즉시 설명할 수 없었던 무엇을 알아챘나요?" 같은)으로 시작하고, 당신의 답을 점점 더 세밀한 질문으로 이어갑니다. 질문은 의도적으로 *미완성*입니다 — 답의 공간을 좁히지 않고 열어둡니다. 5–10 라운드 후, 플러그인은 Concept Pull Map을 산출합니다.

## Concept Pull Map

5개의 명명된 섹션:

- **Impulses** — 이유를 모를 때도 계속 끌리는 것
- **Fragments** — 부분적 재료, 구체적이지만 아직 연결되지 않은 구절·이미지
- **Constraints** — 작업이 할 수 *없는* 것, 봉사할 수 *없는* 사람, 거부하는 register
- **Refusals** — 이 작업이 *특정하게 되지 않기를* 바라는 것
- **Residue** — 위 어디에도 맞지 않는 끌림의 부분; 폐기되지 않고 잔여로 명시됨

이 map은 미완성 사유의 스냅숏이지 로드맵이 아닙니다.

## IRON rules

- **Stay-rough default** — 당신의 목소리는 답에서 그대로 보존됩니다; 플러그인이 단편을 AI-statement 산문으로 다듬지 않습니다.
- **탐색 의도에서 자동 수렴 없음** — `socratic` 끝에서 플러그인이 "당신의 컨셉은 X입니다"라고 말하지 않습니다. map을 제시하고 어느 단편을 따라갈지 묻습니다.
- **턴-테이킹** — 당신이 응답하기 전에 플러그인은 다음 질문으로 진행하지 않습니다.

## 하지 말 것

- artist-statement 스타일의 단락 답변을 쓰지 마세요; 단편으로 쓰세요. 거칢이 데이터입니다.
- map 산출 전에 "내가 어디 있는지 요약해줘"를 요청하지 마세요; 요약은 작업이 준비되기 전에 pull을 단일 방향으로 무너뜨립니다.
- Socratic 모드 내에서 lineage나 provocation을 요청하지 마세요; 모드는 명시적으로 전환하세요.

## 세션 오프너 예시

```text
You: /art-socratic
Plugin: [Socratic 모드 활성. 완성된 사유를 추출하기보다 미완성 사유를
        표면화하도록 설계된 질문을 던지겠습니다. 거칠게 — 단락이 아닌
        단편으로 쓰세요. Concept Pull Map으로 마무리합니다.]

Plugin: 최근에 즉시 설명할 수 없었던 무엇을 알아챘나요 —
        이미지, 구절, 만남?

You: 할머니가 남긴 오래된 사진이 있는데, 뒷면에
     할머니 글씨가 아닌 손글씨가 있었어

Plugin: [더 세밀한 질문으로 계속]
```

## 다음 행보

Concept Pull Map 이후:

- 여전히 막연하면 `socratic`에 머물러 한 라운드 더.
- 막힌 단편에 대한 전통-태그 provocation을 위해 [`provoke`](provoke.md)로 전환.
- 초기 선례를 명명할 수 있으면 [`lineage`](lineage.md)로 전환.

## 참고

- [첫 세션](../getting-started/first-session.ko.md)
- [인지적 스캐폴드](../philosophy/cognitive-scaffold.md) — 플러그인이 당신을 대신해 해석하기를 거부하는 이유
