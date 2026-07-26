# Job application profile

Copy this file to `profile.md` in the same folder and fill it in.
The agent reads `profile.md` only—never invent missing facts.
**Do not commit `profile.md` to git** (see `.gitignore`).

## Identity

- name:
- name_en: (optional)
- phone:
- email:
- city:
- wechat: (optional)

## Links

- resume_path: (absolute path to master resume, e.g. `C:/Users/you/Documents/resume.pdf`)
- resume_doc_path: (optional editable `.docx` / `.md`)
- portfolio:
- github:
- linkedin:

## Target

- roles: (e.g. 新媒体运营, 内容运营)
- level: (应届 / 1-3年 / 3-5年 / 高级)
- cities: (e.g. 深圳, 远程)
- salary_min:
- salary_max:
- job_types: (全职 / 实习 / 兼职)
- min_match_score: 60
- max_apps_per_day: 10

## Preferences

- must_have: (e.g. 双休)
- avoid: (e.g. 纯外包)
- languages: (中文, English)
- work_auth: (e.g. 中国大陆公民)

## Experience summary

For each role, list only true facts:

### Company — Title (YYYY-MM ~ YYYY-MM)

- stack:
- bullets:
  - …
  - …

## Education

- school — degree — major — years

## Skills

- strong: …
- familiar: …
- tools: …

## Default form answers

- expected_salary:
- available_from:
- notice_period:
- willing_to_relocate: yes/no
- highest_education:
- years_of_experience:

## Greeting style

Controls auto-generated 打招呼语 (resume + JD).

- language: auto
- max_chars_zh: 160
- max_words_en: 45
- tone: professional
- must_include: 作品集邀请语+链接
- must_avoid: 期望薪资
- prefer_metric: yes
- always_ask_user_before_send: yes
- append_portfolio_link: yes
- portfolio_invite_zh: 以下是我的作品集，欢迎查阅：
- portfolio_invite_en: Here is my portfolio — welcome to take a look:

### Final 格式（推荐）

```text
您好，本人约{years}年{domain}经验，擅长{skill1}/{skill2}，做过{one_proof}。看到贵司{role}岗。{extra}。期待沟通。
以下是我的作品集，欢迎查阅：
{portfolio}
```

- zh: （按上方 Final 格式填写）
- en: Hi — {years} yrs in {domain}, strong in {skill1}/{skill2}; {one_proof}. Saw your {role} opening. {extra}. Happy to chat.\nHere is my portfolio — welcome to take a look:\n{portfolio}
