#!/usr/bin/env python3
"""
Free LLM API - 统一调用示例
Unified interface for free LLM APIs
"""

from openai import OpenAI

# 可用的免费 API 客户端
PROVIDERS = {
    "openrouter": {
        "base_url": "https://openrouter.ai/v1",
        "key_env": "OPENROUTER_API_KEY",
        "free_models": [
            "meta-llama/llama-3.2-3b-instruct:free",
            "google/gemma-3-12b-it:free",
            "qwen/qwen3-4b:free",
        ]
    },
    "groq": {
        "base_url": "https://api.groq.com/openai/v1",
        "key_env": "GROQ_API_KEY",
        "free_models": [
            "llama-3.1-70b-versatile",
            "llama-3.1-8b-instant",
            "mixtral-8x7b-32768",
        ]
    },
    "cerebras": {
        "base_url": "https://api.cerebras.ai/v1",
        "key_env": "CEREBRAS_API_KEY",
        "free_models": [
            "llama-3.1-70b",
        ]
    },
}

def create_client(provider: str, api_key: str) -> OpenAI:
    """创建指定提供商的 API 客户端"""
    if provider not in PROVIDERS:
        raise ValueError(f"Unknown provider: {provider}")
    
    config = PROVIDERS[provider]
    return OpenAI(api_key=api_key, base_url=config["base_url"])

def chat(provider: str, model: str, message: str, api_key: str) -> str:
    """发送聊天请求"""
    client = create_client(provider, api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content

# 示例用法
if __name__ == "__main__":
    import os
    
    # 使用示例
    print("=== OpenRouter 示例 ===")
    try:
        result = chat(
            provider="openrouter",
            model="meta-llama/llama-3.2-3b-instruct:free",
            message="你好",
            api_key=os.environ.get("OPENROUTER_API_KEY", "YOUR_KEY")
        )
        print(f"回复: {result}")
    except Exception as e:
        print(f"错误: {e}")
    
    print("\n=== Groq 示例 ===")
    try:
        result = chat(
            provider="groq",
            model="llama-3.1-8b-instant",
            message="你好",
            api_key=os.environ.get("GROQ_API_KEY", "YOUR_KEY")
        )
        print(f"回复: {result}")
    except Exception as e:
        print(f"错误: {e}")