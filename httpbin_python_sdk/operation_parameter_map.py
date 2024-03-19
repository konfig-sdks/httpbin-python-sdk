operation_parameter_map = {
    '/anything/{anything}-DELETE': {
        'parameters': [
        ]
    },
    '/anything-GET': {
        'parameters': [
        ]
    },
    '/anything-DELETE': {
        'parameters': [
        ]
    },
    '/anything-PATCH': {
        'parameters': [
        ]
    },
    '/anything/{anything}-GET': {
        'parameters': [
        ]
    },
    '/anything-TRACE': {
        'parameters': [
        ]
    },
    '/anything/{anything}-TRACE': {
        'parameters': [
        ]
    },
    '/anything-POST': {
        'parameters': [
        ]
    },
    '/anything-PUT': {
        'parameters': [
        ]
    },
    '/anything/{anything}-PUT': {
        'parameters': [
        ]
    },
    '/anything/{anything}-POST': {
        'parameters': [
        ]
    },
    '/anything/{anything}-PATCH': {
        'parameters': [
        ]
    },
    '/digest-auth/{qop}/{user}/{passwd}-GET': {
        'parameters': [
            {
                'name': 'qop'
            },
            {
                'name': 'user'
            },
            {
                'name': 'passwd'
            },
        ]
    },
    '/bearer-GET': {
        'parameters': [
            {
                'name': 'Authorization'
            },
        ]
    },
    '/digest-auth/{qop}/{user}/{passwd}/{algorithm}/{stale_after}-GET': {
        'parameters': [
            {
                'name': 'qop'
            },
            {
                'name': 'user'
            },
            {
                'name': 'passwd'
            },
            {
                'name': 'algorithm'
            },
            {
                'name': 'stale_after'
            },
        ]
    },
    '/basic-auth/{user}/{passwd}-GET': {
        'parameters': [
            {
                'name': 'user'
            },
            {
                'name': 'passwd'
            },
        ]
    },
    '/hidden-basic-auth/{user}/{passwd}-GET': {
        'parameters': [
            {
                'name': 'user'
            },
            {
                'name': 'passwd'
            },
        ]
    },
    '/digest-auth/{qop}/{user}/{passwd}/{algorithm}-GET': {
        'parameters': [
            {
                'name': 'qop'
            },
            {
                'name': 'user'
            },
            {
                'name': 'passwd'
            },
            {
                'name': 'algorithm'
            },
        ]
    },
    '/cookies/delete-GET': {
        'parameters': [
            {
                'name': 'freeform'
            },
        ]
    },
    '/cookies-GET': {
        'parameters': [
        ]
    },
    '/cookies/set/{name}/{value}-GET': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/cookies/set-GET': {
        'parameters': [
            {
                'name': 'freeform'
            },
        ]
    },
    '/base64/{value}-GET': {
        'parameters': [
            {
                'name': 'value'
            },
        ]
    },
    '/delay/{delay}-DELETE': {
        'parameters': [
            {
                'name': 'delay'
            },
        ]
    },
    '/delay/{delay}-GET': {
        'parameters': [
            {
                'name': 'delay'
            },
        ]
    },
    '/drip-GET': {
        'parameters': [
            {
                'name': 'duration'
            },
            {
                'name': 'numbytes'
            },
            {
                'name': 'code'
            },
            {
                'name': 'delay'
            },
        ]
    },
    '/links/{n}/{offset}-GET': {
        'parameters': [
            {
                'name': 'n'
            },
            {
                'name': 'offset'
            },
        ]
    },
    '/uuid-GET': {
        'parameters': [
        ]
    },
    '/bytes/{n}-GET': {
        'parameters': [
            {
                'name': 'n'
            },
        ]
    },
    '/delay/{delay}-PUT': {
        'parameters': [
            {
                'name': 'delay'
            },
        ]
    },
    '/delay/{delay}-POST': {
        'parameters': [
            {
                'name': 'delay'
            },
        ]
    },
    '/delay/{delay}-PATCH': {
        'parameters': [
            {
                'name': 'delay'
            },
        ]
    },
    '/delay/{delay}-TRACE': {
        'parameters': [
            {
                'name': 'delay'
            },
        ]
    },
    '/stream/{n}-GET': {
        'parameters': [
            {
                'name': 'n'
            },
        ]
    },
    '/range/{numbytes}-GET': {
        'parameters': [
            {
                'name': 'numbytes'
            },
        ]
    },
    '/stream-bytes/{n}-GET': {
        'parameters': [
            {
                'name': 'n'
            },
        ]
    },
    '/delete-DELETE': {
        'parameters': [
        ]
    },
    '/post-POST': {
        'parameters': [
        ]
    },
    '/put-PUT': {
        'parameters': [
        ]
    },
    '/get-GET': {
        'parameters': [
        ]
    },
    '/patch-PATCH': {
        'parameters': [
        ]
    },
    '/image-GET': {
        'parameters': [
        ]
    },
    '/image/jpeg-GET': {
        'parameters': [
        ]
    },
    '/image/png-GET': {
        'parameters': [
        ]
    },
    '/image/svg-GET': {
        'parameters': [
        ]
    },
    '/image/webp-GET': {
        'parameters': [
        ]
    },
    '/absolute-redirect/{n}-GET': {
        'parameters': [
            {
                'name': 'n'
            },
        ]
    },
    '/redirect/{n}-GET': {
        'parameters': [
            {
                'name': 'n'
            },
        ]
    },
    '/redirect-to-PUT': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'status_code'
            },
        ]
    },
    '/relative-redirect/{n}-GET': {
        'parameters': [
            {
                'name': 'n'
            },
        ]
    },
    '/redirect-to-DELETE': {
        'parameters': [
        ]
    },
    '/redirect-to-GET': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'status_code'
            },
        ]
    },
    '/redirect-to-PATCH': {
        'parameters': [
        ]
    },
    '/redirect-to-POST': {
        'parameters': [
            {
                'name': 'url'
            },
            {
                'name': 'status_code'
            },
        ]
    },
    '/redirect-to-TRACE': {
        'parameters': [
        ]
    },
    '/headers-GET': {
        'parameters': [
        ]
    },
    '/ip-GET': {
        'parameters': [
        ]
    },
    '/user-agent-GET': {
        'parameters': [
        ]
    },
    '/brotli-GET': {
        'parameters': [
        ]
    },
    '/deflate-GET': {
        'parameters': [
        ]
    },
    '/deny-GET': {
        'parameters': [
        ]
    },
    '/robots.txt-GET': {
        'parameters': [
        ]
    },
    '/gzip-GET': {
        'parameters': [
        ]
    },
    '/html-GET': {
        'parameters': [
        ]
    },
    '/json-GET': {
        'parameters': [
        ]
    },
    '/xml-GET': {
        'parameters': [
        ]
    },
    '/encoding/utf8-GET': {
        'parameters': [
        ]
    },
    '/cache/{value}-GET': {
        'parameters': [
            {
                'name': 'value'
            },
        ]
    },
    '/response-headers-POST': {
        'parameters': [
            {
                'name': 'freeform'
            },
        ]
    },
    '/cache-GET': {
        'parameters': [
            {
                'name': 'If-Modified-Since'
            },
            {
                'name': 'If-None-Match'
            },
        ]
    },
    '/response-headers-GET': {
        'parameters': [
            {
                'name': 'freeform'
            },
        ]
    },
    '/etag/{etag}-GET': {
        'parameters': [
            {
                'name': 'If-None-Match'
            },
            {
                'name': 'If-Match'
            },
        ]
    },
    '/status/{codes}-GET': {
        'parameters': [
            {
                'name': 'codes'
            },
        ]
    },
    '/status/{codes}-PUT': {
        'parameters': [
            {
                'name': 'codes'
            },
        ]
    },
    '/status/{codes}-POST': {
        'parameters': [
            {
                'name': 'codes'
            },
        ]
    },
    '/status/{codes}-DELETE': {
        'parameters': [
            {
                'name': 'codes'
            },
        ]
    },
    '/status/{codes}-PATCH': {
        'parameters': [
            {
                'name': 'codes'
            },
        ]
    },
    '/status/{codes}-TRACE': {
        'parameters': [
            {
                'name': 'codes'
            },
        ]
    },
};