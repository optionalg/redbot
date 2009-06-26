"""
A collection of messages that the RED can emit.

Each should be in the form:

MESSAGE_ID = (classification, level, 
    {'lang': u'message'}
    {'lang': u'long message'}
)

where 'lang' is a language tag, 'message' is a string (NO HTML) that
contains the message in that language, and 'long message' is a longer
explanation that may contain HTML.

Both message forms may contain %(var)s style variable interpolation.
"""

__author__ = "Mark Nottingham <mnot@mnot.net>"
__copyright__ = """\
Copyright (c) 2009 Mark Nottingham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

# message classifications
GENERAL = u"General"
CONNEG = u"Content Negotiation"
CACHING = u"Caching"
VALIDATION = u"Validation"
CONNECTION = u"Connection"
RANGE = u"Partial Content"

# message levels
GOOD = u'good'
BAD = u'bad'
INFO = u'info'
WARN = u'warning'

response = {
    'this': {'en': 'This response'},
    'conneg': {'en': 'The uncompressed response'},
    'LM validation': {'en': 'The 304 response'},
    'ETag validation': {'en': 'The 304 response'},
    'range': {'en': 'The partial response'},
}

URI_TOO_LONG = (GENERAL, WARN,
    {
    'en': u"The URI is very long (%(uri_len)s characters)."
    },
    {
    'en': u"Long URIs aren't supported by some implementations, including proxies. \
    A reasonable upper size limit is 8192 characters."
    }
)

URI_BAD_SYNTAX = (GENERAL, BAD,
    {
    'en': u"The URI's syntax isn't valid."
    },
    {
    'en': u"""This URI doesn't validate successfully. Look for illegal characters \
    and other problems; see <a href='http://www.ietf.org/rfc/rfc3986.txt'>RFC3986</a> 
    for more information."""
    }
)

FIELD_NAME_BAD_SYNTAX = (GENERAL, BAD,
    {
     'en': u'"%(field_name)s" is not a valid header field-name.'
    },
    {
    'en': u"Header field names are limited to the TOKEN production in HTTP; i.e., \
    they can't contain parenthesis, angle brackes (&lt;&gt;), ampersands (@), \
    commas, semicolons, colons, backslashes (\\), forward slashes (/), quotes, \
    square brackets ([]), question marks, equals signs (=), curly brackets ({}) \
    spaces or tabs."
    }
)

HEADER_BLOCK_TOO_LARGE = (GENERAL, BAD,
    {
    'en': u"%(response)s's headers are very large (%(header_block_size)s)."
    },
    {
    'en': u"""Some implementations have limits on the total size of headers
    that they'll accept. For example, Squid's default configuration limits
    header blocks to 20k."""
    }
)

HEADER_TOO_LARGE = (GENERAL, WARN,
    {
    'en': u"The %(header_name)s header is very large (%(header_size)s)."
    },
    {
    'en': u"""Some implementations limit the size of any single header line."""
    }
)

HEADER_NAME_ENCODING = (GENERAL, BAD,
    {
     'en': u"The %(header_name)s header's name contains non-ASCII characters."
    },
    {
     'en': u"""HTTP header field-names can only contain ASCII characters."""
    }
)

HEADER_VALUE_ENCODING = (GENERAL, INFO,
    {
     'en': u"The %(header_name)s header's value contains non-ASCII characters."
    },
    {
     'en': u"""HTTP headers use the ISO-8859-1 character set, but in most 
     cases are pure ASCII (a subset of this encoding).<p>
     This header has non-ASCII characters, which RED has interpreted as
     being encoded in ISO-8859-1. If another encoding is used (e.g., UTF-8),
     the results may be unpredictable."""
    }
)

HEADER_DEPRECATED = (GENERAL, WARN,
    {
    'en': u"The %(header_name)s header is deprecated."
    },
    {
    'en': u"""This header field is no longer recommended for use, because of 
    interoperability problems and/or lack of use. See 
    <a href="%(ref)s">its documentation</a> for more information.""" 
    }
)

SINGLE_HEADER_REPEAT = (GENERAL, BAD,
    {
    'en': u"Only one %(field_name)s header is allowed in a response."
    },
    {
    'en': u"""This header is designed to only occur once in a message. When it 
    occurs more than once, a receiver needs to choose the one to use, which
    can lead to interoperability problems, since different implementations may
    choose different instances to use.<p>
    For the purposes of its tests, RED uses the last instance of the header that
    is present; other implementations may choose a different one."""
    }
)

BODY_NOT_ALLOWED = (CONNECTION, BAD,
    {
     'en': u"%(response)s is not allowed to have a body."
    },
    {
     'en': u"""HTTP defines a few special situations where a response does not
     allow a body. This includes 101, 204 and 304 responses, as well as responses
     to the <code>HEAD</code> method.<p>
     %(response)s had a body, despite it being disallowed. Clients receiving 
     it may treat the body as the next response in the connection, leading to
     interoperability and security issues."""
    }               
)

BAD_SYNTAX = (GENERAL, BAD,
    {
    'en': u"The %(field_name)s header's syntax isn't valid."
    },
    {
    'en': u"""The value for this header doesn't conform to its specified syntax; see
    <a href="%(ref_uri)s">its definition</a> for more information.
    """
    }
)

KEEP_ALIVE_HEADER = (GENERAL, INFO,
    {
    'en': u"The Keep-Alive header isn't necessary."
    },
    {
    'en': u"""HTTP/1.0-style persistent connections rely upon the 
    <code>Connection: Keep-Alive</code> header to indicate that the server
    is willing to keep the connection open for another request.<p>
    It also defines the <code>Keep-Alive</code> header, since connection 
    tokens refer to headers, and it was desireable to reserve the name.<p>
    However, it isn't necessary to actually send the <code>Keep-Alive</code>
    header to use persistent connections; <code>Connection: Keep-Alive</code>
    is enough.<p>
    Some implementations do send information (e.g. the number of requests they're
    willing to serve on a single connection) in this header, but this information
    isn't usually used by clients. It's safe to remove this header if you wish
    to save a few bytes in the response."""
    }
)

BAD_CC_SYNTAX = (CACHING, BAD,
    {
     'en': u"The %(bad_cc_attr)s Cache-Control directive's syntax is incorrect."
    },
    {
     'en': u"This value must be an integer."
    }
)

AGE_NOT_INT = (CACHING, BAD,
    {
    'en': u"The Age header's value should be an integer."
    },
    {
    'en': u"""The <code>Age</code> header indicates the age of the response; i.e., 
    how long it has been cached since it was generated. The value given was not 
    an integer, so it is not a valid age."""
    }
)

AGE_NEGATIVE = (CACHING, BAD,
    {
    'en': u"The Age headers' value must be a positive integer."
    },
    {
    'en': u"""The <code>Age</code> header indicates the age of the response; i.e., 
    how long it has been cached since it was generated. The value given was 
    negative, so it is not a valid age."""
    }
)

BAD_CHUNK = (CONNECTION, BAD,
    {
     'en': u"%(response)s had chunked encoding errors."
    },
    {
     'en': u"""The response indicates it uses HTTP chunked encoding, but there
     was a problem decoding the chunking.<p>     
     A valid chunk looks something like this:<p>
     <code>[chunk-size in hex]\\r\\n[chunk-data]\\r\\n</code><p>
     However, the chunk sent started like this:<p>
     <code>%(chunk_sample)s</code><p>
     This is a serious problem, because HTTP uses chunking to delimit one
     response from the next one; incorrect chunking can lead to interoperability
     and security problems.<p>
     This issue is often caused by sending an integer chunk size instead of one
     in hex, or by sending <code>Transfer-Encoding: chunked</code> without
     actually chunking the response body."""
    }
)

BAD_GZIP = (CONNEG, BAD,
    {
    'en': u"%(response)s was compressed using GZip, but the header wasn't valid."
    },
    {
    'en': u"""GZip-compressed responses have a header that contains metadata. 
    %(response)s's header wasn't valid; the error encountered was 
    "<code>%(gzip_error)s</code>"."""
    }
)

BAD_ZLIB = (CONNEG, BAD,
    {
    'en': u"%(response)s was compressed using GZip, but the data was corrupt."
    },
    {
    'en': u"""GZip-compressed responses use zlib compression to reduce the number
    of bytes transferred on the wire. However, this response could not be decompressed;
    the error encountered was "<code>%(zlib_error)s</code>".<p>
    %(ok_zlib_len)s bytes were decompressed successfully before this; the erroneous
    chunk starts with "<code>%(chunk_sample)s</code>"."""
    }
)

ENCODING_UNWANTED = (CONNEG, WARN,
    {
     'en': u"The %(encoding)s content-coding wasn't asked for."
    },
    {
     'en': u"""%(response)s's <code>Content-Encoding</code> header indicates it
     has the %(encoding)s content-coding applied, but RED didn't ask for it
     to be.<p>
     Normally, clients ask for the encodings they want in the 
     <code>Accept-Encoding</code> request header. Using encodings that the
     client doesn't explicitly request can lead to interoperability problems."""
    }
)

