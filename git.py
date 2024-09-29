import os
import subprocess
import time
import threading

def git_pull(target_folder, delay):
    while True:
        print(f"Menunggu {delay} detik sebelum melakukan git pull di '{target_folder}'...")
        time.sleep(delay)  # Tunggu sesuai delay sebelum melakukan git pull
        
        try:
            # Cek apakah ada perubahan lokal sebelum melakukan stash
            stash_check = subprocess.run(['git', '-C', target_folder, 'status', '--porcelain'], capture_output=True, text=True)
            if stash_check.stdout:
                # Jika ada perubahan, lakukan stash
                subprocess.run(['git', '-C', target_folder, 'stash'], capture_output=True, text=True)
                print(f"Perubahan lokal disimpan di '{target_folder}'.")

            # Lakukan git pull
            result = subprocess.run(['git', '-C', target_folder, 'pull'], capture_output=True, text=True)
            print(f"Pull dari '{target_folder}':")
            print(result.stdout)
            print(result.stderr)
        except Exception as e:
            print(f"Error di '{target_folder}': {e}")

def main():
    folders = input("Masukkan path folder git (pisahkan dengan koma): ").split(',')
    folders = [folder.strip() for folder in folders]  # Menghapus spasi ekstra
    delay = int(input("Masukkan delay (detik): "))  # Ambil delay dalam detik

    # Memulai thread untuk setiap folder
    threads = []
    for folder in folders:
        thread = threading.Thread(target=git_pull, args=(folder, delay))
        thread.start()
        threads.append(thread)

if __name__ == "__main__":
    main()
