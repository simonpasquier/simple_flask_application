am: alertmanager --config.file=prometheus/alertmanager.yml
prom: prometheus --config.file=prometheus/prometheus.yml
app: ./run.sh
loatest1: loadtest --uri http://localhost:3000/?name=loadtest1 -rate 2
loatest2: loadtest --uri http://localhost:3000/ -rate 0.05
