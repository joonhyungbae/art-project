# Security Policy

## Supported versions

Only the latest release on the `main` branch receives security fixes.

| Version | Supported |
|---------|-----------|
| Latest (`main`) | Yes |
| Older releases | No |

## Reporting a vulnerability

If you find a security issue (e.g. prompt injection, credential exposure,
unintended data exfiltration through the SessionStart hook, supply-chain risk
in the marketplace manifest), **do not open a public issue**.

Instead, use GitHub's **private vulnerability reporting**:

1. Go to the [Security Advisories](https://github.com/joonhyungbae/art-project/security/advisories) page.
2. Click **"Report a vulnerability"**.
3. Fill in the details — what you found, how to reproduce it, and the potential impact.

You will receive a response within 7 days. If the report is accepted, a fix
will be issued and credited in the release notes. If declined, you will
receive an explanation.

## Scope

The following are in scope for security reports:

- **Prompt injection** — inputs that cause the plugin to bypass an IRON RULE
  (no auto-convergence under exploratory intent; preserved unhelpfulness in
  `provoke`; lineage-requires-artist-supplied-candidates; formative-not-decisional
  rehearsal; Concession Threshold Protocol) or an Authentic Practice Boundary.
- **Hook-script execution issues** — anything in `scripts/announce-art-project-loaded.sh`
  or `hooks/hooks.json` that could be exploited by a malicious marketplace
  manifest or a poisoned plugin install path.
- **Credential leakage** — paths through which an `ANTHROPIC_API_KEY` or
  similar secret could be exfiltrated by the plugin's normal operation.
- **Local-state pollution** — anything that writes outside the documented
  paths (`~/.art-project/rehearsal-log.jsonl`, `~/.art-project/projects/<codename>/`)
  without the artist's knowledge.
- **Marketplace-manifest tampering** — anything that lets a third party
  inject content into `.claude-plugin/marketplace.json` discovery.

The following are **out of scope**:

- AI output quality issues (hallucinations, weak provocations, lineage
  entries that miss obvious precedents) — these are research limitations,
  not security vulnerabilities. File them as regular [Issues](https://github.com/joonhyungbae/art-project/issues).
- Disagreements with the cognitive-scaffold position or with specific
  tradition tags — open a Discussion.
- Feature requests or general bugs — use [Issues](https://github.com/joonhyungbae/art-project/issues).
