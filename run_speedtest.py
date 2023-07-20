import matplotlib.pyplot as plt
import numpy as np
import speedtest
import os


def run_speed_test():
    try:
        st = speedtest.Speedtest()
        st.get_best_server()

        print("Testing download speed...")
        download_speed = st.download() / 1_000_000  # Convert to Mbps
        print(f"Download speed: {download_speed:.2f} Mbps")

        print("\nTesting upload speed...")
        upload_speed = st.upload() / 1_000_000  # Convert to Mbps
        print(f"Upload speed: {upload_speed:.2f} Mbps")
        return download_speed, upload_speed

    except speedtest.SpeedtestException as e:
        print(f"An error occurred: {e}")


def write_to_file(download_speed, upload_speed):
    # if file doesnt exist, create it
    if not os.path.exists("speedtest.txt"):
        try:
            with open("speedtest.txt", 'w') as file:
                pass
        except IOError:
            print("An error occurred while creating the file.")

    with open("speedtest.txt", "r") as file:
        try:
            last_line = file.readlines()[-1]
            first_letter = last_line[0]
            number = int(last_line[0]) + 1 if first_letter.isdigit() else 1
        except IndexError:
            number = 1

    with open("speedtest.txt", "a") as file:
        file.write(f"{number} {download_speed:.2f} {upload_speed:.2f}\n")


if __name__ == "__main__":
    download_values, upload_values = run_speed_test()
    write_to_file(download_values, upload_values)
