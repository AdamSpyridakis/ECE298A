<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

This is an 8-bit up counter with tri-state outputs, asynchronous reset, and synchronous load functionality.

Set the enable bit, ena, to enable the counter outputs. The counter counts while the enable bit is low,
but the output will be high Z. Once the enable bit is set, the counter will drive the output pins.

Unset the rst_n to set the counter to 0.

Set the uio_in[0] bit to 1 and set the desired counter value on uo_out[7:0] to load that value into the
counter.

## How to test

Testing is done using cocotb framework.
