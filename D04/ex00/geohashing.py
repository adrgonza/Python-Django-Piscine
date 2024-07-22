import sys
import antigravity

def main():
    if len(sys.argv) != 4:
        return
    date = sys.argv[1]
    try:
        latitude = float(sys.argv[2])
        longitude = float(sys.argv[3])
    except ValueError:
        return

    try:
        antigravity.geohash(latitude, longitude, date.encode())
    except Exception as e:
        print(f"Error computing geohash: {e}")

if __name__ == "__main__":
    main()
