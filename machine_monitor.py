from pathlib import Path

LOG_FOLDER = Path(__file__).parent / "logs"


def main():
    files = list(LOG_FOLDER.glob("*.log"))
    print(f"{len(files)} Logdateien gefunden.")

    for file in files:
        text = file.read_text()

        data = {}

        for line in text.splitlines():
            key, value = line.split("=", 1)
            data[key] = value

        if data["status"] == "WARNING" or data["status"] == "ERROR":
            print(
                "Maschine:", data["machine"], ",",
                "Temperatur:", data["temperature"], ",",
                "Status:", data["status"],
                "Fehler:", data["error"]
            )


if __name__ == "__main__":
    main()

