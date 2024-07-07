# Criminal-Database
Project Description

Topic: File Handling in Python

Data file used: Binary file

Name: Maintaining Criminal Records

About: This project is a set of modules that enable the
users to create a database wherein information
regarding criminals can be managed. The user can also
modify, display and delete the records, apart from
searching for a specific record based on its serial
number. The program generates a new serial number of
every new record, so that the burden of manual input
can be minimized. Efforts have been made to ensure a
personalized experience.

#Files and Methods

Files Created-

1. Criminals.dat- This file stores all the criminal records
created by the user.

2. sno.txt- This file is used to generate a new serial number
every time the user chooses to create new records.

3. Temp.dat- A temporary file, this is used in ‘modify’
module copy the original records and to accept and make
the required modifications in the same. The original
file(crime.dat) is deleted and temp.dat is renamed as
crime.dat to copy the new records.

Methods Created

1. Create/Append- This module creates new records or can
add new records to the criminal database.

2. Modify- This module makes changes to the pre-existing
records on the basis of the serial number.

3. Read/Display- This module displays all the pre-existing
records of the database.

4. Search- This module searches for a certain record on
the basis of its serial number.

5. Delete- This module searches and deletes the record user
wants to eliminate on the basis of its serial number.

#Data File

Text Files

A text file stores information in ASCII or Unicode Characters
(the one which is default for your programming platform). In
text files, each line of text is terminated, (delimited with a special
character) known as EOL(End of Line) character. In text files
some internal translations take place when this EOL character is
read or written. In python, by default, this EOL character is the
new line character(‘\n’) or carriage- return, new line
combination(‘\r\n’).

Binary Files

A binary file is just a file that contains information in the same
format in which the information is held in memory, i.e., the file
content that is returned to you is raw (with no translation or no
specific encoding). In binary file, there is no delimiter for a line.
Also no translations occur in binary files. As a result binary files
are faster and easier for a program to read and write than are text
files. As long as the file doesn’t need to be read by people or to
be ported to a different type of system, binary files are the best
way to store program information.

I have personally opted to use the binary data type to maintain
the database as it is comparatively more space efficient as
compared to the text files type. Another reason for using binary
formats is that they can map directly onto the internal
representation of the data that the program is using.

#Modules Imported

1. Pickle

Python pickle module is used for serializing and de-serializing a Python
object structure. Any object in Python can be pickled so that it can be
saved on disk. What pickle does is that it “serializes” the object first
before writing it to file. “Pickling” is a way to convert a python object
(list, dict, etc.) into a byte stream (using the dump() function). The idea
is that this character stream contains all the information necessary to
reconstruct the object in another python script. “Unpickling” is the
inverse operation, whereby a byte stream (from a binary file) is converted
back into an object hierarchy (using the load() function).

pickle.dump (obj, file)Writes the pickled representation of the
object obj to the open file object file.

pickle.load (file)Reads the pickled representation of an object from
the open file object file and return the reconstituted object hierarchy
specified therein.

2. Os

The OS module in python provides functions for interacting with the
operating system. OS, comes under Python's standard utility modules.
This module provides a portable way of using operating system
dependent functionality.

os.rename (old, new) Changes the name of the existing file old to
new.

os.remove (path) Deletes the file whose path is specified.
