<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&height=300&color=gradient&customColorList=6D28D9,7E22CE,9333EA,3ECF8E&text=VED%20CHAUHAN&fontColor=ffffff&fontSize=70&animation=fadeIn&section=header&desc=Founder%20%40%20SNOWBROS%20%C2%B7%20Systems%20%26%20Dev-Tools%20Engineer&descSize=18&descAlignY=62" width="100%" />

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&duration=2800&pause=600&center=true&vCenter=true&multiline=true&width=820&height=120&color=9333EA&lines=Founder+%40+SNOWBROS+%E2%80%94+software+engineering+studio;Systems+%26+Developer-Tools+Engineer;Rust+%C2%B7+TypeScript+%C2%B7+Python;Building+Atlas+%E2%80%94+a+multi-language+static+analyzer)](https://github.com/VED2107)

<a href="https://snowbros.me"><img src="https://img.shields.io/badge/SNOWBROS-6D28D9?style=for-the-badge&logo=rocket&logoColor=white" alt="SNOWBROS" /></a>
<a href="https://ved.exe.snowbros.me"><img src="https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Portfolio" /></a>
<a href="https://linkedin.com/in/ved-chauhan2107"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" /></a>
<a href="mailto:vedchauhan2107@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" /></a>

![Profile Views](https://komarev.com/ghpvc/?username=VED2107&style=flat-square&color=6D28D9&label=Profile+Views)

</div>

---

## 🧠 About Me

I'm **Ved Chauhan** — founder of **[SNOWBROS](https://snowbros.me)**, an independent software engineering studio. I build across two worlds:

- **Developer tools & systems** — writing a **native Rust** static-analysis engine ([Snowbros Atlas](https://github.com/snowbros-labs/atlas)) with a shared semantic IR, a tree-sitter frontend per language, a built-in LSP, and a VS Code extension.
- **Full-stack products** — shipping production **Next.js + Supabase** applications, from luxury e-commerce to education platforms, to paying customers.

I care about work that is **deterministic, provable, and fast** — and about UI that feels premium.

```rust
struct Engineer {
    name: &'static str,
    studio: &'static str,
    focus: [&'static str; 3],
    principle: &'static str,
}

fn main() {
    let ved = Engineer {
        name: "Ved Chauhan",
        studio: "SNOWBROS",
        focus: ["Developer Tools", "Systems (Rust)", "Full-Stack Products"],
        principle: "Same input in, same result out — accuracy over quantity.",
    };
    println!("{} builds {} kinds of things.", ved.name, ved.focus.len());
}
```

---

## 🚀 Flagship: Snowbros Atlas

<div align="center">

**A deterministic, multi-language static-analysis engine — written in Rust.**

<a href="https://github.com/snowbros-labs/atlas"><img src="https://img.shields.io/github/stars/snowbros-labs/atlas?style=for-the-badge&logo=github&color=6D28D9&labelColor=1a1a2e" alt="Stars" /></a>
<a href="https://crates.io/crates/snowbros-atlas"><img src="https://img.shields.io/crates/v/snowbros-atlas?style=for-the-badge&logo=rust&color=DE5833&labelColor=1a1a2e&label=crates.io" alt="crates.io" /></a>
<a href="https://www.npmjs.com/package/snowbros"><img src="https://img.shields.io/npm/v/snowbros?style=for-the-badge&logo=npm&color=CB3837&labelColor=1a1a2e" alt="npm" /></a>
<a href="https://marketplace.visualstudio.com/items?itemName=snowbros.snowbros-atlas"><img src="https://img.shields.io/visual-studio-marketplace/v/snowbros.snowbros-atlas?style=for-the-badge&logo=visualstudiocode&color=007ACC&labelColor=1a1a2e&label=VS%20Code" alt="VS Code Marketplace" /></a>

</div>

As of **v0.4.0** Atlas is multi-language by architecture: **JavaScript, TypeScript, React, Next.js, and Python** all lower into **one shared semantic IR**, and every rule is either language-agnostic or scoped to a language family in one place — never an `if language ==` branch inside a detector. It builds whole-project symbol, import, and file graphs, then reports problems it can **prove** — circular imports, dead files, server/client boundary leaks, React hook misuse, unused deps, hardcoded secrets, oversized functions — each with an evidence chain. Ships an LSP + VS Code extension, SARIF/JSON/HTML/Markdown reports, and a guarded auto-fix engine. **23 rules**, cross-platform, published to crates.io, npm, Homebrew, and the VS Code Marketplace.

> Also building **[Mentor](https://github.com/snowbros-labs/mentor-skill)** — an engineering-intelligence orchestrator skill for Claude Code (TEACH or BUILD mode across the whole stack).

---

## 🛠️ Tech Stack

**Languages**

![Rust](https://img.shields.io/badge/Rust-DE5833?style=for-the-badge&logo=rust&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Dart](https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-CC2927?style=for-the-badge&logo=postgresql&logoColor=white)

**Frontend**

![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white)
![GSAP](https://img.shields.io/badge/GSAP-88C430?style=for-the-badge&logo=greensock&logoColor=white)
![Framer Motion](https://img.shields.io/badge/Framer_Motion-0055FF?style=for-the-badge&logo=framer&logoColor=white)
![shadcn/ui](https://img.shields.io/badge/shadcn/ui-000000?style=for-the-badge&logo=shadcnui&logoColor=white)

**Systems & Backend**

![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Tree-sitter](https://img.shields.io/badge/Tree--sitter-000000?style=for-the-badge&logo=treehouse&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)
![Prisma](https://img.shields.io/badge/Prisma-2D3748?style=for-the-badge&logo=prisma&logoColor=white)

**Mobile & Cloud**

![Flutter](https://img.shields.io/badge/Flutter-02569B?style=for-the-badge&logo=flutter&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Vercel](https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

---

## 🐍 Watch my contributions get eaten

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/VED2107/VED2107/output/github-contribution-grid-snake-dark.svg?v=2" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/VED2107/VED2107/output/github-contribution-grid-snake.svg?v=2" />
  <img alt="snake eating my contribution graph" src="https://raw.githubusercontent.com/VED2107/VED2107/output/github-contribution-grid-snake.svg?v=2" />
</picture>

</div>

---

## 💼 Featured Projects

<details open>
<summary><b>🦀 Snowbros Atlas — Multi-Language Static Analysis Engine (Rust)</b></summary>

<br>

Deterministic engineering-intelligence platform. One shared semantic IR across JS/TS and Python; the same rule runs on every language it applies to.

| Category | Details |
|----------|---------|
| Stack | Rust, Tree-sitter, LSP, VS Code API |
| Languages analyzed | JavaScript, TypeScript, React, Next.js, Python |
| Distribution | crates.io · npm · Homebrew · VS Code Marketplace |
| Highlights | Shared IR · 23 rules · evidence-first · guarded auto-fix · SARIF/LSP |
| Repo | [github.com/snowbros-labs/atlas](https://github.com/snowbros-labs/atlas) |
| Live | [snowbros.me/atlas](https://snowbros.me/atlas) |

</details>

<details>
<summary><b>🤖 Mentor — Engineering-Intelligence Skill for Claude Code</b></summary>

<br>

A capability orchestrator that composes only the specialist expertise a task needs, in TEACH or BUILD mode across the whole stack.

| Category | Details |
|----------|---------|
| Type | Claude Code skill / orchestrator |
| Repo | [github.com/snowbros-labs/mentor-skill](https://github.com/snowbros-labs/mentor-skill) |
| Focus | Software · backend · frontend · architecture · security · AI · DevOps |

</details>

<details>
<summary><b>🎮 VED.EXE — Retro-Gaming Developer Portfolio</b></summary>

<br>

Production developer portfolio with CRT effects, terminal UI, RPG mechanics, and live GitHub integrations.

| Category | Details |
|----------|---------|
| Stack | Next.js 16, React 19, GSAP, TypeScript |
| Live | [ved.exe.snowbros.me](https://ved.exe.snowbros.me) |
| Features | CRT effects, terminal UI, RPG mechanics, GitHub GraphQL integration |

</details>

<details>
<summary><b>🛍️ Vinnys Vogue — Luxury Fashion E-Commerce</b></summary>

<br>

Role-based fashion commerce platform with checkout, order tracking, and admin management.

| Category | Details |
|----------|---------|
| Stack | Next.js, Supabase, PostgreSQL |
| Features | Catalog, cart, payments, order tracking, admin dashboard |
| Security | Row-Level Security (RLS), auth |
| Live | [vinnysvogue.in](https://www.vinnysvogue.in) |

</details>

<details>
<summary><b>✨ Lunora Studio — Handmade Bouquet E-Commerce</b></summary>

<br>

Cinematic GSAP storytelling landing page + full commerce workflow for handmade bouquets.

| Category | Details |
|----------|---------|
| Stack | Next.js, Supabase, GSAP, shadcn/ui |
| Features | Custom bouquet requests, coupon engine, admin analytics, CMS |
| Live | [lunorastudio.vercel.app](https://lunorastudio.vercel.app) |

</details>

<details>
<summary><b>📚 STC — Education Platform · 🎥 Filmica — Flutter Camera App</b></summary>

<br>

**STC** — learning-management + attendance system for students (Next.js, Supabase, RBAC). <br>
**Filmica** — cross-platform film-companion camera app with AI-powered GLSL shader effects (Flutter, Dart, Firebase).

</details>

---

## 📊 GitHub Analytics

<div align="center">

<img height="180em" src="https://github-readme-stats.vercel.app/api?username=VED2107&show_icons=true&theme=tokyonight&hide_border=true&include_all_commits=true&count_private=true" />
<img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username=VED2107&layout=compact&theme=tokyonight&hide_border=true&langs_count=8" />

![GitHub Streak](https://streak-stats.demolab.com?user=VED2107&theme=tokyonight&hide_border=true)

![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=VED2107&theme=tokyo-night&hide_border=true&area=true)

![Trophies](https://github-profile-trophy.vercel.app/?username=VED2107&theme=tokyonight&no-frame=true&column=7&margin-w=8)

</div>

---

## 🧭 What I'm Building Next

```yaml
now:
  - Atlas M4 — more language frontends (Go, Rust, Java) on the shared IR
  - Cross-language rules driven by real-world feedback
  - Mentor — expanding the capability orchestrator

principles:
  - Deterministic: same code + config -> same findings, always
  - Provable: never guess; unresolved is labeled, not hidden
  - Fast: native Rust, incremental cache, run-on-save speed

open_to:
  - Developer-tools / systems engineering
  - Product engineering & founder collaborations
  - Open-source contributions
```

---

## 🎓 Coding Profiles

<div align="center">

<a href="https://leetcode.com/ved-chauhan2107/"><img src="https://img.shields.io/badge/LeetCode-000000?style=for-the-badge&logo=LeetCode&logoColor=#d16c06" alt="LeetCode" /></a>
<a href="https://www.geeksforgeeks.org/user/ved-chauhan2107/"><img src="https://img.shields.io/badge/GeeksforGeeks-298D46?style=for-the-badge&logo=geeksforgeeks&logoColor=white" alt="GeeksforGeeks" /></a>
<a href="https://www.hackerrank.com/ved-chauhan2107/"><img src="https://img.shields.io/badge/HackerRank-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white" alt="HackerRank" /></a>
<a href="https://www.codechef.com/users/ved-chauhan2107/"><img src="https://img.shields.io/badge/CodeChef-5B4D37?style=for-the-badge&logo=codechef&logoColor=white" alt="CodeChef" /></a>

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&section=footer&height=160&color=gradient&customColorList=6D28D9,7E22CE,9333EA,3ECF8E" width="100%" />

**Building systems that are deterministic, provable, and fast.**

</div>
