# e2e_manual_demo

Describe what this plugin does and how to configure it.

## Development

This repository is meant to live at:

```text
N.E.K.O/plugin/plugins/e2e_manual_demo
```

When publishing to the plugin market, use this GitHub repository name:

```text
n.e.k.o_plugin_e2e_manual_demo
```

From the N.E.K.O repository root:

```bash
uv run python -m plugin.neko_plugin_cli.cli check e2e_manual_demo
uv run python -m plugin.neko_plugin_cli.cli check -r e2e_manual_demo
```

## Market release

Push a tag matching `plugin.toml` version to create a GitHub Release asset:

```bash
git tag v0.1.0
git push origin v0.1.0
```

The generated `.github/workflows/release.yml` uploads `e2e_manual_demo.neko-plugin`.
Use that GitHub Release URL when publishing a version in the plugin market.

## Entry

```toml
entry = "plugin.plugins.e2e_manual_demo:E2eManualDemoPlugin"
```
