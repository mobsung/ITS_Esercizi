package com.spring.base.controller;

import java.util.HashMap;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/string")
public class StringheController {
	
	@GetMapping(path = "/numerica")
	boolean stringaNumerica(String s) {
		for (int i = 0; i < s.length(); i++) {
			if (s.charAt(i) > '9') {
				return false;
			}
		}
		return true;
	}
	
	@GetMapping(path = "/data")
	StringBuilder formatData(String data) {
		HashMap<String, String> mapMese = new HashMap<>();
		mapMese.put("01", "Gennaio");
		mapMese.put("02", "Febbraio");
		mapMese.put("03", "Marzo");
		mapMese.put("04", "Aprile");
		mapMese.put("05", "Maggio");
		mapMese.put("06", "Giugno");
		mapMese.put("07", "Luglio");
		mapMese.put("08", "Agosto");
		mapMese.put("09", "Settembre");
		mapMese.put("10", "Ottobre");
		mapMese.put("11", "Novembre");
		mapMese.put("12", "Dicembre");
		
		StringBuilder rString = new StringBuilder();
		
		for (int i = 0; i < data.length(); i++) {
			if (i < 2 && data.charAt(i) != '/') {
				rString.append(data.charAt(i));
			}
			else if (i > 5) {
				rString.append(data.charAt(i));
			} else {
				rString.append(mapMese.get(data.charAt(i)));
			}
			
		}
		
	
		return rString;
	}

}
