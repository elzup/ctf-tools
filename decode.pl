use Encode;
use MIME::Base64 ();
use URI::Escape;
if (defined $ARGV[0]) {
    $v = $ARGV[0];
} else {
    print "val?\n";
    $v = <STDIN>;
}
chomp($v);

print("$v (prain)\n");
print("base64         : ", (MIME::Base64::encode($v)), "\n");
print("base64dec      : ", (MIME::Base64::decode($v)), "\n");
print("\n");
print("utf            : ", (Encode::encode('utf-8', $v)), "\n");
print("utfdec         : ", (Encode::decode('utf-8', $v)), "\n");
print("\n");
print("url            : ", (url_escape_utf8($v)), "\n");
print("urldec         : ", (url_unescape($v)), "\n");
print("\n");
print("high hex       : ", (pack "H*", $v), "\n");
print("low hex        : ", (pack "h*", $v), "\n");
print("binary         : ", (pack "a*", $v), "\n");
print("ASCHII         : ", (pack "A*", $v), "\n");
print("ASCHIZ         : ", (pack "Z*", $v), "\n");
print("bit up         : ", (pack "b*", $v), "\n");
print("bit down       : ", (pack "B*", $v), "\n");
print("8bit           : ", (pack "c*", $v), "\n");
print("octet          : ", (pack "C*", $v), "\n");
print("large octet    : ", (pack "W*", $v), "\n");
print("16bit          : ", (pack "s*", $v), "\n");
print("us16bit        : ", (pack "S*", $v), "\n");
print("32bit          : ", (pack "l*", $v), "\n");
print("us32bit        : ", (pack "L*", $v), "\n");
print("64bit          : ", (pack "q*", $v), "\n");
print("us64bit        : ", (pack "Q*", $v), "\n");
