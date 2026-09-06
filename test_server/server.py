from fastapi import FastAPI, Request
import json

app = FastAPI()


@app.post("/internal/gateway/events")
async def receive_gateway_event(request: Request):
    try:
        event = await request.json()
    except Exception:
        return {
            "status": "error",
            "error": "invalid_json",
        }

    print("\n===== GATEWAY EVENT RECEIVED =====")
    print(
        json.dumps(
            event,
            ensure_ascii=False,
            indent=2,
        )
    )

    return {
        "status": "received",
        "request_id": event.get("request_id"),
    }


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "service": "llm-gateway-test-server",
    }