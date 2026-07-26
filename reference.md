# Reference — ABC packets, confirm, log

Scoring detail: [docs/scoring.md](docs/scoring.md)

## Prompts

| File | Output |
|------|--------|
| [prompts/score_job.md](prompts/score_job.md) | Scorecard JSON + grade A/B/C + hard_requirements |
| [prompts/generate_packet.md](prompts/generate_packet.md) | `packets/{A\|B\|C}/*.txt` |
| [prompts/confirm_submit.md](prompts/confirm_submit.md) | Confirm UX; batch A→B |

## Packet layout

1. **摘要卡**：标题、A/B/C、分、星、结论、推荐原因 / 风险或🚫、硬性核对  
2. 一、岗位信息  
3. 二、打招呼语  
4. 三～六：定位 / Cover / Form / 邮件  
5. **七、HR视角模拟**（优势✓ 疑虑× 淘汰原因）  
6. **八、简历修改建议**（A 免改；B/C 给「现状→改法」，不整份重写）  
7. **九、投递备注**

Path: `applications/packets/A|B|C/<date>-<company>-<role>.txt`

## Grades (quick)

- **A 90–100**：强匹配，优先投  
- **B 60–89**：有机会，需包装（尤其 60–80）  
- **C &lt;60**：不推荐  

Hard-requirement fails cap score (see scoring.md).

## Confirm commands

| 指令 | 效果 |
|------|------|
| `确认投递` / `发送` / `允许浏览器投递` | 投当前 |
| `一键投递` | 只投列表里 A+B（已排序） |
| `一键投递 1,3` | 指定行 |
| `强制投递` + C 序号 | 投不推荐岗 |
| `跳过` / `编辑后再投` / `先别投` | 不投或改稿 |

## Log columns

`date | company | role | platform | score | grade | status | url | notes`

Example grade column: `A` / `B` / `C`.

## Platforms

Boss：立即沟通 / 继续沟通，首条用 Final。  
51job / 智联 / 官网 / 邮件：见既有说明；提交前必须确认。
