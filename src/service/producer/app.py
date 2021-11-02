
import os, time, json, uuid
from dapr.clients import DaprClient
from essential_generators import DocumentGenerator

gen = DocumentGenerator()
pubsub = os.getenv("PUBSUB", "request-pubsub")
topic = os.getenv("TOPIC", "request-topic")
interval = os.getenv("INTERVAL", 2)
id = 0

with DaprClient() as d: 
    while True:
        id += 1
        req_data = { 'id': str(uuid.UUID(int=id)), 'message': gen.sentence() }
        resp = d.publish_event(
            pubsub_name = pubsub,
            topic_name = topic,
            data = json.dumps(req_data),
            data_content_type = 'application/json',
        )
        print(req_data, flush=True)
        time.sleep(interval)
