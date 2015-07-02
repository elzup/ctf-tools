#!/usr/bin/ruby
require 'net/http'
require 'uri'
uri=URI.parse('http://www.hackerschool.jp/hack/51/index.php')
DATA.each{|e|
	puts 'Trying '+e
	_e=e.split(':')
	begin
		Net::HTTP::Proxy(_e[0],_e[1].to_i).start(uri.host){|http|
			resp=http.get(uri.path)
			puts resp.body
			#exit
		}
	rescue; end
}
