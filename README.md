# auto-job-apply

> **GitHub About：** AI 求职助手 Skill：简历解析 → JD 硬性条件核对 → A/B/C 匹配评分 → 生成投递包（开场白、HR模拟、简历优化建议）。保留人工确认环节，不进行无人值守批量投递。

一个基于 AI Agent 的求职辅助 Skill，帮助用户从职位分析到投递准备完成完整流程：

- 📄 简历读取与能力提取
- 🔍 JD 硬性条件匹配检查
- 📊 A/B/C 求职匹配评分体系
- 💬 自动生成 Boss/前程无忧沟通话术
- 🎤 HR 视角模拟面试与简历优化建议
- ✅ 用户确认后执行投递

> **不是无人值守群发器。** 人工确认→ 预览打招呼原文 → 等你说「确认投递 / 一键投递」→ 才点 招聘软件的「立即沟通」等按钮。

### GitHub 仓库介绍词（可直接粘贴）

**Repository name**

```text
auto-job-apply
```

**Description（About 栏）**

```text
AI 求职助手 Skill：简历解析 → JD 硬性条件核对 → A/B/C 匹配评分 → 生成投递包（开场白、HR模拟、简历优化建议）。保留人工确认环节，不进行无人值守批量投递。
```

**Topics（标签）**

```text
cursor-skill, job-search, resume, boss-zhipin, 51job, ai-agent, chinese
```

| 给谁读 | 文件 |
|--------|------|
| 人类（安装、理念、演示） | 本 README |
| Agent / Cursor | [`SKILL.md`](SKILL.md) |
| 打分公式 | [`docs/scoring.md`](docs/scoring.md) |
| 平台与确认指令 | [`reference.md`](reference.md) |

---

## 能做什么

1. **吃 JD**（链接 / 粘贴 / 截图）
2. **硬性要求核对 + 加权打分** → **A / B / C**（防误判：硬性不过不能强行 A）
3. **生成一份** `applications/packets/{A|B|C}/<日期>-公司-岗位.txt`（摘要卡、打招呼、HR 视角、简历建议…）
4. **预览 → 等确认 → 提交**；一键投递默认 **A→B 排序**，C 需强制
5. **写 log**（含 grade）；可用脚本粗统计投递量 / 回复率标记

支持平台约定：Boss 直聘、前程无忧、智联、公司站、邮件（见 `reference.md`）。

---

## 快速安装（Cursor）

1. 克隆本仓库，或把本目录拷到：

```text
~/.cursor/skills/auto-job-apply/
```

2. 复制画像与配置（**不要**提交真实文件到 Git）：

```bash
cp profile.template.md profile.md
cp config.example.yaml config.yaml
cp applications/log.example.md applications/log.md
```

3. 编辑 `profile.md`：姓名、联系方式、`resume_path`、目标岗位、`min_match_score`。  
4. 在 Cursor Agent 对话里说：

```text
用 auto-job-apply 处理这个岗位，先生成材料，别投：
<JD 或链接>
```

确认后再说：`确认投递` 或 `一键投递`。

---

## 打分（核心）：A / B / C

详见 **[docs/scoring.md](docs/scoring.md)**。

| 等级 | 分数 | 含义 |
|------|------|------|
| **A** | 90–100 | 强匹配，建议优先投递 |
| **B** | 60–89 | 有机会；需包装简历表述（尤其 60–80） |
| **C** | &lt;60 | 不推荐；写清🚫原因 |

- 加权维度：方向25 + 技能25 + 年限15 + 学历10 + 地点10 + 薪资10 + 偏好5  
- **防误判**：JD 硬性要求（学历/年限/六级等）未过 → 分封顶（1项最高79不能A；≥2项最高59强制C）。技能再像也不能强行A。  
- 样例 A：[`examples/sample-scorecard.json`](examples/sample-scorecard.json)  
- 样例 C（硬性未过）：[`examples/sample-scorecard-hardfail-C.json`](examples/sample-scorecard-hardfail-C.json)

Packet 按优先级进目录：`applications/packets/A|B|C/`。

---

## Packet 里有什么

| 块 | 内容 |
|----|------|
| **摘要卡** | 等级/分/星/结论/**推荐原因**或**🚫不建议原因**/硬性核对 |
| 一～六 | 岗位信息、打招呼、定位、Cover、Form、邮件 |
| **七 HR视角模拟** | 优势✓ / 疑虑× / 可能淘汰原因 |
| **八 简历修改建议** | A免改；B/C 给「现状→改法」（不整份重写） |
| 九 投递备注 | 状态与确认门闩 |

完整版式见 [`templates/packet.txt`](templates/packet.txt)、[`examples/sample-packet.txt`](examples/sample-packet.txt)。

---

## 人工确认（请保留）

```text
写稿 → 展示 Final → 你下指令 → 才提交
一键投递默认只投 A→B（已排序）；C 需强制
```

| 你说 | 效果 |
|------|------|
| `确认投递` / `发送` | 投当前 |
| `一键投递` / `一键投递 1,3` | 批投 A+B |
| `强制投递` | 明确投 C |
| `跳过` / `编辑后再投` / `先别投` | 不投或改稿 |

完整说明：[reference.md](reference.md)。

---

## 日志与统计

- 表头见 `applications/log.example.md`  
- 本地统计：

```bash
python scripts/stats_log.py
python scripts/stats_log.py --log applications/log.md
```

在 `notes` 里写上「已回复」「面试」等，脚本会粗算回复率。

---

## 仓库里不要出现什么

`.gitignore` 已排除：

- `profile.md`、`config.yaml`
- `applications/packets/`、`applications/log.md`、cookies / `.env`

只提交 `*.template` / `*.example` / `examples/` 脱敏样例。

---

## 目录结构

```text
auto-job-apply/
├── SKILL.md
├── README.md
├── LICENSE
├── config.example.yaml
├── profile.template.md
├── reference.md
├── docs/scoring.md
├── prompts/          # score / packet / confirm
├── templates/        # packet.txt, greeting.md
├── examples/         # 脱敏 JD + 打分卡 + packet
├── scripts/stats_log.py
└── applications/     # 本地 log / packets/A|B|C（gitignore）
```

---

## License

MIT — see [LICENSE](LICENSE).

求职材料与账号安全自负；本工具不保证面试或录用结果。
