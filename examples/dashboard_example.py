#!/usr/bin/env python3
"""Example demonstrating a complete dashboard."""

from colorterminal import (
    Box,
    ColoredTable,
    Colors,
    MultiProgressBar,
    SemanticPrinter,
    StylePrinter,
)


def main():
    print("\n=== System Dashboard ===\n")

    # Header
    Box(width=60, height=1, style="double", title="Server Monitoring Dashboard").draw()
    print()

    # System status
    StylePrinter.bold("System Status:")
    SemanticPrinter.success("CPU: Normal (45%)")
    SemanticPrinter.warning("Memory: High (85%)")
    SemanticPrinter.error("Disk: Critical (92%)")
    print()

    # Services table
    StylePrinter.bold("Services Status:")
    table = ColoredTable(headers=["Service", "Status", "Uptime", "Load"])
    table.add_row(["Web Server", "Running", "99.9%", "Medium"], color=Colors.GREEN)
    table.add_row(["Database", "Running", "100%", "High"], color=Colors.GREEN)
    table.add_row(["Cache", "Degraded", "98.5%", "Low"], color=Colors.YELLOW)
    table.add_row(["API Gateway", "Stopped", "0%", "None"], color=Colors.RED)
    table.display()
    print()

    # Resource usage
    StylePrinter.bold("Resource Usage:")
    multi = MultiProgressBar()
    multi.add_bar("CPU", total=100, color_code=Colors.GREEN)
    multi.add_bar("Memory", total=100, color_code=Colors.YELLOW)
    multi.add_bar("Disk", total=100, color_code=Colors.RED)
    multi.add_bar("Network", total=100, color_code=Colors.CYAN)

    multi.update("CPU", 45)
    multi.update("Memory", 85)
    multi.update("Disk", 92)
    multi.update("Network", 35)
    multi.display_all()

    # Footer
    Box(
        width=60, height=1, style="light", title="Last Updated: 2024-10-08 14:30:00"
    ).draw()
    print()


if __name__ == "__main__":
    main()