TRANSFER_CODING_IDENTITY = (CONNECTION, INFO,
    {
    'en': u"The identity transfer-coding isn't necessary."
    },
    {
    'en': u"""HTTP defines <em>transfer-codings</em> as a hop-by-hop encoding
    of the message body. The <code>identity</code> tranfer-coding was defined
    as the absence of encoding; it doesn't do anything, so it's necessary.<p>
    You can remove this token to save a few bytes."""
    }
)

TRANSFER_CODING_UNWANTED = (CONNECTION, BAD,
    {
     'en': u"The %(encoding)s transfer-coding wasn't asked for."
    },
    {
     'en': u"""%(response)s's <code>Transfer-Encoding</code> header indicates it
     has the %(encoding)s transfer-coding applied, but RED didn't ask for it
     to be.<p>
     Normally, clients ask for the encodings they want in the 
     <code>TE</code> request header. Using codings that the
     client doesn't explicitly request can lead to interoperability problems."""
    }
)

BAD_DATE_SYNTAX = (GENERAL, BAD,
    {
    'en': u"The %(field_name)s header's value isn't a valid date."
    },
    {
    'en': u"""HTTP dates have very specific syntax, and sending an invalid date can 
    cause a number of problems, especially around caching. Common problems include
    sending "1 May" instead of "01 May" (the month is a fixed-width field), and 
    sending a date in a timezone other than GMT. See 
    <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec3.html#sec3.3">the 
    HTTP specification</a> for more information."""
    }
)

