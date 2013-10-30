from optparse import OptionParser

class pars3r:

    def __init__(self, options_2_add=list()):
        """
        options_2_add is a list where...
        each variable is a dict()

        example:
        options_2_add = (
          { '-':'-c',
            '--':'--cssfie',
            'action':'store',
            'dest':'cssfile',
            'default':'style.css',
            'help':'CSS file to link',
            'type':'float, bool, int, long, complex', },
          { '-':'-q',
            'type':'choice',
            'choices':['a', 'b', 'c',], },
          )
        """

        self.options_2_add = options_2_add
        print self.options_2_add
        self.args = None
        self.opts = None
        self.parser = OptionParser()

    def setup(self):
        print 'setup...'

        self._process_options()
        
        self.args, self.opts = self.parser.parse_args()

    def print_this(self):
        print 'args: %s' % str(self.args)
        print 'opts: %s' % str(self.opts)

    def _process_options(self):
        print '_process_options...'
        options = self.options_2_add

        print '%s: %s' % ( type( options ), options )
        if options and isinstance(options, list):
            print 'options good format'
            for _option in options:
                self._add_option( _option )

    def _add_option(self, option):
        self.parser.add_option( self._translate_options( option ) )

    def _translate_options(self, option):
        #need -, --, choices, and the_rest
        
        #tmp = dict()
        #template = """%(flag1)s%(flag2)s%(action)s%(choices)s%(dest)s%(default)s%(help)s"""
        tmp_lst = list()
        
        print 'before trans: %s' % str( option )

        if isinstance(option, dict):
            for key, val in option.iteritems():
                if key == '-':
                    tmp_lst.append( val )
                elif key == '--':
                    tmp_lst.append( val )
                else:
                    tmp_lst.append( %s="%s"' % ( key, val ) )

        print 'after trans: %s' % str( tmp_lst )

        return tmp_lst
                    
            

def main():
    
    #opts = ({},{},)
    opts = [
          { '-':'-c',
            '--':'--cssfie',
            'action':'store',
            'dest':'cssfile',
            'default':'style.css',
            'help':'CSS file to link',
            'type':'float, bool, int, long, complex', },
          { '-':'-q',
            'type':'choice',
            'choices':['a', 'b', 'c',], },
          ]
    p = pars3r( opts )
    p.setup()
    p.print_this()

if __name__ == "__main__":
    main()
