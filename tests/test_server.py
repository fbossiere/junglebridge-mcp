import sys
from pathlib import Path

from fastmcp import Client
from fastmcp.client.transports import StdioTransport

from junglebridge_mcp.server import create_server


async def test_only_read_only_status_tool_is_exposed() -> None:
    async with Client(create_server()) as client:
        tools = await client.list_tools()
        assert [tool.name for tool in tools] == ["get_connection_status"]
        tool = tools[0]
        assert tool.input_schema.get("properties", {}) == {}
        assert tool.annotations is not None
        assert tool.annotations.read_only_hint is True
        assert tool.annotations.destructive_hint is False
        assert tool.annotations.open_world_hint is False
        result = await client.call_tool("get_connection_status", {})
        assert result.structured_content is not None
        assert result.structured_content["status"] == "not_implemented"
        assert result.structured_content["api_verified"] is False


async def test_installed_console_entry_point_over_stdio() -> None:
    executable = Path(sys.executable).parent / "junglebridge-mcp"
    transport = StdioTransport(command=str(executable), args=[], keep_alive=False)
    async with Client(transport, timeout=15) as client:
        result = await client.call_tool("get_connection_status", {})
        assert result.structured_content is not None
        assert result.structured_content["api_verified"] is False
