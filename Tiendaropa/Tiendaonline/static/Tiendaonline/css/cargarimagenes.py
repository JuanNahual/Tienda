def dialog_open_lattice(self):
        """Read lattice from file"""

        filename = QFileDialog.getOpenFileName(self.mw, 'Open Lattice', '', "Python Files (*.py);;All Files (*)", options=QFileDialog.DontUseNativeDialog)[0]
        if filename == '':
            return 0
        print(filename)
            
        self.mw.lattice = GUILattice()    
        
        # executing opened file
        loc_dict = {}
        try:
            exec(open(filename).read(), globals(), loc_dict)
        except Exception as err:
            self.mw.error_window('Open Lattice File Error', str(err))
        
        # parsing sequences and create elements list from cell
        if 'cell' in loc_dict:
            self.mw.lattice.cell = deepcopy(loc_dict['cell'])
            lp = Parser()
            self.mw.lattice.elements = lp.get_elements(self.mw.lattice.cell)
        else:
            self.mw.error_window('Open Lattice File Error', 'NO secuence named "cell"')
        
        # parsing method
        if 'method' in loc_dict:
            self.mw.lattice.method = deepcopy(loc_dict['method'])
        
        # parsing beam
        if 'beam' in loc_dict:
            self.mw.lattice.beam = deepcopy(loc_dict['beam'])
        
        # parsing tws0
        if 'tws0' in loc_dict:
            self.mw.lattice.tws0 = deepcopy(loc_dict['tws0'])
        
        self.mw.menu_edit.edit_lattice() 
        print(filename)