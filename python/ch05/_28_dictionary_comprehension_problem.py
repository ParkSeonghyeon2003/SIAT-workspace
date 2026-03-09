logs_json = [
    {"url": "/login", "status": 200},
    {"url": "/board", "status": 404},
    {"url": "/admin", "status": 500}
]

error_logs = {
    log["url"]:
        "SERVER_ERROR" if log["status"] >= 500 else "CLIENT_ERROR"
        for log in logs_json
        if log["status"] >= 400
}

print(error_logs)