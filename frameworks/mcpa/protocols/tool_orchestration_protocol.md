---
title: "Tool Orchestration Protocol (TOP)"
category: "frameworks/mcpa/protocols"
tags: ["protocol", "tools", "mcpa", "orchestration"]
created: "2025-03-22"
updated: "2025-03-22"
version: "1.0"
---

# Tool Orchestration Protocol (TOP)

## Overview

The Tool Orchestration Protocol (TOP) standardizes how modules interact with external tools in the MCPA framework. TOP handles tool registration, discovery, selection, invocation, and result integration, providing a uniform interface for tool-augmented reasoning.

## Protocol Structure

```json
{
  "protocol": "TOP",
  "version": "1.0",
  "tools": [
    {
      "id": "string",
      "name": "string",
      "description": "string",
      "capabilities": ["string"],
      "parameters": {
        "paramName": {
          "type": "string",
          "description": "string",
          "required": "boolean",
          "default": "any",
          "enum": ["string"]
        }
      },
      "returns": {
        "type": "string",
        "description": "string"
      }
    }
  ],
  "invocation": {
    "invoke": "string",
    "status": "string",
    "cancel": "string"
  }
}
```

## Core Operations

### Tool Management

- **Register**: Add a new tool to the registry
- **Unregister**: Remove a tool from the registry
- **Discover**: Query available tools and capabilities
- **Describe**: Get detailed information about a specific tool

### Tool Invocation

- **Invoke**: Execute a tool with specified parameters
- **Status**: Check the status of a tool invocation
- **Cancel**: Terminate a running tool invocation
- **Result**: Retrieve the result of a completed invocation

### Message Types

1. **Tool Registration**
   ```json
   {
     "type": "tool_registration",
     "tool": {
       "id": "data-analyzer",
       "name": "Data Analyzer",
       "description": "Analyzes structured data to extract patterns and insights",
       "capabilities": ["statistical-analysis", "trend-detection"],
       "parameters": {
         "data": {
           "type": "json",
           "description": "The data to analyze",
           "required": true
         },
         "analysisType": {
           "type": "string",
           "description": "The type of analysis to perform",
           "required": false,
           "default": "statistical",
           "enum": ["statistical", "temporal", "relational"]
         }
       },
       "returns": {
         "type": "json",
         "description": "Analysis results with insights and visualizations"
       }
     }
   }
   ```

2. **Tool Discovery Query**
   ```json
   {
     "type": "tool_discovery_query",
     "capabilities": ["data-visualization"],
     "requestId": "discovery-123"
   }
   ```

3. **Tool Discovery Response**
   ```json
   {
     "type": "tool_discovery_response",
     "tools": [
       {
         "id": "chart-generator",
         "name": "Chart Generator",
         "description": "Generates visual charts from data",
         "capabilities": ["data-visualization"]
       }
     ],
     "requestId": "discovery-123"
   }
   ```

4. **Tool Invocation**
   ```json
   {
     "type": "tool_invocation",
     "toolId": "data-analyzer",
     "parameters": {
       "data": {...},
       "analysisType": "temporal"
     },
     "invocationId": "inv-456"
   }
   ```

5. **Tool Status Query**
   ```json
   {
     "type": "tool_status_query",
     "invocationId": "inv-456"
   }
   ```

6. **Tool Status Response**
   ```json
   {
     "type": "tool_status_response",
     "invocationId": "inv-456",
     "status": "running",
     "progress": 0.65,
     "estimatedCompletion": "2025-03-22T15:35:00Z"
   }
   ```

7. **Tool Result**
   ```json
   {
     "type": "tool_result",
     "invocationId": "inv-456",
     "result": {...},
     "status": "completed",
     "timestamp": "2025-03-22T15:34:23Z"
   }
   ```

## Integration with MCP

TOP is designed to be compatible with the Model Context Protocol (MCP) Tool features while specializing for reasoning frameworks:

1. **Tool Description**
   - Extends MCP tool schema with reasoning-specific metadata
   - Maintains backward compatibility with MCP tool definitions

2. **Invocation Handling**
   - Uses standardized invocation patterns
   - Adds support for stateful, long-running operations

3. **Result Processing**
   - Provides structured result formats optimized for reasoning
   - Supports progressive result streaming

## Implementation Guidelines

### Tool Registry Implementation

