from kafka import KafkaProducer
producer = KafkaProducer(bootstrap_servers='localhost:19092,localhost:29092,localhost:39092')
future = producer.send('kopo_topic',b'HWY TEST')
result = future.get(timeout=60)
