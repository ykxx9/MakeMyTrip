# Contributing Guide

## 🎯 Goal

The goal of this project is not just to build the project, but also to learn how a real software development team works.

We want everyone to get comfortable with:

- Git and GitHub
- Branches
- Pull Requests
- Code Reviews
- Working with other developers

## Why do we work this way?

In a real development environment, developers usually don't directly change the stable code.

Instead, developers work on separate branches, submit their changes through Pull Requests, and have other developers review the code before it becomes part of the shared codebase.

This workflow helps us:

- Avoid breaking stable code
- Catch mistakes through code review
- Learn how to work in a team
- Get comfortable with the workflow used in professional projects

The goal is to **learn the process**, not to create unnecessary rules.

---

# 🌿 Branches

We use three types of branches:

- `main` → Stable code
- `dev` → Development branch
- `feature/<name>` → Individual tasks/features

Example:

```text
main
└── dev
    ├── feature/login
    ├── feature/navbar
    └── feature/profile
```

---

# 🔄 How to Work

For a new task:

### 1. Start from `dev`

```bash
git checkout dev
git pull
```

### 2. Create a feature branch

```bash
git checkout -b feature/my-task
```

### 3. Work and commit

Keep commits simple and meaningful.

Examples:

```text
feat: add login
fix: fix login validation
docs: update README
```

### 4. Push your branch

```bash
git push -u origin feature/my-task
```

### 5. Create a Pull Request

Create:

```text
feature/my-task → dev
```

---

# 👀 Code Review

Everyone can review everyone else's Pull Requests.

When reviewing, check:

- Does the code work?
- Is the change related to the task?
- Is anything obviously broken?
- Is the code understandable?

Ask questions if something is unclear. Code review is for learning as well as finding bugs.

---

# 🔀 Merging

Everyone can merge PRs after they have been reviewed.

For `main`, a Pull Request and review are required.

When `dev` is stable:

```text
dev → PR → main
```

`main` should always contain stable code.

---

# 📌 Important Rules

1. **Do not commit directly to `main`.**
2. Use `feature/<name>` branches for tasks.
3. **One PR = one task/feature.**
4. Feature PRs should go into `dev`.
5. Review each other's PRs.
6. Keep commit messages simple and meaningful.
7. Keep PRs focused and easy to review.

---

## The Workflow

```text
Pick a task
    ↓
Create feature branch
    ↓
Write code
    ↓
Commit
    ↓
Push
    ↓
Create PR → dev
    ↓
Code review
    ↓
Merge
    ↓
dev becomes stable
    ↓
PR → main
```

**The goal is simple: build the project while learning how to work like a real development team.**
