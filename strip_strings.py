import os

PYINSTALLER_STRINGS = [
    b'pyi-windows-manifest-filename',
    b'pyi-windows-dll-path',
    b'pyi-runtime-tmpdir',
    b'LOADER: ',
    b'Cannot open self',
    b'Traceback (most recent call last):',
    b'Fatal Python error',
    b'site-packages',
    b'Lib\\site-packages',
]


def sanitize_binary(file_path):
    if not os.path.isfile(file_path):
        print(f"[-] File not found: {file_path}")
        return

    with open(file_path, 'r+b') as f:
        data = f.read()
        total_replaced = 0

        for sig in PYINSTALLER_STRINGS:
            idx = 0
            while True:
                idx = data.find(sig, idx)
                if idx == -1:
                    break
                print(f"[+] Found: {sig.decode(errors='ignore')} at offset {hex(idx)}")
                f.seek(idx)
                f.write(b'\x00' * len(sig))
                idx += len(sig)
                total_replaced += 1

        if total_replaced == 0:
            print("[*] No PyInstaller signatures found.")
        else:
            print(f"[+] {total_replaced} occurrences sanitized.")

if __name__ == "__main__":
    binary_path = input("Enter path to your PyInstaller .exe binary: ").strip('"')
    sanitize_binary(binary_path)




