# djangobenchmark

0. Setup Ubuntu
```
apt update && apt install -y pipenv
git clone https://github.com/escrichov/djangobenchmark && cd djangobenchmark
```

1. Install

```
pipenv install
```

2. Start server

```
./bin/server_gunicorn.sh
```

3. Run Benchmark

```
./bin/benchmark.sh http://127.0.0.1:8000 results_gunicorn.txt
```

3. View results

```
cat output/results_gunicorn.txt
```
