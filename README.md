# 🌐 Free LLM API Tokens 共享开源项目

> 整理免费 LLM API 资源，让 AI 开发更简单

## 📋 目录

- [免费 API 提供商](#免费-api-提供商)
- [使用示例](#使用示例)
- [注意事项](#注意事项)
- [贡献指南](#贡献指南)

---

## 🚀 免费 API 提供商

### ✅ 完全免费 (无需信用卡)

| 提供商 | 免费限制 | 支持模型 | API 兼容 |
|--------|----------|----------|----------|
| **OpenRouter** | 20 req/min, 50 req/天 | Gemma 3, Llama 3.2, Qwen3, Mistral 等 | OpenAI |
| **Google AI Studio** | 250K tokens/min, 20-500 req/天 | Gemini 3 Flash, Gemma 3 | OpenAI |
| **NVIDIA NIM** | 40 req/min | 各种开源模型 | OpenAI |
| **Mistral (La Plateforme)** | 1 req/sec, 500K tokens/min | Mistral, Codestral | OpenAI |
| **Groq** | 免费 | Llama, Qwen, Mistral | OpenAI |
| **Cerebras** | 免费 | Llama, Mistral | OpenAI |
| **Cohere** | 免费 | Command R | OpenAI |
| **GitHub Models** | 免费 | Llama, Phi, Mistral | OpenAI |
| **Cloudflare Workers AI** | 免费 | Llama, Mistral | OpenAI |
| **HuggingFace** | 免费 tier | 各种开源模型 | HuggingFace |

### 💳 需要试用积分 (免费注册)

| 提供商 | 试用额度 | 特点 |
|--------|----------|------|
| **Fireworks** | $20 免费 | 高性能 |
| **Nebius** | $20 免费 | 多种模型 |
| **Novita** | $10 免费 | 便宜 |
| **AI21** | 免费积分 | Jamba 系列 |
| **Upstage** | 免费 | 韩国模型 |
| **Hyperbolic** | 免费 | 便宜 |

---

## 💻 使用示例

### OpenRouter 示例

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_OPENROUTER_KEY",
    base_url="https://openrouter.ai/v1"
)

response = client.chat.completions.create(
    model="meta-llama/llama-3.2-3b-instruct:free",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### Google AI Studio 示例

```python
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_KEY")
model = genai.GenerativeModel('gemini-2.0-flash')
response = model.generate_content("Hello!")
print(response.text)
```

### Groq 示例

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_GROQ_KEY",
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="llama-3.1-70b-versatile",
    messages=[{"role": "user", "content": "Hello!"}]
)
```

---

## ⚠️ 注意事项

1. **不要滥用** - 这些服务是为开发者提供的，请合理使用
2. **不要分享私钥** - 只分享你的项目，不要泄露 API Key
3. **检查最新限制** - 限制可能随时变化，请查看官方文档
4. **遵守服务条款** - 确保符合提供商的使用政策

---

## 🤝 贡献指南

欢迎提交 PR！添加新的免费 API 提供商或更新现有信息。

```bash
# 克隆项目
git clone https://github.com/yourusername/free-llm-tokens.git
# 创建分支
git checkout -b add-new-provider
# 提交更改
git commit -m "Add XXX provider"
# 推送
git push origin add-new-provider
```

---

## 📚 参考资源

- [Free LLM API Resources (GitHub)](https://github.com/cheahjs/free-llm-api-resources)
- [Public APIs - Free LLM APIs](https://publicapis.io/blog/free-llm-apis)
- [Free LLM Directory](https://free-llm.com/)

---

## 📄 License

MIT License - 自由使用，共享改进