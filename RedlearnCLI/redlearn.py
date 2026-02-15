import argparse
from core.banner import show_banner
from core.formatter import print_section
from core.exporter import export_output

from modules.xss.generator import generate_xss
from modules.xss.explain import explain_xss

from modules.sqli.generator import generate_sqli
from modules.sqli.explain import explain_sqli

from modules.cmdi.generator import generate_cmdi
from modules.cmdi.explain import explain_cmdi


def main():
    show_banner()

    parser = argparse.ArgumentParser(
        description="Redlearn CLI – Educational Offensive Security Payload Templates"
    )

    parser.add_argument("--module", choices=["xss", "sqli", "cmdi"], required=True)
    parser.add_argument("--db", choices=["mysql", "postgresql", "mssql"])
    parser.add_argument("--export", choices=["json", "txt"])

    args = parser.parse_args()

    if args.module == "xss":
        payloads = generate_xss()
        explain_xss(payloads)

    elif args.module == "sqli":
        payloads = generate_sqli(args.db)
        explain_sqli(payloads)

    elif args.module == "cmdi":
        payloads = generate_cmdi()
        explain_cmdi(payloads)

    export_output(payloads, args.export)


if __name__ == "__main__":
    main()
