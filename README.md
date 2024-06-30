## FastAPI Rate limit Demo
Demo rate limit with Fast API

### Setup env
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run server
```bash
uvicorn main:app --reload
```
or with docker
```bash
docker compose up --build
```

### Access redis cli
```bash
docker-compose exec redis redis-cli
docker-compose exec redis redis-cli KEYS '*' # list all keys
docker-compose exec redis redis-cli GET your_key # get value of key
docker-compose exec redis redis-cli HGETALL your_key # get all fields of key
```
