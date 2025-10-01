# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Edge
from cocotb.triggers import ClockCycles

async def setup_test(dut):
    dut._log.info("Setup")
    dut.ena.value = 1
    dut.rst_n.value = 1
    dut.ui_in.value = 0
    dut.uo_out.value = 0
    dut.uio_in.value = 0

    # Set the clock period to 1 ns (100 MHz)
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

@cocotb.test()
async def count(dut):
    await setup_test(dut)
    dut._log.info("Test count behavior")

    # Reset to 0.
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    assert dut.uo_out.value == 0
    dut.rst_n.value = 1

    # check count from 1-255, 0-45
    for i in range(300):
        await ClockCycles(dut.clk, 1)
        await Edge(dut.uo_out)
        assert dut.uo_out.value == (i + 1) % 256

@cocotb.test()
async def notEnabled(dut):
    await setup_test(dut)
    dut._log.info("Test counter disabled")

    # disable the counter
    dut.ena.value = 0
    await ClockCycles(dut.clk, 5)
    # expect high Z
    assert dut.uo_out.value.is_resolvable == False

@cocotb.test()
async def load(dut):
    await setup_test(dut)
    dut._log.info("Test synchronous load behavior")

    dut.uio_in.value = 1

    # test handful of arbitrary values
    dut.ui_in.value = 50
    await ClockCycles(dut.clk, 5)
    assert dut.uo_out.value == 50

    dut.ui_in.value = 186
    await ClockCycles(dut.clk, 5)
    assert dut.uo_out.value == 186

    dut.ui_in.value = 233
    await ClockCycles(dut.clk, 5)
    assert dut.uo_out.value == 233
