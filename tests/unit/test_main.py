"""Unit tests for Data-Copilot main.py functionality."""
import pytest
from unittest.mock import Mock, patch, MagicMock
import sys

# Mock all heavy dependencies before importing main
mock_modules = [
    'tushare',
    'numpy',
    'numpy.core',
    'numpy._core',
    'numpy._core.multiarray',
    'numpy._core.umath',
    'pandas',
    'matplotlib',
    'matplotlib.pyplot',
    'matplotlib.ticker',
    'matplotlib.font_manager',
    'torch',
    'transformers',
    'sklearn',
    'openai',
    'tiktoken',
    'gradio',
    'dashscope',
    'lab_llms_call',
    'tools',
    'tools.stock',
    'tools.visualization',
    'tools.economic',
    'tools.fund',
    'tools.company',
    'mplfinance',
    'tool',
    'blessed',
    'prettytable',
]

for mod in mock_modules:
    mock = MagicMock()
    sys.modules[mod] = mock


class TestMainFunctions:
    """Tests for functions in main.py."""

    def test_run_function_exists(self):
        """Test that run function exists."""
        import main
        assert hasattr(main, 'run')
        assert callable(main.run)

    def test_add_to_queue_exists(self):
        """Test that add_to_queue function exists."""
        import main
        assert hasattr(main, 'add_to_queue')
        assert callable(main.add_to_queue)

    def test_send_chat_request_exists(self):
        """Test that send_chat_request function exists."""
        import main
        assert hasattr(main, 'send_chat_request')
        assert callable(main.send_chat_request)

    def test_gradio_interface_exists(self):
        """Test that gradio_interface function exists."""
        import main
        assert hasattr(main, 'gradio_interface')

    def test_send_chat_request_variants_exist(self):
        """Test that various send_chat_request variants exist."""
        import main
        # Check that different model handlers exist
        assert hasattr(main, 'send_chat_request_Azure')
        assert hasattr(main, 'send_chat_request_qwen')


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
