# Concept Brief 스키마

[`brief`](../modes/brief.md) 모드가 산출하는 10-필드 스키마. 각 필드는 명시적 인식론 구조를 갖고; 스키마는 세션 실행 전에 고정되어 있습니다.

## 10개 필드

### 1. Working title

작업의 placeholder 이름. `[working title]` 또는 `untitled-N` 사용 가능. brief에 referenceable handle을 제공하기 위함; commitment가 아닙니다.

### 2. Provocation

작업이 추구하는 *not-yet-knowing*, [Borgdorff 2012](https://doi.org/10.4000/critiquedart.1380) 의미에서. 작업이 답하는 질문이 아닌; 작업이 열어둔 채로 유지하는 질문.

**좋은 provocation**: "inscription이 authorship을 disclaim한다는 것은 무엇을 의미하는가?"
**나쁜 provocation** (너무 답할 수 있음): "사진은 어떻게 부패하는가?"

### 3. Proposition

작업이 하는 주장. 종종 가장 어려운 필드. stay-rough default 적용 — 단편 수용.

**예시**: "the work is about marks that don't claim authorship"

### 4. Anti-proposition

작업이 *반대하는* 것, [Sullivan 2010](https://us.sagepub.com/en-us/nam/art-practice-as-research/book230864)의 dialectical 의미에서. 작업이 자신을 position하는 상대 입장.

**예시** (위 proposition과 짝): "the work argues against the curatorial assumption that authorship is the locus of value"

### 5. Disconfirmation condition

스튜디오 용어로 작업을 *falsify*하는 것. 논리적 falsification이 아닌; 예술적인 것. 어떤 viewing experience 또는 critical reading이 작업이 자신의 의도된 aim에 실패했다는 의미인가?

**예시**: "the work fails if the viewer reads it as a memorial"

### 6. Intended encounter

[Viewpoints](https://www.tcg.org/Publications/Books/PublicationDetail/View/the-viewpoints-book) (Bogart & Landau 2005) 의미에서 작업이 어떻게 만나지길 의도하는지. 만남의 spatial, temporal, bodily, social 차원 포함.

**예시**: "a single viewer at a time, in dim light, with permission to handle the work"

### 7. Lineage anchor

작업이 position하는 선례. [`lineage`](../modes/lineage.md) Map에서.

**예시**: "opposition to On Kawara's date paintings (Kawara claims authorship through ritual; this work refuses the claim). Kin: [the artist's lineage candidate]"

### 8. Materials and scale

작업의 재료적 약속, 크기·count·지속시간 포함. 단편적이어도 됩니다.

**예시**: "photographs, the size of a hand. number unknown yet. duration of viewing: unbounded"

### 9. Risk and refusal

두 개의 sub-claim으로 분할:

- **Risk**: 작업이 risk하는 것 (a reading, an outcome, a mis-reception).
- **Refusal**: 작업이 특정하게 되지 *않기를* 바라는 것.

risk sub-claim은 *transferable* (의미 손실 없이 paraphrase 가능). refusal sub-claim은 *generative* (작업을 앞으로 shape함).

**예시**:
- Risk: "the work reads as nostalgia"
- Refusal: "not a memorial; not a family history piece"

### 10. Frayling-type declaration

Research [*into*](../philosophy/frayling-typology.md) / *through* / *for* art. 아티스트가 선언해야 함; 플러그인이 대신 고르지 않음.

**예시**: "Research-FOR art (만듦을 지원하는 작업, 작품이 지식의 locus). [Artist must confirm.]"

## Reconstruction benchmark용 cell 분할

10개 필드는 scoring 시 **11개 cell**을 산출하며, field 9 (Risk/refusal)이 두 sub-claim으로 분할되기 때문입니다. 11개 cell 중:

- **6개는 generative-layer**: Provocation, Proposition, Anti-proposition, Disconfirmation condition, Refusal sub-claim, Frayling-type declaration. gold reading이 documentation만으로는 추론 불가능해야 할 아티스트의 claim을 운반하는 cell.
- **5개는 transferable 또는 mixed**: Working title, Intended encounter, Lineage anchor, Materials and scale, Risk sub-claim. input-pack content가 leakage 없이 gold reading을 지원할 수 있는 cell.

이 분할은 reconstruction 후 선택되지 않고 스키마에 의해 고정됩니다. benchmark는 [paper의 §4 audit design](https://github.com/joonhyungbae/art-project/blob/main/art-project_paper/sections/04-evaluation.tex) 참조.

## Stay-rough default

기본적으로 brief는 이전 모드에서 온 필드의 아티스트 목소리를 verbatim 보존합니다. 빈 필드는 `[gap, not in input]`으로 보고됩니다. 플러그인은 단편을 AI register로 *다듬지 않고*, 빈 필드용 content를 *fabricate하지 않습니다*.

제출용 smoothing을 요청하려면 `/art-brief --polish`. 플래그는 opt-in만.

## 참고

- [Brief 모드](../modes/brief.md) — brief 모드 진입법.
- [Frayling 분류](../philosophy/frayling-typology.md) — 선언 필드의 인식론적 약속.
