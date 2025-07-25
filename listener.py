import socket
import struct
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 49002))

print("✅ Listening for X-Plane DATA packets...")
print("✅ Do not close this window")

latest = {
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "pitch": 0,
    "roll": 0,
    "true_heading": 0,
    "heading": 0,
    "ground_speed": 0,
    "ground_track": 0,
    "speed": 0,
    "mach": 0,
    "vspeed": 0
}

while True:
    data, addr = sock.recvfrom(1024)
    if data.startswith(b'DATA'):
        payload = data[5:]

        for i in range(0, len(payload), 36):
            block = payload[i:i+36]
            if len(block) < 36:
                continue

            index = struct.unpack('<i', block[0:4])[0]

            # Index 3: vertical speed (fpm)
            if index == 3:
                values = struct.unpack('<8f', block[4:])
                latest["vspeed"] = values[0]

            # Index 17: pitch, roll, headings
            elif index == 17:
                values = struct.unpack('<8f', block[4:])
                # print("🧭 Index 17 full block:", [f"{v:.2f}" for v in values])
                latest["pitch"] = values[0]
                latest["roll"] = values[1]
                latest["true_heading"] = values[2]
                latest["heading"] = values[4] % 360  # Using field 4 for MAG heading
                latest["ground_speed"] = 0  # Invalid data in your case, override with 0
                latest["ground_track"] = values[5]

            # Index 20: lat, lon, alt, airspeed
            elif index == 20:
                values = struct.unpack('<8f', block[4:])
                latest["lat"] = values[0]
                latest["lon"] = values[1]
                latest["alt"] = values[2]
                latest["speed"] = values[3] * 1.94384  # m/s to knots
                latest["mach"] = values[7]

        with open("position.json", "w") as f:
            json.dump(latest, f)
