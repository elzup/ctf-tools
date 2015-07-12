require 'uri'
require 'net/http'
require 'execjs'

uri        = URI.parse "http://ctfq.sweetduet.info:10080/~q31/kangacha.php"
# 1 => 224
# known_ship = "1"
# known_sign = "24b7447578c89ea8f5f8854d60e253f23bb5b8856d8a135c19af423db354ac60a1a4c932cecd800a0550211e8cc6e28e73e1ac93e7b9c786adc24702e48701c5"
#
# 2 => 220
# known_ship = "1,7"
# known_sign = "f1d19519e780bb0b8cdfb3e3ab9f9282229ae53648587bfda138d04489a03ef0a4720dd7b9ddc25a60087c4b77685beb7017ad28b6e303e62885420f7328f3ee"
#
# 3 => 216
# known_ship = "5,8,3"
# known_sign = "bba4d95c42c118a829eaa7da087f47ac7b9ba8301f6ccfd2b016311b8445b30fb6f653a171bd6de699b8b25a31acdf3e9718515a031e3f145795f99c21b31ab0"
#
# 28 => 112
# known_ship = "8,6,9,3,1,1,9,7,3,7,3,9,0,0,5,6,5,2,3,3,8,3,9,7,7,4,5,2"
# known_sign = "b196e3559516d5cbab12b7a26145292f160f8ea785ae60c9c03522ba305a813b95f241fd4b8fa529d08812e303f9bba37196458ed1bdf9671aa7289ad14493fe"
# 
# 32 => 100
# known_ship = "8,6,9,3,1,1,9,7,3,7,3,9,0,0,5,6,5,2,3,3,8,3,9,7,7,4,5,2,2,9,1,6"
# known_sign = "650714149d45916fa848de709577ec487a94fc6f2e3c6330a25a601daeb8fb189637f6c154ac3694fd5117096b90e580fd313046f9ad011128420c4fa667008b"
#
# 50 => 28
known_ship = "8,6,9,3,1,1,9,7,3,7,3,9,0,0,5,6,5,2,3,3,8,3,9,7,7,4,5,2,2,9,1,6,3,8,8,9,8,5,1,6,0,7,8,1,4,4,7,7,9,9"
known_sign = "45f6c3d0a058ccfd4d360f01cacb586987632b556baa1fcc1e52e61ecb80e1a3ba3454b2609e8cad48f20157359002dc2de557aa6d5f142735822672c9ab97ea"
#
# 57 => 28
# known_ship = "8,6,9,3,1,1,9,7,3,7,3,9,0,0,5,6,5,2,3,3,8,3,9,7,7,4,5,2,2,9,1,6,3,8,8,9,8,5,1,6,0,7,8,1,4,4,7,7,9,9,2,1,7,7,3,5,8"
# known_sign = "635eafb97d28561df57a37a299c02898fcdaa23e0d5277758d62c8e19a4033443e4690a1e7ba34f3af2f4296579bca4e6343b7d48ae04f41008a1fb34d7999a2"

# ? => ??
# known_ship = "8,6,9,3,1,1,9,7,3,7,3,9,0,0,5,6,5,2,3,3,8,3,9,7,7,4,5,2,4,5,5,6,7,8,7,1,9,4,1,2,7,9,3,2,6,3,5,8,4,3,4,7,2,6,6,8,4,8,2,9,6,5"
# known_sign = "37c1b57fcb8d1ce39ee49f150ee307b11853eb3421ca20f4eb07e124cc144d99f364d677ce607937720127350934e7ff439113ba3efb9c1d21bd0f2edae36907"
add_data   = ",10"
trials     = 24
 
http = Net::HTTP.new uri.host, uri.port
http.start {
 
	(10..trials).each do |i|
		hashpump = `hashpump -s #{known_sign} -d "#{known_ship}" -a "#{add_data}" -k #{i}`
		sign, data = hashpump.split("\n")
 
		head = data.slice! 0
		tail = data.slice!(-3, 3)
		data = head + data.split('\x').map { |d| d.to_i(16).chr }.join + tail
		puts data
 
		header = {
			'Cookie' => "ship=#{data}; signature=#{sign}"
		}
		response = http.get(uri.path, header).body
 
		if (response.index "flag") != nil
			puts "Trial #{i}: succeeded!"
			puts response
			break
		else
			puts "Trial #{i}: failed"
		end
	end
}
