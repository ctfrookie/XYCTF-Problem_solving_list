# 使用 Python 3.10 的官方镜像作为基础镜像
FROM python:3.10

# 设置工作目录
WORKDIR /app

# 复制当前文件夹下的 XYCTF 题目描述文件夹到容器的 /app 目录下
COPY templates /app
COPY app.py /app

# 进入题目描述文件夹
WORKDIR /app

# 安装相关依赖
RUN pip install flask
RUN pip install requests
# 暴露容器的端口
EXPOSE 80

# 运行应用
CMD ["python", "app.py"]
