#freetoolljekeywu

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))