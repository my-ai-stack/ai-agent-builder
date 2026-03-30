"""Tests for AI Agent Builder"""
import pytest
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


def test_agent_builder_import():
    """Test agent_builder module imports"""
    from agent_builder import AgentBuilder, LLMNode, ToolNode
    assert AgentBuilder is not None


def test_builder_init():
    """Test AgentBuilder initialization"""
    from agent_builder import AgentBuilder
    builder = AgentBuilder()
    assert builder is not None
    assert len(builder.nodes) == 0


def test_add_llm_node():
    """Test adding LLM node"""
    from agent_builder import AgentBuilder
    builder = AgentBuilder()
    node = builder.add_llm_node("test_llm", "gpt-4", "You are helpful.")
    assert node is not None
    assert node.model == "gpt-4"


def test_add_tool_node():
    """Test adding tool node"""
    from agent_builder import AgentBuilder
    builder = AgentBuilder()
    node = builder.add_tool_node("test_tool", "search")
    assert node is not None


def test_add_memory_node():
    """Test adding memory node"""
    from agent_builder import AgentBuilder
    builder = AgentBuilder()
    node = builder.add_memory_node("test_memory")
    assert node is not None


def test_execute_empty():
    """Test executing empty builder"""
    from agent_builder import AgentBuilder
    builder = AgentBuilder()
    result = builder.execute("test input")
    assert result == "No nodes in workflow"


def test_to_json():
    """Test JSON export"""
    from agent_builder import AgentBuilder
    builder = AgentBuilder()
    builder.add_llm_node("llm1")
    json_str = builder.to_json()
    assert json_str is not None
    assert "nodes" in json_str


def test_from_json():
    """Test JSON import"""
    from agent_builder import AgentBuilder
    json_str = '{"nodes": [{"id": "test", "type": "llm", "config": {}}], "connections": []}'
    builder = AgentBuilder.from_json(json_str)
    assert builder is not None