## XYCTF-解题榜

### 一.文件配置(app.py)

```python
# 设置 Token 值（第10行）
TOKEN = ""

# 设置 URL（第21行）
base_url = ""  # 设置为实际的域名或 IP URL
```

### 二.启动方式

#### 1.配置完成之后直接运行app.py

```python
PS C:\Users\Administrator\Desktop\XYCTF-解题榜> & D:/Python310/python.exe c:/Users/Administrator/Desktop/XYCTF-解题榜/app.py
 * Serving Flask app 'app'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:80
 * Running on http://192.168.1.108:80
Press CTRL+C to quit
```

#### 2.使用dockerfile文件

使用以下命令构建镜像：

```dockerfile
docker build -t myxy .
```

然后通过以下命令运行容器：

```dockerfile
docker run -d -p 80:80 --name my-container myxy
```

### 三.文件列表

```bash
├─XYCTF-解题榜
│  │  app.py			#主要的 Python 文件
│  │  dockerfile		#用于构建 Docker 镜像
│  │  README.md			#项目的说明文档				
│  │
│  └─templates			#网页模板的文件夹
│          index.html	#网页模板的文件
```
### 四.效果图
![image](https://github.com/ctfrookie/XYCTF-Problem_solving_list/assets/112057820/e2e2e845-193d-4db8-994a-a5afe2620636)

