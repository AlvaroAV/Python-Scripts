import urllib2
import datetime

# This example was tested using the app IP WEB CAM
ip_cam_url = 'http://127.0.0.1:8080/video'  # The URL should take directly to the video file
ipcam_site = urllib2.urlopen(ip_cam_url)  # Open url of the IP web camera


file_name = 'example_video.mjpg'
f = open(file_name, 'wb')  # Open file for writing

block_sz = 1024  # Size of the buffer
file_size_dl = 0  # Downloaded file size
start_time = datetime.datetime.now()
total_record_time = 10  # Record time set to 10 seconds

while True:
    buffer = ipcam_site.read(block_sz)

    if not buffer:  # Buffer is empty, the url doesn't return expected video
        break

    recording_time = datetime.datetime.now() - start_time
    if recording_time.seconds >= total_record_time:
        break
    file_size_dl += len(buffer)  # Add buffer size to file size downloaded
    f.write(buffer)  # Write the buffer to file

    status = r"Downloading: %s - %10d" % (file_name, file_size_dl)  # Generate string to show downloaded bytes

    # Used this to print allways in the same line
    status = status + chr(8)*(len(status)+1)
    print status,
