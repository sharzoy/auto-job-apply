# Prompt: Confirm before submit

Stop until explicit approval. Default batch = **A then B only** (C excluded).

## Single

```markdown
## Ready to submit?
- {公司} · {岗位}
- 等级/分数: {A|B|C} {score} {stars}
- 结论: {decision}
- Packet: `applications/packets/{A|B|C}/...`
- 硬性未过: {list or 无}
- 风险: …
- Greeting:
  > …

指令：`确认投递` / `跳过` / `编辑后再投` / `先别投`
```

## Batch (priority sorted)

Sort rows: all A by score desc, then B by score desc. List C separately under「不推荐（默认不投）」.

```markdown
## 待投递列表（已按 A→B 优先级排序）
| # | 等级 | 分 | 公司 | 岗位 | packet |
| 1 | A | 95 | … | … | packets/A/... |
| 2 | B | 74 | … | … | packets/B/... |

## 不推荐 C（默认跳过）
| # | 分 | 公司 | 岗位 | 🚫原因摘要 |

- `一键投递` — 只投表中 A+B
- `一键投递 1,2` — 指定序号
- `强制投递 C1` — 明确投 C
- `跳过 2` / `全部先别投`
```
