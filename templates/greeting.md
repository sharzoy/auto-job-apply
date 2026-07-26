# Greeting generation rules

Generate one greeting per JD from resume facts + JD keywords. Never invent experience.

## Inputs

1. `profile.md` + master resume (`resume_path` / `resume_doc_path`)
2. Current JD requirements
3. Optional style overrides in `profile.md` → `Greeting style`

## Algorithm

1. **Extract resume anchors** (facts only):
   - years in the role domain
   - current/latest title + domain
   - 1 strongest quantified achievement relevant to JD
   - 2–3 skills that appear in both resume and JD
2. **Pick angle** (one only):
   - skill match (default)
   - project outcome (if JD is result-oriented)
   - industry match (if same vertical)
3. **Write 1 greeting** + optional **short variant** (A/B).
4. If `profile.portfolio` exists, **always append** invite + URL, e.g.:
   ```text
   以下是我的作品集，欢迎查阅：
   {url}
   ```
   Prefer `profile.portfolio_invite_zh` / `portfolio_invite_en` if set. Never only write bare `作品集：`.
5. Save into the unified packet `.txt` (section 二), not a separate md.

## Hard limits

| Constraint | Value |
|------------|--------|
| Chinese body length | 50–90 characters (hard max 100); **exclude** portfolio URL line |
| English body length | 25–45 words (hard max 50); **exclude** portfolio URL line |
| Sentences | 1–2 only in body |
| Tone | professional, direct, no flattery |
| Metrics | only if on resume |
| Portfolio | required when profile has `portfolio` |

## Structure (Chinese, Boss) — preferred Final

```text
您好，本人约{years}年{domain}经验，擅长{skill1}/{skill2}，做过{one_proof}。看到贵司{role}岗。{extra}。期待沟通。
以下是我的作品集，欢迎查阅：
{portfolio}
```

Legacy short skeleton (only if profile forces it):

```text
您好，申请「{role}」。我{years}年{domain}经验，擅长{skill1}/{skill2}，{one_proof}。方便聊聊吗？
```

`one_proof` examples (must be true):

- 做过{系统/业务}，QPS/用户量/降本等有数字则带数字
- 主导过{项目类型}
- 覆盖过 JD 的核心栈：`React/Node` 等

## Structure (English)

```text
Hi — applying for {role}. {years} yrs in {domain}, strong in {skill1}/{skill2}; {one_proof}. Happy to chat.
```

## Anti-patterns (do not)

- Wall of text / paste full resume
- 「非常期待加入贵司」「百忙之中」等套话堆砌
- Fake metrics or titles not on resume
- Listing 5+ skills
- Asking salary in the first message

## Output format (`greeting.md`)

```markdown
# Greeting — {company} / {role}

## Final (use this)
{text}

## Variant B (backup)
{text}

## Evidence used
- …
- …

## Why this angle
One sentence.
```
