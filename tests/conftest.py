"""pytest configuration for Data-Copilot tests."""
import pytest


@pytest.fixture
def sample_openai_key():
    """Sample OpenAI key fixture."""
    return "sk-test-key-12345"


@pytest.fixture
def sample_azure_config():
    """Sample Azure configuration fixture."""
    return {
        "api_key": "azure-key-12345",
        "api_base": "https://test.openai.azure.com",
        "engine": "gpt-35",
    }


@pytest.fixture
def sample_question():
    """Sample question fixture."""
    return "我想看看贵州茅台的股价走势"


@pytest.fixture
def mock_llm_response():
    """Mock LLM response fixture."""
    return {
        "intent": "Extract stock data",
        "task_plan": {"task1": "Get stock prices"},
        "result": "Test result",
    }
