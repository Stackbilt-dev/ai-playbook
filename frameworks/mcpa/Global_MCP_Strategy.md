# Global MCP Infrastructure: Prompt Codex & Essential Services

Create a persistent MCP ecosystem accessible across all Claude projects, with two primary components:

## 1. Prompt Library Repository as MCP Filesystem Server
Transform the AI playbook into a globally accessible MCP filesystem server that:
- Serves as a "prompt codex" for Claude Code to reference when seeking persona guidance
- Structures content for automated extraction (consider YAML frontmatter, clear directory hierarchy)
- Remains persistent and accessible across all projects

## 2. Essential MCP Servers (Global Persistence)
Ensure these MCP servers are globally available in every Claude instance:

### Memory Server (Already Configured)
```
Path: C:\Program Files\nodejs\node.exe
Args: C:\Program Files\nodejs\node_modules\@modelcontextprotocol\server-memory\dist\index.js
Environment:
  MEMORY_PERSIST=true
  MEMORY_FILE_PATH=~/.claude/memory.json
```

### Additional Required Servers
- **Sequential Thinking**: https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
- **Desktop Commander**: https://github.com/wonderwhy-er/DesktopCommanderMCP
- **Tavily Search**: https://github.com/tavily-ai/tavily-mcp
- **Browser Tools**: https://github.com/AgentDeskAI/browser-tools-mcp

## Implementation Focus
1. Configure prompt library for MCP filesystem server access
2. Structure for easy automated parsing and retrieval
3. Ensure all servers persist across Claude restarts
4. Create unified configuration approach for global availability