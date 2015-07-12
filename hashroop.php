<?php

$salt = "8946";
$pass_parts = "tanaka";
$target_hash = '89B1pK00C26w6';

$lib = range(33, 126);
foreach ($lib as $i) {
    echo chr($i);
    # print("$i " . chr($i)) . "\n";
}
echo "\n";

foreach ($lib as $c1) {
    foreach ($lib as $c2) {
        $check_pass = $pass_parts . chr($c1) . chr($c2);
        $hash = crypt($check_pass, $salt);
        echo "$check_pass: $hash\n";
        if ($target_hash == $hash) {
            echo "[{$check_pass}]\n";
            break 2;
        }
    }
}
