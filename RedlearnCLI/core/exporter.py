import json

def export_output(payloads, export_type):
    if not export_type:
        return

    if export_type == "json":
        with open("output/payloads.json", "w") as f:
            json.dump(payloads, f, indent=4)

    elif export_type == "txt":
        with open("output/payloads.txt", "w") as f:
            for p in payloads:
                f.write(str(p) + "\n")
