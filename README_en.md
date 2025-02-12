
## English Version

[中文版](./README.md)

This is a FastAPI template repository designed to help developers quickly set up projects based on FastAPI.

## Features

- **Quick Start**: Provides a ready-to-use project structure
- **High Performance**: Leverages FastAPI's high-performance features
- **Easy to Extend**: Modular design for easy extension and maintenance


## Create Your Own Repository

Click [Use this template](https://github.com/xmanlucian/Fastapi_Template/generate) to create your own repository.

## Installation

```bash
git clone https://github.com/xmanlucian/Fastapi_Template.git
cd Fastapi_Template
pip install -r requirements.txt
```

## Usage

1. Start

    ```bash
    make up
    ```

2. Open your browser and visit `http://127.0.0.1:8000` to see the result.

## Project Structure

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



## Contributing

Feel free to submit Issues and Pull Requests to help improve this project.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
