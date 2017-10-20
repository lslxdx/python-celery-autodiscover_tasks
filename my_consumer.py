# coding: utf-8

import sys
from foo.tasks import add

rslt_id = sys.argv[1]
# rslt_id =  38121448-1d17-4b1e-a6ff-0d37bf9664e9
print 'rslt_id = ', rslt_id

rslt = add.AsyncResult(rslt_id)
# rslt.get() =  4
print 'rslt.get() = ', rslt.get()
