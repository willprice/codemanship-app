class DecisionTable(object):
    """ Mixin class that provides blanks methods for all SLIM table calls"""
    def table(self, table):
        pass

    def begin_table(self):
        pass

    def end_table(self):
        pass

    def execute(self):
        pass

    def reset(self):
        pass

    def do_table(self, table_rows):
        pass
