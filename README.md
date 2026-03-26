# 免费 LLM API 资源导航

> 汇集互联网免费大模型API接口地址、模型参数配置，帮助开发者快速接入AI能力

[![每日更新](https://img.shields.io/badge/更新-2026--03--26-green.svg)](https://linux503.github.io/free-llm-tokens/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

## 🌟 特点

- ☁️ **15+ 云端免费 API** - 无需本地部署，直接调用
- 💻 **本地部署模型** - Ollama、LM Studio、GPT4All、Jan
- 📋 **一键复制** - API Endpoint 复制即用
- 🔄 **每日更新** - 持续跟踪最新免费资源

## ☁️ 云端免费 API

| 提供商 | 免费额度 | 特点 | GitHub 搜索关键词 |
|--------|----------|------|------------------|
| **OpenRouter** | 有限 | 100+免费模型聚合 | `openrouter free api gpt` |
| **Groq** | 14,400次/天 | 超高速800+ tokens/s | `groq api free llm` |
| **Hugging Face** | 免费额度 | 2000+开源模型 | `huggingface inference api free` |
| **Google Gemini** | 免费 | 15 RPM | `gemini api google free` |
| **DeepSeek** | 价格低廉 | 国产顶尖模型 | `deepseek api chatgpt alternative` |
| **Together AI** | 每周赠送 | 高性能推理 | `together ai free api` |
| **Cloudflare Workers** | 10万次/天 | 全球CDN加速 | `cloudflare workers ai free` |
| **Azure OpenAI** | $200/180天 | 企业级稳定 | `azure openai free trial` |
| **Novita AI** | 新用户赠送 | 高速响应 | `novita ai free api` |
| **Hyperbolic** | 每月免费 | 高并发 | `hyperbolic api free llm` |
| **Cerebras** | 完全免费 | 1800 tokens/s | `cerebras api free inference` |
| **Mistral** | 免费额度 | 欧洲合规 | `mistral api free chat` |
| **GitHub Models** | 免费额度 | GitHub集成 | `github models ai free` |
| **Fireworks AI** | 新用户赠送 | 100+模型 | `fireworks ai api` |
| **Perplexity** | 免费额度 | 联网搜索 | `perplexity api sonar` |
| **Anthropic** | 新用户免费 | 超强推理 | `anthropic claude api free` |

## 💻 本地部署模型

| 工具 | 特点 | GitHub 搜索关键词 |
|------|------|------------------|
| **Ollama** | 命令行运行，跨平台 | `ollama local llm run` |
| **LM Studio** | 图形界面，模型管理 | `lm studio local ai` |
| **GPT4All** | 隐私优先，CPU/GPU | `gpt4all local models` |
| **Jan** | 开源ChatGPT替代 | `jan ai local chatgpt` |

## 🔍 GitHub 搜索技巧

### 找到更多免费 API

```
# 免费 LLM API
free llm api openai alternative
free gpt api open-source
free chatgpt api key

# 开源模型
open source llm model api
llama3 api gpt alternative
qwen2.5 api model

# 本地部署
local llm self-hosted
ollama docker kubernetes
llm inference server

# 聚合平台
unified llm api gateway
multi-provider llm api
llm api aggregator
```

### 找到相关开源项目

```
# API 代理/网关
llm api gateway proxy
openai api compatible
api proxy llm

# SDK/客户端
llm sdk python js
chatgpt api client library

# 提示词/工具
llm prompt template
ai api wrapper library
```

## 📖 使用示例

### Python 调用示例

```python
import openai

client = openai.OpenAI(
    api_key="YOUR_API_KEY",
    base_url="https://openrouter.ai/api/v1/"
)

response = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{"role": "user", "content": "你好!"}]
)
print(response.choices[0].message.content)
```

### curl 调用示例

```bash
curl https://api.groq.com/openai/v1/chat/completions \
  -H "Authorization: Bearer $GROQ_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama-3.3-70b-versatile",
    "messages": [{"role": "user", "content": "你好"}]
  }'
```

## 📱 在线访问

**[https://linux503.github.io/free-llm-tokens/](https://linux503.github.io/free-llm-tokens/)**

## 📧 联系与反馈

如果您有任何问题或建议，欢迎随时联系：
- Email: abbtoe@yandex.com

## 🤝 贡献

欢迎提交 PR 更新新的免费 API 资源！

## 🔍 更多 GitHub 搜索关键词

### 免费 API 聚合器
```
free-api-aggregator llm
free llm proxy gateway
multi-llm-api-wrapper
llm-api-aggregator free
```

### 免费模型列表
```
free-gpt-models gpt4-free
free-llm-models-list
free-open-source-llm
free-ai-models-api
```

### 开发者工具
```
llm-dashboard free
chatbot-template free
ai-api-key-generator
free-api-key-tools
```

### 自托管方案
```
self-hosted-llm docker
local-ai-gateway
ollama-api-server
llm-self-host-guide
```

### 特定模型相关
```
deepseek-api-free
qwen-api-open-source
llama3-free-api
minimax-api-free
kimi-api-open
```

### 中文搜索关键词
```
免费GPT API
免费大模型API
免费LLM API接口
免费AI API key
国内免费LLM
ChatGPT免费替代
GPT4免费调用
AI大模型免费API
```

## 📄 许可证

MIT License

---

> ⚠️ **注意**: 本页面仅供学习交流，请遵守各平台服务条款，合理使用免费额度。
