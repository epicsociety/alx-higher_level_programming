** Get the main page from a web-server: **
> curl https://www.example.com/

** Get a README file from an FTP server: **
> curl ftp://ftp.funet.fi/README

Get a web page from a server using port 8000:

curl http://www.weirdserver.com:8000/
Get a directory listing of an FTP site:

curl ftp://ftp.funet.fi
Get the definition of curl from a dictionary:

curl dict://dict.org/m:curl
Fetch two documents at once:

curl ftp://ftp.funet.fi/ http://www.weirdserver.com:8000/
Get a file off an FTPS server:

curl ftps://files.are.secure.com/secrets.txt
or use the more appropriate FTPS way to get the same file:

curl --ftp-ssl ftp://files.are.secure.com/secrets.txt
Get a file from an SSH server using SFTP:

curl -u username sftp://example.com/etc/issue
Get a file from an SSH server using SCP using a private key (not
        password-protected) to authenticate:

curl -u username: --key ~/.ssh/id_rsa scp://example.com/~/file.txt
Get a file from an SSH server using SCP using a private key
(password-protected) to authenticate:

curl -u username: --key ~/.ssh/id_rsa --pass private_key_password
scp://example.com/~/file.txt
Get the main page from an IPv6 web server:

curl "http://[2001:1890:1112:1::20]/"
Get a file from an SMB server:

curl -u "domain\username:passwd" smb://server.example.com/share/file.txt
Download to a File
Get a web page and store in a local file with a specific name:

curl -o thatpage.html http://www.example.com/
Get a web page and store in a local file, make the local file get the name of
the remote document (if no file name part is specified in the URL, this will
        fail):

    curl -O http://www.example.com/index.html
    Fetch two files and store them with their remote names:

    curl -O www.haxx.se/index.html -O curl.se/download.html
    Using Passwords
    FTP
    To ftp files using name and password, include them in the URL like:

    curl ftp://name:passwd@machine.domain:port/full/path/to/file
    or specify them with the -u flag like

    curl -u name:passwd ftp://machine.domain:port/full/path/to/file
    FTPS
    It is just like for FTP, but you may also want to specify and use
    SSL-specific options for certificates etc.

    Note that using FTPS:// as prefix is the implicit way as described in the
    standards while the recommended explicit way is done by using FTP:// and
    the --ssl-reqd option.

    SFTP / SCP
    This is similar to FTP, but you can use the --key option to specify a
    private key to use instead of a password. Note that the private key may
    itself be protected by a password that is unrelated to the login password
    of the remote system; this password is specified using the --pass option.
    Typically, curl will automatically extract the public key from the private
    key file, but in cases where curl does not have the proper library support,
    a matching public key file must be specified using the --pubkey option.

    HTTP
    Curl also supports user and password in HTTP URLs, thus you can pick a file
    like:

    curl http://name:passwd@machine.domain/full/path/to/file
    or specify user and password separately like in

    curl -u name:passwd http://machine.domain/full/path/to/file
    HTTP offers many different methods of authentication and curl supports
    several: Basic, Digest, NTLM and Negotiate (SPNEGO). Without telling which
    method to use, curl defaults to Basic. You can also ask curl to pick the
    most secure ones out of the ones that the server accepts for the given URL,
    by using --anyauth.

    Note! According to the URL specification, HTTP URLs can not contain a user
    and password, so that style will not work when using curl via a proxy, even
    though curl allows it at other times. When using a proxy, you must use the
    -u style for user and password.
