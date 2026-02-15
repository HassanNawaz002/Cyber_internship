from core.formatter import print_section

def explain_sqli(payloads):
    print_section("SQL Injection Explanation")

    for p in payloads:
        print(f"Type     : {p['type']}")
        print(f"DB       : {p['db']}")
        print(f"Template : {p['payload']}")
        print("Why works: SQL logic manipulation")
        print("Defense  : Parameterized queries & WAF rules\n")
