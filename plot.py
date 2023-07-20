import matplotlib.pyplot as plt
import numpy as np


def plot(upload_values, download_values, places):
    mean_upload = np.mean(upload_values)
    mean_download = np.mean(download_values)

    # Create a horizontal bar graph with two separate columns for upload and download
    plt.figure(figsize=(10, 6))
    bar_width = 0.25  # Width of the bars
    bar_offset = 0.05  # Offset between upload and download bars

    # Position of the bars on the y-axis
    y_positions = np.arange(len(places))

    # Plot upload bars
    plt.barh(y_positions - bar_width / 2 - bar_offset/2, upload_values,
             height=bar_width, color='#734B9D',  label='Upload')

    # Plot download bars with a whitespace separator
    plt.barh(y_positions + bar_width / 2 + bar_offset/2, download_values,
             height=bar_width, color='#58CAC6',    label='Download')

    # Add a vertical line to represent the mean values
    plt.axvline(mean_upload, color='#734B9D', linestyle='dashed',
                linewidth=2, label='Mean Upload')
    plt.axvline(mean_download, color='#58CAC6', linestyle='dashed',
                linewidth=2, label='Mean Download')

    # Set y-axis ticks and labels to display place names
    plt.yticks(y_positions, places)

    # Add labels, title, and legend
    plt.xlabel('Speed (Mbps)')
    plt.ylabel('Places')
    plt.title('Upload and Download Speeds in Different Places')
    plt.legend()

    # plt.text(mean_upload, y_positions[-1] - bar_width / 2 - bar_offset,
    #          f"Mean Upload: {mean_upload:.2f} Mbps", color='#734B9D', va='center', ha='left', fontweight='bold')
    # plt.text(mean_download, y_positions[-1] + bar_width / 2 + bar_offset,
    #          f"Mean Download: {mean_download:.2f} Mbps", color='#58CAC6', va='center', ha='left', fontweight='bold')

    plt.tight_layout()
    plt.show()


def read_file_and_plot():
    with open("speedtest.txt", "r") as file:
        places = []
        upload_values = []
        download_values = []
        lines = file.readlines()
        for line in lines:
            line = line.split()
            print(line)
            places.append(int_to_letter(int(line[0])))
            upload_values.append(float(line[1]))
            download_values.append(float(line[2]))

    plot(upload_values, download_values, places)


def int_to_letter(num):
    if 1 <= num <= 26:
        return chr(ord('A') + num - 1)
    else:
        return "Invalid input. Please provide an integer between 1 and 26."


if __name__ == "__main__":
    read_file_and_plot()
