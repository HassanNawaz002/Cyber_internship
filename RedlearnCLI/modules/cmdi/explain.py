from core.formatter import print_section

def explain_cmdi(payloads):
    print_section("Command Injection Explanation")

    for p in payloads:
        print(f"OS        : {p['os']}")
        print(f"Template  : {p['payload']}")
        print("Why works : Shell interprets command separators")
        print("Defense  : Strict input validation & allowlists\n")
