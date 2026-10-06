require "pathname"

LOG_FOLDER = Pathname.new(__dir__) / "logs"

def main
  files = LOG_FOLDER.glob("*.log")
  puts "#{files.length} Logdateien gefunden."

  for file in files
    text = file.read

    data = {}

    for line in text.lines
      key, value = line.strip.split("=", 2)
      data[key] = value
    end

    if data["status"] == "WARNING" || data["status"] == "ERROR"
      puts"Maschine: #{data["machine"]}, Temperatur: #{data["temperature"]}, Status: #{data["status"]}, Fehler: #{data["error"]}"
    end
  end
end

main