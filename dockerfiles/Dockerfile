FROM ubuntu:22.04 AS build

RUN apt update && apt install -y python3-pip libxcb-cursor0 libxcb-icccm4 libxcb-render-util0 libxkbcommon-x11-0 libxcb-image0 libxcb-xkb-dev libxcb-keysyms1 && \
		 apt install -y libglib2.0-0 libdbus-1-3 libwayland-cursor0 libwayland-client0 libx11-xcb-dev libxcb-xfixes0 libxcb-shape0 libxcb-sync1 libxcb-randr0 \ 
		 libwayland-egl1-mesa libxcb-glx0 libgtk-3-0 libpangocairo-1.0-0 libpango-1.0-0 libgtk-3-0 libcairo-gobject2 libatk1.0-0 libgdk-pixbuf2.0-0 libcairo2 && \
		 rm -rf /var/cache/apt && python3 -m pip install pyinstaller pycryptodomex
COPY . /code
WORKDIR /code
RUN python3 -m pip install -r requirements.txt 
RUN pyinstaller main.py --onefile --name wart-dapp-ubuntu22

FROM scratch AS export-stage
COPY --from=build /code/dist/wart-dapp-ubuntu22 .