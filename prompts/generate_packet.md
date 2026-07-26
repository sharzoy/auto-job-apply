# Prompt: Generate unified packet.txt (ABC layout)

Facts only from PROFILE + RESUME. Never fabricate metrics.

## Inputs

- PROFILE, RESUME_FACTS, JD, SCORECARD (from score_job)
- templates/packet.txt

## Output path (priority folders)

```text
applications/packets/{A|B|C}/<YYYY-MM-DD>-<company>-<role-slug>.txt
```

Use SCORECARD.grade for the folder. If an old flat path exists, prefer writing into A/B/C and mention move in 投递备注.

## Document structure (mandatory order)

### 0) Summary card (top)

```text
{公司} · {岗位}
{A|B|C}级 {score}分
{stars}
匹配结论：
{decision}
推荐原因 / 优势适配：
- …
投递风险：
- …
```

If grade C, also or instead:

```text
🚫 不建议投递原因：
- 要求：…
- 你的经历：…
- 匹配度：…%
```

Always include:

```text
硬性要求核对：
- [通过/未通过] …
```

### 1–6) Keep existing sections

一、岗位信息（含匹配分、等级、强匹配、缺口）  
二、打招呼语 Final  
三、定位要点  
四、Cover  
五、Form  
六、邮件  

### 7) HR视角模拟

```text
HR第一眼评价：
优势：
✓ …
疑虑：
× …
HR可能淘汰原因：
…
```

### 8) 简历修改建议

- **A级**：写「无需为该 JD 单独改简历，使用现有版本即可。」
- **B/C**：表格或条目：`JD要求 | 你简历现状 | 建议改法`  
  Example: 内容发布 → 品牌账号矩阵运营，粉丝增长300%（数字必须真实）  
  Do **not** rewrite the whole resume file; only suggest wording gaps.

### 9) 投递备注

status + 优先级目录 A/B/C + 确认前禁止提交

## Greeting

Follow profile Final 格式 + portfolio block. No salary in greeting.
