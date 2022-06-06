# How to Demo Kafka in PDS
Do you need a quick way to get show some basic actions in Kafka?

1. Deploy Kafka on PDS.

2. clone this repo.
```
git clone https://github.com/2vcps/py-kafka.git
```

3. Edit the `env-secret.yaml` with your connection servername, username and password from your PDS deployment. Also change the topic name if you would like.

4. Deploy to k8s in this order.
```
kubectl apply -f env-secret.yaml
kubectl apply -f producer.yaml
kubectl apply -f consumer.yaml
```

5. Optional, Scale the deployments for fun.
```
kubectl scale deployment producer-kafka --replicas 8
```
