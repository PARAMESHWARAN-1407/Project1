def parse_document(text):
    return {
        "status": "parsed",
        "characters": len(text),
        "preview": text[:100]
    }