LM_FUTURE = (CACHING, BAD,
    {
    'en': u"The Last-Modified time is in the future."
    },
    {
    'en': u"""The <code>Last-Modified</code> header indicates the last point in 
    time that the resource has changed. %(response)s's 
    <code>Last-Modified</code> time is in the future, which doesn't have any 
    defined meaning in HTTP."""
    }
)

LM_PRESENT = (CACHING, INFO, 
    {
    'en': u"The resource last changed %(last_modified_string)s."
    },
    {
    'en': u"""The <code>Last-Modified</code> header indicates the last point in 
    time that the resource has changed. It is used in HTTP for validating cached
    responses, and for calculating heuristic freshness in caches."""
    }
)

MIME_VERSION = (GENERAL, INFO, 
    {
    'en': u"The MIME-Version header generally isn't necessary in HTTP."
    },
    {
    'en': u"""<code>MIME_Version</code> is a MIME header, not a HTTP header; it's 
    only used when HTTP messages are moved over MIME-based protocols 
    (e.g., SMTP), which is uncommon."""
    }
)

PRAGMA_NO_CACHE = (CACHING, WARN,
    {
    'en': u"Pragma: no-cache is a request directive, not a response directive."
    },
    {
    'en': u"""<code>Pragma</code> is a very old request header that is sometimes 
    used as a response header, even though this is not specified behaviour. 
    <code>Cache-Control: no-cache</code> is more appropriate."""
    }
)

PRAGMA_OTHER = (GENERAL, WARN,
    {
    'en': u"""Pragma only defines the 'no-cache' request directive, and is 
    deprecated for other uses."""
    },
    {
    'en': u"""<code>Pragma</code> is a very old request header that is sometimes 
    used as a response header, even though this is not specified behaviour."""
    }
)

VARY_ASTERISK = (CACHING, WARN,
    {
    'en': u"Vary: * effectively makes responses for this URI uncacheable."
    },
    {
    'en': u"""<code>Vary *</code> indicates that responses for this resource vary 
    by some aspect that can't (or won't) be described by the server. This makes 
    this response effectively uncacheable."""
    }
)

VARY_USER_AGENT = (CACHING, WARN,
    {
     'en': u"Vary: User-Agent is bad practice."
    },
    {
    'en': u""""""
    }
)

VARY_HOST = (CACHING, WARN,
    {
     'en': u"Vary: Host is not necessary."
    },
    {
    'en': u"""Some servers (e.g., <a href="http://httpd.apache.org/">Apache</a>
    with 
    <a href="http://httpd.apache.org/docs/2.0/mod/mod_rewrite.html">mod_rewrite</a>) 
    will send <code>Host</code> in the <code>Vary</code> header, in the belief 
    that since it affects how the server selects what to send back, 
    this is necessary.<p>
    This is not the case; HTTP specifies that the URI is the basis of the cache
    key, and the URI incorporates the <code>Host</code> header.<p>
    The presence of <code>Vary: Host</code> may make some caches not store
    an otherwise cacheable response (since some cache implementations will
    not store anything that has a <code>Vary</code> header)."""
    }
)

VARY_COMPLEX = (CACHING, WARN,
    {
     'en': u"This resource varies in %(vary_count)i ways."
    },
    {
     'en': u"""The <code>Vary</code> mechanism allows a resource to describe the
     dimensions that its responses vary, or change, over; each listed header
     is another dimension.<p>Varying by too many dimensions makes using this
     information impractical."""
    }
)

