# Install

## Prerequisites

- **Claude Code** installed (CLI, desktop app, or web at [claude.ai/code](https://claude.ai/code))
- An Anthropic account with access to Claude (Sonnet 4.6 or higher recommended; Opus tier preferred for `rehearsal` mode)

## 30-second install via plugin marketplace

```text
/plugin marketplace add joonhyungbae/art-project
/plugin install art-project
```

That's it. The six slash commands (`/art-project:socratic`, `/art-project:provoke`, `/art-project:lineage`, `/art-project:brief`, `/art-project:rehearsal`, `/art-project:ideate`) become available in your next Claude Code session.

## Alternative: install from source

If you want to inspect or modify the plugin before installing:

```bash
git clone https://github.com/joonhyungbae/art-project ~/.claude/plugins/art-project
```

Then enable it in Claude Code settings or restart your session.

## Verifying the install

In a new Claude Code session, type:

```text
/art-project:socratic
```

If you see the Socratic mode preamble, the install worked. If you see "command not found," restart Claude Code or check that the plugin is enabled in your settings.

## Configuring language

The plugin defaults to matching the language of your input. If you write in Korean, replies will be in Korean. If you write in English, replies will be in English.

For mixed-language sessions, see [First session](first-session.md) on how to switch mid-conversation.

## Updating

When a new version is released:

```text
/plugin update art-project
```

See the [CHANGELOG](https://github.com/joonhyungbae/art-project/blob/main/CHANGELOG.md) for what's new.

## Uninstalling

```text
/plugin uninstall art-project
```

This removes the plugin but preserves any project files you've created with `/art-project:ideate full` mode.
