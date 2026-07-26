---
name: auto-job-apply
description: >-
  Job apply skill: ABC match grades (A90–100 / B60–89 / C<60), hard-requirement
  anti-misjudgment caps, unified .txt packets in packets/A|B|C, HR simulation,
  resume wording tips, greetings, submit only after confirm. Use for 投简历,
  自动投递, 打招呼, 一键投递, Boss, 前程无忧, JD匹配.
---

# Auto Job Apply

**Never** submit until the user explicitly confirms.

Docs: [README.md](README.md) · [docs/scoring.md](docs/scoring.md) · [reference.md](reference.md)

## Prerequisites

1. [profile.md](profile.md) from [profile.template.md](profile.template.md)
2. Optional [config.yaml](config.example.yaml)
3. Always read resume before writing
4. [applications/log.md](applications/log.md)

## Output rule

One `.txt` per job under **grade folder**:

```text
applications/packets/A|B|C/<date>-<company>-<role-slug>.txt
```

Template: [templates/packet.txt](templates/packet.txt)  
Must include top **摘要卡**（等级/星级/推荐原因或🚫原因/硬性核对）+ 一～六 + **七 HR视角** + **八 简历修改建议** + 九 投递备注.

## Workflow

```
- [ ] 1. Ingest JD
- [ ] 2. Hard-requirement check → scorecard → A/B/C (docs/scoring.md)
- [ ] 3. Write packet into packets/{A|B|C}/
- [ ] 4. Dry-run
- [ ] 5. Confirm (A→B priority; C default skip)
- [ ] 6. Submit
- [ ] 7. Log (include grade)
```

### Score → Grade

| Grade | Score | Action |
|-------|-------|--------|
| A | 90–100 | 优先投；简历建议「无需改」 |
| B | 60–89 | 可投；先包装表述（八） |
| C | &lt;60 | 不推荐；写🚫原因；默认不进一键投递 |

**防误判：** 任 1 项 JD 硬性未过 → 分封顶 79（不能 A）；≥2 项 → 封顶 59（C）。技能再像也不能强行 A。

### Batch priority

Show/submit order: **A high→low, then B high→low**. C listed separately.

Approve phrases: `确认投递` / `一键投递` / `强制投递` …  
Not approve: `先别投` / `跳过`

## Safety

- No invented experience
- No submit without confirm
- No secrets in committed files
