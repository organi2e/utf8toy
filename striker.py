#!/usr/bin/env python
print((u''.join([u'%s\u0336'%c for c in (raw_input().decode('utf-8'))])).encode('utf-8'))
