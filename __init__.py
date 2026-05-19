from typing import Any
from plugin.sdk.plugin import (
    NekoPluginBase, neko_plugin, plugin_entry, lifecycle,
    Ok,
)


@neko_plugin
class E2eManualDemoPlugin(NekoPluginBase):
    """e2e_manual_demo"""

    def __init__(self, ctx: Any):
        super().__init__(ctx)
        self.logger = ctx.logger

    @lifecycle(id="startup")
    def on_startup(self, **_):
        self.logger.info("E2eManualDemoPlugin started")
        return Ok({"status": "ready"})

    @lifecycle(id="shutdown")
    def on_shutdown(self, **_):
        self.logger.info("E2eManualDemoPlugin stopped")
        return Ok({"status": "stopped"})

    @plugin_entry(
        id="hello",
        name="Hello",
        description="Say hello",
        input_schema={
            "type": "object",
            "properties": {
                "name": {"type": "string", "default": "World"}
            }
        }
    )
    def hello(self, name: str = "World", **_):
        return Ok({"message": f"Hello, {name}!"})
