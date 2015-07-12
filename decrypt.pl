use Crypt::DES;

my $key = '8946';
my $ciphertext = '89B1pK00C26w6';
my $cipher = new Crypt::DES $key;
my $plaintext = $cipher->decrypt($ciphertext);

