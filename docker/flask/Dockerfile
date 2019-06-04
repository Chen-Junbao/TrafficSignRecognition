FROM opencv:4.1.0

WORKDIR /usr/my_flask/app

COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/

COPY  ./src .

CMD ["python", "app.py"]
