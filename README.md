# test-log-via-kafka

```
while :; do logger -P 6514 -n 127.0.0.1 unko; sleep 1; done

fig exec kafka1 kafka-console-consumer --bootstrap-server=localhost:19092 --topic=mytopic --from-beginning --consumer.config /etc/kafka/kafka.properties
```