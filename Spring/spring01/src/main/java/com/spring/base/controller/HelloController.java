package com.spring.base.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping(path = "/saluto")
public class HelloController {
	
	public HelloController() {
		// TODO Auto-generated constructor stub
		System.out.println("spring sta costruendo HelloController");
	}
	
	@GetMapping(path = "/mondo")
	String salutaMondo() {
		return "Hello Stefano for Real";
	}
	
	@GetMapping(path = "/pers")
	String salutoPers(String nome) {
		return "Hello " + nome;
	}

	
}
