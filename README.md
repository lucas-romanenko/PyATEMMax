![PyATEMMax](https://clvlabs.github.io/PyATEMMax/assets/images/logo.png)

## About this fork

This fork updates PyATEMMax to work with current ATEM firmware and has been tested on ATEM firmware 10.2. The upstream project at [clvLabs/PyATEMMax](https://github.com/clvLabs/PyATEMMax) targets firmware 7.5 and has been inactive for several years. The connection handshake was changed so the library can connect to switchers running firmware 10.x, and several keyer, transition, and chroma key commands were corrected or added. A pull request with these changes has been opened upstream.

A Python library to monitor and control [Blackmagic Design ATEM](https://www.blackmagicdesign.com/products/atem) video switchers.

It's a port of the great [ATEMmax](https://github.com/kasperskaarhoj/SKAARHOJ-Open-Engineering/tree/master/ArduinoLibs/ATEMmax) Arduino library by [Kasper Skårhøj](https://www.skaarhoj.com/).

## Documentation

You can find an online version of the documentation at https://clvlabs.github.io/PyATEMMax/

## What's in the repo
* `.vscode`: Recommended extensions and settings for VS Code.
* `PyATEMMax`: Library code.
* `docs`: Documentation (using Jekyll and GitHub Pages).
* `examples`: Some code examples to get started.
