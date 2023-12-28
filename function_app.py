import azure.functions as func
import logging
import datetime

app = func.FunctionApp()


@app.event_grid_output(
    arg_name="outputEvent",
    topic_endpoint_uri="EventGridTopicUri",
    topic_key_setting="EventGridTopicKey")

@app.route(route="http_trigger", auth_level=func.AuthLevel.FUNCTION)
def http_trigger(req: func.HttpRequest):
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    logging.info('Python HttpRequest trigger processed an event. Req Body: %s',
                req_body)


