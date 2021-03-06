# https://docs.micropython.org/en/latest/esp32/general.html
# https://github.com/espressif/esptool/

port = /dev/tty.SLAB_USBtoUART

install:
	pip install -r requirements.txt

serial-list:
	ls /dev/{tty,cu}.*

# ------------
# --- Firmware
erase-flash:
	esptool.py --port ${port} erase_flash

get-firmware:
	# https://micropython.org/download/#esp32	
	curl https://micropython.org/resources/firmware/esp32-idf4-20210202-v1.14.bin firmware/

write-firmware-esp32:
	esptool.py --chip esp32 --port ${port} write_flash -z 0x1000 firmware/esp32-idf4-20210202-v1.14.bin

write-firmware-esp8266:
	esptool.py --chip esp8266 --port ${port} write_flash --flash_mode dio --flash_size detect 0x0 firmware/esp8266-20210202-v1.14.bin

# -----------------------
# --- Files on the device
device-list:
	ampy --port ${port} --baud 115200 ls

device-list-file:
	ampy --port ${port} --baud 115200 get ${file}

device-get-file:
	ampy --port ${port} --baud 115200 get ${file} ${local_path}

device-put-file:
	ampy --port ${port} --baud 115200 put ${local_path}