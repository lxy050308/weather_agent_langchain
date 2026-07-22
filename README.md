# lxy20260701
# 🌦️ Weather Agent - Multi-Agent Intelligent Environment Assistant

<div align="center">

基于 **LangChain + LangGraph + DeepSeek LLM** 构建的多 Agent 智能环境助手。

支持天气查询、空气质量分析、旅游规划、用户记忆以及 RAG 知识增强能力。

通过 Agent 自主理解用户需求、规划任务并调用外部工具，实现从传统问答系统向智能 Agent 系统的升级。

</div>


---

# 📖 项目简介

随着大语言模型（LLM）的发展，AI 应用逐渐从传统的文本生成模式，发展为具备：

- 自主理解
- 任务规划
- 工具调用
- 知识检索
- 多 Agent 协作

能力的智能 Agent 系统。

本项目基于 **DeepSeek 大语言模型** 作为推理核心，通过 **LangChain 与 LangGraph 构建 Agent 工作流**，实现一个面向环境信息查询场景的智能助手。


用户无需按照固定格式输入，只需要使用自然语言描述需求：

例如：

> "帮我看看上海今天的天气，空气质量怎么样，适合出去玩吗？"


系统能够自动：

```
用户输入

↓

理解用户意图

↓

任务拆解

↓

Agent选择

↓

调用工具获取数据

↓

结合知识库分析

↓

生成最终回答
```


---

# 🎯 项目目标


## 1. 探索 LLM 应用开发流程

学习并实践：

- 大语言模型调用
- Prompt设计
- Agent设计
- Tool调用
- RAG知识增强


## 2. 构建完整 Agent 架构

实现：

```
用户
 |
 ↓
Supervisor Agent
 |
 ↓
业务Agent
 |
 ↓
Skill
 |
 ↓
Tool
 |
 ↓
外部数据
```


## 3. 从单轮问答升级为智能系统

支持：

- 多步骤推理
- 多 Agent 协作
- 用户上下文记忆
- 外部知识增强


---

# ✨ 核心功能


# 1. 🌤️ 天气查询 Agent


负责处理天气相关任务。


功能：

- 查询城市天气
- 获取实时天气数据
- 分析温度变化
- 提供天气建议


架构：

```
Weather Agent

↓

Weather Skill

↓

Weather Tool

↓

Weather API

↓

返回天气结果
```



---

# 2. 🌫️ 空气质量分析 Agent


负责环境质量分析。


功能：

- AQI查询
- 空气质量等级判断
- 健康建议


流程：

```
用户请求

↓

Environment Agent

↓

Air Quality Tool

↓

AQI API

↓

LLM分析

↓

生成建议
```


---

# 3. 🧠 Supervisor Agent任务调度


系统核心调度模块。


作用：

- 理解用户需求
- 分析任务类型
- 分配任务给不同 Agent


例如：

用户：

> 北京天气怎么样，适合旅游吗？


Supervisor：

拆分：

```
天气查询

↓

Weather Agent


旅游建议

↓

Travel Agent
```


---

# 4. 🧩 Skill能力管理


项目采用 Skill 层设计。


Skill负责：

- 定义 Agent 能力
- 管理业务逻辑
- 组织 Tool调用


结构：

```
Skill

|

├── WeatherSkill

├── AirQualitySkill

├── TravelSkill

└── UserProfileSkill

```


优势：

降低 Agent 和具体工具之间的耦合。


---

# 5. 🔧 Tool工具调用


Tool负责执行具体操作。


例如：

```
Agent

↓

Skill

↓

Tool

↓

API / 数据库

```


当前工具：

| Tool | 功能 |
|-|-|
| weather_tool | 天气数据获取 |
| air_quality_tool | AQI数据获取 |


---

# 6. 🧠 Memory用户记忆


系统支持用户上下文保存。


例如：

第一次：

```
用户：
我在北京
```


系统保存：

```
User Profile

city = Beijing
```


之后：

```
用户：
今天适合出门吗？
```


系统自动结合历史信息。


技术：

- LangGraph Memory
- SQLite


---

# 7. 📚 RAG知识增强


项目加入 Retrieval-Augmented Generation。


通过知识库增强模型回答能力。


流程：

```
Documents

↓

Embedding

↓

Vector Database

↓

Retriever

↓

LLM

↓

Answer

```


知识文件：

```
documents

├── weather_rule.txt

├── air_quality.txt

└── travel_rule.txt

```


使用：

- Chroma Vector Database
- Embedding
- Retriever


---

# 🏗️ 系统整体架构