```python
class ToolRegistry:
    def __init__(self):
        self.tools = {}
        self.invocations = {}
        
    def register_tool(self, tool_definition):
        """Register a new tool with the registry."""
        tool_id = tool_definition["id"]
        self.tools[tool_id] = tool_definition
        return tool_id
        
    def unregister_tool(self, tool_id):
        """Unregister a tool from the registry."""
        if tool_id in self.tools:
            del self.tools[tool_id]
            return True
        return False
        
    def get_tool(self, tool_id):
        """Get a tool definition by ID."""
        return self.tools.get(tool_id)
        
    def discover_tools(self, capabilities=None):
        """Discover tools matching the specified capabilities."""
        if not capabilities:
            return list(self.tools.values())
            
        matching_tools = []
        for tool_id, tool in self.tools.items():
            tool_capabilities = tool.get("capabilities", [])
            if any(cap in tool_capabilities for cap in capabilities):
                matching_tools.append(tool)
                
        return matching_tools
        
    def invoke_tool(self, tool_id, parameters):
        """Invoke a tool with the specified parameters."""
        tool = self.get_tool(tool_id)
        if not tool:
            return {"error": f"Tool '{tool_id}' not found"}
            
        # Validate parameters
        self._validate_parameters(tool, parameters)
        
        # Generate invocation ID
        invocation_id = f"inv-{len(self.invocations) + 1}"
        
        # Create invocation record
        invocation = {
            "id": invocation_id,
            "toolId": tool_id,
            "parameters": parameters,
            "status": "pending",
            "startTime": self._get_timestamp(),
            "result": None
        }
        
        self.invocations[invocation_id] = invocation
        
        # Start invocation (implementation would delegate to actual tool)
        self._execute_tool(invocation)
        
        return {
            "invocationId": invocation_id,
            "status": "pending"
        }
        
    def get_invocation_status(self, invocation_id):
        """Get the status of a tool invocation."""
        if invocation_id not in self.invocations:
            return {"error": f"Invocation '{invocation_id}' not found"}
            
        invocation = self.invocations[invocation_id]
        return {
            "invocationId": invocation_id,
            "status": invocation["status"],
            "progress": invocation.get("progress", 0),
            "result": invocation["result"] if invocation["status"] == "completed" else None
        }
        
    def _validate_parameters(self, tool, parameters):
        """Validate parameters against tool definition."""
        tool_params = tool.get("parameters", {})
        
        # Check required parameters
        for param_name, param_def in tool_params.items():
            if param_def.get("required", False) and param_name not in parameters:
                raise ValueError(f"Required parameter '{param_name}' missing")
                
        # Check parameter types
        # (Implementation would include type validation)
        
    def _execute_tool(self, invocation):
        """Execute the tool invocation (placeholder for actual implementation)."""
        # In a real implementation, this would:
        # 1. Find the actual tool implementation
        # 2. Execute it with the parameters
        # 3. Update the invocation with progress, status, and results
        
        # For now, we'll simulate completion
        invocation["status"] = "running"
        invocation["progress"] = 0.5
        
        # In a real implementation, this would be asynchronous
        # Simulating completion after some time
        invocation["status"] = "completed"
        invocation["progress"] = 1.0
        invocation["result"] = {"example": "tool result"}
        invocation["completionTime"] = self._get_timestamp()
        
    def _get_timestamp(self):
        """Get current timestamp."""
        from datetime import datetime
        return datetime.utcnow().isoformat() + "Z"
```

### Tool Consumer Implementation

```python
class ToolConsumer:
    def __init__(self, tool_registry):
        self.tool_registry = tool_registry
        
    def find_tool_for_task(self, task_description, required_capabilities=None):
        """Find an appropriate tool for a given task."""
        available_tools = self.tool_registry.discover_tools(required_capabilities)
        
        # Simple matching logic (a real implementation would be more sophisticated)
        for tool in available_tools:
            # Check if tool description matches task
            if any(keyword in task_description.lower() for keyword in tool["description"].lower().split()):
                return tool["id"]
                
        return None
        
    def execute_task_with_tool(self, tool_id, parameters):
        """Execute a task using the specified tool."""
        invocation_result = self.tool_registry.invoke_tool(tool_id, parameters)
        
        if "error" in invocation_result:
            return invocation_result
            
        invocation_id = invocation_result["invocationId"]
        
        # Poll for completion (a real implementation would use async/await or callbacks)
        while True:
            status = self.tool_registry.get_invocation_status(invocation_id)
            if status["status"] == "completed":
                return status["result"]
            elif status["status"] == "failed":
                return {"error": "Tool execution failed"}
```

## Security Considerations

1. **Input Validation**
   - Validate all tool parameters against schemas
   - Sanitize inputs to prevent injection attacks

2. **Access Control**
   - Implement tool-level permissions
   - Control which modules can access which tools

3. **Resource Limits**
   - Enforce execution time limits
   - Implement resource usage quotas

## Performance Optimization

1. **Parallelism**
   - Support parallel tool execution
   - Implement non-blocking invocation patterns

2. **Caching**
   - Cache tool results for identical parameters
   - Implement result expiration policies

3. **Prioritization**
   - Support priority levels for invocations
   - Implement fair scheduling for resource allocation