VIA_PRESENT = (GENERAL, INFO,
    {
    'en': u"An intermediary ('%(via_string)s') is present."
    },
    {
    'en': u"""The <code>Via</code> header indicates that an intermediary is 
    present between RED and the origin server for the resource."""
    }
)

### Ranges

UNKNOWN_RANGE = (RANGE, WARN,
    {
     'en': u"%(response)s advertises support for non-standard range-units."
    },
    {
     'en': u"""The <code>Accept-Ranges</code> response header tells clients
     what <code>range-unit</code>s a resource is willing to process in future
     requests. HTTP only defines two: <code>bytes</code> and <code>none</code>.
     <p>
     Clients who don't know about the non-standard range-unit will not be
     able to use it."""
    }
)

RANGE_CORRECT = (RANGE, GOOD,
    {
    'en': u"A ranged request returned the correct partial content."
    },
    {
    'en': u"""This resource advertises support for ranged requests with 
    <code>Accept-Ranges</code>; that is, it allows clients to specify that only 
    part of it should be sent. RED has tested this by requesting part 
    of this response, which was returned correctly."""
    }
)

RANGE_INCORRECT = (RANGE, BAD,
    {
    'en': u'A ranged request returned partial content, but it was incorrect.'
    },
    {
    'en': u"""This resource advertises support for ranged requests with 
    <code>Accept-Ranges</code>; that is, it allows clients to specify that only 
    part of the response should be sent. RED has tested this by requesting part 
    of this response, but the partial response doesn't correspond with the full 
    response retrieved at the same time. This could indicate that the range 
    implementation isn't working properly.
    <p>RED sent<br/>
    <code>Range: %(range)s</code>
    <p>RED expected %(range_expected_bytes)s bytes:<br/> 
    <code>%(range_expected)s</code>
    <p>RED received %(range_received_bytes)s bytes:<br/> 
    <code>%(range_received)s</code>"""
    }
)

RANGE_FULL = (RANGE, WARN,
    {
    'en': u"A ranged request returned the full rather than partial content."
    },
    {
    'en': u"""This resource advertises support for ranged requests with 
    <code>Accept-Ranges</code>; that is, it allows clients to specify that only 
    part of the response should be sent. RED has tested this by requesting part 
    of this response, but the entire response was returned. In other words, 
    although the resource advertises support for partial content, it
    doesn't appear to actually do so."""
    }
)

RANGE_STATUS = (RANGE, INFO,
    {
    'en': u"A ranged request returned a %(range_status)s status."
    },
    {
    'en': u"""This resource advertises support for ranged requests; that is, it allows
    clients to specify that only part of the response should be sent. RED has tested
    this by requesting part of this response, but a %(enc_range_status)s 
    response code was returned, which RED was not expecting."""
    }
)

RANGE_NEG_MISMATCH = (RANGE, BAD,
    {
     'en': u"Partial responses don't have the same support for compression that full ones do."
    },
    {
     'en': u"""This resource supports ranged requests and also supports negotiation for
     gzip compression, but doesn't support compression for both full and partial responses.<p>
     This can cause problems for clients when they compare the partial and full responses, 
     since the partial response is expressed as a byte range, and compression changes the 
     bytes."""
    }
)

### Body

CL_CORRECT = (GENERAL, GOOD,
    {
    'en': u'The Content-Length header is correct.'
    },
    {
    'en': u"""<code>Content-Length</code> is used by HTTP to delimit messages; 
    that is, to mark the end of one message and the beginning of the next. RED 
    has checked the length of the body and found the <code>Content-Length</code> 
    to be correct."""
    }
)

CL_INCORRECT = (GENERAL, BAD,
    {
    'en': u"%(response)s's Content-Length header is incorrect."
    },
    {
    'en': u"""<code>Content-Length</code> is used by HTTP to delimit messages; 
    that is, to mark the end of one message and the beginning of the next. RED 
    has checked the length of the body and found the <code>Content-Length</code> 
    is not correct. This can cause problems not only with connection handling, 
    but also caching, since an incomplete response is considered uncacheable.<p>
    The actual body size sent was %(body_length)s bytes."""
    }
)

CMD5_CORRECT = (GENERAL, GOOD, 
    {
    'en': u'The Content-MD5 header is correct.'
    },
    {
    'en': u"""<code>Content-MD5</code> is a hash of the body, and can be used to 
    ensure integrity of the response. RED has checked its value and found it to 
    be correct."""
    }
)

CMD5_INCORRECT = (GENERAL, BAD,
    {
    'en': u'The Content-MD5 header is incorrect.'
    },
    {
    'en': u"""<code>Content-MD5</code> is a hash of the body, and can be used to 
    ensure integrity of the response. RED has checked its value and found it to 
    be incorrect; i.e., the given <code>Content-MD5</code> does not match what 
    RED thinks it should be (%(calc_md5)s)."""
    }
)

