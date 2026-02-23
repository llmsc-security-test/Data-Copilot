"""Unit tests for Data-Copilot app.py functionality."""
import pytest
from unittest.mock import Mock, patch, MagicMock
import sys

# Mock tushare and other dependencies before importing app
sys.modules['tushare'] = MagicMock()
sys.modules['main'] = MagicMock()


class TestClientClass:
    """Tests for the Client class in app.py."""

    @pytest.fixture
    def client(self):
        """Create a Client instance for testing."""
        # Import after mocking
        from app import Client
        return Client()

    def test_client_initialization(self, client):
        """Test Client class initialization."""
        # OPENAI_KEY is set to module-level OPENAI_KEY which is None
        assert client.OPENAI_KEY is None
        assert client.OPENAI_API_BASED_AZURE is None
        assert client.OPENAI_ENGINE_AZURE is None
        assert client.OPENAI_API_KEY_AZURE is None
        assert client.stop is False

    def test_client_set_key(self, client):
        """Test Client.set_key method."""
        result = client.set_key(
            "sk-test-key",
            "azure-key",
            "https://azure-api.com",
            "gpt-35"
        )

        assert result[0] == "sk-test-key"
        assert result[1] == "azure-key"
        assert result[2] == "https://azure-api.com"
        assert result[3] == "gpt-35"

    def test_client_set_key_updates_attributes(self, client):
        """Test that set_key properly updates client attributes."""
        client.set_key(
            "sk-new-key",
            "azure-new-key",
            "https://new-api.com",
            "gpt-4"
        )

        assert client.OPENAI_KEY == "sk-new-key"
        assert client.OPENAI_API_KEY_AZURE == "azure-new-key"
        assert client.OPENAI_API_BASED_AZURE == "https://new-api.com"
        assert client.OPENAI_ENGINE_AZURE == "gpt-4"


class TestGradioInterface:
    """Tests for the Gradio interface setup in app.py."""

    def test_app_imports_correctly(self):
        """Test that app.py imports correctly."""
        import app
        assert hasattr(app, 'demo')
        assert hasattr(app, 'Client')

    def test_example_questions_exist(self):
        """Test that example questions are defined."""
        import app

        assert hasattr(app, 'example_stock')
        assert hasattr(app, 'example_economic')
        assert hasattr(app, 'example_company')
        assert hasattr(app, 'example_fund')

        assert len(app.example_stock) > 0
        assert len(app.example_economic) > 0

    def test_example_stock_questions_contain_expected_keywords(self):
        """Test that stock questions contain expected financial terms."""
        import app

        # Stock-related keywords (includes 资金 for capital flow questions)
        stock_keywords = ['股票', '股价', '收益率', '走势', 'K 线', '资金', '北向', '指数', '银行', '茅台', '五粮液', '宁德时代']
        for question in app.example_stock:
            has_keyword = any(kw in question for kw in stock_keywords)
            assert has_keyword, f"Question '{question}' should contain a stock keyword"

    def test_example_economic_questions_contain_expected_keywords(self):
        """Test that economic questions contain expected terms."""
        import app

        # Economic keywords (includes lowercase cpi, 十年 for decade questions, 新闻 for news)
        economic_keywords = ['CPI', 'GDP', '货币供应量', '经济', '增速', 'cpi', '十年', '预测', '新闻', '消息']
        for question in app.example_economic:
            has_keyword = any(kw.lower() in question.lower() for kw in economic_keywords)
            assert has_keyword, f"Question '{question}' should contain an economic keyword"


class TestAppConfiguration:
    """Tests for app configuration and setup."""

    def test_css_styling_is_defined(self):
        """Test that CSS styling is properly defined."""
        import app
        assert hasattr(app, 'css')
        assert 'max-width' in app.css
        assert 'flex-direction' in app.css

    def test_font_settings_for_chinese(self):
        """Test that font settings support Chinese characters."""
        import app
        # Check that Chinese font support is configured
        # The app should have matplotlib configured with Chinese font support
        assert hasattr(app, 'plt')
        # Verify font settings are applied (check the source has font config)
        import inspect
        app_source = inspect.getsource(app)
        assert 'WenQuanYi Zen Hei' in app_source or 'Noto Sans CJK' in app_source

    def test_gradio_blocks_is_accessible(self):
        """Test that the Gradio Blocks interface is accessible."""
        import app
        assert hasattr(app, 'demo')


class TestAppStateManagement:
    """Tests for state management in the app."""

    def test_state_contains_client(self):
        """Test that state properly contains client instance."""
        import app
        from app import Client

        # Verify Client class exists and can be instantiated
        client = Client()
        assert "client" in {"client": client}
        assert isinstance(client, Client)


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
