# FastAPI 模板库

[English Version](./README_en.md)

这是一个 FastAPI 的模版库，旨在帮助开发者快速搭建基于 FastAPI 的项目。

## 特性

- **快速启动**: 提供开箱即用的项目结构
- **高性能**: 基于 FastAPI 的高性能特性
- **易于扩展**: 模块化设计，方便扩展和维护


## 创建自己的库

点击 [使用此模版](https://github.com/xmanlucian/Fastapi_Template/generate) 创建自己的库。

## 安装

```bash
git clone https://github.com/xmanlucian/Fastapi_Template.git
cd Fastapi_Template
pip install -r requirements.txt
```

## 使用

1. 启动：

    ```bash
    make up
    ```

2. 打开浏览器访问 `http://127.0.0.1:8000` 查看效果。

## 项目结构

```
Fastapi_Template/
├── Makefile
├── README.md
├── README_en.md
├── app
│   ├── __init__.py
│   ├── __main__.py
│   ├── api
│   ├── config
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── default
│   │       └── default.yml
│   ├── core
│   ├── factory.py
│   ├── models
│   ├── routers
│   │   ├── __init__.py
│   │   ├── heartbeat.py
│   │   └── posts.py
│   ├── schemas
│   └── services
├── docker
│   ├── Dockerfile
│   └── docker-compose.yml
└── requirements.txt
```




## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目。

## 许可证

本项目采用 MIT 许可证，详情请参阅 [LICENSE](./LICENSE) 文件。