### Conneg

CONNEG_GZIP = (CONNEG, GOOD,
    {
    'en': u'Content negotiation for gzip compression is supported.'
    },
    {
    'en': u"""HTTP supports compression of responses by negotiating for 
    <code>Content-Encoding</code>. When RED asked for a compressed response, 
    the resource provided one, saving %(savings)s%% of its original size 
    (%(orig_size)s bytes).<p>
    The compressed response's headers displayed."""
    }
)

CONNEG_NO_GZIP = (CONNEG, INFO,
    {
    'en': u'Content negotiation for gzip compression isn\'t supported.'
    },
    {
    'en': u"""HTTP supports compression of responses by negotiating for 
    <code>Content-Encoding</code>. When RED asked for a compressed response, 
    the resource did not provide one."""
    }
)

CONNEG_NO_VARY = (CONNEG, BAD,
    {
    'en': u"%(response)s is negotiated, but doesn't have an appropriate Vary header."
    },
    {
    'en': u"""Any response that's content negotiated needs to have a
    <code>Vary</code> header that reflects the header(s) used to select the
    response.<p>
    %(response)s was negotiated for <code>gzip</code> content encoding, so
    the <code>Vary</code> header needs to contain <code>Accept-Encoding</code>,
    the request header used."""
    }
)

CONNEG_GZIP_WITHOUT_ASKING = (CONNEG, BAD,
    {
    'en': u"A gzip-compressed response was sent when it wasn't asked for."
    },
    {
    'en': u"""HTTP supports compression of responses by negotiating for 
    <code>Content-Encoding</code>. Even though RED didn't ask for a compressed 
    response, the resource provided one anyway. Doing so can break clients that 
    aren't expecting a compressed response."""
    }
)

VARY_INCONSISTENT = (CONNEG, BAD,
    {
    'en': u"The resource doesn't send Vary consistently."
    },
    {
    'en': u"""HTTP requires that the <code>Vary</code> response header be sent 
    consistently for all responses if they change based upon different aspects 
    of the request.<p>
    This resource has both compressed and uncompressed variants 
    available, negotiated by the <code>Accept-Encoding</code> request header, 
    but it sends different Vary headers for each;<p>
    <ul>
      <li>"<code>%(conneg_vary)s</code>" when the response is compressed, and</li>
      <li>"<code>%(no_conneg_vary)s</code>" when it is not.</li>
    </ul>
    <p>This can cause problems for downstream caches, because they 
    cannot consistently determine what the cache key for a given URI is."""
    }
)

ETAG_DOESNT_CHANGE = (CONNEG, BAD,
    {
    'en': u"The ETag doesn't change between representations."
    },
    {
    'en': u"""HTTP requires that the <code>ETag</code>s for two different 
    responses associated with the same URI be different as well, to help caches 
    and other receivers disambiguate them. This resource, however, sent the same
    ETag for both the compressed and uncompressed versions of it (negotiated by 
    <code>Accept-Encoding</code>. This can cause interoperability problems, 
    especially with caches."""
    }
)

### Clock

DATE_CORRECT = (GENERAL, GOOD,
    {
    'en': u"The server's clock is correct."
    },
    {
    'en': u"""HTTP's caching model assumes reasonable synchronisation between 
    clocks on the server and client; using RED's local clock, the server's clock 
    appears to be well-synchronised."""
    }
)

DATE_INCORRECT = (GENERAL, BAD,
    {
    'en': u"The server's clock is %(clock_skew_string)s."
    },
    {
    'en': u"""HTTP's caching model assumes reasonable synchronisation between 
    clocks on the server and client; using RED's local clock, the server's clock 
    does not appear to be well-synchronised. Problems can include responses that 
    should be cacheable not being cacheable (especially if their freshness
    lifetime is short)."""
    }
)

DATE_CLOCKLESS = (GENERAL, WARN,
    {
     'en': u"%(response)s doesn't have a Date header."
    },
    {
     'en': u"""Although HTTP allowes a server not to send a <code>Date</code> header if it
     doesn't have a local clock, this can make calculation of the response's age
     inexact."""
    }
)

DATE_CLOCKLESS_BAD_HDR = (CACHING, BAD,
    {
     'en': u"Responses without a Date aren't allowed to have Expires or Last-Modified values."
    },
    {
     'en': u"""Because both the <code>Expires</code> and <code>Last-Modified</code>
     headers are date-based, it's necessary to know when the message was generated
     for them to be useful; otherwise, clock drift, transit times between nodes as 
     well as caching could skew their application."""
    }
)

### Caching

