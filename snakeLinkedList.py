from classes.cell import Cell

class SnakeLinkedList:
    def __init__(self):
        self.head_cell = None
        self.last_cell = None

    def list_print(self):
        print_val = self.head_cell
        while print_val is not None:
            print(print_val.Xcord)
            print(print_val.Ycord)
            print_val = print_val.next_cell

    def count_cell(self):
        count = 0
        temp = self.head_cell
        while temp is not None:
            count += 1
            temp = temp.next_cell
        return count

    def at_beginning(self, new_cell):
        NewCell = Cell(new_cell,new_cell)
        self.head_cell = NewCell

    def at_end(self, new_Xcord, new_Ycord):
        NewCell = Cell(new_Xcord, new_Ycord)
        if self.head_cell is None:
            self.head_cell = self.last_cell = NewCell
            return
        else:
            self.last_cell.next_cell = NewCell
            self.last_cell = NewCell

    # Delete the last Cell
    def del_at_end(self):
        p = self.head_cell
        if self.head_cell is None:
            return
        else:
            self.head_cell = p.next_cell

    def del_at_beginning(self):
        if self.head_cell is None:
            return
        else:
            p = self.head_cell
            self.head_cell = p.next_cell



