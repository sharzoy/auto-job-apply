# Prompt: Score a job (ABC grade + hard-requirement caps)

Do NOT invent resume facts. Do NOT give grade A if any JD hard requirement failed.

## Inputs

- PROFILE, RESUME_FACTS, JD
- WEIGHTS / caps from config (see docs/scoring.md)

## Step 1 — Extract hard requirements

List JD must-haves: education, years, language/certs, “必须/限” skills or domain.

For each: `{ name, jd, you, pass: true|false }`.

## Step 2 — Dimension scores

Fill weighted dimensions (sum weights = 100). Compute `raw_sum` / `score_before_cap`.

## Step 3 — Apply caps (mandatory)

- If `hard_fail_count == 1`: `score = min(score_before_cap, 79)`
- If `hard_fail_count >= 2`: `score = min(score_before_cap, 59)`
- Skills looking like 90% match **cannot** override failed 学历/年限/英语六级 etc.

## Step 4 — Grade

- A: score >= 90
- B: 60 <= score <= 89
- C: score < 60

Stars: 90+ ★★★★★; 80–89 ★★★★☆; 60–79 ★★★☆☆; 40–59 ★★☆☆☆; else ★☆☆☆☆

Decision text:

- A → 建议立即投递
- B → 可以投递，建议先按「简历修改建议」包装表述
- C → 🚫 不建议投递

## Output JSON only

```json
{
  "company": "",
  "role": "",
  "hard_requirements": [],
  "hard_fail_count": 0,
  "dimensions": {
    "role_domain": 0,
    "skills": 0,
    "years": 0,
    "education": 0,
    "location": 0,
    "salary": 0,
    "prefs": 0
  },
  "penalties": [],
  "raw_sum": 0,
  "score_before_cap": 0,
  "score": 0,
  "grade": "A",
  "stars": "★★★★★",
  "decision": "建议立即投递",
  "recommend_reasons": [],
  "risks": [],
  "reject_reasons": []
}
```

For C, fill `reject_reasons` like:
`"要求：硕士英语六级3年 / 你的经历：专科英语弱2年 / 技能表面匹配约90% / 综合42%"`
