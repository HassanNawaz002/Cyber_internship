from core.formatter import print_section

def explain_xss(payloads):
    print_section("XSS Payload Explanation")

    for p in payloads:
        print(f"Type      : {p['type']}")
        print(f"Context   : {p['context']}")
        print(f"Template  : {p['payload']}")
        print("Why works : Browser executes injected script in this context")
        print("WAF block : Detects script patterns or event handlers\n")
