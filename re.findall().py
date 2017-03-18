#look the following example to get a view of how to use re.findall() to find two []s:

import re
line = '这是1个test'
line = ''.join(re.findall(u'[\u0030-\u007a\u4e00-\u9fff]+', line))
print line

# I have not figure out this problem, so I will rewrite this latter.