METHOD_UNCACHEABLE = (CACHING, INFO,
    {
     'en': u"Responses to the %(method)s method can't be stored by caches."
    },
    {
    'en': u""""""
    }
)

NO_STORE = (CACHING, INFO,
    {
     'en': u"%(response)s can't be stored by a cache."
    },
    {
    'en': u"""The <code>Cache-Control: no-store</code> directive indicates that 
    this response can't be stored by a cache."""
    }
)

PRIVATE_CC = (CACHING, INFO,
    {
     'en': u"%(response)s can only be stored by a private cache."
    },
    {
    'en': u"""The <code>Cache-Control: private</code> directive indicates that the
    response can only be stored by caches that are specific to a single user; for
    example, a browser cache. Shared caches, such as those in proxies, cannot store
    it."""
    }
)

PRIVATE_AUTH = (CACHING, INFO,
    {
     'en': u"%(response)s can only be stored by a private cache."
    },
    {
    'en': u"""Because the request was authenticated and this response doesn't contain
    a <code>Cache-Control: public</code> directive, this response can only be 
    stored by caches that are specific to a single user; for example, a browser 
    cache. Shared caches, such as those in proxies, cannot store
    it."""
    }
)

STOREABLE = (CACHING, INFO,
    {
     'en': u"""%(response)s can be stored by any cache."""
    },
    {
     'en': u"""A cache can store this response; it may or may not be able to 
     use it to satisfy a particular request."""
    }
)

NO_CACHE = (CACHING, INFO,
    {
     'en': u"%(response)s cannot be served from cache without validation."
    },
    {
     'en': u"""The <code>Cache-Control: no-store</code> directive means that 
     while caches <strong>can</strong> store this response, they cannot use
     it to satisfy a request unless it has been validated (either with an 
     <code>If-None-Match</code> or <code>If-Modified-Since</code> conditional) 
     for that request.<p>
     If the response doesn't have a <code>Last-Modified</code> or
     <code>ETag</code> header, it effectively can't be used by a cache."""
    }
)

PUBLIC = (CACHING, WARN,
    {
     'en': u"Cache-Control: public is rarely necessary."
    },
    {
     'en': u"""The <code>Cache-Control: public</code> directive is useful 
     to make a response cacheable even when the request had an
     <code>Authorization</code> header (i.e., HTTP authentication was in use).<p>
     This is useful if your site uses HTTP authentication; often, only some 
     resources need to be authenticated, but clients will send the
     <code>Authentication</code> header for all requests covered by the
     realm.<p>
     Additionally, <a href="http://firefox.org/">Firefox</a>'s cache
     will store SSL-protected responses on disk when <code>public</code> is
     present; otherwise, they are only cached in memory.<p>
     <p>Therefore, SSL-protected or HTTP-authenticated (NOT cookie-authenticated)
     resources <em>may</em> have use for <code>public</code> to improve 
     cacheability, if used judiciously.<p>
     However, other resources <strong>do not need to send <code>public</code>
     </strong>; it does not make the response "more cacheable", and only
     makes the response headers larger."""
    }
)

CURRENT_AGE = (CACHING, INFO,
    {
     'en': u"%(response)s has been cached for %(current_age)s."
    },
    {
    'en': u"""The <code>Age</code> header indicates the age of the response; 
    i.e., how long it has been cached since it was generated. HTTP takes this 
    as well as any apparent clock skew into account in computing how old the 
    response already is."""
    }
)

FRESHNESS_FRESH = (CACHING, GOOD,
    {
     'en': u"%(response)s is fresh until %(freshness_left)s from now."
    },
    {
    'en': u"""A response can be considered fresh when its age (here, %(current_age)s)
    is less than its freshness lifetime (in this case, %(freshness_lifetime)s)."""
    }
)

FRESHNESS_STALE = (CACHING, INFO,
    {
     'en': u"%(response)s is stale."
    },
    {
    'en': u"""A cache considers a HTTP response stale when its age (here, %(current_age)s)
    is equal to or exceeds its freshness lifetime (in this case, %(freshness_lifetime)s)."""
    }
)

HEURISTIC_FRESHNESS = (CACHING, INFO,
    {
     'en': u"%(response)s allows heuristic freshness to be used." 
    },
    {
     'en': u"""When the response doesn't have explicit freshness information (like a <code>
     Cache-Control: max-age</code> directive, or <code>Expires</code> header), caches are
     allowed to estimate how fresh the response is using a heuristic.<p>
     Usually, but not always, this is done using the <code>Last-Modified</code> header. For 
     example, if your response was last modified a week ago, a cache might decide to consider
     the response fresh for a day."""
    }
)

