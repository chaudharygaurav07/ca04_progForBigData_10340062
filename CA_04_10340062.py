# open the file - and read all of the lines.
changes_file = "C:\\Users\\c971458\\Desktop\\Programming course\\changes_python.log"
# use strip to strip out spaces and trim the line.

#my_file = open(changes_file, 'r')
#data = my_file.readlines()

data = [line.strip() for line in open(changes_file, 'r')]

# print the number of lines read
print(len(data))

sep = 72*'-'

# create the commit class to hold each of the elements - I am hoping there will be 422
# otherwise I have messed up.
class Commit:
    'class for commits'
    final_data = []
    author = []
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None, month = None,datetimestamp = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
        self.month = month
        self.datetimestamp = datetimestamp
		

    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
 # this new function gets lists of list for author and date they create a commit and can be plotted on graphs with delimiter as :
    def get_author_dates(self):
      return self.author + ':' + str(self.date)
  # this function return revision number, date and time stmap with Author name and can be plotted on graphs with delimiter as :
    def get_commit_time_by_author(self):
      return str(self.revision) + ':' + str(self.datetimestamp) + self.author
  # this function returns author by month  and can be plotted on graphs with delimiter as :
    def get_author_month(self):
      return self.author + ':' + str(self.month)
  
    def __str__(self):
        return '%s,%s,%s,%s,%s,%s,%s\n' % (self.revision,self.author,self.date,self.month,self.datetimestamp,self.comment_line_count,self.changes)

    	
commits = []
current_commit = None 
index = 0




while True:
    try:
        # parse each of the commits and put them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip().split('(')[1].split(')')[0]
        current_commit.month = current_commit.date.split(' ')[2]
        current_commit.datetimestamp = details[2].strip().split('+')[0]
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
       # print(current_commit.changes) 
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        print(current_commit.comment) 
        commits.append(current_commit)
        Commit.final_data.append(current_commit)
        Commit.author.append(current_commit.author)
    except IndexError:
        break

print(len(commits))

commits.reverse()
#print author
unique_author = set(Commit.author)
print unique_author

for index, commit in enumerate(commits):
   print commit.get_commit_comment()
   
for index, commit in enumerate(commits):
    author_commit_by_date = commit.get_author_dates()
    print author_commit_by_date
    
for index, commit in enumerate(commits):
    commit_time = commit.get_commit_time_by_author()
    print commit_time
    
for index, commit in enumerate(commits):
    commit_month = commit.get_author_month()
    print commit_month
	
for commit in commits:
    print commit


