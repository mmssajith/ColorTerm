#!/usr/bin/env python3
"""Example demonstrating table functionality."""

from colorterminal import ColoredTable, Colors, Grid, Table


def main():
    print("\n=== ColorTerm Tables Example ===\n")

    # Basic table
    print("Basic Table:")
    table = Table(headers=["Name", "Age", "City"])
    table.add_row(["Alice", "30", "New York"])
    table.add_row(["Bob", "25", "San Francisco"])
    table.add_row(["Charlie", "35", "Los Angeles"])
    table.display()

    # Table with alignment
    print("\nTable with Alignment:")
    table = Table(
        headers=["Item", "Price", "Quantity"], alignment=["left", "right", "center"]
    )
    table.add_row(["Laptop", "$999", "2"])
    table.add_row(["Mouse", "$25", "10"])
    table.add_row(["Keyboard", "$75", "5"])
    table.display()

    # Table with different border style
    print("\nDouble Border Style:")
    table = Table(headers=["Server", "Status", "Uptime"], style="double")
    table.add_row(["web-01", "Online", "99.9%"])
    table.add_row(["db-01", "Online", "100%"])
    table.add_row(["cache-01", "Degraded", "95.0%"])
    table.display()

    # Colored table
    print("\nColored Table:")
    table = ColoredTable(headers=["Test", "Result", "Time"])
    table.add_row(["Test 1", "PASSED", "0.5s"], color=Colors.GREEN)
    table.add_row(["Test 2", "PASSED", "0.3s"], color=Colors.GREEN)
    table.add_row(["Test 3", "FAILED", "1.2s"], color=Colors.RED)
    table.add_row(["Test 4", "PASSED", "0.7s"], color=Colors.GREEN)
    table.display()

    # Grid layout
    print("\nGrid Layout:")
    grid = Grid(columns=3, cell_width=15, cell_height=2)
    grid.add_cell("Item 1")
    grid.add_cell("Item 2")
    grid.add_cell("Item 3")
    grid.add_cell("Item 4")
    grid.add_cell("Item 5")
    grid.add_cell("Item 6")
    grid.display()

    print()


if __name__ == "__main__":
    main()
