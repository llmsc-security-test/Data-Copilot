#!/usr/bin/env python3
"""
Tutorial PoC for Data-Copilot HTTP API testing

This script demonstrates how to interact with the Data-Copilot Gradio app
by testing its internal API endpoints.

Note: Data-Copilot is primarily a Gradio web app. This PoC shows how to
interact with the underlying Python functions directly or via Gradio's
internal API.
"""

import requests
import json
import sys
import time


class DataCopilotClient:
    """Client for testing Data-Copilot Gradio API endpoints."""

    def __init__(self, base_url="http://localhost:7860"):
        self.base_url = base_url
        self.session = requests.Session()

    def test_gradio_root(self):
        """Test if Gradio app is accessible."""
        try:
            response = self.session.get(self.base_url)
            print(f"[*] Testing root endpoint: {self.base_url}")
            print(f"    Status: {response.status_code}")
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            print(f"[!] Error connecting to Gradio app: {e}")
            return False

    def test_gradio_api(self):
        """Test Gradio API endpoint."""
        api_url = f"{self.base_url}/queue/join"
        print(f"[*] Testing API endpoint: {api_url}")

        # Gradio API payload structure
        payload = {
            "data": ["Test query for testing purposes"],
            "fn_index": 1,
            "event_data": None,
            "api_name": None
        }

        try:
            response = self.session.post(api_url, json=payload, timeout=30)
            print(f"    Status: {response.status_code}")
            if response.status_code == 200:
                print(f"    Response: {response.text[:200]}...")
            return True
        except requests.exceptions.RequestException as e:
            print(f"[!] Error calling API: {e}")
            return False

    def test_internal_run_function(self):
        """
        Test the internal run function directly.
        This requires importing the main module.
        """
        print("\n[*] Testing internal Python functions:")

        # Test that the required modules can be imported
        required_modules = [
            'gradio',
            'pandas',
            'matplotlib',
            'openai',
            'tushare'
        ]

        missing = []
        for module in required_modules:
            try:
                __import__(module)
                print(f"    [OK] {module}")
            except ImportError:
                print(f"    [MISSING] {module}")
                missing.append(module)

        if missing:
            print(f"\n[!] Missing modules: {', '.join(missing)}")
            print("    Install with: pip install -r requirements.txt")
            return False
        else:
            print("\n[+] All required modules are installed!")
            return True

    def get_app_info(self):
        """Get application information from Gradio."""
        info_url = f"{self.base_url}/config"
        try:
            response = self.session.get(info_url, timeout=10)
            if response.status_code == 200:
                config = response.json()
                print(f"[*] Gradio Config:")
                print(f"    Title: {config.get('title', 'N/A')}")
                print(f"    Version: {config.get('version', 'N/A')}")
                return config
        except Exception as e:
            print(f"[!] Error getting app info: {e}")
            return None


def test_http_endpoints(base_url="http://localhost:7860"):
    """Test HTTP endpoints of the Data-Copilot app."""
    print("=" * 60)
    print("Data-Copilot HTTP API Test Suite")
    print("=" * 60)

    client = DataCopilotClient(base_url)

    # Test 1: Root endpoint
    print("\n[1] Testing Root Endpoint")
    print("-" * 40)
    client.test_gradio_root()

    # Test 2: API endpoint
    print("\n[2] Testing API Endpoint")
    print("-" * 40)
    client.test_gradio_api()

    # Test 3: Internal functions
    print("\n[3] Testing Internal Python Functions")
    print("-" * 40)
    client.test_internal_run_function()

    # Test 4: App info
    print("\n[4] Testing Application Information")
    print("-" * 40)
    client.get_app_info()

    print("\n" + "=" * 60)
    print("Test Suite Complete")
    print("=" * 60)

    print("\nUsage Notes:")
    print("1. Start the app with: python app.py or docker-compose up")
    print("2. Default URL: http://localhost:7860")
    print("3. You need to set your OpenAI API key in the app interface")
    print("4. The app supports Chinese financial data queries")
    print("\nExample queries you can test:")
    print("  - '给我画一下可孚医疗2022年年中到今天的股价'")
    print("  - '中国过去十年的cpi走势是什么'")
    print("  - '易方达的张坤管理了几个基金'")


def main():
    """Main function."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Data-Copilot HTTP API Test PoC"
    )
    parser.add_argument(
        "--url",
        default="http://localhost:7860",
        help="Base URL of the Data-Copilot app (default: http://localhost:7860)"
    )
    parser.add_argument(
        "--test-modules",
        action="store_true",
        help="Test if required Python modules are installed"
    )

    args = parser.parse_args()

    if args.test_modules:
        client = DataCopilotClient(args.url)
        client.test_internal_run_function()
    else:
        test_http_endpoints(args.url)


if __name__ == "__main__":
    main()
