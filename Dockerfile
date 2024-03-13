FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && apt-get install -y graphviz \
    && rm -rf /var/lib/apt/lists/*

CMD ["sh", "-c", "python main.py && dot -Tps shortest_paths.dot -o shortest_paths.ps"]