```
                         User Query

                              |

                              ↓

                    Supervisor Agent

                              |

        ------------------------------------------------

        |                      |                       |

        ↓                      ↓                       ↓


 Weather Agent        Environment Agent        Travel Agent


        |                      |                       |


 Weather Skill        AirQuality Skill        Travel Skill


        |                      |                       |


 Weather Tool         AQI Tool                 Knowledge Base


        |                      |                       |


        ------------------ External Data ----------------


                              |

                              ↓


                         DeepSeek LLM


                              |

                              ↓


                       Final Response

```


---

# 🔄 系统运行流程


完整执行流程：

```
1. 用户输入自然语言请求


        ↓


2. DeepSeek理解用户意图


        ↓


3. Supervisor Agent任务拆解


        ↓


4. 调度对应业务Agent


        ↓


5. Skill加载对应能力


        ↓


6. Tool调用外部服务


        ↓


7. RAG检索相关知识


        ↓


8. LLM综合分析


        ↓


9. 返回最终答案

```


---

# 🛠️ 技术架构


## AI模型

| 技术 | 作用 |
|-|-|
| DeepSeek LLM | 核心推理模型 |
| Prompt | 指令设计 |
| Embedding | 文本向量化 |


---

## Agent框架

| 技术 | 作用 |
|-|-|
| LangChain | Agent应用开发框架 |
| LangGraph | Agent流程编排 |


---

## AI能力模块


```
Agent

├── Planning

├── Tool Calling

├── Memory

└── RAG

```


---

## 数据存储


|技术|用途|
|-|-|
|SQLite|用户记忆|
|Chroma|向量数据库|


---

## 开发环境


|技术|版本|
|-|-|
|Python|3.x|
|LangChain|1.x|
|LangGraph|latest|
|DeepSeek API|LLM服务|


---

# 📂 项目结构


```
weather_agents

│
├── agents
│   ├── supervisor_agent.py
│   ├── weather_agent.py
│   └── environment_agent.py
│
├── skills
│   ├── weather_skill.py
│   ├── air_quality_skill.py
│   ├── travel_skill.py
│   └── user_profile_skill.py
│
├── tools
│   ├── weather_tool.py
│   └── air_quality_tool.py
│
├── rag
│   ├── create_vector.py
│   └── rag_retriever.py
│
├── documents
│   ├── weather_rule.txt
│   ├── air_quality.txt
│   └── travel_rule.txt
│
├── memory
│
├── main.py
│
├── requirements.txt
│
├── .env
│
└── README.md

```


---

# 🚀 环境部署


## 1. 克隆项目


```bash
git clone https://github.com/lxy050308/lxy20260701.git
```


进入目录：

```bash
cd weather_agents
```



---

## 2. 安装依赖


```bash
pip install -r requirements.txt
```



---

## 3. 配置环境变量


创建：

```
.env
```


配置：

```env
DEEPSEEK_API_KEY=your_api_key

WEATHER_API_KEY=your_api_key

AQI_API_KEY=your_api_key
```


注意：

`.env` 文件不会上传 GitHub。


---

# ▶️ 项目运行


启动：

```bash
python main.py
```


示例：

输入：

```
查询北京天气
```


系统：

```
理解需求

↓

调用Weather Agent

↓

获取天气数据

↓

生成回答

```


---

# 📈 项目版本迭代


## Version 1

基础天气查询

实现：

- API调用
- LLM问答


---

## Version 2

加入 Agent


实现：

- LangChain Agent
- Tool Calling


---

## Version 3

多 Agent 架构


加入：

- Supervisor Agent
- Environment Agent


---

## Version 4

智能化增强


加入：

- Memory
- RAG
- Skill层设计


---

# 🔮 后续规划


未来计划继续完善：


## 1. 更多领域 Agent

例如：

- 新闻Agent
- 日程Agent
- 数据分析Agent


## 2. Web应用化

增加：

- Vue前端
- FastAPI后端


## 3. 企业级部署


增加：

- Docker
- Redis
- PostgreSQL
- Kubernetes


## 4. Agent能力增强


增加：

- Planning机制
- Reflection机制
- Multi-Agent协商


---

# 📌 项目总结


本项目围绕大语言模型应用开发流程展开实践。

通过：

- DeepSeek LLM
- LangChain
- LangGraph
- Agent
- Tool
- Memory
- RAG


构建了一个具备：

✅ 自然语言理解能力  
✅ 任务规划能力  
✅ 工具调用能力  
✅ 知识检索能力  
✅ 多 Agent 协作能力  


的智能环境助手。


项目实践了从：

```
传统程序开发

↓

LLM应用开发

↓

Agent智能系统开发

```

的完整学习过程。


---

# 👤 Author

lxy

AI Application Learning Project

2026