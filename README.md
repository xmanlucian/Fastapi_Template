# FastAPI Template Repository

[English Version](./README_en.md)

这是一个 FastAPI 的模版库，旨在帮助开发者快速搭建基于 FastAPI 的项目。

## 特性

- **快速启动**: 提供开箱即用的项目结构
- **高性能**: 基于 FastAPI 的高性能特性
- **易于扩展**: 模块化设计，方便扩展和维护

## 安装

```bash
git clone https://github.com/xmanlucian/fastapi-template.git
cd fastapi-template
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
fastapi-template/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── tests/
├── .gitignore
├── requirements.txt
├── README_en.md
└── README.md
```

## 创建自己的库

点击 [使用此模版](https://github.com/xmanlucian/fastapi-template/generate) 创建自己的库。

## 贡献

欢迎提交 Issue 和 Pull Request 来帮助改进这个项目。

## 许可证

本项目采用 MIT 许可证，详情请参阅 [LICENSE](./LICENSE) 文件。