STALE_SERVABLE = (CACHING, INFO,
    {
     'en': u"%(response)s can be served stale."
    },
    {
    'en': u"""HTTP allows stale responses to be served under some circumstances; 
    for example, if the origin server can't be contacted, a stale response can 
    be used (even if it doesn't have explicit freshness information).<p>This 
    behaviour can be prevented by using the <code>Cache-Control: must-revalidate</code> 
    response directive."""
    }
)

STALE_MUST_REVALIDATE = (CACHING, INFO,
    {
     'en': u"%(response)s cannot be served stale by caches."
    },
    {
    'en': u"""The <code>Cache-Control: must-revalidate</code> directive forbids 
    caches from using stale responses to satisfy requests.<p>For example, 
    caches often use stale responses when they cannot connect to the origin 
    server; when this directive is present, they will return an error rather 
    than a stale response."""
    }
)

STALE_PROXY_REVALIDATE = (CACHING, INFO,
    {
     'en': u"%(response)s cannot be served stale by shared caches."
    },
    {
    'en': u"""The presence of the <code>Cache-Control: proxy-revalidate</code> 
    and/or <code>s-maxage</code> directives forbids shared caches (e.g., proxy 
    caches) from using stale responses to satisfy requests.<p>For example, 
    caches often use stale responses when they cannot connect to the origin 
    server; when this directive is present, they will return an error rather 
    than a stale response.<p>These directives do not affect private caches; for 
    example, those in browsers."""
    }
)

### ETag Validation

INM_304 = (VALIDATION, GOOD,
    {
    'en': u"If-None-Match conditional requests are supported."
    },
    {
    'en': u"""HTTP allows clients to make conditional requests to see if a copy 
    that they hold is still valid. Since this response has an <code>ETag</code>, 
    clients should be able to use an <code>If-None-Match</code> request header 
    for validation. RED has done this and found that the resource sends a 
    <code>304 Not Modified</code> response, indicating that it supports 
    <code>ETag</code> validation."""
    }
)

INM_FULL = (VALIDATION, WARN,
    {
    'en': u"An If-None-Match conditional request returned the full content unchanged."
    },
    {
    'en': u"""HTTP allows clients to make conditional requests to see if a copy 
    that they hold is still valid. Since this response has an <code>ETag</code>, 
    clients should be able to use an <code>If-None-Match</code> request header 
    for validation. RED has done this and found that the resource sends a full 
    response even though it hadn't changed, indicating that it doesn't support 
    <code>ETag</code> validation."""
    }
)

INM_UNKNOWN = (VALIDATION, INFO,
    {
     'en': u"An If-None-Match conditional request returned the full content, but it had changed."
    },
    {
    'en': u"""HTTP allows clients to make conditional requests to see if a copy 
    that they hold is still valid. Since this response has an <code>ETag</code>, 
    clients should be able to use an <code>If-None-Match</code> request header 
    for validation. RED has done this, but the response changed between the 
    original request and the validating request, so RED can't tell whether or 
    not <code>ETag</code> validation is supported."""
    }
)

INM_STATUS = (VALIDATION, INFO,
    {
    'en': u"An If-None-Match conditional request returned a %(inm_status)s status."
    },
    {
    'en': u"""HTTP allows clients to make conditional requests to see if a copy 
    that they hold is still valid. Since this response has an <code>ETag</code>, 
    clients should be able to use an <code>If-None-Match</code> request header 
    for validation. RED has done this, but the response had a %(enc_inm_status)s 
    status code, so RED can't tell whether or not <code>ETag</code> validation 
    is supported."""
    }
)

### Last-Modified Validation

IMS_304 = (VALIDATION, GOOD,
    {
    'en': u"If-Modified-Since conditional requests are supported."
    },
    {
    'en': u"""HTTP allows clients to make conditional requests to see if a copy 
    that they hold is still valid. Since this response has a 
    <code>Last-Modified</code> header, clients should be able to use an 
    <code>If-Modified-Since</code> request header for validation.<p>
    RED has done this and found that the resource sends a 
    <code>304 Not Modified</code> response, indicating that it supports 
    <code>Last-Modified</code> validation."""
    }
)

IMS_FULL = (VALIDATION, WARN,
    {
    'en': u"An If-Modified-Since conditional request returned the full content unchanged."
    },
    {
    'en': u"""HTTP allows clients to make conditional requests to see if a copy 
    that they hold is still valid. Since this response has a 
    <code>Last-Modified</code> header, clients should be able to use an 
    <code>If-Modified-Since</code> request header for validation.<p>
    RED has done this and found that the resource sends a full response even 
    though it hadn't changed, indicating that it doesn't support 
    <code>Last-Modified</code> validation."""
    }
)

