import os

JOKE = "I wrote 'per my last email' so politely that the reader apologised to me for a mistake I made."

def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)

if __name__ == "__main__":
    main()
