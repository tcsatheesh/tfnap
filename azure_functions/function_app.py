"""Azure Function to run periodically."""

import os
import json
import logging
from datetime import datetime, timezone

import azure.functions as func

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

logging.getLogger("azure").setLevel(logging.WARNING)

_logger = logging.getLogger(__name__)

# Heartbeat service to check Azure Function health and build number
@app.route(route="heartbeat", methods=["GET"])
def heartbeat(req: func.HttpRequest) -> func.HttpResponse:
    """Heartbeat API to check the health of the Azure function

    Args:
        req (func.HttpRequest): requesting status

    Returns:
        func.HttpResponse: response with live status
    """

    _build_id = os.getenv("BUILD_ID", "Local Build")
    _logger.info(
        "Build id %s: Heartbeat request received @%s. Time is in UTC.",
        _build_id,
        datetime.utcnow(),
    )
    _json_data = {
        "build_id": _build_id,
        "datetime": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": "Function App is running",
    }
    _json_data = json.dumps(_json_data)
    return func.HttpResponse(
        _json_data,
        headers={"Content-Type": "application/json"},
        status_code=200,
    )
