############## Dis-Embowel-py ##############
#
#By Chris Harty
#started: sept-4-2011
#
#The purpose of this script is to disembowel any python code structure under a specified directory
#
# - 2 main goals at the moment:
#   - 1) build a tree diagram of parent child hierarchy via imports for files and folders
#   - 2) create docs linking functionality (ie where it was called from and the way it was imported) (perhaps we might want to specify certain functionality first)
#
# - minor goal.  maybe later it can be used for robust docs and even churned for use with sphinx
#
############################################

import os
import pprint

#description:
# check root for file
#    disembowel them
# grab folders
# now go through each one
#    check for files
#        disembowel them
#
# return output


class Disembowel(object):

    n_debug = 5 #normal debug level
    c_debug = 4 #current testing debug level

    def __init__(self, debug=n_debug):
        self.DEBUG = debug
        self.tree = dict()
        self._file_descriptor = '__files__'
        #self.tree[self._file_descriptor] = list()
        self.i = 0
    
    def process(self):

        current_directory = os.path.abspath('somefolder/')
        self.build_dir_struct( current_directory, self.tree)
        #self.add_branch(self.tree, current_directory)                

        print "tree:"
        #print self.tree
        pp = pprint.PrettyPrinter(indent=4)
        pp.pprint( self.tree )

    def add_branch(self, cur_tree_pos, branch):
        cur_tree_pos[branch] = dict()
        #cur_tree_pos[branch][self._file_descriptor] = list()
        #print 'cur: %s' % cur_tree_pos[branch]
        return cur_tree_pos[branch]

    def add_leaf(self, cur_tree_pos, leaf):
        #print 'cur leaf: %s' % cur_tree_pos
        #cur_tree_pos[self._file_descriptor].append( leaf )
        cur_tree_pos[leaf]=''

    def process_files(self):
        current_directory = os.path.abspath('')
        if self.DEBUG > self.n_debug: print "Current directory: %s" % current_directory

        #grab all files we need
        current_files = self.grab_files_filtered( current_directory )

        self.print_files( current_files )

    def print_files(self, files):
        if self.DEBUG > self.n_debug: print "\nFiles found after filter."
        for file in files:
            print " - file: %s" % file

    def grab_files_filtered( self, directory, file_types=( '.py',) ):
        remove_files = list()
        files = self.grab_files( directory )
        exit()
        if self.DEBUG > self.n_debug: print "\nAll files found in this current directory."
        for file in files:
            
            if self.DEBUG > self.n_debug: print " - file: %s / %s " % ( file, file[-3:] )
            if not file[-3:] in file_types:     
                remove_files.append( file )
                
        for f in remove_files:
            files.remove( f )
            
        return files

    def build_dir_struct(self, cur_dir, curr_tree_pos):
        print cur_dir
        #print self.tree
        #print ''

        tmp_cur_dir = ''
        self.i += 1
        
        if self.i > 50:
            print "\nlimit to 50 entries, just in case, exiting...\n"
            exit()

        obj_list = os.listdir( cur_dir )
        for o in obj_list:
            tmp_cur_dir = cur_dir + "/" + o
            if not os.path.isfile( tmp_cur_dir ):
                if '.svn' not in o:
                    self.build_dir_struct( tmp_cur_dir , self.add_branch( curr_tree_pos, o ) )
            else:
                self.add_leaf( curr_tree_pos, o )


    def grab_files(self, directory):
        files = list()
        folders = list()
        
        obj_list = os.listdir( directory )

        for obj in obj_list:
            if os.path.isfile( obj ):
                print "%s is a file" % obj
            else: 
                print "%s is a folder" % obj
        

    def run(self):
        self.process_files()



if __name__ == "__main__":
    d = Disembowel()
    #d.run()
    d.process()
