import os.path

# Write triple to given file, creates new file if a file with that name doesn't exist.
# Variable file can be a file path, too.
def writeFile( file, triple ):
    #opens file or creates it if it doesn't exist
    f = open( file, 'w+' )
    f.write( triple + "\n" )
    f.close()


writeFile( "data/test.txt", "this-is-a-triple-test" )