IMS_UNKNOWN = (VALIDATION, INFO,
    {
     'en': u"An If-Modified-Since conditional request returned the full content, but it had changed."
    },
    {
    'en': u"""HTTP allows clients to make conditional requests to see if a copy 
    that they hold is still valid. Since this response has a 
    <code>Last-Modified</code> header, clients should be able to use an 
    <code>If-Modified-Since</code> request header for validation.<p>
    RED has done this, but the response changed between the original request and 
    the validating request, so RED can't tell whether or not 
    <code>Last-Modified</code> validation is supported."""
    }
)

IMS_STATUS = (VALIDATION, INFO,
    {
    'en': u"An If-Modified-Since conditional request returned a %(ims_status)s status."
    },
    {
    'en': u"""HTTP allows clients to make conditional requests to see if a copy 
    that they hold is still valid. Since this response has a 
    <code>Last-Modified</code> header, clients should be able to use an 
    <code>If-Modified-Since</code> request header for validation.<p>
    RED has done this, but the response had a %(enc_ims_status)s status code, so 
    RED can't tell whether or not <code>Last-Modified</code> validation is 
    supported."""
    }
)

### Status checks

REDIRECT_WITHOUT_LOCATION = (GENERAL, BAD,
    {
     'en': u"Redirects need to have a Location header."
    },
    {
     'en': u"""The %(enc_status)s status code redirects users to another URI. The
     <code>Location</code> header is used to convey this URI, but a valid one
     isn't present in this response."""
    }
)

STATUS_DEPRECATED = (GENERAL, BAD,
    {
     'en': u"The %(status)s status code is deprecated."
    },
    {
     'en': u"""When a status code is deprecated, it should not be used, 
     because its meaning is not well-defined enough to ensure interoperability."""
    }
)

STATUS_RESERVED = (GENERAL, BAD,
    {
     'en': u"The %(status)s status code is reserved."
    },
    {
     'en': u"""Reserved status codes can only be used by future, standard protocol
     extensions; they are not for private use."""
    }
)

STATUS_NONSTANDARD = (GENERAL, BAD,
    {
     'en': u"%(status)s is not a standard HTTP status code."
    },
    {
     'en': u"""Non-standard status codes are not well-defined and interoperable.
     Instead of defining your own status code, you should reuse one of the more
     generic ones; for example, 400 for a client-side problem, or 500 for a 
     server-side problem."""
    }
)

STATUS_FORBIDDEN = (GENERAL, INFO,
    {
     'en': u"The server has forbidden this request."
    },
    {
     'en': u""" """
    }
)

STATUS_NOT_FOUND = (GENERAL, INFO,
    {
     'en': u"The resource could not be found."
    },
    {
     'en': u""" """
    }
)

STATUS_CONFLICT = (GENERAL, INFO,
    {
     'en': u"The request conflicted with the state of the resource."
    },
    {
     'en': u""" """
    }
)

STATUS_GONE = (GENERAL, INFO,
    {
     'en': u"The resource is gone."
    },
    {
     'en': u""" """
    }
)

STATUS_REQUEST_ENTITY_TOO_LARGE = (GENERAL, INFO,
    {
     'en': u"The request body was too large."
    },
    {
     'en': u""" """
    }
)

STATUS_URI_TOO_LONG = (GENERAL, BAD,
    {
    'en': u"The server won't accept a URI this long (%(uri_len)s characters)."
    },
    {
    'en': u"""The %(enc_status)s status code means that the server can't or won't accept
    a request-uri this long."""
    }
)

STATUS_UNSUPPORTED_MEDIA_TYPE = (GENERAL, INFO,
    {
     'en': u"The resource doesn't support this media type in requests."
    },
    {
     'en': u""" """
    }
)

STATUS_INTERNAL_SERVICE_ERROR = (GENERAL, INFO,
    {
     'en': u"There was a general server-side error."
    },
    {
     'en': u""" """
    }
)

STATUS_NOT_IMPLEMENTED = (GENERAL, INFO,
    {
     'en': u"The server doesn't implement the request method."
    },
    {
     'en': u""" """
    }
)

STATUS_BAD_GATEWAY = (GENERAL, INFO,
    {
     'en': u"An intermediary encountered an error."
    },
    {
     'en': u""" """
    }
)

STATUS_SERVICE_UNAVAILABLE = (GENERAL, INFO,
    {
     'en': u"The server is temporarily unavailable."
    },
    {
     'en': u""" """
    }
)

STATUS_GATEWAY_TIMEOUT = (GENERAL, INFO,
    {
     'en': u"An intermediary timed out."
    },
    {
     'en': u""" """
    }
)

STATUS_VERSION_NOT_SUPPORTED = (GENERAL, BAD,
    {
     'en': u"The request HTTP version isn't supported."
    },
    {
     'en': u""" """
    }
)
