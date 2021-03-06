![](demo_video/logo_gif/logo.gif)


DESCRIPTION
===========
* MCUSH is the short name for MCU-SHell.
* A practical project that enhance microcontroller serial port console with shell features like in many linux systems.
* The goal of the project is to provide a firmware template that will expand commands for new applications, so it should be designed with simple API and easy to use.
* MCUSH is initially based on FreeRTOS, but can also be adapted to other RTOSes.
* The core shell runs as a stand-alone task with middle level priority.
* Test suites and templates written in python are privided to ease the test work and create CLI/GUI applications.
* Hosted on github: <https://github.com/pengshulin/mcush>
* Python core module released on PYPI and installed by 'pip install mcush'


FEATURES
========
* SUPPORT:
  * command functions are called with arguments in form of argc and argv
  * arguments parser with short option '-' and long option '--'
  * low memory requirement, suitable for some tiny chips
  * prompt hook function for customize
  * compact history command list
  * multi-line input
  * may port to different architectures, but currently it runs on CORTEX-M only
* NOT SUPPORT:
  * lineedit features that require multi-bytes (such as array keys, shell colors...) are not supported, only simple features that require single-byte (such as BACKSPACE, Ctrl-A/B/C/D/E/F/K/N/P) are supported


ROADMAP
=======
(done)
* run the basic shell on STM32 chips
* use USB virtual com port driver provided by ST
* add file system support (spiffs...)
* add file utils (ls,cp,rm,cat,...) for file system
* add ST/HAL Driver support
* ported to RTX5 platform

(todo/in progress)
* test embedded dynamic languages (eg. lua/picolisp/tinyscheme/micropython...)
* add bootloader and upgrade support
* add practical utilities for lwip network, such as traceroute, ntp update...
* add remote debug support


ENVIRONMENT
===========
* arm-none-eabi-gcc, newlibc, arm-none-eabi-gdb, cgdb
* scons + personal MCU build scripts
  <https://github.com/pengshulin/site_scons>
* STLink v2 + st-flash(flasher) + st-util(gdb server)
  <https://github.com/texane/stlink>
* openocd
* develope and test on Debian/Ubuntu machines


RESOURCES
=========
* Snapshots: <https://github.com/pengshulin/mcush/tree/master/snapshots> 
* Demo videos: <https://github.com/pengshulin/mcush/tree/master/demo_video>  Suitable for beginners and give you a brief overview.
* Windows/VCP(Virtual Com Port) driver: <https://github.com/pengshulin/mcush/tree/master/vcp_driver>


HARDWARE
========
* tiny controller: <https://github.com/pengshulin/mcush/tree/master/hardware_tiny>


LICENSE
=======
* source codes:
  * As this is my personal software toolkit, you can use it freely only for non-commercial purpose.
  * Contact the author for commercial authorization, or it's NOT AUTHORIZED.
* binary executables:
  * images provided in build directory are free as BSD
* hardware design files:
  * similar to the source codes: need commercial authorization


COMMERCIAL
==========
Contact Shanghai Linkong Software Technologies Co., Ltd for commerical support.
http://www.linkongsoft.com/


AUTHOR
======
Peng Shulin <trees_peng@163.com>
Shanghai, China 2020

